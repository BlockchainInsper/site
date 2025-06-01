import reflex as rx
from components.learn.Blog import blog
from components.learn.Curso import curso
from components.learn.Pilares import pilares
from App.Template import template


@template
def aprenda():
    return rx.box(
        pilares(),
        curso(),
        blog(),
    )
