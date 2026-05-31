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
                width=rx.breakpoints(initial="90%", sm="100%"),
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

        #  ==== FOOTER ====
        rx.box(
            rx.text(
                "Desarrollado por: Diego Videla Silva",
                size="2",
                color="#464649",
            ),
            rx.image("/DAVS.png", width="70px"),
            rx.text(
                "© 2026 Cron-t. Todos los derechos reservados.",
                size="2",
                color="#464649",
            ),
            width="100%",
            background_color="#FFC52E",
            display="flex",
            # CAMBIO: Columna centrada en móvil, fila espaciada en desktop
            flex_direction=rx.breakpoints(initial="column", sm="row"),
            justify_content="space-between",
            align_items="center",
            padding_x="4",
            padding_y="2", # Reemplaza el height="40px" fijo
            gap="3", # Espacio entre elementos cuando estén en columna
        ),

        min_height="100vh",
        width="100%",
        background_color="#F5F5F7",
        display="flex",
        flex_direction="column",
    )


app = rx.App(
    # Bug fix: stylesheet sin "/" inicial puede fallar en producción.
    # Reflex sirve los assets desde la raíz, siempre usar "/" al inicio.
    stylesheets=["/style.css"],
)
app.add_page(index)