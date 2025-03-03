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
                class_name="space-x-2",
            ),
            class_name="rounded-full text-lg font-normal px-6 text-white bg-[#5865F2] hover:bg-[#5865F2]",
        ),
        href="https://discord.gg/jdK5yB48Mm",
        is_external=True,
        class_name="no-underline",
    )


def blob(props=None):
    """Blob component precisely matching the original JavaScript implementation."""
    if props is None:
        props = {}

    class_name = props.pop("class_name", "")

    return rx.el.svg(
        rx.el.svg.path(
            fill_rule="evenodd",
            clip_rule="evenodd",
            d="M239.184 439.443c-55.13-5.419-110.241-21.365-151.074-58.767C42.307 338.722-7.478 282.729.938 221.217c8.433-61.644 78.896-91.048 126.871-130.712 34.337-28.388 70.198-51.348 112.004-66.78C282.34 8.024 325.382-3.369 370.518.904c54.019 5.115 112.774 10.886 150.881 49.482 39.916 40.427 49.421 100.753 53.385 157.402 4.13 59.015 11.255 128.44-30.444 170.44-41.383 41.683-111.6 19.106-169.213 30.663-46.68 9.364-88.56 35.21-135.943 30.551z",
            fill="currentColor",
        ),
        view_box="0 0 578 440",
        fill="none",
        xmlns="http://www.w3.org/2000/svg",
        class_name=f"w-full h-[150%] inline-block leading-[1em] flex-shrink-0 align-middle text-[#f68b23] absolute -top-[20%] left-0 z-0 {class_name}",
        **props,
    )


def call_to_action_with_video():
    return rx.box(
        rx.box(  # Outer container para centralizar
            rx.stack(
                # Stack da esquerda com texto e botão
                rx.stack(
                    # Heading
                    rx.heading(
                        rx.text(
                            "Venha conhecer",
                            as_="span",
                            class_name="relative z-[1] after:content-[''] after:absolute after:w-full after:h-[30%] after:bottom-[1px] after:left-0 after:bg-[#f68b23] after:z-[-1]",
                        ),
                        rx.el.br(),
                        rx.text(
                            "nosso trabalho!",
                            as_="span",
                            class_name="text-[#f68b23]",
                        ),
                        class_name="font-semibold leading-[1.1] text-3xl sm:text-4xl lg:text-6xl",
                    ),
                    # Texto descritivo
                    rx.text(
                        "Criada em setembro de 2017, a Blockchain Insper é a primeira "
                        "organização estudantil da América Latina focada em estudo de tecnologias "
                        "blockchain. Derivada de uma iniciativa universitária, que reúne "
                        "estudantes de administração, economia, engenharias e direito a entidade está "
                        "dividida em três áreas de estudo: Business, Finance e Tecnologia.",
                        class_name="text-gray-500 font-bold",
                    ),
                    # Botões (só o Discord neste caso)
                    rx.stack(
                        discord_button(),
                        class_name="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-6",
                    ),
                    class_name="flex-1 flex flex-col space-y-5 md:space-y-10",
                ),
                # Flex da direita com o vídeo
                rx.flex(
                    # Box que contém o blob e o vídeo com overflow para o blob não ser cortado
                    rx.box(
                        # Blob de decoração
                        blob(),  # Aumentando o blob um pouco
                        # Box do vídeo
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
                            class_name="relative h-[300px] rounded-2xl shadow-2xl w-full overflow-hidden z-10",
                        ),
                        class_name="relative w-full h-full",  # Container para o blob e vídeo
                    ),
                    class_name="flex-1 flex justify-center items-center relative w-full overflow-visible",  # Overflow visible para o blob
                ),
                class_name="flex flex-col md:flex-row items-center py-20 md:py-28 space-y-8 md:space-y-0 md:space-x-10 w-full",
            ),
            class_name="max-w-[90rem] px-4 md:px-8 w-full mx-auto",  # Container centralizado, largura adequada
        ),
        class_name="w-full py-12 flex justify-center bg-[#1A202C] text-white",  # Box externo com background color
    )
