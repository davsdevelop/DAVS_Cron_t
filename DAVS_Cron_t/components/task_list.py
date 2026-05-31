import reflex as rx
from ..states.task_state import TaskState
from .task_card import task_card


def _empty_list() -> rx.Component:
    return rx.vstack(
        rx.icon("clock", size=48, color="#C7C7CC"),
        rx.text(
            # Fix ortografía: "Sin tareas activas" — minúscula en "tareas"
            # para consistencia con sentence case.
            "Sin tareas activas",
            size="4",
            weight="medium",
            color="#8E8E93",
        ),
        rx.text(
            "Agrega una tarea para empezar a cronometrar",
            size="2",
            color="#AEAEB2",
        ),
        spacing="2",
        align="center",
        padding_y="10",
        width="100%",
    )


def task_list() -> rx.Component:
    return rx.cond(
        TaskState.tasks.length() == 0,
        _empty_list(),
        # Dentro de task_list()
        rx.grid(
            rx.foreach(TaskState.tasks, task_card),
            # CAMBIO: 1 columna en móvil, 2 en pantallas más grandes
            columns=rx.breakpoints(initial="1", sm="2"),
            spacing="4",
            width="100%",
        )
    )