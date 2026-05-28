import reflex as rx

config = rx.Config(
    app_name="DAVS_Cron_t",
    # 1. Fijamos el frontend para que apunte al backend correcto
    api_url="https://davs-cron-t.onrender.com", 
    # 2. Permitimos que el backend reciba la conexión
    cors_allowed_origins=[
        "*"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="light",
                has_background=True
            )
        )
    ]
)