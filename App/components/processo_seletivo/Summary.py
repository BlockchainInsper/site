import reflex as rx


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
            "padding": "1rem",  # p-4
            "border_radius": "0.375rem",  # rounded-md
            "transition": "background-color 0.2s",  # transition-colors
            "_hover": {
                "background": rx.color_mode_cond(
                    light="rgba(0, 0, 0, 0.05)",  # Escuro suave no modo claro
                    dark="rgba(255, 255, 255, 0.05)",  # Branco suave no modo escuro
                ),
            },
            "direction": "row",
            "align_items": "inherit",  # Centralização vertical
            "gap": "1rem",
        },
    )


def summary():
    bitcoin_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 512 512">
            <path fill="currentColor" d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256S119.033 8 256 8s248 111.033 248 248m-141.651-35.33c4.937-32.999-20.191-50.739-54.55-62.573l11.146-44.702l-27.213-6.781l-10.851 43.524c-7.154-1.783-14.502-3.464-21.803-5.13l10.929-43.81l-27.198-6.781l-11.153 44.686c-5.922-1.349-11.735-2.682-17.377-4.084l.031-.14l-37.53-9.37l-7.239 29.062s20.191 4.627 19.765 4.913c11.022 2.751 13.014 10.044 12.68 15.825l-12.696 50.925c.76.194 1.744.473 2.829.907c-.907-.225-1.876-.473-2.876-.713l-17.796 71.338c-1.349 3.348-4.767 8.37-12.471 6.464c.271.395-19.78-4.937-19.78-4.937l-13.51 31.147l35.414 8.827c6.588 1.651 13.045 3.379 19.4 5.006l-11.262 45.213l27.182 6.781l11.153-44.733a1038 1038 0 0 0 21.687 5.627l-11.115 44.523l27.213 6.781l11.262-45.128c46.404 8.781 81.299 5.239 95.986-36.727c11.836-33.79-.589-53.281-25.004-65.991c17.78-4.098 31.174-15.792 34.747-39.949m-62.177 87.179c-8.41 33.79-65.308 15.523-83.755 10.943l14.944-59.899c18.446 4.603 77.6 13.717 68.811 48.956m8.417-87.667c-7.673 30.736-55.031 15.12-70.393 11.292l13.548-54.327c15.363 3.828 64.836 10.973 56.845 43.035" />
        </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "2.5rem",  # w-10
            "height": "2.5rem",  # h-10
        },
    )

    building_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 24 24">
                <path fill="currentColor" d="M17 11V3H7v4H3v14h8v-4h2v4h8V11zM7 19H5v-2h2zm0-4H5v-2h2zm0-4H5V9h2zm4 4H9v-2h2zm0-4H9V9h2zm0-4H9V5h2zm4 8h-2v-2h2zm0-4h-2V9h2zm0-4h-2V5h2zm4 12h-2v-2h2zm0-4h-2v-2h2z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "2.5rem",  # w-10
            "height": "2.5rem",  # h-10
        },
    )

    # SVG atualizado para projetos
    projects_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 1024 1024">
                <path fill="currentColor" d="M312.1 591.5c3.1 3.1 8.2 3.1 11.3 0l101.8-101.8l86.1 86.2c3.1 3.1 8.2 3.1 11.3 0l226.3-226.5c3.1-3.1 3.1-8.2 0-11.3l-36.8-36.8c-3.1-3.1-8.2-3.1-11.3 0L517 485.3l-86.1-86.2c-3.1-3.1-8.2-3.1-11.3 0L275.3 543.4c-3.1 3.1-3.1 8.2 0 11.3z" />
                <path fill="currentColor" d="M904 160H548V96c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H120c-17.7 0-32 14.3-32 32v520c0 17.7 14.3 32 32 32h356.4v32L311.6 884.1c-3.7 2.4-4.7 7.3-2.3 11l30.3 47.2v.1c2.4 3.7 7.4 4.7 11.1 2.3L512 838.9l161.3 105.8c3.7 2.4 8.7 1.4 11.1-2.3v-.1l30.3-47.2c2.4-3.7 1.3-8.6-2.3-11L548 776.3V744h356c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 512H160V232h704z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "2.5rem",  # w-10
            "height": "2.5rem",  # h-10
        },
    )

    return rx.box(
        rx.box(
            rx.grid(
                rx.link(
                    feature(
                        "Núcleos",
                        "Clique aqui para conhecer nossas áreas de estudos",
                        bitcoin_svg,
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
                        building_svg,
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
                        projects_svg,
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
                    ),  # columns=rx.breakpointss(...)
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
