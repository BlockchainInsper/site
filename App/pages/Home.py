import reflex as rx
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials
from App.Template import template


def with_background_image():
    return rx.flex(
        rx.flex(
            rx.vstack(
                rx.text(
                    "Conheça nossas áreas! Estamos estruturados em áreas de estudo e áreas administrativas",
                    style={
                        "font_weight": "700",
                        "line_height": "1.2",
                        "font_size": rx.breakpoints(
                            initial="1.875rem",  # 3xl
                            md="2.25rem",  # 4xl
                        ),
                        "text_align": "left",
                        "color": rx.color_mode_cond(
                            light="gray.600", dark="rgba(255, 255, 255, 0.92)"
                        ),
                    },
                ),
                rx.link(
                    rx.button(
                        "Nossas áreas",
                        size="3",
                        style={
                            "background": "#f68b23",
                            "border_radius": "9999px",
                            "color": "white",
                            "padding": "0.75rem 1.5rem",
                            "_hover": {"background": "#f68b70"},
                        },
                    ),
                    href="#/areas",
                ),
                style={
                    "gap": "1.5rem",
                    "align_items": "flex-start",
                    "width": "100%",
                },
            ),
            style={
                "max_width": "42rem",  # 2xl
                "width": "100%",
                "justify_content": "center",
            },
        ),
        style={
            "width": "100%",
            "height": "30vh",
            "background_image": "url('/overlay.png')",
            "background_size": "cover",
            "background_position": "center center",
            "display": "flex",
            "justify_content": "center",
            "align_items": "center",
            "background_color": rx.color_mode_cond(
                light="rgba(255, 255, 255, 0.92)", dark="#1A202C"
            ),
        },
    )


@template
def home():
    return rx.box(
        call_to_action_with_video(),
        features(),
        testimonials(),
        with_background_image(),
        style={"overflow_x": "hidden"},  # Tirar barra de rolagem horizontal
    )
