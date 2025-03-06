import reflex as rx


def location_info():
    return rx.box(
        rx.flex(
            rx.box(
                rx.box(
                    rx.aspect_ratio(
                        rx.el.iframe(
                            title="Localização",
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1828.0847263800329!2d-46.67881990221802!3d-23.598254999967665!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce575374b7481f%3A0x50e5aad2656c43ed!2sInsper%20Learning%20Institution!5e0!3m2!1sen!2sbr!4v1586359937804!5m2!1sen!2sbr",
                            style={
                                "border": "none",
                                "width": "100%",
                                "height": "100%",
                            },
                        ),
                        ratio=16 / 9,
                    ),
                    style={
                        "border_radius": "0.5rem",
                        "width": "100%",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                style={
                    "border_radius": "0.5rem",
                    "justify_content": "center",
                    "width": "100%",
                    "max_width": "1000px",
                    "margin": rx.breakpoints(sm="1rem", md="4rem", lg="3.125rem"),
                    "padding": rx.breakpoints(sm="1.25rem", md="1.25rem", lg="1.25rem"),
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
            rx.box(
                rx.stack(
                    rx.heading(
                        rx.text(
                            "Venha conhecer a Blockchain Insper e o Insper!",
                            as_="span",
                            style={
                                "position": "relative",
                                "z_index": "1",
                                "_after": {
                                    "content": "''",
                                    "width": "100%",
                                    "height": "30%",
                                    "position": "absolute",
                                    "bottom": "1px",
                                    "left": "0",
                                    "background": "#F68B23",
                                    "z_index": "-1",
                                },
                                "color": rx.color_mode_cond(
                                    light="#2D3748", dark="#F7FAFC"
                                ),
                            },
                        ),
                        style={
                            "line_height": "1.1",
                            "font_weight": "600",
                            "font_size": rx.breakpoints(
                                initial="1rem", sm="1.5rem", lg="1.875rem"
                            ),
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                        },
                    ),
                    rx.text(
                        "Aberto de Segunda à Sexta das 07:00 às 23:00",
                        style={
                            "font_weight": "bold",
                            "color": rx.color_mode_cond(
                                light="#4A5568", dark="#E2E8F0"
                            ),
                        },
                    ),
                    style={
                        "flex_direction": "column",
                        "spacing": "0.75rem",
                    },
                ),
                style={
                    "align_items": "center",
                    "justify_content": "center",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    "padding": "1rem",
                    "border_radius": "0.5rem",
                },
            ),
            style={
                "flex_direction": rx.breakpoints(initial="column", md="row"),
                "align_items": "center",
                "justify_content": "center",
                "margin_top": "2rem",
                "margin_bottom": "2rem",
            },
        ),
        style={
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "height": "100%",
            "overflow": "hidden",  # Evita barras de rolagem desnecessárias
        },
    )
