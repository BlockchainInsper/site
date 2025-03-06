import reflex as rx


def curso():
    return rx.box(
        rx.box(
            rx.stack(
                rx.heading(
                    "Aprenda blockchain ",
                    rx.el.br(),
                    rx.text(
                        "agora",
                        as_="span",
                        style={
                            "color": "#f68b23",
                        },
                    ),
                    style={
                        "font_weight": "600",
                        "font_size": rx.breakpoints(
                            initial="1.5rem", sm="2.25rem", md="3.75rem"
                        ),
                        "line_height": "110%",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.text(
                    "A Blockchain Insper tem o prazer de apresentar o Curso de Introdução à Blockchain! "
                    "Na linha de contribuir para o acesso à informação e o fomento do estudo das novas tecnologias, "
                    "o curso é realizado no formato online, e é aberto para qualquer pessoa. "
                    "Os conteúdos foram escolhidos pelos membros da entidade, abordando desde contexto histórico até futuras "
                    "perspectivas da tecnologia.",
                    style={
                        "color": rx.color_mode_cond(light="#A0AEC0", dark="#CBD5E0"),
                    },
                ),
                rx.stack(
                    rx.link(
                        rx.button(
                            "Vamos começar!",
                            style={
                                "background": "#f68b23",
                                "color": "white",
                                "border_radius": "9999px",
                                "padding_x": "1.5rem",
                                "_hover": {
                                    "background": "#f68b70",
                                },
                            },
                        ),
                        href="#/learn/curso-intro",
                    ),
                    style={
                        "direction": "column",
                        "spacing": "0.75rem",
                        "align": "center",
                        "align_self": "center",
                        "position": "relative",
                    },
                ),
                style={
                    "flex_direction": "column",
                    "align_items": "center",
                    "justify_content": "center",
                    "text_align": "center",
                    "spacing": rx.breakpoints(initial="2rem", md="3.5rem"),
                    "padding_y": rx.breakpoints(initial="5rem", md="7.5rem"),
                },
            ),
            style={
                "max_width": "48rem",
                "padding_y": "2.5rem",
                "margin": "0 auto",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "width": "full",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
