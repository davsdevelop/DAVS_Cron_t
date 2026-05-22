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
            return TaskState.add_task
        

    @rx.event
    def add_task(self):
        name = self.new_task_name.strip()
        if not name:
            return
        
        task = {
            "id": str(uuid.uuid4())[:8],
            "name": name, 
            "seconds": 0,
            "display":"00:00:00",
            "running": True,
        }

        self.tasks.append(task)
        self.new_task_name = ""
        #ejecutar ticks
        if not self.ticker_running:
            self.ticker_running = True
            return TaskState.tick


    @rx.event(background=True)
    async def tick(self):
        #loop
        while True:
            await asyncio.sleep(1)

            async with self:
                #si no hay una tarea corriendo, detener el loop
                if not any(t["running"] for t in self.tasks):
                    self.ticker_running = False
                    break

                update = []
                for task in self.tasks:
                    if task["running"]:
                        secs = task["seconds"] + 1
                        #calculos para el reloj
                        h = secs // 3600
                        m = (secs % 3600) // 60
                        s = secs % 60

                        display = f"{h:02d}:{m:02d}:{s:02d}"
                        update.append({**task, "seconds": secs, "display":display})
                    else:
                        update.append(task)
                
                self.tasks = update


    @rx.event
    def reset_task(self, task_id: str):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks[i] = {**task, "seconds": 0, "display": "00:00:00"}



    @rx.event
    def play_pause_task(self, task_id: str):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks[i] = {**task, "running": not task["running"]}

        if any(t["running"] for t in self.tasks) and not self.ticker_running:
            self.ticker_running = True
            return TaskState.tick




    @rx.event
    def delete_task(self, task_id: str):
        filtered_tasks = [
            task for task in self.tasks
            if task["id"] != task_id
        ]
        self.tasks = filtered_tasks