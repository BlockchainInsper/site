import reflex as rx

# Lista completa de parceiros
CARDS = [
    {
        "name": "Insper",
        "image": "/parceiros/insper.png",
        "link": "https://www.insper.edu.br/",
    },
    {
        "name": "Mercado Bitcoin",
        "image": "/parceiros/mercadobtc.jpg",
        "link": "https://www.mercadobitcoin.com.br/",
    },
    {
        "name": "Ambev",
        "image": "/parceiros/ambev.jfif",
        "link": "https://www.ambev.com.br/",
    },
    {
        "name": "Itaú",
        "image": "/parceiros/itau.webp",
        "link": "https://www.itau.com.br/",
    },
    {
        "name": "Dotz",
        "image": "/parceiros/dotz.png",
        "link": "https://www.dotz.com.br/",
    },
    {
        "name": "GCB Investimentos",
        "image": "/parceiros/gcb.jfif",
        "link": "https://gcbinvestimentos.com/",
    },
    {
        "name": "Peer BR",
        "image": "/parceiros/peer.png",
        "link": "https://peerbr.com/",
    },
    {
        "name": "Coins",
        "image": "/parceiros/coins.jfif",
        "link": "https://coins.com.br/",
    },
    {
        "name": "Fernando Ulrich",
        "image": "/parceiros/ulrich.jpg",
        "link": "https://www.linkedin.com/in/fernando-ulrich-aa805821/",
    },
    {
        "name": "Blockchain Berkeley",
        "image": "/parceiros/blockchainberkeley.png",
        "link": "https://blockchain.berkeley.edu/",
    },
    {
        "name": "BeeTech",
        "image": "/parceiros/beetech.jpeg",
        "link": "https://beetech.global/",
    },
    {
        "name": "Block Master",
        "image": "/parceiros/blockmaster.jpg",
        "link": "https://www.blockmaster.com.br/",
    },
    {
        "name": "iCoLab",
        "image": "/parceiros/icolab.png",
        "link": "https://icolab.org.br/",
    },
    {
        "name": "Mar Ventures",
        "image": "/parceiros/marventures.png",
        "link": "https://www.mar.ventures/",
    },
    {
        "name": "Portal do Bitcoin",
        "image": "/parceiros/portaldobtc.webp",
        "link": "https://portaldobitcoin.uol.com.br/",
    },
]


def card(card_info: dict) -> rx.Component:
    return rx.center(
        rx.box(
            rx.box(
                rx.image(
                    src=card_info["image"],
                    style={
                        "height": "230px",
                        "width": "282px",
                        "object_fit": "cover",
                        "border_radius": "0.5rem",  # lg
                    },
                ),
                style={
                    "border_radius": "0.5rem",  # lg
                    "margin_top": "-3rem",  # -12
                    "position": "relative",
                    "height": "230px",
                },
            ),
            rx.stack(
                rx.heading(
                    card_info["name"],
                    style={
                        "line_height": "1.2",
                        "font_size": "1.5rem",  # 2xl
                        "font_weight": "500",
                    },
                ),
                rx.link(
                    rx.button(
                        "Mais informações",
                        style={
                            "width": "100%",
                            "margin_top": "0.75rem",  # 3
                            "background": "#f68b23",
                            "color": "white",
                            "border_radius": "0.375rem",  # md
                            "_hover": {
                                "transform": "translateY(-2px)",
                                "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",  # lg
                            },
                        },
                    ),
                    href=card_info["link"],
                    is_external=True,
                ),
                spacing="0",
                style={
                    "flex_direction": "column",
                    "padding_top": "2.5rem",  # 10
                    "align_items": "center",
                },
            ),
            style={
                "role": "group",
                "padding": "1.5rem",  # 6
                "max_width": "330px",
                "width": "100%",
                "background": rx.color_mode_cond(
                    light="white", dark="#1A202C"
                ),  # useColorModeValue
                "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",  # 2xl
                "border_radius": "0.5rem",  # lg
                "position": "relative",
                "z_index": "1",
            },
        ),
        style={
            "padding_top": "3rem",  # py={12}
            "padding_bottom": "3rem",
        },
    )


def render_cards():
    return rx.box(
        rx.flex(
            *[
                rx.box(
                    card(card_info),
                    key=card_info["name"],
                    style={
                        "padding": "1rem",  # 4
                    },
                )
                for card_info in CARDS
            ],
            style={
                "flex_wrap": "wrap",
                "justify_content": "center",
                "background": rx.color_mode_cond(
                    light="white", dark="#1A202C"
                ),  # useColorModeValue
            },
        ),
    )
