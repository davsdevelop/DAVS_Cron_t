import reflex as rx
import uuid
import asyncio


class TaskState(rx.State):
    tasks: list[dict] = []
    new_task_name: str = ""
    ticker_running: bool = False

    @rx.event
    def set_new_task_name(self, value: str):
        self.new_task_name = value

    @rx.event
    def enter_key(self, key: str):
        if key == "Enter":
            return TaskState.add_task()

    @rx.event
    def add_task(self):
        name = self.new_task_name.strip()
        if not name:
            return

        task = {
            "id": str(uuid.uuid4())[:8],
            "name": name,
            "seconds": 0,
            "display": "00:00:00",
            "running": True,
        }

        self.tasks.append(task)
        self.new_task_name = ""

        # Solo lanza el ticker si no está corriendo ya
        if not self.ticker_running:
            self.ticker_running = True
            return TaskState.tick()

    @rx.event(background=True)
    async def tick(self):
        # Bug fix: try/finally garantiza que ticker_running vuelva a False
        # aunque ocurra una excepción (ej: error de red, reinicio en Render).
        # Sin esto, ticker_running podía quedar en True indefinidamente y
        # los cronómetros dejaban de avanzar sin forma de recuperarse.
        try:
            while True:
                await asyncio.sleep(1)

                async with self:
                    # Si no hay ninguna tarea corriendo, detener el loop
                    if not any(t["running"] for t in self.tasks):
                        self.ticker_running = False
                        break

                    update = []
                    for task in self.tasks:
                        if task["running"]:
                            secs = task["seconds"] + 1
                            h = secs // 3600
                            m = (secs % 3600) // 60
                            s = secs % 60
                            display = f"{h:02d}:{m:02d}:{s:02d}"
                            update.append({**task, "seconds": secs, "display": display})
                        else:
                            update.append(task)

                    self.tasks = update
        finally:
            # Bug fix: siempre liberar el flag al salir del loop,
            # sea por condición normal o por excepción inesperada
            async with self:
                self.ticker_running = False

    @rx.event
    def reset_task(self, task_id: str):
        # Bug fix: reset detiene el cronómetro (running=False) además de
        # poner el tiempo en cero. Antes el cronómetro reiniciado seguía
        # corriendo inmediatamente, lo cual es confuso para el usuario.
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks[i] = {
                    **task,
                    "seconds": 0,
                    "display": "00:00:00",
                    "running": False,
                }

    @rx.event
    def play_pause_task(self, task_id: str):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks[i] = {**task, "running": not task["running"]}

        # Si hay tareas corriendo y el ticker no está activo, relanzarlo
        if any(t["running"] for t in self.tasks) and not self.ticker_running:
            self.ticker_running = True
            return TaskState.tick()

    @rx.event
    def delete_task(self, task_id: str):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]

        # Bug fix: si ya no quedan tareas corriendo, asegurarse de que
        # el ticker se detenga en su próximo ciclo (ya lo hace solo),
        # pero si la lista quedó vacía no hay nada que iterar — seguro.
        # Si además no quedan tareas en absoluto, limpiar el flag ya.
        if not self.tasks:
            self.ticker_running = False