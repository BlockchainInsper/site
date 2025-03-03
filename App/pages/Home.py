import reflex as rx
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials


def with_background_image():
    return rx.flex(
        rx.vstack(
            rx.stack(
                rx.text(
                    "Conheça nossas áreas! Estamos estruturados em áreas de estudo e áreas administrativas",
                    font_weight="700",
                    line_height=1.2,
                    font_size=rx.breakpoints(initial="3xl", md="4xl"),
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
            width="full",
            justify="center",
            px=rx.breakpoints(initial="4", md="8"),
        ),
        width="full",
        height="30vh",
        background_image="url('/overlay.png')",
        background_size="cover",
        background_position="center center",
    )


def home():
    return rx.box(
        call_to_action_with_video(),
        features(),
        testimonials(),
        with_background_image(),
    )
