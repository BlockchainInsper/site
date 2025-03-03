import reflex as rx
from components.fundo.fundo_info import info_fundo
from components.fundo.fundo_intro import intro_fundo


def fundo():
    return rx.box(
        intro_fundo(),
        info_fundo(),
    )
