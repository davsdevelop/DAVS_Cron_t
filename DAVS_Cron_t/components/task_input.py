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
            rx.hstack(
                rx.input(
                    placeholder="Escribe un nombre al cronómetro de tu tarea...",
                    color="black",
                    value=TaskState.new_task_name,
                    on_change=TaskState.set_new_task_name,
                    on_key_down=TaskState.enter_key,
                    size="3",
                    border_radius="12px",
                    background_color="#FCE3A2",
                    width="470px",
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
                ),
                spacing="3",
                width="100%",
                align="center",
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