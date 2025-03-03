import reflex as rx


def feature(text, icon, icon_bg):
    """Componente Feature que exibe um ícone com texto."""
    return rx.flex(
        rx.flex(
            icon,
            class_name=f"w-8 h-8 items-center justify-center rounded-full bg-[{icon_bg}] flex",
        ),
        rx.text(
            text,
            class_name="font-semibold ml-3",
        ),
        class_name="flex flex-row items-center",
    )


def features():
    """Componente principal que exibe informações sobre a organização com imagem."""
    return rx.box(
        rx.container(
            # SimpleGrid com 2 colunas em desktop, 1 em mobile
            rx.grid(
                # COLUNA 1 - Stack vertical com texto e features
                rx.vstack(
                    # Título
                    rx.heading(
                        "Reavaliando o presente e construindo o futuro",
                        class_name="text-2xl font-bold",
                    ),
                    # Descrição
                    rx.text(
                        "Buscamos criar um time altamente engajado e preparado "
                        "para enfrentar a nova onda de tecnologia no mercado de trabalho. "
                        "Seguimos com o objetivo de estimular o estudo e a adoção "
                        "dessa tecnologia no Brasil, criando conhecimento não apenas "
                        "para o agora, como também para o futuro.",
                        class_name="text-gray-400 text-lg",
                    ),
                    # Stack com as 3 seções divididas
                    rx.vstack(
                        # Seção Nossa Missão
                        rx.box(
                            feature(
                                text="Nossa Missão",
                                icon=rx.icon(
                                    tag="rocket",
                                    class_name="text-yellow-500 w-5 h-5",
                                ),
                                icon_bg="#744210",
                            ),
                            rx.text(
                                "Fomentar o desenvolvimento do ecossistema brasileiro "
                                "em torno da tecnologia blockchain, criando um futuro mais eficiente "
                                "através da tecnologia.",
                                class_name="text-gray-400 mt-2",
                            ),
                        ),
                        # Divider
                        rx.divider(class_name="border-gray-700"),
                        # Seção Nossa Visão
                        rx.box(
                            feature(
                                text="Nossa Visão",
                                icon=rx.icon(
                                    tag="eye",
                                    class_name="text-green-500 w-5 h-5",
                                ),
                                icon_bg="#1C4532",
                            ),
                            rx.text(
                                "Capacitar os alunos com o melhor conteúdo e conectá-los ao mercado, "
                                "no intuito de incluir nosso país nesse cenário de inovação.",
                                class_name="text-gray-400 mt-2",
                            ),
                        ),
                        # Divider
                        rx.divider(class_name="border-gray-700"),
                        # Seção Nossos Valores
                        rx.box(
                            feature(
                                text="Nossos Valores",
                                icon=rx.icon(
                                    tag="compass",
                                    class_name="text-purple-500 w-5 h-5",
                                ),
                                icon_bg="#44337A",
                            ),
                            rx.text(
                                "Alto comprometimento, proatividade, inovação, "
                                "trabalho em equipe, multidisciplinaridade, excelência e eficiência.",
                                class_name="text-gray-400 mt-2",
                            ),
                        ),
                        class_name="space-y-4 w-full",
                        align_items="start",
                    ),
                    class_name="space-y-4 w-full",
                    align_items="start",
                ),
                # COLUNA 2 - Imagem
                rx.flex(
                    rx.image(
                        src="/insper.jpg",
                        alt="Auditório Insper",
                        class_name="w-full h-full rounded-md object-cover",
                    ),
                    class_name="w-full h-full",
                ),
                # Configuração do grid
                class_name="grid grid-cols-1 md:grid-cols-2 gap-10",
            ),
            class_name="max-w-[90rem] py-12 px-6",
        ),
        class_name="w-full bg-[#1A202C] text-white",
    )
