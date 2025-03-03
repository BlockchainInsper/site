import reflex as rx


def feature(text, icon, icon_bg):
    """Componente Feature que exibe um ícone com texto."""
    return rx.flex(
        rx.flex(
            icon,
            width="2rem",
            height="2rem",
            align="center",
            justify="center",
            border_radius="full",
            bg=icon_bg,
        ),
        rx.text(text, font_weight="600", margin_left="0.75rem"),
        align="center",
    )


def features():
    """Componente principal que exibe informações sobre a organização com imagem."""
    return rx.box(
        rx.container(
            # Substituindo o grid por hstack para layout horizontal
            rx.hstack(
                # Coluna da esquerda com texto
                rx.vstack(
                    rx.heading(
                        "Reavaliando o presente e construindo o futuro",
                        size="4",
                        margin_bottom="1.5rem",
                    ),
                    rx.text(
                        "Buscamos criar um time altamente engajado e preparado "
                        "para enfrentar a nova onda de tecnologia no mercado de trabalho. "
                        "Seguimos com o objetivo de estimular o estudo e a adoção "
                        "dessa tecnologia no Brasil, criando conhecimento não apenas "
                        "para o agora, como também para o futuro.",
                        color="#A0AEC0",
                        margin_bottom="2rem",
                    ),
                    # Seção Nossa Missão
                    rx.vstack(
                        rx.box(
                            feature(
                                text="Nossa Missão",
                                icon=rx.icon(
                                    tag="rocket",
                                    color="#D69E2E",
                                    width="1.25rem",
                                    height="1.25rem",
                                ),
                                icon_bg="#744210",
                            ),
                            width="100%",
                        ),
                        rx.text(
                            "Fomentar o desenvolvimento do ecossistema brasileiro "
                            "em torno da tecnologia blockchain, criando um futuro mais eficiente "
                            "através da tecnologia.",
                            color="#A0AEC0",
                            margin_top="0.5rem",
                            margin_bottom="1rem",
                        ),
                        rx.divider(border_color="#2D3748"),
                        align_items="start",
                        width="100%",
                        spacing="4",
                        margin_bottom="1rem",
                    ),
                    # Seção Nossa Visão
                    rx.vstack(
                        rx.box(
                            feature(
                                text="Nossa Visão",
                                icon=rx.icon(
                                    tag="eye",
                                    color="#38A169",
                                    width="1.25rem",
                                    height="1.25rem",
                                ),
                                icon_bg="#1C4532",
                            ),
                            width="100%",
                        ),
                        rx.text(
                            "Capacitar os alunos com o melhor conteúdo e conectá-los ao mercado, "
                            "no intuito de incluir nosso país nesse cenário de inovação.",
                            color="#A0AEC0",
                            margin_top="0.5rem",
                            margin_bottom="1rem",
                        ),
                        rx.divider(border_color="#2D3748"),
                        align_items="start",
                        width="100%",
                        spacing="4",
                        margin_bottom="1rem",
                    ),
                    # Seção Nossos Valores
                    rx.vstack(
                        rx.box(
                            feature(
                                text="Nossos Valores",
                                icon=rx.icon(
                                    tag="compass",
                                    color="#805AD5",
                                    width="1.25rem",
                                    height="1.25rem",
                                ),
                                icon_bg="#44337A",
                            ),
                            width="100%",
                        ),
                        rx.text(
                            "Alto comprometimento, proatividade, inovação, "
                            "trabalho em equipe, multidisciplinaridade, excelência e eficiência.",
                            color="#A0AEC0",
                            margin_top="0.5rem",
                        ),
                        align_items="start",
                        width="100%",
                        spacing="4",
                    ),
                    align_items="flex-start",
                    spacing="0",
                    width="100%",
                ),
                # Coluna da direita com imagem
                rx.box(
                    rx.image(
                        src="/insper.jpg",
                        alt="Auditório Insper",
                        width="100%",
                        height="100%",
                        border_radius="md",
                        object_fit="cover",
                    ),
                ),
                # Configuração do hstack
                spacing="8",
                align_items="center",
                width="100%",
                # Tornando responsivo para dispositivos móveis
                flex_direction=rx.cond(rx.breakpoints(md=True), "row", "column"),
            ),
            max_width="90rem",
            padding_y="3rem",
            padding_x="1.5rem",
        ),
        background_color="#1A202C",
        color="white",
    )
