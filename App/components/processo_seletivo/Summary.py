import reflex as rx
from components.icons.icons import bitcoin_icon, building_icon, projects_icon


def feature(title: str, children: str, icon: rx.Component):
    return rx.flex(
        # Ícone à esquerda com tamanho ajustado
        rx.box(
            icon,
            style={
                "height": "100%",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "min_width": "4rem",
            },
        ),
        # Container vertical para título e descrição
        rx.vstack(
            rx.text(
                title,
                style={
                    "font_weight": "800",  # extrabold
                    "font_size": "1.125rem",  # text-lg
                    "color": rx.color_mode_cond(
                        light="#1A202C",  # Escuro no modo claro
                        dark="white",  # Branco no modo escuro
                    ),
                },
            ),
            rx.text(
                children,
                style={
                    "color": rx.color_mode_cond(
                        light="#4A5568",
                        dark="#A0AEC0",
                    ),
                },
            ),
            style={
                "margin_left": "1rem",
                "align_items": "flex-start",
            },
            spacing="1",
        ),
        style={
            "border_radius": "0.375rem",  # rounded-md
            "transition": "background-color 0.2s",  # transition-colors
            "_hover": {
                "background": rx.color_mode_cond(
                    light="rgba(0, 0, 0, 0.05)",  # Escuro suave no modo claro
                    dark="rgba(255, 255, 255, 0.05)",  # Branco suave no modo escuro
                ),
            },
            "direction": "row",
            "align_items": "center",  # Centralização vertical
        },
    )


def summary():
    return rx.box(
        rx.box(
            rx.grid(
                rx.link(
                    feature(
                        "Núcleos",
                        "Clique aqui para conhecer nossas áreas de estudos",
                        bitcoin_icon(3.75, 60),
                    ),
                    href="/areas",
                    style={
                        "text_decoration": "none"  # no-underline
                    },
                ),
                rx.link(
                    feature(
                        "Parceiros",
                        "Clique aqui para conhecer nossos parceiros",
                        building_icon(2.5, 60),
                    ),
                    href="/partnerships",
                    style={
                        "text_decoration": "none"  # no-underline
                    },
                ),
                rx.link(
                    feature(
                        "Projetos",
                        "Clique aqui para conhecer nossos alguns dos nossos melhores projetos",
                        projects_icon(2.5, 60),
                    ),
                    href="/projects",
                    style={
                        "text_decoration": "none"  # no-underline
                    },
                ),
                style={
                    "width": "100%",  # w-full
                    "grid_template_columns": rx.breakpoints(
                        initial="repeat(1, 1fr)",
                        md="repeat(2, 1fr)",
                    ),
                    "column_gap": "2.5rem",  # gap_x="10"
                    "row_gap": rx.breakpoints(
                        initial="2rem",  # gap_y inicial "8"
                        md="3.5rem",  # gap_y md "14"
                    ),
                },
            ),
            style={
                "max_width": "64rem",  # max-w-5xl (aproximadamente 64rem)
                "margin_left": "auto",  # mx-auto
                "margin_right": "auto",
                "padding_top": "1rem",  # pt-4
                "padding_bottom": "3rem",  # pb-12
                "padding_left": rx.breakpoints(
                    initial="1.5rem", md="2rem"
                ),  # px-6 md:px-8
                "padding_right": rx.breakpoints(
                    initial="1.5rem", md="2rem"
                ),  # px-6 md:px-8
            },
        ),
        style={
            "width": "100%",  # w-full
            "background": rx.color_mode_cond(
                light="white",
                dark="#1A202C",
            ),
        },
        as_="section",
    )
