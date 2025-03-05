import reflex as rx
from datetime import datetime


def footer() -> rx.Component:
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
                        "align": "flex-start",
                        "justify_content": "center",
                        "gap": "0.5rem",
                    },
                ),
                rx.flex(
                    rx.link(
                        rx.el.svg(
                            rx.el.svg.path(
                                d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z",
                                fill=rx.color_mode_cond(
                                    light="#4A5568",  # gray-600
                                    dark="rgba(255, 255, 255, 0.92)",  # gray-400
                                ),
                            ),
                            viewBox="0 0 24 24",
                            width="20px",
                            height="20px",
                            xmlns="http://www.w3.org/2000/svg",
                            style={"color": "white"},
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
                            "align": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    # LinkedIn
                    rx.link(
                        rx.icon(tag="linkedin", size=20, style={"color": "white"}),
                        href="https://www.linkedin.com/company/blockchain-insper",
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
                            "margin_left": "0.5rem",
                            "display": "flex",
                            "align": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    # Instagram
                    rx.link(
                        rx.icon(tag="instagram", size=20, style={"color": "white"}),
                        href="https://www.instagram.com/blockchainsper/",
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
                            "margin_left": "0.5rem",
                            "display": "flex",
                            "align": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    # GitHub
                    rx.link(
                        rx.icon(tag="github", size=20, style={"color": "white"}),
                        href="https://github.com/BlockchainInsper",
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
                            "margin_left": "0.5rem",
                            "display": "flex",
                            "align": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    # Email
                    rx.link(
                        rx.icon(tag="mail", size=20, style={"color": "white"}),
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
                            "margin_left": "0.5rem",
                            "display": "flex",
                            "align": "center",
                            "justify_content": "center",
                            "min_width": "2.5rem",
                            "height": "2.5rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex_direction": "row",
                        "align": "center",
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
                    "align": rx.breakpoints(initial="center", sm="flex-start"),
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
            "width": "100%",
            "padding": "3rem 0",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
