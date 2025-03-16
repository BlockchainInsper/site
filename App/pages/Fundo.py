import reflex as rx
from components.fundo.fundo_info import info_fundo
from components.fundo.fundo_intro import intro_fundo
from components.fundo.fundo_graph import graph_fundo
from App.Template import template


@rx.page(route="/fund")
@template
def fundo():
    return rx.box(
        # Container principal
        rx.container(
            rx.vstack(
                rx.heading(
                    "Em breve... ",
                    rx.text(
                        "Essa página está sendo atualizada para a atual gestão.",
                        # time["ano"],
                        as_="span",
                        style={
                            "color": "#ED8936",  # cor orange.400
                        },
                    ),
                    style={
                        "font_weight": "600",
                        "font_size": rx.breakpoints(
                            initial="1.875rem",  # 3xl
                            sm="2.25rem",  # 4xl
                            md="3.75rem",  # 6xl
                        ),
                        "line_height": "110%",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                        "text_align": "center",
                    },
                ),
                style={
                    "text_align": "center",
                    "align_items": "center",
                    "spacing": rx.breakpoints(initial="2rem", md="2.5rem"),
                    "padding_y": rx.breakpoints(initial="2.5rem", md="5rem"),
                },
            ),
            style={
                "max_width": "80rem",  # 5xl
                "margin": "0 auto",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
    # return rx.box(
    #     intro_fundo(),
    #     graph_fundo(),
    #     info_fundo(),
    # )
