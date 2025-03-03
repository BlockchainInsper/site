"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from App.Template import template
from pages.Home import home
from pages.Areas import areas
from pages.Fundo import fundo
from pages.Aprenda import aprenda
from pages.Parcerias import parceiros
from pages.ProcessoSeletivo import processo_seletivo
from pages.Contato import contato


@rx.page(route="/")
@template
def index():
    return rx.vstack(
        home(),
    )


@rx.page(route="/ps")
@template
def ps():
    return rx.vstack(
        processo_seletivo(),
    )


@rx.page(route="/members/actual")
@template
def team():
    return rx.vstack(
        rx.box(
            rx.box(
                rx.heading(
                    "Conhe\u00e7a nosso time ",
                    rx.text.span("2022.1", class_name="chakra-text css-1jkapds"),
                    class_name="chakra-heading css-124aq96",
                    as_="h2",
                    size="6",
                ),
                class_name="chakra-stack css-1tcwzuj",
            ),
            class_name="chakra-container css-1a3ltpp",
        ),
        rx.box(
            rx.box(
                rx.el.svg(
                    rx.el.svg.circle(
                        cx="50",
                        cy="50",
                        r="42",
                        stroke_width="10px",
                        class_name="chakra-progress__track css-ol3i12",
                    ),
                    rx.el.svg.circle(
                        cx="50",
                        cy="50",
                        r="42",
                        stroke_width="10px",
                        class_name="chakra-progress__indicator css-sp5bsz",
                    ),
                    viewbox="0 0 100 100",
                    class_name="css-jf70f3",
                ),
                class_name="chakra-progress css-120wkjd",
                aria_valuemax="100",
                aria_valuemin="0",
                role="progressbar",
                custom_attrs={"data-indeterminate": ""},
            ),
            class_name="css-gmuwbf",
        ),
        id="root",
    )


def alumni():
    pass


@rx.page(route="/areas")
@template
def nucleos():
    return rx.vstack(
        areas(),
    )


def projetos():
    pass


@rx.page(route="/fund")
@template
def fund():
    return rx.vstack(
        fundo(),
    )


@rx.page(route="/partnerships")
@template
def partners():
    return rx.vstack(
        parceiros(),
    )


@rx.page(route="/learn")
@template
def learn():
    return rx.vstack(
        aprenda(),
    )


@rx.page(route="/contact")
@template
def contact():
    return rx.vstack(
        contato(),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
)
app.add_page(index, route="/")
app.add_page(ps, route="/ps")
app.add_page(team, route="/members/actual")
app.add_page(nucleos, route="/areas")
app.add_page(fund, route="/fund")
app.add_page(partners, route="/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contact, route="/contact")
