import reflex as rx
from components.contato.info_contato import contato_info
from components.contato.location import location_info


def contato():
    return rx.box(
        contato_info(),
        location_info(),
    )
