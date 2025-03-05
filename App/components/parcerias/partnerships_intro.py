import reflex as rx


def intro_partnerships():
    return rx.box(
        rx.box(
            rx.heading(
                "Parceiros",
                style={
                    "font_size": "3rem",  # 3xl
                    "font_weight": "extrabold",
                    "letter_spacing": "tight",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
                as_="h2",
            ),
            rx.text(
                "Aqui você encontrará todos os parceiros da Blockchain Insper",
                style={
                    "margin_top": "1rem",  # mt="4"
                    "font_size": "1.125rem",  # lg
                    "color": rx.color_mode_cond(light="gray.700", dark="gray.300"),
                },
            ),
            style={
                "max_width": "42rem",  # 2xl
                "margin_left": "auto",
                "margin_right": "auto",
                "padding_x": rx.breakpoints(initial="1.5rem", lg="2rem"),  # px
                "padding_y": rx.breakpoints(initial="4rem", sm="5rem"),  # py
                "text_align": "center",
            },
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
