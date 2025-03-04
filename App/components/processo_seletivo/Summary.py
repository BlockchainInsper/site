import reflex as rx


def feature(title: str, children: str, icon: rx.Component):
    return rx.flex(
        # Ícone à esquerda com tamanho ajustado
        rx.center(
            icon,
            class_name="h-full flex items-center justify-center min-w-[4rem]",
        ),
        # Container vertical para título e descrição
        rx.vstack(
            rx.text(
                title,
                class_name="font-extrabold text-lg text-white",
            ),
            rx.text(
                children,
                class_name="text-white",
            ),
            align_items="flex-start",
            spacing="1",
            class_name="items-start py-2",
        ),
        # Flex sempre na horizontal
        direction="row",
        gap="4",
        class_name="hover:bg-white/5 p-4 rounded-md transition-colors",
        align_items="stretch",  # Alinha itens para esticar verticalmente
    )


def summary():
    bitcoin_svg = rx.el.svg(
        rx.el.svg.path(
            d="M23.638 14.904c-1.602 6.43-8.113 10.34-14.542 8.736C2.67 22.05-1.244 15.525.362 9.105 1.962 2.67 8.475-1.243 14.9.358c6.43 1.605 10.342 8.115 8.738 14.548v-.002zm-6.35-4.613c.24-1.59-.974-2.45-2.64-3.03l.54-2.153-1.315-.33-.525 2.107c-.345-.087-.705-.167-1.064-.25l.526-2.127-1.32-.33-.54 2.165c-.285-.067-.565-.132-.84-.2l-1.815-.45-.35 1.407s.974.225.955.236c.535.136.63.486.615.766l-1.477 5.92c-.075.166-.24.406-.614.314.015.02-.96-.24-.96-.24l-.66 1.51 1.71.426.93.236-.54 2.19 1.32.327.54-2.17c.36.1.705.19 1.05.273l-.51 2.154 1.32.33.545-2.19c2.24.427 3.93.257 4.64-1.774.57-1.637-.03-2.58-1.217-3.196.854-.193 1.5-.76 1.68-1.93h.01zm-3.01 4.22c-.404 1.64-3.157.75-4.05.53l.72-2.9c.896.23 3.757.67 3.33 2.37zm.41-4.24c-.37 1.49-2.662.735-3.405.55l.654-2.64c.744.18 3.137.524 2.75 2.084v.006z",
            fill="currentColor",
        ),
        view_box="0 0 24 24",
        class_name="text-white w-10 h-10",
    )

    building_svg = rx.el.svg(
        rx.el.svg.path(
            d="M17 11V3H7v4H3v14h8v-4h2v4h8V11h-4zM7 19H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V9h2v2zm4 4H9v-2h2v2zm0-4H9V9h2v2zm0-4H9V5h2v2zm4 8h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2zm4 12h-2v-2h2v2zm0-4h-2v-2h2v2z",
            fill="currentColor",
        ),
        view_box="0 0 24 24",
        class_name="text-white w-10 h-10",
    )

    # SVG atualizado para projetos
    # SVG atualizado para projetos - sem usar o parâmetro nomeado "children"
    projects_svg = rx.el.svg(
        rx.el.svg.path(
            # Gráfico
            d="M7.3 13.8c.07.07.19.07.26 0l2.38-2.38l2.02 2.02c.07.07.19.07.26 0l5.3-5.3c.07-.07.07-.19 0-.27l-.86-.86c-.07-.07-.19-.07-.26 0L12.1 11.4l-2.02-2.02c-.07-.07-.19-.07-.26 0L6.45 12.7c-.07.07-.07.19 0 .27l.85.83z",
            fill="currentColor",
        ),
        rx.el.svg.path(
            # Monitor/dispositivo
            d="M21.2 3.8h-8.3V2.3c0-.1-.08-.19-.18-.19h-1.3c-.1 0-.19.08-.19.19v1.5H2.8c-.41 0-.75.33-.75.75v12.2c0 .41.33.75.75.75h8.34v.75l-3.66 2.4c-.09.06-.11.17-.05.26l.71 1.1v.003c.06.09.17.11.26.05l4.7-3.08l3.78 2.47c.09.06.2.03.26-.05v-.001l.71-1.1c.06-.09.03-.2-.05-.26L14.3 18.2v-.75h8.33c.41 0 .75-.33.75-.75V4.5c0-.41-.33-.75-.75-.75M20.25 15.8H3.8V5.45h16.45v10.35z",
            fill="currentColor",
        ),
        xmlns="http://www.w3.org/2000/svg",
        view_box="0 0 24 24",  # Alterado para 24x24
        class_name="text-white w-10 h-10",
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
                    class_name="no-underline",
                ),
                rx.link(
                    feature(
                        "Parceiros",
                        "Clique aqui para conhecer nossos parceiros",
                        building_svg,
                    ),
                    href="/partnerships",
                    class_name="no-underline",
                ),
                rx.link(
                    feature(
                        "Projetos",
                        "Clique aqui para conhecer nossos alguns dos nossos melhores projetos",
                        projects_svg,
                    ),
                    href="/projects",
                    class_name="no-underline",
                ),
                columns=rx.breakpoints(initial="1", md="2"),
                gap_x="10",
                gap_y=rx.breakpoints(initial="8", md="14"),
                class_name="w-full",
            ),
            class_name="max-w-5xl mx-auto pt-4 pb-12 px-6 md:px-8",
        ),
        class_name="w-full bg-[#1A202C]",
        as_="section",
    )
