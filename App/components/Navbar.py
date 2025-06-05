import reflex as rx

NAV_ITEMS = [
    {
        "label": "Processo Seletivo",
        "href": "/ps",
    },
    {
        "label": "Time",
        "children": [
            {
                "label": "Alumni",
                "subLabel": "Conheça nossos ex-membros",
                "href": "/members/alumni",
            },
        ],
        "href": "/members/actual",
    },
    {
        "label": "Núcleos",
        "children": [
            {
                "label": "Projetos",
                "subLabel": "Conheça alguns dos nossos melhores projetos",
                "href": "/projects",
            },
        ],
        "href": "/areas",
    },
    {
        "label": "Fundo",
        "href": "/fund",
    },
    {
        "label": "Parceiros",
        "href": "/partnerships",
    },
    {
        "label": "Aprenda",
        "href": "/learn",
    },
    {
        "label": "Contato",
        "href": "/contact",
    },
]


class MobileNavState(rx.State):
    is_open: bool = False

    def toggle(self):
        self.is_open = not self.is_open


class NavItemState(rx.State):
    open_items: dict[str, bool] = {}

    def toggle_item(self, label: str):
        if label in self.open_items:
            self.open_items[label] = not self.open_items[label]
        else:
            self.open_items[label] = True

    def is_item_open(self, label: str) -> bool:
        return self.open_items.get(label, False)


def desktop_sub_nav(label, href, subLabel):
    return rx.link(
        rx.hstack(
            rx.vstack(
                rx.text(
                    label,
                    as_="span",
                    color=rx.color_mode_cond(light="#4A5568", dark="#E2E8F0"),
                    transition="all 0.3s ease",
                    font_weight="500",
                ),
                rx.text(
                    subLabel,
                    font_size="0.875rem",
                    color=rx.color_mode_cond(light="#4A5568", dark="#E2E8F0"),
                ),
                align_items="start",
                spacing="0",
            ),
            rx.icon(
                tag="chevron_right",
                color="#f68b23",
                width="1.25rem",
                height="1.25rem",
                opacity="0",
                transition="all 0.3s ease",
                transform="translateX(-10px)",  # Posição inicial à esquerda
            ),
            width="100%",
            spacing="2",
            align_items="center",
        ),
        href=href,
        display="block",
        padding="0.5rem",
        border_radius="0.375rem",
        text_decoration="none",
        _hover={
            "background": rx.color_mode_cond(light="#f7e2dc", dark="#171923"),
            "text_decoration": "none",
            "& span": {"color": "#f68b23"},
            "& svg": {
                "opacity": "1",
                "transform": "translateX(0)",  # Move para a posição original no hover
            },
        },
    )


def desktop_nav():
    nav_items = []
    for navItem in NAV_ITEMS:
        link_component = rx.link(
            rx.box(
                navItem["label"],
                style={
                    "padding": "0.5rem",
                    "font_size": "0.875rem",
                    "font_weight": "500",
                    "text_decoration": "none",
                    "color": rx.color_mode_cond(light="#4A5568", dark="#E2E8F0"),
                    "_hover": {
                        "text-decoration": "none",
                        "color": rx.color_mode_cond(light="black", dark="white"),
                    },
                },
            ),
            href=navItem.get("href", "#"),
            style={"text_decoration": "none"},
        )

        if navItem.get("children"):
            nav_items.append(
                rx.box(
                    rx.hover_card.root(
                        rx.hover_card.trigger(link_component),
                        rx.hover_card.content(
                            rx.stack(
                                *[
                                    desktop_sub_nav(
                                        child["label"],
                                        child["href"],
                                        child.get("subLabel", ""),
                                    )
                                    for child in navItem.get("children", [])
                                ],
                            ),
                            style={
                                "border": "none",
                                "box_shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1)",
                                "background": rx.color_mode_cond(
                                    light="white", dark="#1A202C"
                                ),
                                "padding": "1rem",
                                "border_radius": "0.75rem",
                                "min_width": "24rem",
                            },
                        ),
                        trigger="hover",
                        placement="bottom-start",
                    ),
                    key=navItem["label"],
                )
            )
        else:
            nav_items.append(
                rx.box(
                    link_component,
                    key=navItem["label"],
                )
            )

    return rx.stack(
        *nav_items,
        style={
            "display": "flex",
            "flex_direction": "row",
            "align_items": "center",
            "gap": "0.5rem",
        },
    )


