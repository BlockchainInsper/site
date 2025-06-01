import reflex as rx
from components.contato.info_contato import contato_info
from components.contato.location import location_info
from App.Template import template


@template
def contato():
    return rx.box(
        contato_info(),
        location_info(),
    )
