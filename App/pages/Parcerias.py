import reflex as rx
from components.parcerias.Card import render_cards
from components.parcerias.partnerships_intro import intro_partnerships
from App.Template import template


@rx.page(route="/partnerships")
@template
def parceiros():
    return rx.box(
        intro_partnerships(),
        render_cards(),
    )
