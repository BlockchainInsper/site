import reflex as rx
from components.processo_seletivo.Intro import intro
from components.processo_seletivo.Summary import summary


def processo_seletivo():
    return rx.box(
        intro(),
        summary(),
    )
