import reflex as rx


def external_link_icon():
    return rx.icon(
        "external_link",
        style={
            "margin_left": "2px",
            "margin_right": "2px",
        },
    )


def materiais(materiais: list, titulo: str):
    return rx.container(
        rx.grid(
            rx.vstack(
                rx.heading(
                    titulo,
                    style={
                        "font_weight": "bold",
                        "font_size": "1.875rem",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Tema"),
                            rx.table.column_header_cell("Conteúdos"),
                        ),
                    ),
                    rx.table.body(
                        *[
                            rx.table.row(
                                rx.table.cell(material.get("nome", "")),
                                rx.table.cell(
                                    rx.link(
                                        "Acesse ",
                                        external_link_icon(),
                                        href=material.get("link", "#"),
                                        is_external=True,
                                        style={
                                            "color": rx.color_mode_cond(
                                                light="#3182CE", dark="#63B3ED"
                                            ),
                                            "text_decoration": "none",
                                            "_hover": {
                                                "text_decoration": "underline",
                                            },
                                        },
                                    )
                                ),
                                key=f"material-{i}",
                            )
                            for i, material in enumerate(materiais)
                        ]
                    ),
                    style={
                        "width": "100%",
                        "border_collapse": "collapse",
                        "margin_top": "1rem",
                        "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                    },
                ),
                spacing="4",
            ),
            spacing="10",
            style={
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "max_width": "80rem",  # 5xl
            "padding_y": "1.25rem",  # py={5} = 1.25rem
            "margin": "0 auto",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
