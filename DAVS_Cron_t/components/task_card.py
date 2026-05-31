import reflex as rx
from ..states.task_state import TaskState


def task_card(task: dict) -> rx.Component:
    return rx.card(
        rx.vstack(
            # Cabecera
            rx.hstack(
                rx.cond(
                    task["running"],
                    rx.box(
                        width="10px",
                        height="10px",
                        border_radius="50%",
                        background_color="#34C759",
                        box_shadow="0 0 6px #34C759",
                    ),
                    rx.box(
                        width="10px",
                        height="10px",
                        border_radius="50%",
                        background_color="#C7C7CC",
                    ),
                ),
                rx.text(
                    task["name"],
                    size="4",
                    weight="bold",
                    color="#1D1D1F",
                ),
                align="center",
                spacing="2",
                width="100%",
            ),
            # Cronómetro
            # Bug fix: style dict usa camelCase (estándar CSS-in-JS),
            # no snake_case. Con snake_case la conversión interna de Reflex
            # no es confiable entre dev y prod.
            rx.text(
                task["display"],
                style={
                    "fontFamily": "ui-monospace, 'SF Mono', monospace",
                    # CAMBIO: clamp(min, ideal, max) para que escale suavemente
                    "fontSize": "clamp(35px, 8vw, 50px)",
                    "fontWeight": "300",
                    "letterSpacing": "-1px",
                    "lineHeight": "1",
                    "color": "#1D1D1F",
                },
            ),
            # Botones
            rx.hstack(
                rx.cond(
                    task["running"],
                    # Botón pausa
                    rx.button(
                        rx.icon("pause", size=15),
                        "Pausar",
                        on_click=TaskState.play_pause_task(task["id"]),
                        background_color="#FFC52E",
                        border_radius="12px",
                        cursor="pointer",
                        size="2",
                        color="#464649",
                        border="0.1px solid #000000",
                    ),
                    # Botón reanudar
                    rx.button(
                        rx.icon("play", size=15),
                        "Reanudar",
                        on_click=TaskState.play_pause_task(task["id"]),
                        background_color="#31D44F",
                        border_radius="12px",
                        cursor="pointer",
                        size="2",
                        color="#464649",
                        border="0.1px solid #000000",
                    ),
                ),
                # Botones reiniciar y eliminar
                rx.button(
                    rx.icon("rotate-ccw", size=15),
                    "Reiniciar",
                    on_click=TaskState.reset_task(task["id"]),
                    background_color="#FFC52E",
                    border_radius="12px",
                    cursor="pointer",
                    size="2",
                    color="#464649",
                    border="0.1px solid #000000",
                ),
                rx.button(
                    rx.icon("trash-2", size=30),
                    on_click=TaskState.delete_task(task["id"]),
                    variant="ghost",
                    color_scheme="red",
                    cursor="pointer",
                    size="4",
                ),
                flex_wrap="wrap", 
                justify_content="center"
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        background_color="white",
        border_radius="16px",
        box_shadow="0 2px 16px rgba(0, 0, 0, 0.08)",
        padding="6",
        width="100%",
        # Bug fix: border y outline duplicados dibujaban dos bordes superpuestos.
        # outline no reemplaza a border — son propiedades distintas.
        border="0.1px solid #000000",
    )