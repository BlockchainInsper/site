import reflex as rx
from App.Template import template


@rx.page(route="/projects")
@template
def projetos():
    return rx.box(
        rx.text("Projetos"),
        rx.text("Aqui estão alguns dos projetos que desenvolvemos."),
    )
