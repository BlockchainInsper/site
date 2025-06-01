import reflex as rx
from components.Footer import footer
from components.Navbar import navbar
from typing import Callable


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.flex(
        navbar(),
        rx.box(
            page(),
            style={
                "width": "100%",
                "flex": "1",
                "min_height": "100%",
            },
        ),
        footer(),
        direction="column",
        min_height="100vh",
        style={
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
