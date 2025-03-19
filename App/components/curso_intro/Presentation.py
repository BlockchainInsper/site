import reflex as rx


def feature(text, icon, icon_bg):
    return rx.hstack(
        rx.flex(
            icon,
            style={
                "width": "2rem",  # w={8}
                "height": "2rem",  # h={8}
                "align_items": "center",
                "justify_content": "center",
                "border_radius": "9999px",  # rounded={'full'}
                "background": icon_bg,
            },
        ),
        rx.text(
            text,
            style={
                "font_weight": "600",
                "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
            },
        ),
        align="center",
    )


def presentation():
    analytics_icon = rx.icon(
        "chart-line",
        style={
            "color": "#ECC94B",  # yellow.500
            "width": "1.25rem",  # w={5}
            "height": "1.25rem",  # h={5}
        },
    )

    bitcoin_icon = rx.icon(
        "bitcoin",
        style={
            "color": "#38A169",  # green.500
            "width": "1.25rem",  # w={5}
            "height": "1.25rem",  # h={5}
        },
    )

    return rx.box(
        rx.container(
            rx.grid(
                rx.heading(
                    "Curso de Introdução à Blockchain",
                    style={
                        "font_weight": "bold",
                        "font_size": "1.875rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.vstack(
                    rx.vstack(
                        rx.box(
                            feature(
                                "Sobre",
                                analytics_icon,
                                rx.color_mode_cond(
                                    light="#FFFFF0", dark="#744210"
                                ),  # yellow.100, yellow.900
                            ),
                            rx.text(
                                "O maior experimento financeiro e sociológico do século XXI, o Bitcoin veio solucionar diversos problemas antes sem solução. "
                                "O Curso Fundamental vai te dar base para entender o que está por trás da construção do protocolo e o que motivou "
                                "Satoshi Nakamoto a desenvolvê-lo, entre muitas outras coisas que rondam essa tecnologia que está revolucionando a economia mundial.",
                                style={
                                    "color": "#718096",  # gray.500
                                    "font_size": "1rem",  # medium
                                    "margin_top": "1.25rem",  # marginTop={5}
                                },
                            ),
                        ),
                        rx.divider(
                            style={
                                "border_color": rx.color_mode_cond(
                                    light="#EDF2F7", dark="#4A5568"
                                ),  # gray.100, gray.700
                                "margin_y": "1rem",
                            },
                        ),
                        rx.box(
                            feature(
                                "Objetivos",
                                bitcoin_icon,
                                rx.color_mode_cond(
                                    light="#F0FFF4", dark="#1C4532"
                                ),  # green.100, green.900
                            ),
                            rx.text(
                                "O curso está dividido em 7 módulos (Introdução, Bitcoin, Blockchain, Crypto Assets, Chains, Tecnologia e Regulação). "
                                "Dentro desses módulos, há tópicos com textos ou vídeos explicando o assunto, existe mais de um link sobre o tema, "
                                "caso já tenha entendido o conceito sinta-se à vontade para passar para o próximo tema.\n\n"
                                "O curso será disponibilizado nesse site de seguinte maneira: cada página é um módulo, dentro desses módulos existem "
                                "subtemas que se relacionam com o assunto principal, e em seguida os links com os conteúdos.",
                                style={
                                    "color": "#718096",  # gray.500
                                    "font_size": "1rem",  # medium
                                    "margin_top": "1.25rem",  # marginTop={5}
                                    "white_space": "pre-wrap",  # Para preservar quebras de linha
                                },
                            ),
                        ),
                        spacing="4",
                        style={
                            "divide": "solid 1px",
                            "divide_color": rx.color_mode_cond(
                                light="#EDF2F7", dark="#4A5568"
                            ),  # gray.100, gray.700
                        },
                    ),
                    spacing="4",
                ),
                gap="2.5rem",
                style={
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
            style={
                "max_width": "80rem",  # 5xl
                "margin": "0 auto",
            },
        ),
        style={
            "padding_y": "2rem",  # py={12} = 3rem
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
