import reflex as rx


def card(member: dict) -> rx.Component:
    # Extrair informações do membro
    nome = member.get("name", "")
    cargo = member.get("cargo", "")
    curso = member.get("curso", "")
    ano_entrada = member.get("ano_entrada", "")
    imagem = member.get("image", "https://via.placeholder.com/300")

    return rx.box(
        rx.box(
            rx.image(
                src=imagem,
                alt=nome,
                style={
                    "border_radius": "0.5rem",  # lg
                    "height": "260px",
                    "width": "260px",
                    "object_fit": "cover",
                },
            ),
            rx.box(
                rx.heading(
                    nome,
                    style={
                        "font_size": "1.25rem",  # xl
                        "margin_top": "0.5rem",  # 2
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                rx.text(
                    cargo,
                    style={
                        "font_weight": "600",  # semibold
                        "color": "#ED8936",  # orange.400
                        "letter_spacing": "0.05em",  # wide
                        "font_size": "0.75rem",  # xs
                        "text_transform": "uppercase",
                        "margin_top": "0.25rem",  # 1
                    },
                ),
                rx.vstack(
                    rx.text(
                        curso,
                        style={
                            "color": rx.color_mode_cond(
                                light="#718096", dark="#CBD5E0"
                            ),
                            "font_size": "0.875rem",  # sm
                        },
                    ),
                    rx.text(
                        f"Desde {ano_entrada}",
                        style={
                            "color": rx.color_mode_cond(
                                light="#718096", dark="#CBD5E0"
                            ),
                            "font_size": "0.875rem",  # sm
                        },
                    ),
                    style={
                        "margin_top": "0.5rem",  # 2
                        "spacing": "0",
                        "align_items": "flex-start",
                    },
                ),
                style={
                    "padding": "1.5rem",
                },
            ),
            style={
                "max_width": "260px",
                "border_radius": "0.5rem",  # lg
                "overflow": "hidden",
                "box_shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",  # xl
                "background": rx.color_mode_cond(light="white", dark="#2D3748"),
            },
        ),
        style={
            "padding": "0.5rem",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
        },
    )
