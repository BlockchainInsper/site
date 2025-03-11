import reflex as rx


def intro_fundo():
    return rx.box(
        rx.box(
            rx.heading(
                "Fundo Blockchain Insper",
                style={
                    "font_size": "3.75rem",
                    "font_weight": "800",
                    "letter_spacing": "-0.025em",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    "text_align": "center",
                    "line_height": "1",
                },
                as_="h2",
            ),
            rx.text(
                "Nossa tese de investimento consiste em analisar os whitepapers de "
                "diversas criptomoedas, a partir disso avaliando sua aplicabilidade, "
                "escalabilidade e potencial de crescimento futuro. Dessa forma, realizamos "
                "a alocação de ativos do nosso fundo simulado.",
                style={
                    "margin_top": "1rem",
                    "font_size": "1.125rem",
                    "color": rx.color_mode_cond(
                        light="#1A202C", dark="rgba(255, 255, 255, 0.92)"
                    ),
                    "text_align": "center",
                },
            ),
            style={
                "max_width": "48rem",
                "margin_left": "auto",
                "margin_right": "auto",
                "padding_x": rx.breakpoints(initial="1.5rem", lg="2rem"),
                "padding_y": rx.breakpoints(initial="4rem", sm="5rem"),
            },
        ),
        as_="section",
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
