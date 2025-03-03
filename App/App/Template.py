import reflex as rx
from components.Footer import footer
from components.Navbar import navbar
from typing import Callable


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            page(),
        ),
        footer(),
    )
