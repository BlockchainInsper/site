import reflex as rx
from App.Template import template


# Definição dos caminhos para imagens
ambev = "/projetos/ambev.jpeg"
fundo = "/projetos/fundo.png"
gaugecash = "/projetos/gaugecash.jpg"
mineracao = "/projetos/mineracao.jpg"
nfts = "/projetos/nfts.jpg"
precatorios = "/projetos/precatorios.jpeg"


# Lista de projetos
projetos = [
    {
        "nome": "Business Case Ambev",
        "descricao": "Foi avaliada a aplicação de blockchain na operação da Ambev para tornar o gerenciamento da sua cadeia logística mais eficiente e transparente, visando diminuir custos e ao mesmo tempo criar valor para o consumidor.",
        "imagem": ambev,
    },
    {
        "nome": "Tokenização de Precatórios",
        "descricao": "Foi desenvolvida uma solução de tokenização de recebíveis judiciais no padrão ERC-20, junto ao Grupo GCB e à PeerBR.",
        "imagem": precatorios,
    },
    {
        "nome": "ICO Presale da GAUGECASH",
        "descricao": "Durante este projeto foi desenvolvido, em parceria com uma grande empresa do mercado, um Initial Coin Offering para a GAUGECASH, o primeiro sistema monetário descentralizado. ",
        "imagem": gaugecash,
    },
    {
        "nome": "Fundo Simulado",
        "descricao": "Como um norte para os estudos produzidos, o Fundo Simulado surgiu para testar e refinar a eficácia das análises desenvolvidas pelos membros, colocando na prática toda a pesquisa e bagagem teórica adquiridas.",
        "imagem": fundo,
    },
    {
        "nome": "Registro dos membros em NFTs",
        "descricao": "Foi desenvolvido um sistema de registro a fim de guardar as informações de nossos membros de uma maneira segura e eterna. O sistema usa o IPFS e a rede Polygon, garantindo imutabilidade e segurança.",
        "imagem": nfts,
    },
    {
        "nome": "Valuation Mineração",
        "descricao": "Em parceria com uma grande empresa do mercado, foi realizado um estudo completo que estipulou diversos fatores do setor de mineração de criptoativos. Esses números foram, então, analisados para averiguar um possível investimento.",
        "imagem": mineracao,
    },
]


