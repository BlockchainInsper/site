import reflex as rx
from datetime import datetime


def footer() -> rx.Component:
    return rx.box(
        # Container centralizado com largura máxima
        rx.box(
            # Flex para organizar os elementos
            rx.flex(
                # Coluna da esquerda com logo e copyright
                rx.flex(
                    # Logo
                    rx.image(
                        src=rx.color_mode_cond(
                            "/logo-light.svg",
                            "/logo-dark.svg",
                        ),
                        width="100px",
                    ),
                    # Texto de copyright abaixo da logo
                    rx.text(
                        f"© {datetime.now().year} Blockchain Insper. All rights reserved.",
                        class_name="text-sm text-gray-600 dark:text-gray-400",
                    ),
                    class_name="flex flex-col items-start justify-center space-y-2",
                ),
                # Flex com ícones na direita
                rx.flex(
                    # Discord com SVG personalizado
                    rx.link(
                        rx.el.svg(
                            rx.el.svg.path(
                                d="M14.82 4.26a10.14 10.14 0 0 0-.53 1.1 14.66 14.66 0 0 0-4.58 0 10.14 10.14 0 0 0-.53-1.1 16 16 0 0 0-4.13 1.3 17.33 17.33 0 0 0-3 11.59 16.6 16.6 0 0 0 5.07 2.59A12.89 12.89 0 0 0 8.23 18a9.65 9.65 0 0 1-1.71-.83 3.39 3.39 0 0 0 .42-.33 11.66 11.66 0 0 0 10.12 0q.21.18.42.33a10.84 10.84 0 0 1-1.71.84 12.41 12.41 0 0 0 1.08 1.78 16.44 16.44 0 0 0 5.06-2.59 17.22 17.22 0 0 0-3-11.59 16.09 16.09 0 0 0-4.09-1.35zM8.68 14.81a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.93 1.93 0 0 1 1.8 2 1.93 1.93 0 0 1-1.8 2zm6.64 0a1.94 1.94 0 0 1-1.8-2 1.93 1.93 0 0 1 1.8-2 1.92 1.92 0 0 1 1.8 2 1.92 1.92 0 0 1-1.8 2z",
                                fill="currentColor",
                            ),
                            viewBox="0 0 24 24",
                            width="20px",
                            height="20px",
                            xmlns="http://www.w3.org/2000/svg",
                            class_name="text-white",
                        ),
                        href="https://discord.gg/jdK5yB48Mm",
                        is_external=True,
                        class_name="text-white hover:bg-white/10 hover:rounded-md ml-4 flex items-center justify-center min-w-[2.5rem] h-10",
                    ),
                    # LinkedIn
                    rx.link(
                        rx.icon(
                            tag="linkedin",
                            size=20,
                            class_name="text-white",
                        ),
                        href="https://www.linkedin.com/company/blockchain-insper",
                        is_external=True,
                        class_name="text-white hover:bg-white/10 hover:rounded-md ml-2 flex items-center justify-center min-w-[2.5rem] h-10",
                    ),
                    # Instagram
                    rx.link(
                        rx.icon(
                            tag="instagram",
                            size=20,
                            class_name="text-white",
                        ),
                        href="https://www.instagram.com/blockchainsper/",
                        is_external=True,
                        class_name="text-white hover:bg-white/10 hover:rounded-md ml-2 flex items-center justify-center min-w-[2.5rem] h-10",
                    ),
                    # GitHub
                    rx.link(
                        rx.icon(
                            tag="github",
                            size=20,
                            class_name="text-white",
                        ),
                        href="https://github.com/BlockchainInsper",
                        is_external=True,
                        class_name="text-white hover:bg-white/10 hover:rounded-md ml-2 flex items-center justify-center min-w-[2.5rem] h-10",
                    ),
                    # Email
                    rx.link(
                        rx.icon(
                            tag="mail",
                            size=20,
                            class_name="text-white",
                        ),
                        href="mailto:blockchainsper@gmail.com",
                        is_external=True,
                        class_name="text-white hover:bg-white/10 hover:rounded-md ml-2 flex items-center justify-center min-w-[2.5rem] h-10",
                    ),
                    class_name="flex flex-row items-center",
                ),
                # Ajustes do container principal - responsivo
                class_name="flex flex-col sm:flex-row justify-between w-full items-center sm:items-start space-y-4 sm:space-y-0",
            ),
            # Container centralizado com padding e largura máxima
            class_name="max-w-7xl mx-auto px-4 md:px-8 w-full",
        ),
        role="contentinfo",
        # Box externo ocupa toda a largura da tela
        class_name="w-full py-12 bg-[#1A202C]",
    )