def mobile_nav_item(label, children, href):
    has_children = children is not None and len(children) > 0

    if has_children:
        return rx.accordion.root(
            rx.accordion.item(
                header=rx.link(
                    rx.text(
                        label,
                        style={
                            "font_weight": "600",
                            "color": "rgb(229, 231, 235)",
                            "text_align": "left",  # Alinha o texto à esquerda
                        },
                    ),
                    href=href,
                    style={
                        "text_decoration": "none",
                        "flex": "1",
                        "text_align": "left",  # Alinha o link à esquerda
                    },
                ),
                content=rx.stack(
                    *[
                        rx.link(
                            rx.box(
                                child["label"],
                                href=child["href"],
                                style={
                                    "padding": "0.75rem 0",
                                    "color": "rgb(229, 231, 235)",
                                    "font_weight": "500",
                                    "text_decoration": "none",
                                    "text_align": "left",  # Alinha os links filhos à esquerda
                                },
                            ),
                            underline="hover",
                            color_scheme="gray",
                        )
                        for child in children
                    ],
                    style={
                        "padding_left": "1.5rem",
                        "align_items": "flex-start",  # Alinha os itens do stack à esquerda
                    },
                ),
                value=label,
                style={
                    "border_bottom": "1px solid rgb(50, 50, 70)"
                    if label != "Contato"
                    else "none",
                    "width": "100%",
                    "text_align": "left",  # Alinha o conteúdo do item à esquerda
                },
            ),
            collapsible=True,
            width="100%",
            variant="ghost",
            style={
                "background": "#1A202C",
                "border": "none",
                "box_shadow": "none",
                "& .AccordionTrigger": {
                    "padding": "0.5rem 0",
                    "background": "none",
                    "text_align": "left",  # Alinha o trigger à esquerda
                    "&:hover": {
                        "background": "none",
                    },
                    "font_size": "1rem",
                },
                "& .AccordionContent": {
                    "background": "#1A202C",
                    "padding": "0",
                    "text_align": "left",  # Alinha o conteúdo à esquerda
                },
                "& .AccordionChevron": {
                    "color": "rgb(229, 231, 235)",
                    "width": "1.5rem",
                    "height": "1.5rem",
                },
            },
        )
    else:
        return rx.link(
            rx.flex(
                rx.text(
                    label,
                    style={
                        "font_weight": "600",
                        "color": "rgb(229, 231, 235)",
                        "text_align": "left",  # Alinha o texto à esquerda
                    },
                ),
                style={
                    "padding": "0.5rem 0",
                    "justify_content": "space_between",
                    "align_items": "center",
                    "width": "100%",
                    "text_align": "left",  # Alinha o flex à esquerda
                },
            ),
            href=href,
            style={"text_decoration": "none", "width": "100%"},
        )


def mobile_nav():
    return rx.box(
        rx.vstack(
            *[
                mobile_nav_item(
                    navItem["label"], navItem.get("children"), navItem.get("href")
                )
                for navItem in NAV_ITEMS
            ],
            align_items="stretch",
            width="100%",
            spacing="0",
        ),
        style={
            "background": "#1A202C",
            "color": "white",
            "width": "100%",
            "height": "fit-content",  # Alterado de 100vh para fit-content
            "min-height": "fit-content",  # Adicionado min-height
            "overflow_y": "auto",
            "padding": "0.5rem 1rem",
            "@media (min-width: 768px)": {"display": "none"},
        },
    )


def navbar():
    return rx.box(
        rx.flex(
            rx.flex(
                rx.icon_button(
                    rx.cond(
                        MobileNavState.is_open,
                        rx.icon(
                            tag="x",
                            style={
                                "width": "1rem",
                                "height": "1rem",
                                "color": "rgba(255, 255, 255, 0.92)",
                            },
                        ),
                        rx.icon(
                            tag="menu",
                            style={
                                "width": "1.25rem",
                                "height": "1.25rem",
                                "color": "rgba(255, 255, 255, 0.92)",
                            },
                        ),
                    ),
                    variant="ghost",
                    aria_label="Toggle Navigation",
                    on_click=MobileNavState.toggle,
                ),
                style={
                    "@media (min-width: 768px)": {
                        "flex": "auto",
                        "margin_left": "0",
                        "display": "none",
                    },
                    "flex": "1",
                    "margin_left": "-0.5rem",
                    "display": "flex",
                    "align_items": "center",
                },
            ),
            rx.flex(
                rx.link(
                    rx.image(
                        src=rx.color_mode_cond(
                            "/logo-light.svg",
                            "/logo-dark.svg",
                        ),
                        width="100px",
                    ),
                    href="/",
                    style={"display": "flex", "align_items": "center"},
                ),
                rx.flex(
                    desktop_nav(),
                    style={
                        "@media (min-width: 768px)": {"display": "flex"},
                        "display": "none",
                        "margin_left": "2.5rem",
                        "align_items": "center",
                    },
                ),
                style={
                    "@media (min-width: 768px)": {"justify_content": "flex-start"},
                    "justify_content": "center",
                    "flex": "1",
                    "align_items": "center",
                },
            ),
            rx.stack(
                rx.color_mode.button(
                    style={"color": rx.color_mode_cond(light="#1A202C", dark="white")}
                ),
                style={
                    "@media (min-width: 768px)": {"flex": "0"},
                    "flex": "1",
                    "justify_content": "flex-end",
                    "flex_direction": "row",
                    "gap": "1.5rem",
                    "align_items": "center",
                },
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                "color": rx.color_mode_cond(light="#4A5568", dark="#E2E8F0"),
                "min_height": "60px",
                "padding": "0.5rem 1rem",
                "border_bottom": "1px solid",
                "border_color": rx.color_mode_cond(
                    light="rgb(229, 231, 235)", dark="rgb(17, 24, 39)"
                ),
                "width": "100%",
                "position": "relative",
                "z-index": "10",
            },
        ),
        rx.cond(
            MobileNavState.is_open,
            mobile_nav(),
            rx.box(),
        ),
        style={
            "width": "100%",
            "box_shadow": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
            "position": "relative",
        },
    )
