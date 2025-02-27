"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from components.Navbar import navbar
from components.Footer import footer
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials
from components.home.With_Background_Image import with_background_image
from components.processo_seletivo.Intro import intro
from components.processo_seletivo.Summary import summary
from pages.Areas import areas
from components.fundo.intro import intro_fundo
from components.fundo.fundo_info import info_fundo
from components.parcerias.intro import intro_partnerships
from components.parcerias.Card import render_cards
from components.learn.Pilares import pilares
from components.learn.Curso import curso
from components.learn.Blog import blog
from components.contato.info_contato import contato_info
from components.contato.location import location_info


class State(rx.State):
    """The app state."""

    ...


def index():
    # Welcome Page (Index)
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                call_to_action_with_video(),
                features(),
                testimonials(),
                with_background_image(),
                footer(),
                id="root",
            )
        )
    )


def processo_seletivo():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                intro(),
                summary(),
                footer(),
                id="root",
            )
        )
    )


def time():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Conhe\u00e7a nosso time ",
                            rx.text.span(
                                "2022.1", class_name="chakra-text css-1jkapds"
                            ),
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
                footer(),
                id="root",
            )
        )
    )


def alumni():
    pass


def nucleos():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                areas(),
                footer(),
                id="root",
            )
        )
    )


def projetos():
    pass


def fundo():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                intro_fundo(),
                info_fundo(),
                footer(),
                id="root",
            )
        )
    )


def parceiros():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                intro_partnerships(),
                render_cards(),
                footer(),
                id="root",
            )
        )
    )


def aprenda():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                pilares(),
                curso(),
                blog(),
                footer(),
                id="root",
            )
        )
    )


def contato():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                contato_info(),
                location_info(),
                footer(),
                id="root",
            )
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(processo_seletivo, route="/ps")
app.add_page(time, route="/members/actual")
app.add_page(nucleos, route="/areas")
app.add_page(fundo, route="/fund")
app.add_page(parceiros, route="/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contato, route="/contact")
