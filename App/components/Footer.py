import reflex as rx
from datetime import datetime
from components.icons.icons import discord_icon


def footer() -> rx.Component:
    accent_color = "#F68B23"

    return rx.box(
        rx.box(
            rx.flex(
                rx.flex(
                    rx.image(
                        src=rx.color_mode_cond(
                            "/logo-light.svg",
                            "/logo-dark.svg",
                        ),
                        width="100px",
                    ),
                    rx.text(
                        f"© {datetime.now().year} Blockchain Insper. All rights reserved.",
                        style={
                            "font_size": "0.875rem",
                            "color": rx.color_mode_cond(
                                light="#1A202C",  # gray-600
                                dark="rgba(255, 255, 255, 0.92)",  # gray-400
                            ),
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex_direction": "column",
                        "align_items": "flex-start",
                        "justify_content": "center",
                        "gap": "0.5rem",
                    },
                ),
                rx.flex(
                    rx.link(
                        rx.box(
                            discord_icon(20, 20),
                            style={
                                "width": "40px",
                                "height": "40px",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "border_radius": "50%",
                                "min_width": "2.5rem",
                                "color": rx.color_mode_cond(
                                    "#4A5568",
                                    "rgba(255, 255, 255, 0.92)",
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
                        style={
                            "_hover": {
                                "background": "rgba(255, 255, 255, 0.1)",
                                "border_radius": "0.375rem",
                            },
                            "margin_left": "1rem",
                            "display": "flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    # LinkedIn
                    rx.link(
                        rx.box(
                            rx.icon(
                                "linkedin",
                                size=20,
                            ),
                            style={
                                "width": "40px",
                                "height": "40px",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "border_radius": "50%",
                                "margin_left": "0.5rem",
                                "min_width": "2.5rem",
                                "color": rx.color_mode_cond(
                                    "#4A5568", "rgba(255, 255, 255, 0.92)"
                                ),
                                "transition": "all 0.3s ease",
                                "_hover": {
                                    "background": accent_color,
                                    "transform": "translateY(-3px)",
                                },
                            },
                        ),
                        href="https://www.linkedin.com/company/blockchain-insper",
                        is_external=True,
                    ),
                    # Instagram
                    rx.link(
                        rx.box(
                            rx.icon(
                                "instagram",
                                size=20,
                            ),
                            style={
                                "width": "40px",
                                "height": "40px",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "border_radius": "50%",
                                "margin_left": "0.5rem",
                                "min_width": "2.5rem",
                                "color": rx.color_mode_cond(
                                    "#4A5568", "rgba(255, 255, 255, 0.92)"
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
                    # GitHub
                    rx.link(
                        rx.box(
                            rx.icon(
                                "github",
                                size=20,
                            ),
                            style={
                                "width": "40px",
                                "height": "40px",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "border_radius": "50%",
                                "margin_left": "0.5rem",
                                "min_width": "2.5rem",
                                "color": rx.color_mode_cond(
                                    "#4A5568", "rgba(255, 255, 255, 0.92)"
                                ),
                                "transition": "all 0.3s ease",
                                "_hover": {
                                    "background": accent_color,
                                    "transform": "translateY(-3px)",
                                },
                            },
                        ),
                        href="https://github.com/BlockchainInsper",
                        is_external=True,
                    ),
                    # Email
                    rx.link(
                        rx.box(
                            rx.icon(
                                "mail",
                                size=20,
                            ),
                            style={
                                "width": "40px",
                                "height": "40px",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center",
                                "border_radius": "50%",
                                "margin_left": "0.5rem",
                                "min_width": "2.5rem",
                                "color": rx.color_mode_cond(
                                    "#4A5568", "rgba(255, 255, 255, 0.92)"
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
                        style={
                            "color": rx.color_mode_cond(
                                light="#4A5568",  # gray-600
                                dark="rgba(255, 255, 255, 0.92)",  # gray-400
                            ),
                            "_hover": {
                                "background": "rgba(255, 255, 255, 0.1)",
                                "border_radius": "0.375rem",
                            },
                            "display": "flex",
                            "align_items": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex_direction": "row",
                        "align_items": "center",
                        "color": rx.color_mode_cond(
                            light="#4A5568",  # gray-600
                            dark="rgba(255, 255, 255, 0.92)",  # gray-400
                        ),
                    },
                ),
                style={
                    "display": "flex",
                    "flex_direction": rx.breakpoints(initial="column", sm="row"),
                    "justify_content": "space-between",
                    "width": "100%",
                    "align_items": rx.breakpoints(initial="center", sm="flex-start"),
                    "gap": rx.breakpoints(initial="1rem", sm="0"),
                },
            ),
            style={
                "max_width": "80rem",  # 7xl
                "margin": "0 auto",
                "padding": rx.breakpoints(initial="0 1rem", md="0 2rem"),
                "width": "100%",
            },
        ),
        role="contentinfo",
        style={
            "height": "10rem",
            "width": "100%",
            "padding": "3rem 0",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
