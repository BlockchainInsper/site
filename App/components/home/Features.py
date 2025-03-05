import reflex as rx


def feature(text, icon, icon_bg):
    """Componente Feature que exibe um ícone com texto."""
    return rx.flex(
        rx.flex(
            icon,
            style={
                "width": "2rem",
                "height": "2rem",
                "align_items": "center",
                "justify_content": "center",
                "border_radius": "9999px",
                "background": icon_bg,
                "display": "flex",
            },
        ),
        rx.text(text, style={"font_weight": "600", "margin_left": "0.75rem"}),
        style={"display": "flex", "flex_direction": "row", "align_items": "center"},
    )


def features():
    return rx.box(
        rx.container(
            rx.grid(
                # COLUNA 1
                rx.vstack(
                    rx.heading(
                        "Reavaliando o presente e construindo o futuro",
                        style={"font_size": "1.5rem", "font_weight": "700"},
                    ),
                    rx.text(
                        "Buscamos criar um time altamente engajado e preparado "
                        "para enfrentar a nova onda de tecnologia no mercado de trabalho. "
                        "Seguimos com o objetivo de estimular o estudo e a adoção "
                        "dessa tecnologia no Brasil, criando conhecimento não apenas "
                        "para o agora, como também para o futuro.",
                        style={
                            "color": rx.color_mode_cond(
                                light="rgb(107, 114, 128)", dark="rgb(156, 163, 175)"
                            ),
                            "font_size": "1.125rem",
                        },
                    ),
                    rx.vstack(
                        rx.box(
                            feature(
                                text="Nossa Missão",
                                icon=rx.icon(
                                    tag="rocket",
                                    style={
                                        "color": "rgb(245, 158, 11)",  # yellow.500
                                        "width": "1.25rem",
                                        "height": "1.25rem",
                                    },
                                ),
                                icon_bg=rx.color_mode_cond(
                                    light="rgb(254, 243, 199)",  # yellow.100
                                    dark="rgb(116, 66, 16)",  # yellow.900
                                ),
                            ),
                            rx.text(
                                "Fomentar o desenvolvimento do ecossistema brasileiro "
                                "em torno da tecnologia blockchain, criando um futuro mais eficiente "
                                "através da tecnologia.",
                                style={
                                    "color": rx.color_mode_cond(
                                        light="rgb(107, 114, 128)",
                                        dark="rgb(156, 163, 175)",
                                    ),
                                    "margin_top": "0.5rem",
                                },
                            ),
                        ),
                        rx.divider(
                            style={
                                "border_color": rx.color_mode_cond(
                                    light="rgb(243, 244, 246)",  # gray.100
                                    dark="rgb(55, 65, 81)",  # gray.700
                                )
                            }
                        ),
                        rx.box(
                            feature(
                                text="Nossa Visão",
                                icon=rx.icon(
                                    tag="eye",
                                    style={
                                        "color": "rgb(34, 197, 94)",  # green.500
                                        "width": "1.25rem",
                                        "height": "1.25rem",
                                    },
                                ),
                                icon_bg=rx.color_mode_cond(
                                    light="rgb(220, 252, 231)",  # green.100
                                    dark="rgb(28, 69, 50)",  # green.900
                                ),
                            ),
                            rx.text(
                                "Capacitar os alunos com o melhor conteúdo e conectá-los ao mercado, "
                                "no intuito de incluir nosso país nesse cenário de inovação.",
                                style={
                                    "color": rx.color_mode_cond(
                                        light="rgb(107, 114, 128)",
                                        dark="rgb(156, 163, 175)",
                                    ),
                                    "margin_top": "0.5rem",
                                },
                            ),
                        ),
                        rx.divider(
                            style={
                                "border_color": rx.color_mode_cond(
                                    light="rgb(243, 244, 246)",  # gray.100
                                    dark="rgb(55, 65, 81)",  # gray.700
                                )
                            }
                        ),
                        rx.box(
                            feature(
                                text="Nossos Valores",
                                icon=rx.icon(
                                    tag="compass",
                                    style={
                                        "color": "rgb(168, 85, 247)",  # purple.500
                                        "width": "1.25rem",
                                        "height": "1.25rem",
                                    },
                                ),
                                icon_bg=rx.color_mode_cond(
                                    light="rgb(243, 232, 255)",  # purple.100
                                    dark="rgb(68, 51, 122)",  # purple.900
                                ),
                            ),
                            rx.text(
                                "Alto comprometimento, proatividade, inovação, "
                                "trabalho em equipe, multidisciplinaridade, excelência e eficiência.",
                                style={
                                    "color": rx.color_mode_cond(
                                        light="rgb(107, 114, 128)",
                                        dark="rgb(156, 163, 175)",
                                    ),
                                    "margin_top": "0.5rem",
                                },
                            ),
                        ),
                        style={
                            "gap": "1rem",
                            "width": "100%",
                            "align_items": "flex-start",
                        },
                    ),
                    style={"gap": "1rem", "width": "100%", "align_items": "flex-start"},
                ),
                # COLUNA 2
                rx.flex(
                    rx.image(
                        src="/insper.jpg",
                        alt="Auditório Insper",
                        style={
                            "width": "100%",
                            "height": "100%",
                            "border_radius": "0.375rem",
                            "object_fit": "cover",
                        },
                    ),
                    style={"width": "100%", "height": "100%"},
                ),
                style={
                    "display": "grid",
                    "grid_template_columns": rx.breakpoints(
                        initial="1fr", md="repeat(2, 1fr)"
                    ),
                    "gap": "2.5rem",
                },
            ),
            style={"max_width": "90rem", "padding": "3rem 1.5rem"},
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "color": rx.color_mode_cond(light="black", dark="white"),
        },
    )
