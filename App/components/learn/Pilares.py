import reflex as rx
from components.icons.icons import idea_icon, collaboration_icon, businessman_icon


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
                "color": rx.color_mode_cond(light="#4A5568", dark="#718096"),
            },
        ),
        style={
            "flex_direction": "column",
        },
    )


def pilares():
    # Ícones dos pilares

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
                        idea_icon(2.5, 40),
                    ),
                    feature(
                        "Aprender a fazer",
                        "Ele se refere à formação do profissional. Fala sobre como conseguir usar os conhecimentos "
                        "adquiridos na prática, no mercado de trabalho, criando qualificação profissional e experiência.",
                        collaboration_icon(2.5, 40),
                    ),
                    feature(
                        "Aprender a ser",
                        "Ele defende que o ser humano precisa se tornar apto a pensar de forma autônoma e crítica, "
                        "sendo capaz de formular o próprio juízo de valor e sabendo que atitudes tomar ante as circunstâncias da vida.",
                        businessman_icon(2.5, 40),
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
