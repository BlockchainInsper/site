import reflex as rx
from components.icons.icons import discord_icon
from App.States import ContactFormState


def contato_info():
    accent_color = "#F68B23"

    return rx.box(
        rx.box(
            rx.flex(
                # Coluna da esquerda - Informações de contato
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Entre em contato",
                            style={
                                "font_size": "2rem",
                                "font_weight": "700",
                                "color": rx.color_mode_cond(
                                    light="#2D3748", dark="#F7FAFC"
                                ),
                                "margin_bottom": "1.5rem",
                            },
                        ),
                        rx.text(
                            "Estamos ansiosos para ouvir você! Envie sua mensagem e entraremos em contato o mais rápido possível.",
                            style={
                                "color": rx.color_mode_cond(
                                    light="#4A5568", dark="#CBD5E0"
                                ),
                                "line_height": "1.6",
                                "margin_bottom": "2rem",
                                "max_width": "400px",
                            },
                        ),
                        # Informações de contato detalhadas
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.icon(
                                        "mail",
                                        style={
                                            "color": accent_color,
                                            "font_size": "1.25rem",
                                        },
                                    ),
                                    rx.text(
                                        "blockchainsper@gmail.com",
                                        style={
                                            "color": rx.color_mode_cond(
                                                light="#4A5568", dark="#E2E8F0"
                                            ),
                                        },
                                    ),
                                    align="center",
                                    spacing="3",
                                ),
                                rx.hstack(
                                    rx.icon(
                                        "map_pin",
                                        style={
                                            "color": accent_color,
                                            "font_size": "1.25rem",
                                        },
                                    ),
                                    rx.text(
                                        "R. Quatá, 300 - Vila Olímpia, São Paulo",
                                        style={
                                            "color": rx.color_mode_cond(
                                                light="#4A5568", dark="#E2E8F0"
                                            ),
                                        },
                                    ),
                                    align="center",
                                    spacing="3",
                                ),
                                align="start",
                                spacing="4",
                            ),
                            style={
                                "margin_bottom": "2.5rem",
                            },
                        ),
                        # Redes sociais
                        rx.box(
                            rx.text(
                                "Siga-nos nas redes sociais",
                                style={
                                    "font_weight": "600",
                                    "margin_bottom": "1rem",
                                    "color": rx.color_mode_cond(
                                        light="#2D3748", dark="#F7FAFC"
                                    ),
                                },
                            ),
                            rx.flex(
                                rx.link(
                                    rx.box(
                                        discord_icon(20, "20px"),
                                        style={
                                            "width": "40px",
                                            "height": "40px",
                                            "display": "flex",
                                            "align_items": "center",
                                            "justify_content": "center",
                                            "border_radius": "50%",
                                            "color": "rgba(255, 255, 255, 0.92)",
                                            "background": rx.color_mode_cond(
                                                light="#F7FAFC", dark="#2D3748"
                                            ),
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": accent_color,
                                                "transform": "translateY(-3px)",
                                            },
                                        },
                                    ),
                                    href="https://discord.gg/jdK5yB48Mm",
                                    is_external=True,
                                ),
                                rx.link(
                                    rx.box(
                                        rx.icon(
                                            "mail",
                                            size=18,
                                        ),
                                        style={
                                            "width": "40px",
                                            "height": "40px",
                                            "display": "flex",
                                            "align_items": "center",
                                            "justify_content": "center",
                                            "border_radius": "50%",
                                            "color": "rgba(255, 255, 255, 0.92)",
                                            "background": rx.color_mode_cond(
                                                light="#F7FAFC", dark="#2D3748"
                                            ),
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": accent_color,
                                                "transform": "translateY(-3px)",
                                            },
                                        },
                                    ),
                                    href="mailto:blockchainsper@gmail.com",
                                    is_external=True,
                                ),
                                rx.link(
                                    rx.box(
                                        rx.icon(
                                            "linkedin",
                                            size=18,
                                        ),
                                        style={
                                            "width": "40px",
                                            "height": "40px",
                                            "display": "flex",
                                            "align_items": "center",
                                            "justify_content": "center",
                                            "border_radius": "50%",
                                            "color": "rgba(255, 255, 255, 0.92)",
                                            "background": rx.color_mode_cond(
                                                light="#F7FAFC", dark="#2D3748"
                                            ),
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": accent_color,
                                                "transform": "translateY(-3px)",
                                            },
                                        },
                                    ),
                                    href="https://www.linkedin.com/company/blockchain-insper/",
                                    is_external=True,
                                ),
                                rx.link(
                                    rx.box(
                                        rx.icon(
                                            "instagram",
                                            size=18,
                                        ),
                                        style={
                                            "width": "40px",
                                            "height": "40px",
                                            "display": "flex",
                                            "align_items": "center",
                                            "justify_content": "center",
                                            "border_radius": "50%",
                                            "color": "rgba(255, 255, 255, 0.92)",
                                            "background": rx.color_mode_cond(
                                                light="#F7FAFC", dark="#2D3748"
                                            ),
                                            "transition": "all 0.3s ease",
                                            "_hover": {
                                                "background": accent_color,
                                                "transform": "translateY(-3px)",
                                            },
                                        },
                                    ),
                                    href="https://www.instagram.com/blockchainsper/",
                                    is_external=True,
                                ),
                                gap="1rem",
                                style={
                                    "margin_top": "0.5rem",
                                },
                            ),
                        ),
                        align="stretch",
                        style={
                            "height": "100%",
                        },
                    ),
                    style={
                        "width": rx.breakpoints(initial="100%", md="40%"),
                        "padding": "2rem",
                    },
                ),
                # Coluna da direita - Formulário
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "Nome",
                                    style={
                                        "font_weight": "500",
                                        "margin_bottom": "0.5rem",
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#E2E8F0"
                                        ),
                                    },
                                ),
                                rx.input(
                                    placeholder="Seu nome completo",
                                    id="name",
                                    name="name",
                                    type="text",
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#2D3748", dark="white"
                                        ),
                                        "background": rx.color_mode_cond(
                                            light="white", dark="#2D3748"
                                        ),
                                        "border": rx.color_mode_cond(
                                            light="1px solid #E2E8F0",
                                            dark="1px solid #4A5568",
                                        ),
                                        "border_radius": "0.375rem",
                                        "padding_x": "1rem",
                                        "width": "100%",
                                        "outline": "none",
                                        "transition": "all 0.3s ease",
                                        "_focus": {
                                            "border_color": accent_color,
                                            "box_shadow": f"0 0 0 1px {accent_color}",
                                        },
                                    },
                                ),
                                width="100%",
                            ),
                            rx.box(
                                rx.text(
                                    "Email",
                                    style={
                                        "font_weight": "500",
                                        "margin_bottom": "0.5rem",
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#E2E8F0"
                                        ),
                                    },
                                ),
                                rx.input(
                                    placeholder="seuemail@exemplo.com",
                                    id="email",
                                    name="email",
                                    type="email",
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#2D3748", dark="white"
                                        ),
                                        "background": rx.color_mode_cond(
                                            light="white", dark="#2D3748"
                                        ),
                                        "border": rx.color_mode_cond(
                                            light="1px solid #E2E8F0",
                                            dark="1px solid #4A5568",
                                        ),
                                        "border_radius": "0.375rem",
                                        "padding_x": "1rem",
                                        "width": "100%",
                                        "outline": "none",
                                        "transition": "all 0.3s ease",
                                        "_focus": {
                                            "border_color": accent_color,
                                            "box_shadow": f"0 0 0 1px {accent_color}",
                                        },
                                    },
                                ),
                                width="100%",
                            ),
                            rx.box(
                                rx.text(
                                    "Assunto",
                                    style={
                                        "font_weight": "500",
                                        "margin_bottom": "0.5rem",
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#E2E8F0"
                                        ),
                                    },
                                ),
                                rx.select(
                                    [
                                        "Geral",
                                        "Parceria",
                                        "Evento",
                                        "Dúvida sobre Blockchain",
                                        "Outros",
                                    ],
                                    placeholder="Selecione um assunto",
                                    name="subject",
                                    default_value="Geral",
                                    required=True,
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#2D3748", dark="white"
                                        ),
                                        "background": rx.color_mode_cond(
                                            light="white", dark="#2D3748"
                                        ),
                                        "border": rx.color_mode_cond(
                                            light="1px solid #E2E8F0",
                                            dark="1px solid #4A5568",
                                        ),
                                        "border_radius": "0.375rem",
                                        "padding": "0.75rem 1rem",
                                        "width": "100%",
                                        "outline": "none",
                                        "transition": "all 0.3s ease",
                                        "_focus": {
                                            "border_color": accent_color,
                                            "box_shadow": f"0 0 0 1px {accent_color}",
                                        },
                                    },
                                ),
                                width="100%",
                            ),
                            rx.box(
                                rx.text(
                                    "Mensagem",
                                    style={
                                        "font_weight": "500",
                                        "margin_bottom": "0.5rem",
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#E2E8F0"
                                        ),
                                    },
                                ),
                                rx.text_area(
                                    placeholder="Digite sua mensagem aqui...",
                                    id="message",
                                    name="message",
                                    rows="6",
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#2D3748", dark="white"
                                        ),
                                        "background": rx.color_mode_cond(
                                            light="white", dark="#2D3748"
                                        ),
                                        "border": rx.color_mode_cond(
                                            light="1px solid #E2E8F0",
                                            dark="1px solid #4A5568",
                                        ),
                                        "border_radius": "0.375rem",
                                        "padding": "0.75rem 1rem",
                                        "width": "100%",
                                        "outline": "none",
                                        "transition": "all 0.3s ease",
                                        "_focus": {
                                            "border_color": accent_color,
                                            "box_shadow": f"0 0 0 1px {accent_color}",
                                        },
                                        "resize": "vertical",
                                    },
                                ),
                                width="100%",
                            ),
                            rx.button(
                                rx.hstack(
                                    rx.icon("send", size=16),
                                    rx.text("Enviar mensagem"),
                                    spacing="3",
                                    style={
                                        "align_items": "center",
                                    },
                                ),
                                type="submit",
                                style={
                                    "background": accent_color,
                                    "color": "white",
                                    "border_radius": "0.375rem",
                                    "padding": "0.75rem 1.5rem",
                                    "font_weight": "600",
                                    "width": "100%",
                                    "margin_top": "1rem",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background": "#e07b1f",
                                        "transform": "translateY(-2px)",
                                        "box_shadow": "0 4px 12px rgba(246, 139, 35, 0.25)",
                                    },
                                },
                            ),
                            spacing="6",
                            align="stretch",
                        ),
                        on_submit=ContactFormState.handle_submit,
                        reset_on_submit=True,
                    ),
                    style={
                        "width": rx.breakpoints(initial="100%", md="60%"),
                        "padding": "2rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                        "border_radius": "0.75rem",
                        "box_shadow": rx.color_mode_cond(
                            light="0 4px 20px rgba(0, 0, 0, 0.05)",
                            dark="0 4px 20px rgba(0, 0, 0, 0.3)",
                        ),
                    },
                ),
                flex_direction=rx.breakpoints(initial="column", md="row"),
                gap="2rem",
                align_items="stretch",
                style={
                    "width": "100%",
                    "margin": "0 auto",
                    "padding": "2rem 0",
                },
            ),
            style={
                "max_width": "1200px",
                "margin": "0 auto",
            },
        ),
        style={
            "width": "100%",
            "padding": "2rem 1rem",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
