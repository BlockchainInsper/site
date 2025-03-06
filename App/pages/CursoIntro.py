import reflex as rx
from App.Template import template
from components.curso_intro.Content import content
from components.curso_intro.Presentation import presentation


@rx.page(route="/learn/curso-intro")
@template
def curso_intro():
    return rx.box(
        presentation(),
        content(),
    )
