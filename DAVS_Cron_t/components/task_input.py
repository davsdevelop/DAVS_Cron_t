import reflex as rx
from ..states.task_state import TaskState


def task_input() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(
                # Fix ortografía: "Nueva tarea:" con minúscula en "tarea"
                # para consistencia con sentence case del resto de la UI.
                "Nueva tarea:",
                size="3",
                weight="medium",
                color="#464649",
            ),
            # Dentro de task_input()
            rx.hstack(
                rx.input(
                    placeholder="Escribe un nombre...",
                    value=TaskState.new_task_name,
                    on_change=TaskState.set_new_task_name,
                    on_key_down=TaskState.enter_key,
                    size="3",
                    border_radius="12px",
                    background_color="#FCE3A2",
                    # CAMBIO: Quitamos width="470px" y delegamos al flexbox
                    flex="1", 
                    width="100%",
                ),
                rx.button(
                    rx.icon("plus", size=18),
                    "Agregar",
                    on_click=TaskState.add_task,
                    background_color="#FFC52E",
                    size="3",
                    border_radius="12px",
                    cursor="pointer",
                    color="#464649",
                    # En móviles evitamos que el botón se aplaste
                    flex_shrink="0", 
                ),
                spacing="3",
                width="100%",
                align="center",
                # CAMBIO: Apilar en móvil (columna), lado a lado en tablets/desktop (fila)
                flex_direction=rx.breakpoints(initial="column", sm="row"),
            ),
            spacing="3",
            width="100%",
        ),
        border_radius="12px",
        box_shadow="0 2px 16px rgba(0, 0, 0, 0.1)",
        padding="6",
        width="100%",
        # Bug fix: eliminado outline duplicado (mismo que border)
        border="0.1px solid #000000",
    )