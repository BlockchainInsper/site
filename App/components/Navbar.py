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
        rx.stack(
            rx.box(
                rx.text(
                    label,
                    transition="all .3s ease",
                    _group_hover={"color": "#f68b23"},
                    font_weight="500",
                ),
                rx.text(
                    subLabel,
                    font_size="0.875rem",
                ),
            ),
            rx.flex(
                rx.icon(
                    tag="chevron_right",
                    color="#f68b23",
                    width="1.25rem",
                    height="1.25rem",
                ),
                transition="all .3s ease",
                transform="translateX(-10px)",
                opacity="0px",
                _group_hover={
                    "opacity": "100%",
                    "transform": "translateX(0)",
                },
                justify="end",
                align="center",
                flex="0.25rem",
            ),
            direction="row",
            align="center",
        ),
        href=href,
        role="group",
        display="block",
        padding="0.5rem",
        border_radius="md",
        _hover={"bg": rx.color_mode_cond("#f7e2dc", "#171923")},
    )


def desktop_nav():
    nav_items = []
    for navItem in NAV_ITEMS:
        # Link component for all items
        link_component = rx.link(
            navItem["label"],
            href=navItem.get("href", "#"),
            padding="0.5rem",
            font_size="0.875rem",
            font_weight="500",
            color=rx.color_mode_cond("#4A5568", "#E2E8F0"),
            _hover={
                "text_decoration": "none",
                "color": rx.color_mode_cond("#1A202C", "white"),
            },
        )

        # If it has children, wrap in popover, otherwise just use the link
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
                            border="0",
                            box_shadow="0.75rem",
                            bg=rx.color_mode_cond("white", "#1A202C"),
                            padding="1rem",
                            border_radius="0 20px 25px -5px rgba(0, 0, 0, 0.1)",
                            min_width="24rem",
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
        direction="row",
        spacing="2",
        align="center",
    )


def mobile_nav_item(label, children, href):
    # Build flex components differently depending on whether there are children
    flex_children = [
        rx.text(
            label, font_weight="600", color=rx.color_mode_cond("#4A5568", "#E2E8F0")
        )
    ]
    # Only add icon if there are children
    if children:
        flex_children.append(
            rx.icon(
                tag="chevron_down",
                transition="all .25s ease-in-out",
                transform=rx.cond(
                    NavItemState.is_item_open(label), "rotate(180deg)", ""
                ),
                width="1.5rem",
                height="1.5rem",
            )
        )

    # Condition for showing submenu - Children exist and item is open
    submenu = None
    if children:
        submenu = rx.cond(
            NavItemState.is_item_open(label),
            rx.stack(
                *[
                    rx.link(
                        child["label"],
                        key=child["label"],
                        padding_y="1rem",
                        href=child["href"],
                    )
                    for child in children
                ],
                margin_top="0.5rem",
                padding_left="1rem",
                border_left="0.25rem",
                border_style="solid",
                border_color=rx.color_mode_cond("#E2E8F0", "#2D3748"),
                align="start",
            ),
            rx.box(),  # Empty box as fallback
        )
    else:
        # If no children, always render an empty box
        submenu = rx.box()

    # Create flex with appropriate children
    return rx.stack(
        rx.flex(
            *flex_children,
            padding_y="0.5rem",
            as_="a",
            href="#" if children else href,
            justify="between",
            align="center",
            _hover={
                "text_decoration": "none",
            },
            on_click=NavItemState.toggle_item(label) if children else None,
        ),
        submenu,
        spacing="2",
    )


def mobile_nav():
    return rx.stack(
        *[
            mobile_nav_item(
                navItem["label"], navItem.get("children"), navItem.get("href")
            )
            for navItem in NAV_ITEMS
        ],
        bg=rx.color_mode_cond("white", "#1A202C"),
        padding="1rem",
        display=rx.cond(rx.breakpoints(md=True), "none", "block"),
    )


def navbar():
    return rx.box(
        rx.flex(
            # Mobile menu button
            rx.flex(
                rx.icon_button(
                    rx.cond(
                        MobileNavState.is_open,
                        rx.icon(tag="x", width="0.75rem", height="0.75rem"),
                        rx.icon(tag="menu", width="1.25rem", height="1.25rem"),
                    ),
                    variant="ghost",
                    aria_label="Toggle Navigation",
                    on_click=MobileNavState.toggle,
                ),
                flex=rx.cond(rx.breakpoints(md=True), "auto", "0.25rem"),
                margin_left=rx.cond(rx.breakpoints(md=True), "0rem", "-0.5rem"),
                display=rx.cond(rx.breakpoints(md=True), "none", "flex"),
            ),
            # Logo and navigation
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
                ),
                rx.flex(
                    desktop_nav(),
                    display=rx.cond(rx.breakpoints(md=True), "flex", "none"),
                    margin_left="2.5rem",
                ),
                flex="0.5rem",
                justify=rx.cond(rx.breakpoints(md=True), "start", "center"),
            ),
            # Theme toggle button
            rx.stack(
                rx.color_mode.button(),
                flex=rx.cond(rx.breakpoints(md=True), "0rem", "0.25rem"),
                justify="end",
                direction="row",
                spacing="3",
            ),
            # Estilização principal do navbar
            bg=rx.color_mode_cond("white", "#1A202C"),
            color=rx.color_mode_cond("#4A5568", "white"),
            min_height="60px",
            padding_y="0.5rem",
            padding_x="1rem",
            border_bottom="1px",
            border_style="solid",
            border_color=rx.color_mode_cond("#E2E8F0", "#171923"),
            align="center",
            width="100%",
        ),
        # Menu mobile - animação de colapso
        rx.cond(
            MobileNavState.is_open,
            mobile_nav(),
            rx.box(),
        ),
        width="100%",
        shadow="sm",
    )
