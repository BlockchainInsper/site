"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from pages.Home import home


class State(rx.State):
    """The app state."""

    ...


def index():
    # Welcome Page (Index)
    return home()


app = rx.App()
app.add_page(index)
