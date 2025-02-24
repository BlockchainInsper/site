import reflex as rx
# from App.components.home.hero import hero
# from App.components.home.features import features
# from App.components.home.testimonials import testimonials

# Constantes para estilo
OVERLAY_IMAGE = "overlay.png"  # Ajuste o caminho conforme necessário


def background_section() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.stack(
                rx.text(
                    "Conheça nossas áreas! Estamos estruturados em áreas de estudo e áreas administrativas",
                    size="6",
                    weight="bold",
                    line_height="1.2",
                ),
                rx.stack(
                    rx.link(
                        rx.button(
                            "Nossas áreas",
                            bg="#f68b23",
                            border_radius="full",
                            color="white",
                            _hover={"bg": "#f68b70"},
                        ),
                        href="/areas",
                    ),
                    direction="row",
                ),
                max_width="2xl",
                align="start",
                spacing="6",
            ),
            width="100%",
            justify="center",
            padding_x=["4", "8"],
        ),
        width="100%",
        height="30vh",
        background=f"center/cover url({OVERLAY_IMAGE})",
        background_size="cover",
        background_position="center center",
    )


def home() -> rx.Component:
    return rx.box(
        # hero(),
        # features(),
        # testimonials(),
        background_section(),
    )
