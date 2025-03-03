import reflex as rx


def discord_button() -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.el.svg(
                    rx.el.svg.path(
                        d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z",
                        fill="currentColor",
                    ),
                    viewBox="0 0 24 24",
                    class_name="w-6 h-6",
                    xmlns="http://www.w3.org/2000/svg",
                ),
                rx.text("Discord"),
            ),
            rounded="full",
            size="lg",
            font_weight="normal",
            px=6,
            color="white",
            bg="#5865F2",
            _hover={"bg": "#5865F2"},
        ),
        href="https://discord.gg/jdK5yB48Mm",
        is_external=True,
        class_name="no-underline",
    )


def blob(props=None):
    """Blob component precisely matching the original JavaScript implementation."""
    if props is None:
        props = {}

    return rx.el.svg(
        rx.el.svg.path(
            fill_rule="evenodd",
            clip_rule="evenodd",
            d="M239.184 439.443c-55.13-5.419-110.241-21.365-151.074-58.767C42.307 338.722-7.478 282.729.938 221.217c8.433-61.644 78.896-91.048 126.871-130.712 34.337-28.388 70.198-51.348 112.004-66.78C282.34 8.024 325.382-3.369 370.518.904c54.019 5.115 112.774 10.886 150.881 49.482 39.916 40.427 49.421 100.753 53.385 157.402 4.13 59.015 11.255 128.44-30.444 170.44-41.383 41.683-111.6 19.106-169.213 30.663-46.68 9.364-88.56 35.21-135.943 30.551z",
            fill="currentColor",
        ),
        width="100%",
        height="150%",
        display="inline-block",
        line_height="1em",
        flex_shrink="0",
        vertical_align="middle",
        view_box="0 0 578 440",
        fill="none",
        xmlns="http://www.w3.org/2000/svg",
        color="#f68b23",
        position="absolute",
        top="-20%",
        left="0px",
        z_index="0",
        **props,
    )


def call_to_action_with_video():
    # Não use o argumento children e componentes filhos ao mesmo tempo
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                rx.text(
                                    "Venha conhecer",
                                    as_="span",
                                    # Use inline style instead of class to ensure it doesn't get overridden
                                    style={
                                        "position": "relative",
                                        "zIndex": "1",
                                        "_after": {
                                            "content": "''",
                                            "position": "absolute",
                                            "width": "100%",
                                            "height": "30%",
                                            "left": "0",
                                            "bottom": "1px",
                                            "backgroundColor": "#f68b23",
                                            "zIndex": "-1",
                                        },
                                    },
                                ),
                                rx.el.br(),
                                rx.text(
                                    "nosso trabalho!",
                                    as_="span",
                                    class_name="!text-[#f68b23]",
                                ),
                                class_name="font-semibold leading-tight text-3xl sm:text-4xl lg:text-6xl",
                            ),
                        ),
                        rx.text(
                            "Criada em setembro de 2017, a Blockchain Insper é a primeira "
                            "organização estudantil da América Latina focada em estudo de tecnologias "
                            "blockchain. Derivada de uma iniciativa universitária, que reúne "
                            "estudantes de administração, economia, engenharias e direito a entidade está "
                            "dividida em três áreas de estudo: Business, Finance e Tecnologia.",
                            class_name="text-gray-500 font-bold",
                        ),
                        rx.box(
                            rx.link(
                                rx.box(
                                    rx.box(
                                        rx.box(
                                            rx.box(
                                                rx.el.svg(
                                                    rx.el.svg.path(
                                                        d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z",
                                                        fill="currentColor",
                                                    ),
                                                    viewBox="0 0 24 24",
                                                    class_name="w-6 h-6 text-white",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                ),
                                                rx.text(
                                                    "Discord",
                                                    class_name="ml-2 text-white",
                                                ),
                                                class_name="flex items-center justify-center",
                                            ),
                                            class_name="flex items-center justify-center w-full",
                                        ),
                                        class_name="px-6 py-2 bg-[#5865F2] hover:bg-[#4752C4] rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-110",
                                    ),
                                    class_name="inline-flex items-center",
                                ),
                                href="https://discord.gg/jdK5yB48Mm",
                                target="_blank",
                                rel="noopener noreferrer",
                                class_name="no-underline",
                            ),
                            class_name="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6",
                        ),
                        class_name="flex-1 space-y-5 md:space-y-10",
                    ),
                    rx.box(
                        blob(),
                        rx.box(
                            rx.html(
                                """
                                <iframe
                                    title="Teste"
                                    alt="Bitcoin Video"
                                    src="https://www.youtube.com/embed/P3gAHRgNrEE"
                                    allowFullScreen
                                    style="width:100%; height:100%; position:absolute; top:0; left:0; border-radius:inherit"
                                ></iframe>
                                """
                            ),
                            class_name="relative h-[300px] rounded-2xl shadow-2xl w-full overflow-hidden aspect-video",
                        ),
                        class_name="flex-1 flex justify-center items-center relative w-full",
                    ),
                    class_name="flex flex-col md:flex-row items-center py-20 md:py-28 space-y-8 md:space-y-0 md:space-x-10",
                ),
            )
        ),
        margin_x="auto",
        padding_x="1rem",
    )
