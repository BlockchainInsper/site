import reflex as rx
from App.Template import template
from components.members.Card import (
    card,
)  # Componente que já definimos anteriormente

# Dados estáticos para os membros alumni
times = [
    {
        "ano": "2021.2",
        "chain": "polygon",
        "address": "0x7efFf2fb972EB77f61922af70820053566F483C5",
    }
]

# Dados de exemplo para os ex-membros
PRESIDENTES = [
    {
        "name": "Roberto Silva",
        "cargo": "Presidente",
        "curso": "Engenharia da Computação",
        "ano_entrada": "2018",
        "image": "/members/alumni1.jpg",
    }
]

DIRETORES = [
    {
        "name": "Luiza Mendes",
        "cargo": "Diretora de Tech",
        "curso": "Ciência da Computação",
        "ano_entrada": "2019",
        "image": "/members/alumni2.jpg",
    },
    {
        "name": "Pedro Santos",
        "cargo": "Diretor de Business",
        "curso": "Administração",
        "ano_entrada": "2019",
        "image": "/members/alumni3.jpg",
    },
]

BUSINESS = [
    {
        "name": "Clara Oliveira",
        "cargo": "Analista de Business",
        "curso": "Administração",
        "ano_entrada": "2019",
        "image": "/members/alumni4.jpg",
    },
    {
        "name": "Rafael Costa",
        "cargo": "Analista de Business",
        "curso": "Economia",
        "ano_entrada": "2020",
        "image": "/members/alumni5.jpg",
    },
]

FINANCE = [
    {
        "name": "Beatriz Lima",
        "cargo": "Analista de Finance",
        "curso": "Economia",
        "ano_entrada": "2019",
        "image": "/members/alumni6.jpg",
    },
    {
        "name": "Gabriel Almeida",
        "cargo": "Analista de Finance",
        "curso": "Ciências Contábeis",
        "ano_entrada": "2020",
        "image": "/members/alumni7.jpg",
    },
]

TECH = [
    {
        "name": "Carla Santos",
        "cargo": "Analista de Tech",
        "curso": "Engenharia da Computação",
        "ano_entrada": "2019",
        "image": "/members/alumni8.jpg",
    },
    {
        "name": "Bruno Ferreira",
        "cargo": "Analista de Tech",
        "curso": "Ciência da Computação",
        "ano_entrada": "2020",
        "image": "/members/alumni9.jpg",
    },
]


@rx.page(route="/members/alumni")
@template
def membros_alumni():
    # Mock do loading state - você pode substituir por um state real do Reflex
    is_loading = False

    return rx.box(
        # Container principal
        rx.container(
            rx.vstack(
                rx.heading(
                    "Conheça nossos membros ",
                    rx.text(
                        "Alumni",
                        as_="span",
                        style={
                            "color": "#ED8936",  # orange.400
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
        # Conteúdo condicional - mostra carregamento ou o conteúdo
        rx.cond(
            is_loading,
            rx.center(
                rx.spinner(
                    is_indeterminate=True,
                    style={
                        "color": "#ED8936",  # orange.400
                    },
                ),
                style={
                    "padding": "2rem",
                    "width": "100%",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
            rx.box(
                # Seção Ex-Presidentes
                rx.heading(
                    "Ex-Presidentes",
                    style={
                        "text_align": "center",
                        "font_size": "2.25rem",  # 4xl
                        "font_weight": "bold",
                        "margin_top": "2rem",
                        "margin_bottom": "1.5rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    *[
                        rx.box(
                            card(member),
                            style={
                                "padding": "0.75rem",
                            },
                        )
                        for member in PRESIDENTES
                    ],
                    style={
                        "gap": "30px",
                        "justify_content": "center",
                        "flex_wrap": "wrap",
                        "padding": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                # Seção Ex-Diretores
                rx.heading(
                    "Ex-Diretores",
                    style={
                        "text_align": "center",
                        "font_size": "2.25rem",  # 4xl
                        "font_weight": "bold",
                        "margin_top": "3rem",
                        "margin_bottom": "1.5rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    *[
                        rx.box(
                            card(member),
                            style={
                                "padding": "0.75rem",
                            },
                        )
                        for member in DIRETORES
                    ],
                    style={
                        "gap": "30px",
                        "justify_content": "center",
                        "flex_wrap": "wrap",
                        "padding": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                # Seção Ex-Membros de Business
                rx.heading(
                    "Ex-Membros de Business",
                    style={
                        "text_align": "center",
                        "font_size": "2.25rem",  # 4xl
                        "font_weight": "bold",
                        "margin_top": "3rem",
                        "margin_bottom": "1.5rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    *[
                        rx.box(
                            card(member),
                            style={
                                "padding": "0.75rem",
                            },
                        )
                        for member in BUSINESS
                    ],
                    style={
                        "gap": "30px",
                        "justify_content": "center",
                        "flex_wrap": "wrap",
                        "padding": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                # Seção Ex-Membros de Finance
                rx.heading(
                    "Ex-Membros de Finance",
                    style={
                        "text_align": "center",
                        "font_size": "2.25rem",  # 4xl
                        "font_weight": "bold",
                        "margin_top": "3rem",
                        "margin_bottom": "1.5rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    *[
                        rx.box(
                            card(member),
                            style={
                                "padding": "0.75rem",
                            },
                        )
                        for member in FINANCE
                    ],
                    style={
                        "gap": "30px",
                        "justify_content": "center",
                        "flex_wrap": "wrap",
                        "padding": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                # Seção Ex-Membros de Tech
                rx.heading(
                    "Ex-Membros de Tech",
                    style={
                        "text_align": "center",
                        "font_size": "2.25rem",  # 4xl
                        "font_weight": "bold",
                        "margin_top": "3rem",
                        "margin_bottom": "1.5rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    *[
                        rx.box(
                            card(member),
                            style={
                                "padding": "0.75rem",
                            },
                        )
                        for member in TECH
                    ],
                    style={
                        "gap": "30px",
                        "justify_content": "center",
                        "flex_wrap": "wrap",
                        "padding": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                style={
                    "width": "100%",
                    "margin": "0 auto",
                    "padding_bottom": "3rem",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
