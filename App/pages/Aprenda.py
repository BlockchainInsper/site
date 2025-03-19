import reflex as rx
from components.learn.Blog import blog
from components.learn.Curso import curso
from components.learn.Pilares import pilares
from App.Template import template


@rx.page(route="/learn", title="Blockchain Insper")
@template
def aprenda():
    return rx.box(
        pilares(),
        curso(),
        blog(),
    )
