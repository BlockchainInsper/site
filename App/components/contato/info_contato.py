import reflex as rx
from components.icons.icons import discord_icon


def contato_info():
    accent_color = "#F68B23"

    email_icon = rx.icon("mail", size=28)

    linkedin_icon = rx.icon("linkedin", size=28)

    instagram_icon = rx.icon("instagram", size=28)

    return rx.box(
        rx.flex(
            rx.box(
                rx.heading(
                    "Entre em Contato",
                    style={
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.text(
                    "Caso queira fazer contato conosco, preencha o formulário "
                    "abaixo com seu nome, email, e mensagem. Responderemos "
                    "assim que possível!",
                    style={
                        "margin_bottom": "1.25rem",
                        "color": rx.color_mode_cond(light="#4A5568", dark="#E2E8F0"),
                    },
                ),
                rx.form(
                    rx.flex(
                        rx.vstack(
                            rx.text("Nome"),
                            rx.input(
                                placeholder="Seu nome",
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
                                },
                            ),
                            rx.text("Email"),
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
                                },
                            ),
                            rx.text("Mensagem"),
                            rx.text_area(
                                placeholder="Digite sua mensagem...",
                                id="message",
                                name="message",
                                rows="5",
                                style={
                                    "color": rx.color_mode_cond(
                                        light="#2D3748", dark="white"
                                    ),
                                    "background": rx.color_mode_cond(
                                        light="white", dark="#2D3748"
                                    ),
                                },
                            ),
                            rx.button(
                                "Enviar",
                                type="submit",
                                style={
                                    "background": accent_color,
                                    "color": "white",
                                    "width": "100%",
                                    "margin_top": "1rem",
                                    "_hover": {
                                        "background": "#e07b1f",
                                    },
                                },
                            ),
                            style={
                                "spacing": "1rem",
                            },
                        ),
                        style={
                            "flex_wrap": "wrap",
                            "spacing": "2",
                            "width": "100%",
                        },
                    ),
                    on_submit=lambda event: rx.window_alert("Mensagem enviada!"),
                ),
                rx.text(
                    "Ou, se preferir, entre em contato pelas nossas redes:",
                    style={
                        "font_weight": "bold",
                        "margin_top": "2.5rem",
                        "margin_bottom": "1rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.flex(
                    rx.link(
                        discord_icon(28, 40),
                        href="https://discord.gg/jdK5yB48Mm",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon_button(
                            email_icon,
                            aria_label="email",
                        ),
                        href="mailto:blockchainsper@gmail.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon_button(
                            linkedin_icon,
                            aria_label="linkedin",
                        ),
                        href="https://www.linkedin.com/company/blockchain-insper/",
                        is_external=True,
                    ),
                    rx.link(
                        rx.icon_button(
                            instagram_icon,
                            aria_label="instagram",
                        ),
                        href="https://www.instagram.com/blockchainsper/",
                        is_external=True,
                    ),
                    style={
                        "flex_wrap": "wrap",
                        "spacing": "2",
                        "align_items": "center",
                        "justify_content": "center",
                    },
                ),
                style={
                    "padding": "2rem",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    "border_radius": "0.5rem",
                },
            ),
            style={
                "flex_wrap": "wrap",
                "spacing": "2",
                "width": "100%",
                "justify_content": "center",
            },
        ),
        style={
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "width": "100%",
        },
    )
