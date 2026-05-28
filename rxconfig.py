import reflex as rx

config = rx.Config(
    app_name="DAVS_Cron_t",
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