import reflex as rx

# Using the NAV_ITEMS data from your first document
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


class ColorModeState(rx.State):
    color_mode: str = "dark"  # Default to dark mode based on images

    def toggle_color_mode(self):
        self.color_mode = "light" if self.color_mode == "dark" else "dark"


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
                    font_weight=500,
                ),
                rx.text(
                    subLabel,
                    font_size="sm",
                ),
            ),
            rx.flex(
                rx.icon(
                    tag="chevron_right",
                    color="#f68b23",
                    width=5,
                    height=5,
                ),
                transition="all .3s ease",
                transform="translateX(-10px)",
                opacity=0,
                _group_hover={
                    "opacity": "100%",
                    "transform": "translateX(0)",
                },
                justify="end",
                align="center",
                flex=1,
            ),
            direction="row",
            align="center",
        ),
        href=href,
        role="group",
        display="block",
        p=2,
        border_radius="md",
        _hover={
            "bg": rx.cond(ColorModeState.color_mode == "light", "#f7e2dc", "gray.900")
        },
    )


def desktop_nav():
    nav_items = []
    for navItem in NAV_ITEMS:
        # Link component for all items
        link_component = rx.link(
            navItem["label"],
            href=navItem.get("href", "#"),
            font_size="sm",
            font_weight=500,
            color=rx.cond(
                ColorModeState.color_mode == "light",
                "gray.600",
                "#E2E8F0",
            ),
            _hover={
                "text_decoration": "none",
                "color": rx.cond(
                    ColorModeState.color_mode == "light",
                    "gray.800",
                    "white",
                ),
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
                            border=0,
                            box_shadow="xl",
                            bg=rx.cond(
                                ColorModeState.color_mode == "light",
                                "white",
                                "gray.800",
                            ),
                            p=4,
                            border_radius="xl",
                            min_width="sm",
                        ),
                        trigger="hover",
                        placement="bottom-start",
                    ),
                    key=navItem["label"],
                    class_name="flex items-center px-2 py-2",
                )
            )
        else:
            nav_items.append(
                rx.box(
                    link_component,
                    key=navItem["label"],
                    class_name="flex items-center px-2 py-2",
                )
            )

    return rx.stack(
        *nav_items,
        direction="row",
        spacing="4",
        align="center",  # Garantir alinhamento vertical
        class_name="items-center",  # Reforçar com Tailwind
    )


def mobile_nav_item(label, children, href):
    # Build flex components differently depending on whether there are children
    flex_children = [
        rx.text(
            label,
            font_weight=600,
            color=rx.cond(ColorModeState.color_mode == "light", "gray.600", "#E2E8F0"),
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
                width=6,
                height=6,
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
                        py=2,
                        href=child["href"],
                    )
                    for child in children
                ],
                mt=2,
                pl=4,
                border_left=1,
                border_style="solid",
                border_color=rx.cond(
                    ColorModeState.color_mode == "light", "gray.200", "gray.700"
                ),
                align="start",
            ),
            rx.box(),  # Empty box instead of None
        )
    else:
        # If no children, always render an empty box
        submenu = rx.box()

    # Create flex with appropriate children
    return rx.stack(
        rx.flex(
            *flex_children,
            py=2,
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
        spacing="4",
    )


def mobile_nav():
    return rx.stack(
        *[
            mobile_nav_item(
                navItem["label"], navItem.get("children"), navItem.get("href")
            )
            for navItem in NAV_ITEMS
        ],
        bg=rx.cond(ColorModeState.color_mode == "light", "white", "gray.800"),
        p=4,
        display=rx.breakpoints(initial="block", md="none"),
    )


def navbar():
    return rx.box(
        rx.flex(
            # Mobile menu button
            rx.flex(
                rx.icon_button(
                    rx.cond(
                        MobileNavState.is_open,
                        rx.icon(tag="x", width=3, height=3),
                        rx.icon(tag="menu", width=5, height=5),
                    ),
                    variant="ghost",
                    aria_label="Toggle Navigation",
                    on_click=MobileNavState.toggle,
                    class_name="text-[#E2E8F0]",
                ),
                class_name=rx.cond(
                    rx.breakpoints(md=True),
                    "flex-auto ml-0 hidden",
                    "flex-1 -ml-2 flex items-center",
                ),
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
                    class_name="flex items-center",
                ),
                rx.flex(
                    desktop_nav(),
                    class_name=rx.cond(
                        rx.breakpoints(md=True),
                        "ml-10 flex items-center",
                        "hidden",
                    ),
                ),
                class_name=rx.cond(
                    rx.breakpoints(md=True),
                    "flex-1 justify-start items-center",
                    "flex-1 justify-center items-center",
                ),
            ),
            # Theme toggle button
            rx.stack(
                rx.color_mode.button(),
                class_name=rx.cond(
                    rx.breakpoints(md=True),
                    "flex-0 justify-end flex-row space-x-6 items-center",
                    "flex-1 justify-end flex-row space-x-6 items-center",
                ),
            ),
            # Aplicando as classes CSS do .css-1553k70
            class_name=rx.color_mode_cond(
                # Modo claro
                "flex items-center bg-white text-gray-600 min-h-[60px] py-2 px-4 border-b border-solid border-gray-200 w-full",
                # Modo escuro
                "flex items-center bg-[#1A202C] text-[#E2E8F0] min-h-[60px] py-2 px-4 border-b border-solid border-gray-900 w-full",
            ),
        ),
        rx.cond(
            MobileNavState.is_open,
            mobile_nav(),
            rx.box(),
        ),
        class_name="w-full shadow-sm",
    )
