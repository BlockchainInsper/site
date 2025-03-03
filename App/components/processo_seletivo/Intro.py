import reflex as rx


def feature(heading, text):
    return rx.box(
        rx.heading(
            heading,
            class_name="text-xl font-bold mb-2",
            as_="h3",
        ),
        rx.text(
            text,
            class_name="text-gray-600",
        ),
    )


def intro():
    return rx.box(
        rx.box(
            # Grid de duas colunas (1 em mobile)
            rx.grid(
                # Coluna 1 - Título e botões
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Nosso Processo Seletivo chegou!",
                            class_name="text-3xl font-bold",
                            as_="h2",
                        ),
                        rx.link(
                            rx.button(
                                "Inscrever-se",
                                class_name="bg-[#f68b23] text-white hover:bg-[#f68b70] rounded-md px-4 py-2",
                            ),
                            href="https://docs.google.com/forms/d/e/1FAIpQLScQyW4RGcwtcNAAVtYj3iFJdgJ4Khq07rSluQo5tWROKWYxow/viewform",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    # SVG personalizado do Discord
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z",
                                            fill="currentColor",
                                        ),
                                        viewBox="0 0 24 24",
                                        width="20px",
                                        height="20px",
                                        xmlns="http://www.w3.org/2000/svg",
                                        class_name="text-white w-5 h-5",
                                    ),
                                    rx.text("Discord"),
                                ),
                                class_name="bg-[#5865F2] text-white hover:bg-[#5865F2]/90 rounded-md px-4 py-2",
                            ),
                            href="https://discord.gg/jdK5yB48Mm",
                            is_external=True,
                        ),
                        spacing="5",
                        align_items="flex-start",
                        class_name="items-start",
                    ),
                ),
                # Coluna 2 - Texto descritivo
                rx.box(
                    rx.text(
                        "O maior experimento financeiro e sociológico do século XXI, o "
                        "Bitcoin veio solucionar diversos problemas antes sem solução. A "
                        "Blockchain Insper vai te dar base para entender o que está por "
                        "trás da construção do protocolo e o que motivou Satoshi Nakamoto a "
                        "desenvolvê-lo, entre muitas outras coisas que rondam essa "
                        "tecnologia que está revolucionando a economia mundial. Além disso, "
                        "temos parcerias com as maiores empresas do mercado para, além de "
                        "ganhar conhecimento, saber como funcionam os projetos na prática.",
                        class_name="text-gray-600",
                    ),
                ),
                # Configuração do grid
                columns=rx.breakpoints(initial="1", sm="2"),
                gap="1rem",
                class_name="w-full",
            ),
            # Divisor horizontal
            rx.divider(
                class_name="my-12 border-gray-200",
            ),
            # Grid de quatro colunas
            rx.grid(
                # Fase 1
                feature(
                    heading="Primeira Fase",
                    text="Preenchimento de um Forms com detalhes pessoais e perguntas de caráter opinativo.",
                ),
                # Fase 2
                feature(
                    heading="Segunda Fase",
                    text="Resolução de um case elaborado em parceria com o BTG e com a Mynt.",
                ),
                # Fase 3
                feature(
                    heading="Terceira Fase",
                    text="Entrevista individual para conhecer melhor o candidato com perguntas pessoais e possivelmente técnicas.",
                ),
                # Fase 4
                feature(
                    heading="Programa de Trainees",
                    text="Desempenho no Curso de Introdução à Blockchain e Projeto Interno Aplicado (nessa fase, os candidatos já ganham entre 5 e 10 horas complementares).",
                ),
                # Configuração do grid
                columns=rx.breakpoints(initial="1", sm="2", md="4"),
                gap=rx.breakpoints(initial="2rem", sm="3rem", md="4rem"),
                class_name="w-full",
            ),
            # Divisor horizontal
            rx.divider(
                class_name="my-12 border-gray-200",
            ),
            # Configuração do container
            class_name="max-w-7xl mx-auto p-4",
        ),
        class_name="w-full py-10 bg-white dark:bg-gray-800 text-gray-900 dark:text-white",
    )
