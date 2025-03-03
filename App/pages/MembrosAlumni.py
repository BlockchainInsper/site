import reflex as rx
from App.Template import template


@rx.page(route="/members/alumni")
@template
def membros_alumni():
    return rx.box(
        rx.text("Membros Alumni"),
        rx.text("Aqui estão os membros alumni do grupo."),
    )
