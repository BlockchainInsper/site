import reflex as rx
from App.Template import template
from components.members.Card import card  # Componente que vamos definir abaixo

# Definição dos dados estáticos de membros
time = {
    "ano": "2022.1",
    "chain": "matic",
    "address": "0x60063c63fb535c8ae98eff9730a3748e2a805458",
}

# Dados de exemplo dos membros (para evitar chamadas à API)
DIRETORES = [
    {
        "name": "João Silva",
        "cargo": "Presidente",
        "curso": "Engenharia da Computação",
        "ano_entrada": "2020",
        "image": "/members/member1.jpg",
    },
    {
        "name": "Ana Oliveira",
        "cargo": "Diretora de Tech",
        "curso": "Ciência da Computação",
        "ano_entrada": "2021",
        "image": "/members/member2.jpg",
    },
    {
        "name": "Carlos Santos",
        "cargo": "Diretor de Business",
        "curso": "Administração",
        "ano_entrada": "2020",
        "image": "/members/member3.jpg",
    },
]

BUSINESS = [
    {
        "name": "Juliana Lima",
        "cargo": "Analista de Business",
        "curso": "Administração",
        "ano_entrada": "2021",
        "image": "/members/member4.jpg",
    },
    {
        "name": "Ricardo Mendes",
        "cargo": "Analista de Business",
        "curso": "Economia",
        "ano_entrada": "2022",
        "image": "/members/member5.jpg",
    },
]

FINANCE = [
    {
        "name": "Marcos Pereira",
        "cargo": "Analista de Finance",
        "curso": "Economia",
        "ano_entrada": "2021",
        "image": "/members/member6.jpg",
    },
    {
        "name": "Fernanda Costa",
        "cargo": "Analista de Finance",
        "curso": "Ciências Contábeis",
        "ano_entrada": "2022",
        "image": "/members/member7.jpg",
    },
]

TECH = [
    {
        "name": "Lucas Almeida",
        "cargo": "Analista de Tech",
        "curso": "Engenharia da Computação",
        "ano_entrada": "2021",
        "image": "/members/member8.jpg",
    },
    {
        "name": "Mariana Souza",
        "cargo": "Analista de Tech",
        "curso": "Ciência da Computação",
        "ano_entrada": "2022",
        "image": "/members/member9.jpg",
    },
]


@rx.page(route="/members/actual", title="Blockchain Insper")
@template
def membros_atuais():
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
    #     # Container principal
    #     rx.container(
    #         rx.vstack(
    #             rx.heading(
    #                 "Conheça nosso time ",
    #                 rx.text(
    #                     time["ano"],
    #                     as_="span",
    #                     style={
    #                         "color": "#ED8936",  # cor orange.400
    #                     },
    #                 ),
    #                 style={
    #                     "font_weight": "600",
    #                     "font_size": rx.breakpoints(
    #                         initial="1.875rem",  # 3xl
    #                         sm="2.25rem",  # 4xl
    #                         md="3.75rem",  # 6xl
    #                     ),
    #                     "line_height": "110%",
    #                     "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
    #                     "text_align": "center",
    #                 },
    #             ),
    #             style={
    #                 "text_align": "center",
    #                 "align_items": "center",
    #                 "spacing": rx.breakpoints(initial="2rem", md="2.5rem"),
    #                 "padding_y": rx.breakpoints(initial="2.5rem", md="5rem"),
    #             },
    #         ),
    #         style={
    #             "max_width": "80rem",  # 5xl
    #             "margin": "0 auto",
    #             "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #         },
    #     ),
    #     # Conteúdo principal
    #     rx.box(
    #         # Seção Diretores
    #         rx.heading(
    #             "Presidente e Diretores",
    #             style={
    #                 "text_align": "center",
    #                 "font_size": "2.25rem",  # 4xl
    #                 "font_weight": "bold",
    #                 "margin_top": "2rem",
    #                 "margin_bottom": "1.5rem",
    #                 "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
    #             },
    #         ),
    #         rx.flex(
    #             *[
    #                 rx.box(
    #                     card(member),
    #                     style={
    #                         "padding": "0.75rem",
    #                     },
    #                 )
    #                 for member in DIRETORES
    #             ],
    #             style={
    #                 "gap": "30px",
    #                 "justify_content": "center",
    #                 "flex_wrap": "wrap",
    #                 "padding": "1rem",
    #                 "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #             },
    #         ),
    #         # Seção Business
    #         rx.heading(
    #             "Business",
    #             style={
    #                 "text_align": "center",
    #                 "font_size": "2.25rem",  # 4xl
    #                 "font_weight": "bold",
    #                 "margin_top": "3rem",
    #                 "margin_bottom": "1.5rem",
    #                 "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
    #             },
    #         ),
    #         rx.flex(
    #             *[
    #                 rx.box(
    #                     card(member),
    #                     style={
    #                         "padding": "0.75rem",
    #                     },
    #                 )
    #                 for member in BUSINESS
    #             ],
    #             style={
    #                 "gap": "30px",
    #                 "justify_content": "center",
    #                 "flex_wrap": "wrap",
    #                 "padding": "1rem",
    #                 "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #             },
    #         ),
    #         # Seção Finance
    #         rx.heading(
    #             "Finance",
    #             style={
    #                 "text_align": "center",
    #                 "font_size": "2.25rem",  # 4xl
    #                 "font_weight": "bold",
    #                 "margin_top": "3rem",
    #                 "margin_bottom": "1.5rem",
    #                 "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
    #             },
    #         ),
    #         rx.flex(
    #             *[
    #                 rx.box(
    #                     card(member),
    #                     style={
    #                         "padding": "0.75rem",
    #                     },
    #                 )
    #                 for member in FINANCE
    #             ],
    #             style={
    #                 "gap": "30px",
    #                 "justify_content": "center",
    #                 "flex_wrap": "wrap",
    #                 "padding": "1rem",
    #                 "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #             },
    #         ),
    #         # Seção Tech
    #         rx.heading(
    #             "Tech",
    #             style={
    #                 "text_align": "center",
    #                 "font_size": "2.25rem",  # 4xl
    #                 "font_weight": "bold",
    #                 "margin_top": "3rem",
    #                 "margin_bottom": "1.5rem",
    #                 "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
    #             },
    #         ),
    #         rx.flex(
    #             *[
    #                 rx.box(
    #                     card(member),
    #                     style={
    #                         "padding": "0.75rem",
    #                     },
    #                 )
    #                 for member in TECH
    #             ],
    #             style={
    #                 "gap": "30px",
    #                 "justify_content": "center",
    #                 "flex_wrap": "wrap",
    #                 "padding": "1rem",
    #                 "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #             },
    #         ),
    #         style={
    #             "width": "100%",
    #             "margin": "0 auto",
    #             "padding_bottom": "3rem",
    #             "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #         },
    #     ),
    #     style={
    #         "width": "100%",
    #         "background": rx.color_mode_cond(light="white", dark="#1A202C"),
    #     },
    # )
