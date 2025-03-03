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
                    class_name="transition-all duration-300 group-hover:text-[#f68b23] font-medium",
                ),
                rx.text(
                    subLabel,
                    class_name="text-sm",
                ),
                class_name="",
            ),
            rx.flex(
                rx.icon(
                    tag="chevron_right",
                    class_name="text-[#f68b23] w-5 h-5",
                ),
                class_name="transition-all duration-300 -translate-x-10 opacity-0 group-hover:opacity-100 group-hover:translate-x-0 flex justify-end items-center flex-1",
            ),
            class_name="flex flex-row items-center",
        ),
        href=href,
        role="group",
        class_name="block p-2 rounded-md hover:bg-[#f7e2dc] dark:hover:bg-gray-900",
    )


def desktop_nav():
    nav_items = []
    for navItem in NAV_ITEMS:
        # Link component for all items
        link_component = rx.link(
            navItem["label"],
            href=navItem.get("href", "#"),
            class_name="p-2 text-sm font-medium text-gray-600 dark:text-gray-200 hover:no-underline hover:text-gray-800 dark:hover:text-white",
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
                            class_name="border-0 shadow-xl bg-white dark:bg-[#1A202C] p-4 rounded-xl min-w-[24rem]",
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
        class_name="flex flex-row items-center gap-2",
    )


def mobile_nav_item(label, children, href):
    # Build flex components differently depending on whether there are children
    flex_children = [
        rx.text(
            label,
            class_name="font-semibold text-gray-600 dark:text-gray-200",
        )
    ]

    # Only add icon if there are children
    if children:
        flex_children.append(
            rx.icon(
                tag="chevron_down",
                class_name=f"transition-all duration-300 ease-in-out w-6 h-6 {rx.cond(NavItemState.is_item_open(label), 'rotate-180', '')}",
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
                        class_name="py-2",
                        href=child["href"],
                    )
                    for child in children
                ],
                class_name="mt-2 pl-4 border-l border-solid border-gray-200 dark:border-gray-700 items-start",
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
            class_name="py-2 justify-between items-center hover:no-underline",
            as_="a",
            href="#" if children else href,
            on_click=NavItemState.toggle_item(label) if children else None,
        ),
        submenu,
        class_name="gap-2",
    )


def mobile_nav():
    return rx.stack(
        *[
            mobile_nav_item(
                navItem["label"], navItem.get("children"), navItem.get("href")
            )
            for navItem in NAV_ITEMS
        ],
        class_name="bg-white dark:bg-[#1A202C] p-4 md:hidden block",
    )


def navbar():
    return rx.box(
        rx.flex(
            # Mobile menu button
            rx.flex(
                rx.icon_button(
                    rx.cond(
                        MobileNavState.is_open,
                        rx.icon(tag="x", class_name="w-3 h-3"),
                        rx.icon(tag="menu", class_name="w-5 h-5"),
                    ),
                    variant="ghost",
                    aria_label="Toggle Navigation",
                    on_click=MobileNavState.toggle,
                ),
                class_name="md:flex-auto flex-1 md:ml-0 -ml-2 md:hidden flex items-center",
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
                    class_name="md:flex hidden ml-10 items-center",
                ),
                class_name="md:justify-start justify-center flex-1 items-center",
            ),
            # Theme toggle button
            rx.stack(
                rx.color_mode.button(),
                class_name="md:flex-0 flex-1 justify-end flex-row space-x-6 items-center",
            ),
            # Estilização principal do navbar
            class_name="flex items-center bg-white dark:bg-[#1A202C] text-gray-600 dark:text-white min-h-[60px] py-2 px-4 border-b border-solid border-gray-200 dark:border-gray-900 w-full",
        ),
        # Menu mobile - animação de colapso
        rx.cond(
            MobileNavState.is_open,
            mobile_nav(),
            rx.box(),
        ),
        class_name="w-full shadow-sm",
    )
