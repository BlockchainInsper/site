import reflex as rx


def blog_tags(tags, margin_top="1"):
    return rx.hstack(
        *[
            rx.box(
                tag,
                style={
                    "background": "#ED8936",
                    "color": "white",
                    "padding_x": "0.5rem",
                    "padding_y": "0.25rem",
                    "border_radius": "0.375rem",
                    "font_size": "0.875rem",
                    "font_weight": "600",
                },
            )
            for tag in tags
        ],
        style={
            "margin_top": margin_top,
            "spacing": "0.5rem",
        },
    )


def blog():
    return rx.box(
        rx.box(
            rx.heading(
                "Aprenda na prática",
                as_="h1",
                style={
                    "font_size": "2.25rem",
                    "font_weight": "bold",
                    "margin_bottom": "1.5rem",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
            ),
            # Primeiro artigo
            rx.box(
                rx.box(
                    rx.box(
                        rx.link(
                            rx.image(
                                src="/blog/arteAgro.png",
                                alt="some good alt text",
                                style={
                                    "border_radius": "0.5rem",
                                    "object_fit": "contain",
                                    "width": "100%",
                                },
                            ),
                            href="https://drive.google.com/file/d/1zlmy-Juu6i6HVZw7WCYQs_rC4CEDZSFy/view",
                            is_external=True,
                            style={
                                "text_decoration": "none",
                                "_hover": {"text_decoration": "none"},
                            },
                        ),
                        style={
                            "width": rx.breakpoints(initial="100%", sm="85%"),
                            "z_index": "2",
                            "margin_left": rx.breakpoints(initial="0", sm="5%"),
                            "margin_top": "5%",
                        },
                    ),
                    rx.box(
                        rx.box(
                            style={
                                "background": "radial-gradient("
                                + rx.color_mode_cond(
                                    light="rgba(237, 137, 54, 0.6) 1px, transparent 1px",
                                    dark="rgba(237, 137, 54, 0.3) 1px, transparent 1px",
                                )
                                + ")",
                                "background_size": "20px 20px",
                                "opacity": "0.4",
                                "height": "100%",
                            }
                        ),
                        style={
                            "z_index": "1",
                            "width": "100%",
                            "position": "absolute",
                            "height": "100%",
                            "background": rx.color_mode_cond(
                                light="transparent", dark="rgba(26, 32, 44, 0.3)"
                            ),
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "margin_right": "0.75rem",
                        "position": "relative",
                        "align_items": "center",
                    },
                ),
                rx.box(
                    blog_tags(["Agropecuária", "Report"]),
                    rx.heading(
                        rx.link(
                            "Report do setor Agropecuário",
                            href="https://drive.google.com/file/d/1zlmy-Juu6i6HVZw7WCYQs_rC4CEDZSFy/view",
                            is_external=True,
                            style={
                                "text_decoration": "none",
                                "_hover": {"text_decoration": "none"},
                                "color": rx.color_mode_cond(
                                    light="#2D3748", dark="#F7FAFC"
                                ),
                            },
                        ),
                        style={
                            "margin_top": "0.25rem",
                            "font_size": "2.25rem",
                            "font_weight": "bold",
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                        },
                    ),
                    rx.text(
                        "O setor agropecuário é um dos principais setores econômicos do Brasil, "
                        "representando uma parcela de 21% do PIB nacional. Atualmente, ele encontra "
                        "diversos problemas estruturais, os quais poderiam ser solucionados através "
                        "da tecnologia blockchain. No report a seguir esses tópicos serão abordados e discutidos.",
                        style={
                            "margin_top": "0.5rem",
                            "color": rx.color_mode_cond(
                                light="#4A5568", dark="#E2E8F0"
                            ),
                            "font_size": "1.125rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "flex_direction": "column",
                        "justify_content": "center",
                        "margin_top": rx.breakpoints(initial="0.75rem", sm="0"),
                    },
                ),
                style={
                    "margin_top": rx.breakpoints(initial="0.25rem", sm="1.25rem"),
                    "display": "flex",
                    "flex_direction": rx.breakpoints(initial="column", sm="row"),
                    "justify_content": "space-between",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    "padding": "1.5rem",
                    "border_radius": "0.5rem",
                },
            ),
            # Segundo artigo
            rx.box(
                rx.box(
                    blog_tags(["Saúde", "Report"]),
                    rx.heading(
                        rx.link(
                            "Report do setor da Saúde",
                            href="https://drive.google.com/file/d/1KzcVDm7Ipq4yGfkN1DBzlBwWOwS-DfYz/view",
                            is_external=True,
                            style={
                                "text_decoration": "none",
                                "_hover": {"text_decoration": "none"},
                                "color": rx.color_mode_cond(
                                    light="#2D3748", dark="#F7FAFC"
                                ),
                            },
                        ),
                        style={
                            "margin_top": "0.25rem",
                            "font_size": "2.25rem",
                            "font_weight": "bold",
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                        },
                    ),
                    rx.text(
                        "Sendo o assunto de maior importância recentemente, o setor de saúde aparece como enfoque de 2020 "
                        "pela situação vivida com a pandemia do COVID-19. Nesse ano, foi possível notar a importância e os "
                        "benefícios de um sistema de saúde bem estruturado. No report a seguir esses tópicos serão abordados e discutidos.",
                        style={
                            "margin_top": "0.5rem",
                            "color": rx.color_mode_cond(
                                light="#4A5568", dark="#E2E8F0"
                            ),
                            "font_size": "1.125rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "flex_direction": "column",
                        "justify_content": "center",
                        "margin_top": rx.breakpoints(initial="0.75rem", sm="0"),
                    },
                ),
                rx.box(
                    rx.box(
                        rx.link(
                            rx.image(
                                src="/blog/arteHealth.png",
                                alt="some good alt text",
                                style={
                                    "border_radius": "0.5rem",
                                    "object_fit": "contain",
                                    "width": "100%",
                                },
                            ),
                            href="https://drive.google.com/file/d/1KzcVDm7Ipq4yGfkN1DBzlBwWOwS-DfYz/view",
                            is_external=True,
                            style={
                                "text_decoration": "none",
                                "_hover": {"text_decoration": "none"},
                            },
                        ),
                        style={
                            "width": rx.breakpoints(initial="100%", sm="85%"),
                            "z_index": "2",
                            "margin_left": rx.breakpoints(initial="0", sm="5%"),
                            "margin_top": "5%",
                        },
                    ),
                    rx.box(
                        rx.box(
                            style={
                                "background": "radial-gradient("
                                + rx.color_mode_cond(
                                    light="rgba(237, 137, 54, 0.6) 1px, transparent 1px",
                                    dark="rgba(237, 137, 54, 0.3) 1px, transparent 1px",
                                )
                                + ")",
                                "background_size": "20px 20px",
                                "opacity": "0.4",
                                "height": "100%",
                            }
                        ),
                        style={
                            "z_index": "1",
                            "width": "100%",
                            "position": "absolute",
                            "height": "100%",
                            "background": rx.color_mode_cond(
                                light="transparent", dark="rgba(26, 32, 44, 0.3)"
                            ),
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "margin_right": "0.75rem",
                        "position": "relative",
                        "align_items": "center",
                    },
                ),
                style={
                    "margin_top": rx.breakpoints(initial="0.25rem", sm="1.25rem"),
                    "display": "flex",
                    "flex_direction": rx.breakpoints(initial="column", sm="row"),
                    "justify_content": "space-between",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    "padding": "1.5rem",
                    "border_radius": "0.5rem",
                },
            ),
            style={
                "max_width": "80rem",
                "padding": "3rem",
                "margin": "0 auto",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "width": "full",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
