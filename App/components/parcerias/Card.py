import reflex as rx

CARDS = [
    {
        "name": "Insper",
        "image": "/parceiros/insper.png",
        "link": "https://www.insper.edu.br/",
    },
    {
        "name": "Vault",
        "image": "/",
        "link": "https://www.insper.edu.br/",
    },
]


def card(card_info: dict) -> rx.Component:
    return rx.center(
        rx.box(
            rx.box(
                rx.image(
                    src=card_info["image"],
                    height="230px",
                    width="282px",
                    object_fit="cover",
                    border_radius="lg",
                ),
                border_radius="lg",
                margin_top="-12",
                position="relative",
                height="230px",
            ),
            rx.stack(
                rx.heading(
                    card_info["name"],
                    font_size="2xl",
                    font_family="body",
                    font_weight="500",
                ),
                rx.link(
                    rx.button(
                        "Mais informações",
                        width="100%",
                        margin_top="3",
                        bg="#f68b23",
                        color="white",
                        border_radius="md",
                        _hover={
                            "transform": "translateY(-2px)",
                            "box_shadow": "lg",
                        },
                    ),
                    href=card_info["link"],
                    is_external=True,
                ),
                padding_top="10",
                align="center",
            ),
            role="group",
            padding="6",
            max_width="330px",
            width="100%",
            bg="white",
            box_shadow="2xl",
            border_radius="lg",
            position="relative",
            z_index="1",
        ),
        padding_y="12",
    )


def render_cards():
    return (
        rx.box(
            rx.foreach(
                CARDS,
                lambda card_info: rx.box(
                    card(card_info),
                    key=card_info["name"],
                    padding="4",
                ),
            ),
            display="flex",
            flex_wrap="wrap",
            justify="center",
            gap="30px",
            margin="10",
        ),
    )
