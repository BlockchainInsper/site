import reflex as rx


def external_link_icon():
    return rx.icon(
        "external_link",
        size=16,
        style={
            "margin_left": "2px",
            "margin_right": "2px",
        },
    )


def content():
    return rx.box(
        rx.container(
            rx.grid(
                rx.vstack(
                    rx.heading(
                        "Temas e Conteúdos",
                        style={
                            "font_weight": "bold",
                            "font_size": "1.875rem",
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                        },
                    ),
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell(
                                    "Tema",
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#A0AEC0"
                                        ),
                                    },
                                ),
                                rx.table.column_header_cell(
                                    "Conteúdos",
                                    style={
                                        "color": rx.color_mode_cond(
                                            light="#4A5568", dark="#A0AEC0"
                                        ),
                                    },
                                ),
                            ),
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Introdução"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/introducao",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    )
                                ),
                            ),
                            rx.table.row(
                                rx.table.cell("Bitcoin"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/bitcoin",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    ),
                                ),
                            ),
                            rx.table.row(
                                rx.table.cell("Blockchain"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/blockchain",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    ),
                                ),
                            ),
                            rx.table.row(
                                rx.table.cell("CryptoAssets"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/crypto-assets",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    ),
                                ),
                            ),
                            rx.table.row(
                                rx.table.cell("Chains"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/chains",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    ),
                                ),
                            ),
                            rx.table.row(
                                rx.table.cell("Tecnologia"),
                                rx.table.cell(
                                    rx.link(
                                        rx.box(
                                            "Acesse ",
                                            external_link_icon(),
                                            style={
                                                "display": "flex",  # Alinhamento horizontal
                                                "align_items": "center",  # Centraliza itens verticalmente
                                                "color": rx.color_mode_cond(
                                                    light="#1A202C",
                                                    dark="rgba(255, 255, 255, 0.92)",
                                                ),
                                                "text-decoration": "none",
                                            },
                                        ),
                                        href="/learn/curso-intro/tecnologia",
                                        color_scheme="gray",
                                        underline="hover",
                                        high_contrast=True,
                                    ),
                                ),
                            ),
                        ),
                        style={
                            "width": "100%",
                            "border_collapse": "collapse",
                            "margin_top": "1rem",
                            "background": rx.color_mode_cond(
                                light="white", dark="#1A202C"
                            ),
                        },
                    ),
                    spacing="4",
                ),
                gap="2.5rem",
                style={
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
            style={
                "max_width": "80rem",  # 5xl
                "padding_y": "3rem",  # py={12} = 3rem
                "margin": "0 auto",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
