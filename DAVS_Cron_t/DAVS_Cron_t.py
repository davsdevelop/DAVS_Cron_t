import reflex as rx
from .components import task_input
from .components import task_list


def index() -> rx.Component:
    return rx.box(
        # ===== HEADER =====
        rx.box(
            width="100%",
            height="15px",
            background_color="#FFC52E",
        ),
        rx.box(
            width="100%",
            height="25px",
        ),

        # ==== CONTENIDO PRINCIPAL ====
        rx.box(
            rx.vstack(
                rx.vstack(
                    rx.image("/logo_cron_t.svg", width="250px"),
                    rx.text(
                        "Gestiona tus tareas con cronómetros",
                        size="3",
                        weight="regular",
                        color="#8E8E93",
                    ),
                    spacing="1",
                    align="center",
                    padding_bottom="2",
                ),

                # Input principal
                task_input(),

                # Lista de tareas
                task_list(),

                spacing="5",
                width="100%",
                max_width="640px",
                align="center",
            ),
            display="flex",
            justify_content="center",
            padding_x="5",
            padding_y="10",
            flex_grow="1",
        ),

        rx.box(
            width="100%",
            height="25px",
        ),

        # ==== FOOTER ====
        rx.box(
            rx.text(
                "Desarrollado por: Diego Videla Silva",
                size="2",
                color="#464649",
                padding_left="40px",
            ),
            rx.image("/DAVS.png", width="70px"),
            rx.text(
                "© 2026 Cron-t. Todos los derechos reservados.",
                size="2",
                color="#464649",
                padding_right="180px",
            ),
            width="100%",
            # Bug fix: padding_y="" generaba CSS inválido. Eliminado.
            background_color="#FFC52E",
            display="flex",
            justify_content="space-between",
            align_items="center",
            height="40px",
        ),

        min_height="100vh",
        width="100%",
        background_color="#F5F5F7",
        display="flex",
        flex_direction="column",
    )


app = rx.App(
    stylesheets=["/style.css"],
)
app.add_page(index)