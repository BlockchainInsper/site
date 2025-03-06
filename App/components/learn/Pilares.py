import reflex as rx


def feature(title, text, icon):
    return rx.stack(
        rx.flex(
            icon,
            style={
                "width": "4rem",
                "height": "4rem",
                "align": "center",
                "justify": "center",
                "color": "white",
                "border_radius": "9999px",
                "background": rx.color_mode_cond(light="#F7FAFC", dark="#4A5568"),
                "margin_bottom": "0.25rem",
            },
        ),
        rx.text(
            title,
            style={
                "font_weight": "600",
                "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
            },
        ),
        rx.text(
            text,
            style={
                "color": rx.color_mode_cond(light="#718096", dark="#CBD5E0"),
            },
        ),
        style={
            "flex_direction": "column",
        },
    )


def pilares():
    # Ícones dos pilares
    idea_icon = (
        rx.html(
            """<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 48 48">
                <circle cx="24" cy="22" r="20" fill="#fff59d" stroke-width="1" stroke="#fff59d" />
                <path fill="#fbc02d" d="M37 22c0-7.7-6.6-13.8-14.5-12.9c-6 .7-10.8 5.5-11.4 11.5c-.5 4.6 1.4 8.7 4.6 11.3c1.4 1.2 2.3 2.9 2.3 4.8v.3h12v-.1c0-1.8.8-3.6 2.2-4.8c2.9-2.4 4.8-6 4.8-10.1" stroke-width="1" stroke="#fbc02d" />
                <path fill="#fff59d" d="m30.6 20.2l-3-2c-.3-.2-.8-.2-1.1 0L24 19.8l-2.4-1.6c-.3-.2-.8-.2-1.1 0l-3 2c-.2.2-.4.4-.4.7s0 .6.2.8l3.8 4.7V37h2V26c0-.2-.1-.4-.2-.6l-3.3-4.1l1.5-1l2.4 1.6c.3.2.8.2 1.1 0l2.4-1.6l1.5 1l-3.3 4.1c-.1.2-.2.4-.2.6v11h2V26.4l3.8-4.7c.2-.2.3-.5.2-.8s-.2-.6-.4-.7" stroke-width="1" stroke="#fff59d" />
                <circle cx="24" cy="44" r="3" fill="#5c6bc0" stroke-width="1" stroke="#5c6bc0" />
                <path fill="#9fa8da" d="M26 45h-4c-2.2 0-4-1.8-4-4v-5h12v5c0 2.2-1.8 4-4 4" stroke-width="1" stroke="#9fa8da" />
                <path fill="#5c6bc0" d="m30 41l-11.6 1.6c.3.7.9 1.4 1.6 1.8l9.4-1.3q.6-.9.6-2.1m-12-2.3v2L30 39v-2z" stroke-width="1" stroke="#5c6bc0" />
            </svg>""",
            style={
                "width": "2.5rem",
                "height": "2.5rem",
            },
        ),
    )

    collaboration_icon = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 48 48">
                <path fill="#1565c0" d="M25 22h13l6 6V11c0-2.2-1.8-4-4-4H25c-2.2 0-4 1.8-4 4v7c0 2.2 1.8 4 4 4" stroke-width="1" stroke="#1565c0" />
                <path fill="#2196f3" d="M23 19H10l-6 6V8c0-2.2 1.8-4 4-4h15c2.2 0 4 1.8 4 4v7c0 2.2-1.8 4-4 4" stroke-width="1" stroke="#2196f3" />
                <g fill="#ffa726" stroke-width="1" stroke="#ffa726">
                    <circle cx="12" cy="31" r="5" />
                    <circle cx="36" cy="31" r="5" />
                </g>
                <path fill="#607d8b" d="M20 42s-2.2-4-8-4s-8 4-8 4v2h16zm24 0s-2.2-4-8-4s-8 4-8 4v2h16z" stroke-width="1" stroke="#607d8b" />
            </svg>""",
        style={
            "width": "2.5rem",
            "height": "2.5rem",
        },
    )

    businessman_icon = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 48 48">
                <path fill="#ff9800" d="m24 37l-5-6v-6h10v6z" stroke-width="1" stroke="#ff9800" />
                <g fill="#ffa726" stroke-width="1" stroke="#ffa726">
                    <circle cx="33" cy="19" r="2" />
                    <circle cx="15" cy="19" r="2" />
                </g>
                <path fill="#ffb74d" d="M33 13c0-7.6-18-5-18 0v7c0 5 4 9 9 9s9-4 9-9z" stroke-width="1" stroke="#ffb74d" />
                <path fill="#424242" d="M24 4c-6.1 0-10 4.9-10 11v2.3l2 1.7v-5l12-4l4 4v5l2-1.7V15c0-4-1-8-6-9l-1-2z" stroke-width="1" stroke="#424242" />
                <g fill="#784719" stroke-width="1" stroke="#784719">
                    <circle cx="28" cy="19" r="1" />
                    <circle cx="20" cy="19" r="1" />
                </g>
                <path fill="#fff" d="m24 43l-5-12l5 1l5-1z" stroke-width="1" stroke="#fff" />
                <path fill="#d32f2f" d="m23 35l-.7 4.5l1.7 4l1.7-4L25 35l1-1l-2-2l-2 2z" stroke-width="1" stroke="#d32f2f" />
                <path fill="#546e7a" d="m29 31l-5 12l-5-12S8 33 8 44h32c0-11-11-13-11-13" stroke-width="1" stroke="#546e7a" />
            </svg>""",
        style={
            "width": "2.5rem",
            "height": "2.5rem",
        },
    )

    return rx.box(
        rx.box(
            rx.heading(
                "Pilares do Conhecimento",
                style={
                    "text_align": "center",
                    "font_size": "2.25rem",
                    "padding_y": "5rem",
                    "font_weight": "bold",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
            ),
            rx.box(
                rx.grid(
                    feature(
                        "Aprender a conhecer",
                        "Esse aprendizado pretende que cada pessoa possa conhecer o mundo que a rodeia, "
                        "conseguindo assim viver dignamente, desenvolver capacidades profissionais e se comunicar.",
                        idea_icon,
                    ),
                    feature(
                        "Aprender a fazer",
                        "Ele se refere à formação do profissional. Fala sobre como conseguir usar os conhecimentos "
                        "adquiridos na prática, no mercado de trabalho, criando qualificação profissional e experiência.",
                        collaboration_icon,
                    ),
                    feature(
                        "Aprender a ser",
                        "Ele defende que o ser humano precisa se tornar apto a pensar de forma autônoma e crítica, "
                        "sendo capaz de formular o próprio juízo de valor e sabendo que atitudes tomar ante as circunstâncias da vida.",
                        businessman_icon,
                    ),
                    columns=rx.breakpoints(initial="1", md="3"),
                    gap="2.5rem",
                ),
                style={
                    "padding": "1rem",
                    "border_radius": "0.5rem",
                },
            ),
            style={
                "max_width": "80rem",
                "margin_x": "auto",
                "padding_top": "1.25rem",
                "padding_x": rx.breakpoints(initial="0.5rem", sm="3rem", md="4.25rem"),
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                "display": "flex",
                "flex_direction": "column",
            },
        ),
        style={
            "width": "full",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