def card1(data):
    return rx.box(
        rx.box(
            rx.flex(
                # Lado esquerdo - Imagem
                rx.box(
                    rx.box(
                        rx.image(
                            src=data["imagem"],
                            alt="Imagem do projeto",
                            style={
                                "border_radius": "0.5rem",  # borderRadius="lg"
                                "object_fit": "contain",
                            },
                        ),
                        style={
                            "width": rx.breakpoints(initial="100%", sm="85%"),
                            "z_index": "2",
                            "margin_left": rx.breakpoints(initial="0", sm="5%"),
                            "margin_top": "5%",
                        },
                    ),
                    rx.box(
                        rx.box(
                            style={
                                "background": "radial-gradient("
                                + rx.color_mode_cond(
                                    light="#C05621 1px, transparent 1px",
                                    dark="#F6AD55 1px, transparent 1px",
                                )
                                + ")",
                                "background_size": "20px 20px",
                                "opacity": "0.4",
                                "height": "100%",
                            }
                        ),
                        style={
                            "z_index": "1",
                            "width": "100%",
                            "position": "absolute",
                            "height": "100%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "margin_right": "0.75rem",  # marginRight="3"
                        "position": "relative",
                        "align_items": "center",
                    },
                ),
                # Lado direito - Texto
                rx.box(
                    rx.heading(
                        data["nome"],
                        style={
                            "margin_top": "0.25rem",  # marginTop="1"
                            "font_weight": "700",
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                            "font_size": "2.25rem",
                        },
                    ),
                    rx.text(
                        data["descricao"],
                        as_="p",
                        style={
                            "margin_top": "0.5rem",  # marginTop="2"
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#E2E8F0"
                            ),
                            "font_size": "1.125rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "flex_direction": "column",
                        "justify_content": "center",
                        "margin_top": rx.breakpoints(
                            initial="0.75rem", sm="0"
                        ),  # marginTop={{ initial: '3', sm: '0' }}
                    },
                ),
                style={
                    "display": "flex",
                    "flex_direction": rx.breakpoints(initial="column", sm="row"),
                    "justify_content": "space-between",
                    "width": "100%",
                },
            ),
            style={
                "max_width": "7xl",
                "padding": "3rem",  # p="12"
            },
        ),
        style={
            "width": "100%",
            "display": "flex",
            "justify_content": "center",
        },
    )


def card2(data):
    return rx.box(
        rx.box(
            rx.flex(
                # Lado esquerdo - Texto
                rx.box(
                    rx.heading(
                        data["nome"],
                        style={
                            "margin_top": "0.25rem",  # marginTop="1"
                            "font_weight": "700",
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#F7FAFC"
                            ),
                            "font_size": "2.25rem",
                        },
                    ),
                    rx.text(
                        data["descricao"],
                        as_="p",
                        style={
                            "margin_top": "0.5rem",  # marginTop="2"
                            "color": rx.color_mode_cond(
                                light="#2D3748", dark="#E2E8F0"
                            ),
                            "font_size": "1.125rem",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "flex_direction": "column",
                        "justify_content": "center",
                        "margin_top": rx.breakpoints(
                            initial="0.75rem", sm="0"
                        ),  # marginTop={{ initial: '3', sm: '0' }}
                    },
                ),
                # Lado direito - Imagem
                rx.box(
                    rx.box(
                        rx.image(
                            src=data["imagem"],
                            alt="Imagem do projeto",
                            style={
                                "border_radius": "0.5rem",  # borderRadius="lg"
                                "object_fit": "contain",
                                "width": "100%",
                            },
                        ),
                        style={
                            "width": rx.breakpoints(initial="100%", sm="85%"),
                            "z_index": "2",
                            "margin_left": rx.breakpoints(initial="0", sm="5%"),
                            "margin_top": "5%",
                        },
                    ),
                    rx.box(
                        rx.box(
                            style={
                                "background": "radial-gradient("
                                + rx.color_mode_cond(
                                    light="#C05621 1px, transparent 1px",
                                    dark="#F6AD55 1px, transparent 1px",
                                )
                                + ")",
                                "background_size": "20px 20px",
                                "opacity": "0.4",
                                "height": "100%",
                            }
                        ),
                        style={
                            "z_index": "1",
                            "width": "100%",
                            "position": "absolute",
                            "height": "100%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "flex": "1",
                        "position": "relative",
                        "align_items": "center",
                    },
                ),
                style={
                    "display": "flex",
                    "flex_direction": rx.breakpoints(initial="column", sm="row"),
                    "justify_content": "space-between",
                    "width": "100%",
                },
            ),
            style={
                "max_width": "7xl",
                "padding": "3rem",  # p="12"
            },
        ),
        style={
            "width": "100%",
            "display": "flex",
            "justify_content": "center",
        },
    )


@rx.page(route="/projects", title="Blockchain Insper")
@template
def projetos_page():
    return rx.box(
        # Cabeçalho
        rx.box(
            rx.box(
                rx.heading(
                    "Projetos",
                    style={
                        "font_size": "3.75rem",  # size="3xl"
                        "font_weight": "800",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                        "line_height": "1",  # Adicionar controle de altura da linha
                    },
                ),
                rx.text(
                    "Nesta seção, você vai poder conhecer alguns dos nossos projetos públicos",
                    style={
                        "margin_top": "1rem",  # mt="4"
                        "font_size": "1.125rem",
                        "color": rx.color_mode_cond(light="gray.700", dark="gray.300"),
                    },
                ),
                style={
                    "max_width": "42rem",
                    "margin_left": "auto",
                    "margin_right": "auto",
                    "padding_x": rx.breakpoints(
                        initial="1.5rem", lg="2rem"
                    ),  # px={{ initial: '6', lg: '8' }}
                    "padding_y": rx.breakpoints(
                        initial="4rem", sm="5rem"
                    ),  # py={{ initial: '16', sm: '20' }}
                    "text_align": "center",
                },
            ),
            as_="section",
            style={
                "width": "100%",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        # Lista de projetos
        rx.vstack(
            # Usando list comprehension para renderizar os cards
            *[
                card1(projeto) if i % 2 == 0 else card2(projeto)
                for i, projeto in enumerate(projetos)
            ],
            style={
                "width": "100%",
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                "padding_bottom": "3rem",
            },
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
