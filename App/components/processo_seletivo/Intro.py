import reflex as rx
from components.icons.icons import discord_icon


def feature(heading, text):
    return rx.box(
        rx.heading(
            heading,
            style={
                "font_size": "1.25rem",
                "font_weight": "700",
                "margin_bottom": "0.5rem",
                "color": rx.color_mode_cond(light="rgb(17, 24, 39)", dark="white"),
            },
            as_="h3",
        ),
        rx.text(
            text,
            style={
                "color": rx.color_mode_cond(light="rgb(17, 24, 39)", dark="white"),
            },
        ),
        style={},
    )


def intro():
    return rx.box(
        rx.box(
            # Grid de duas colunas (1 em mobile)
            rx.grid(
                # Coluna 1 - Título e botões
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Nosso Processo Seletivo chegou!",
                            style={
                                "font_size": "1.875rem",
                                "font_weight": "700",
                                "color": rx.color_mode_cond(
                                    light="rgb(17, 24, 39)", dark="white"
                                ),
                            },
                            as_="h2",
                        ),
                        rx.link(
                            rx.button(
                                "Inscrever-se",
                                style={
                                    "background": "#f68b23",
                                    "color": "white",
                                    "border_radius": "0.375rem",
                                    "padding_left": "1rem",
                                    "padding_right": "1rem",
                                    "padding_top": "0.5rem",
                                    "padding_bottom": "0.5rem",
                                    "_hover": {
                                        "background": "#f68b70",
                                    },
                                },
                            ),
                            href="https://docs.google.com/forms/d/e/1FAIpQLScQyW4RGcwtcNAAVtYj3iFJdgJ4Khq07rSluQo5tWROKWYxow/viewform",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    # SVG personalizado do Discord
                                    discord_icon(1, 16),
                                    rx.text(
                                        "Discord",
                                        style={
                                            "line_height": "1.1",
                                            "color": "white",
                                        },
                                    ),
                                    style={
                                        "align_items": "center",
                                    },
                                ),
                                style={
                                    "background": "#5865F2",
                                    "color": "white",
                                    "border_radius": "0.375rem",
                                    "padding_left": "1rem",
                                    "padding_right": "1rem",
                                    "padding_top": "0.5rem",
                                    "padding_bottom": "0.5rem",
                                    "_hover": {
                                        "background": "rgba(88, 101, 242, 0.9)",
                                    },
                                },
                            ),
                            href="https://discord.gg/jdK5yB48Mm",
                            is_external=True,
                        ),
                        spacing="5",
                        style={
                            "align_items": "flex_start",
                        },
                    ),
                ),
                # Coluna 2 - Texto descritivo
                rx.box(
                    rx.text(
                        "O maior experimento financeiro e sociológico do século XXI, o "
                        "Bitcoin veio solucionar diversos problemas antes sem solução. A "
                        "Blockchain Insper vai te dar base para entender o que está por "
                        "trás da construção do protocolo e o que motivou Satoshi Nakamoto a "
                        "desenvolvê-lo, entre muitas outras coisas que rondam essa "
                        "tecnologia que está revolucionando a economia mundial. Além disso, "
                        "temos parcerias com as maiores empresas do mercado para, além de "
                        "ganhar conhecimento, saber como funcionam os projetos na prática.",
                        style={
                            "color": rx.color_mode_cond(
                                light="rgb(17, 24, 39)", dark="white"
                            ),
                        },
                    ),
                ),
                # Configuração do grid
                columns=rx.breakpoints(initial="1", sm="2"),
                gap="1rem",
                style={
                    "width": "100%",
                },
            ),
            # Divisor horizontal
            rx.divider(
                style={
                    "margin_top": "3rem",
                    "margin_bottom": "3rem",
                    "border_color": "rgb(229, 231, 235)",
                },
            ),
            # Grid de quatro colunas
            rx.grid(
                # Fase 1
                feature(
                    heading="Primeira Fase",
                    text="Preenchimento de um Forms com detalhes pessoais e perguntas de caráter opinativo.",
                ),
                # Fase 2
                feature(
                    heading="Segunda Fase",
                    text="Resolução de um case elaborado em parceria com o BTG e com a Mynt.",
                ),
                # Fase 3
                feature(
                    heading="Terceira Fase",
                    text="Entrevista individual para conhecer melhor o candidato com perguntas pessoais e possivelmente técnicas.",
                ),
                # Fase 4
                feature(
                    heading="Programa de Trainees",
                    text="Desempenho no Curso de Introdução à Blockchain e Projeto Interno Aplicado (nessa fase, os candidatos já ganham entre 5 e 10 horas complementares).",
                ),
                # Configuração do grid
                columns=rx.breakpoints(initial="1", sm="2", md="4"),
                gap=rx.breakpoints(initial="2rem", sm="3rem", md="4rem"),
                style={
                    "width": "100%",
                },
            ),
            # Divisor horizontal
            rx.divider(
                style={
                    "margin_top": "3rem",
                    "margin_bottom": "3rem",
                    "border_color": "rgb(229, 231, 235)",
                },
            ),
            # Configuração do container
            style={
                "max_width": "80rem",
                "margin_left": "auto",
                "margin_right": "auto",
                "margin_top": "2.5rem",
                "padding": "1rem",
            },
        ),
        style={
            "width": "100%",
            "padding_top": "1rem",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "color": rx.color_mode_cond(light="rgb(17, 24, 39)", dark="white"),
        },
    )
