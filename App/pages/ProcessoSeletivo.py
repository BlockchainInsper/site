import reflex as rx
from components.processo_seletivo.Intro import intro
from components.processo_seletivo.Summary import summary
from App.Template import template


@rx.page(route="/ps")
@template
def processo_seletivo():
    return rx.vstack(
        intro(),
        summary(),
    )
