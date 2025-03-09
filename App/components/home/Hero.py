import reflex as rx
from components.icons.icons import discord_icon


def discord_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                discord_icon(1.125, 18),
                rx.text("Discord", line_height="1.1"),
                style={
                    "align_items": "center",
                    "justify_content": "center",
                },
            ),
            size="4",
            style={
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "border_radius": "9999px",
                "font_size": "1.125rem",
                "font_weight": "normal",
                "padding_x": "1.5rem",
                "color": "white",
                "background_color": "#5865F2",
                "_hover": {"background_color": "#5865F2"},
            },
        ),
        href="https://discord.gg/jdK5yB48Mm",
        is_external=True,
        style={
            "text_decoration": "none",
        },
    )


def blob(props=None):
    if props is None:
        props = {}

    return rx.el.svg(
        rx.el.svg.path(
            fill_rule="evenodd",
            clip_rule="evenodd",
            d="M239.184 439.443c-55.13-5.419-110.241-21.365-151.074-58.767C42.307 338.722-7.478 282.729.938 221.217c8.433-61.644 78.896-91.048 126.871-130.712 34.337-28.388 70.198-51.348 112.004-66.78C282.34 8.024 325.382-3.369 370.518.904c54.019 5.115 112.774 10.886 150.881 49.482 39.916 40.427 49.421 100.753 53.385 157.402 4.13 59.015 11.255 128.44-30.444 170.44-41.383 41.683-111.6 19.106-169.213 30.663-46.68 9.364-88.56 35.21-135.943 30.551z",
            fill="currentColor",
        ),
        view_box="0 0 578 440",
        fill="none",
        xmlns="http://www.w3.org/2000/svg",
        style={
            "width": "150%",
            "height": "150%",
            "display": "inline-block",
            "line_height": "1em",
            "flex_shrink": "0",
            "vertical_align": "middle",
            "color": rx.color_mode_cond(  # Adicionado color mode
                light="rgb(254, 242, 242)",  # red.50 do Chakra
                dark="#f68b23",
            ),
            "position": "absolute",
            "top": "-10%",
            "left": "0",
            "z_index": "0",
        },
        **props,
    )


def call_to_action_with_video():
    return rx.box(
        rx.box(
            rx.stack(
                rx.stack(
                    rx.heading(
                        rx.text(
                            "Venha conhecer",
                            as_="span",
                            style={
                                "position": "relative",
                                "z_index": "1",
                                "color": rx.color_mode_cond(  # Adicionado suporte ao tema
                                    light="#1A202C", dark="rgba(255, 255, 255, 0.92)"
                                ),
                                "_after": {
                                    "content": "''",
                                    "position": "absolute",
                                    "width": "100%",
                                    "height": "30%",
                                    "bottom": "1px",
                                    "left": "0",
                                    "background_color": "#f68b23",
                                    "z_index": "-1",
                                },
                            },
                        ),
                        rx.el.br(),
                        rx.text(
                            "nosso trabalho!", as_="span", style={"color": "#f68b23"}
                        ),
                        style={
                            "font_weight": "600",
                            "line_height": "1.1",
                            # Ajustado para usar breakpoints do Reflex
                            "font_size": rx.breakpoints(
                                initial="1.875rem",  # 3xl
                                sm="2.25rem",  # 4xl
                                lg="3.75rem",  # 6xl
                            ),
                        },
                    ),
                    rx.text(
                        "Criada em setembro de 2017, a Blockchain Insper é a primeira "
                        "organização estudantil da América Latina focada em estudo de tecnologias "
                        "blockchain. Derivada de uma iniciativa universitária, que reúne "
                        "estudantes de administração, economia, engenharias e direito a entidade está "
                        "dividida em três áreas de estudo: Business, Finance e Tecnologia.",
                        style={"color": "rgb(107, 114, 128)", "font_weight": "bold"},
                    ),
                    rx.stack(
                        discord_button(),
                        style={
                            "display": "flex",
                            # Ajustado para breakpoints do Reflex
                            "flex_direction": rx.breakpoints(
                                initial="column", sm="row"
                            ),
                            # Ajustado spacing para breakpoints
                            "gap": rx.breakpoints(initial="1rem", sm="1.5rem"),
                        },
                    ),
                    style={
                        "flex": "1",
                        "display": "flex",
                        "flex_direction": "column",
                        "gap": rx.breakpoints(initial="1.25rem", md="2.5rem"),
                        "justify_content": "center",  # Adicionado para alinhar verticalmente
                        "height": "100%",  # Adicionado para ocupar altura total
                    },
                ),
                rx.flex(
                    rx.box(
                        blob(),
                        rx.aspect_ratio(
                            rx.el.iframe(
                                src="https://www.youtube.com/embed/P3gAHRgNrEE",
                                title="Teste",
                                width="100%",
                                height="100%",
                            ),
                            ratio=16 / 9,
                            style={
                                "position": "relative",
                                "height": "300px",
                                "border_radius": "1rem",
                                "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
                                "width": "100%",
                                "overflow": "hidden",
                                "z_index": "10",
                            },
                        ),
                        style={
                            "position": "relative",
                            "width": "100%",
                            "height": "100%",
                        },
                    ),
                    style={
                        "flex": "1",
                        "display": "flex",
                        "justify": "center",
                        "align_items": "center",
                        "position": "relative",
                        "width": "100%",
                        "overflow": "visible",
                    },
                ),
                style={
                    "display": "flex",
                    # Ajustado para breakpoints do Reflex
                    "flex_direction": rx.breakpoints(initial="column", md="row"),
                    "align_items": "flex-start",
                    # Ajustado padding para breakpoints
                    "padding_top": rx.breakpoints(initial="5rem", md="7rem"),
                    "padding_bottom": rx.breakpoints(initial="5rem", md="7rem"),
                    # Ajustado spacing para breakpoints
                    "gap": rx.breakpoints(initial="2rem", md="2.5rem"),
                    "width": "100%",
                },
            ),
            style={
                "width": "100%",
                # Ajustado padding para breakpoints
                "padding_x": rx.breakpoints(initial="1rem", md="1rem"),
                "margin": "0 auto",
                "max_width": "80rem",  # maxW={'7xl'} do Chakra
            },
        ),
        style={
            "width": "100%",
            "display": "flex",
            "justify_content": "center",
            "background": rx.color_mode_cond(  # Adicionado suporte ao tema
                light="white", dark="#1A202C"
            ),
            "color": "white",
        },
    )
