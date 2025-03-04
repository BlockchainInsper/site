import reflex as rx


def feature(title: str, children: str, icon: rx.Component):
    return rx.stack(
        rx.box(icon, class_name="text-6xl"),
        rx.stack(
            rx.text(title, class_name="font-extrabold text-lg"),
            rx.box(children, class_name="text-gray-600 dark:text-gray-400"),
            class_name="space-y-1",
        ),
        class_name="flex flex-col md:flex-row space-y-3 md:space-y-0 md:space-x-6",
    )


def summary():
    bitcoin_svg = rx.el.svg(
        rx.el.svg.path(
            d="M23.638 14.904c-1.602 6.43-8.113 10.34-14.542 8.736C2.67 22.05-1.244 15.525.362 9.105 1.962 2.67 8.475-1.243 14.9.358c6.43 1.605 10.342 8.115 8.738 14.548v-.002zm-6.35-4.613c.24-1.59-.974-2.45-2.64-3.03l.54-2.153-1.315-.33-.525 2.107c-.345-.087-.705-.167-1.064-.25l.526-2.127-1.32-.33-.54 2.165c-.285-.067-.565-.132-.84-.2l-1.815-.45-.35 1.407s.974.225.955.236c.535.136.63.486.615.766l-1.477 5.92c-.075.166-.24.406-.614.314.015.02-.96-.24-.96-.24l-.66 1.51 1.71.426.93.236-.54 2.19 1.32.327.54-2.17c.36.1.705.19 1.05.273l-.51 2.154 1.32.33.545-2.19c2.24.427 3.93.257 4.64-1.774.57-1.637-.03-2.58-1.217-3.196.854-.193 1.5-.76 1.68-1.93h.01zm-3.01 4.22c-.404 1.64-3.157.75-4.05.53l.72-2.9c.896.23 3.757.67 3.33 2.37zm.41-4.24c-.37 1.49-2.662.735-3.405.55l.654-2.64c.744.18 3.137.524 2.75 2.084v.006z",
            fill="currentColor",
        ),
        view_box="0 0 24 24",
        class_name="h-12 w-12",
    )

    building_svg = rx.el.svg(
        rx.el.svg.path(
            d="M17 11V3H7v4H3v14h8v-4h2v4h8V11h-4zM7 19H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V9h2v2zm4 4H9v-2h2v2zm0-4H9V9h2v2zm0-4H9V5h2v2zm4 8h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2zm4 12h-2v-2h2v2zm0-4h-2v-2h2v2z",
            fill="currentColor",
        ),
        view_box="0 0 24 24",
        class_name="h-12 w-12",
    )

    projects_svg = rx.el.svg(
        rx.el.svg.path(
            d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z",
            fill="currentColor",
        ),
        view_box="0 0 24 24",
        class_name="h-12 w-12",
    )

    return rx.box(
        rx.grid(
            rx.link(
                feature(
                    "Núcleos",
                    "Clique aqui para conhecer nossas áreas de estudos",
                    bitcoin_svg,
                ),
                href="#/areas",
            ),
            rx.link(
                feature(
                    "Parceiros",
                    "Clique aqui para conhecer nossos parceiros",
                    building_svg,
                ),
                href="#/partnerships",
            ),
            rx.link(
                feature(
                    "Projetos",
                    "Clique aqui para conhecer nossos alguns dos nossos melhores projetos",
                    projects_svg,
                ),
                href="#/projects",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-x-10 gap-y-8 md:gap-y-14",
        ),
        class_name="max-w-5xl mx-auto pt-4 pb-12 px-6 md:px-8",
    )


# Configuração do app
app = rx.App()
app.add_page(summary)
