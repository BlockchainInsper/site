import reflex as rx


# Lista de pesquisas/researches
researches = [
    {
        "nome": "Avalanche",
        "tags": ["Research", "2022"],
        "texto": "A Avalanche é uma plataforma pública e open-source que conta com uma blockchain layer 1 que suporta tanto smart contracts como redes personalizáveis.",
        "link": "https://docs.google.com/document/d/1elHJm_2-mVJG-Kll-drSWQPqbuYEthND/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://media.seudinheiro.com/uploads/2021/11/avalanche-avax-criptomoeda-logotipo.png",
    },
    {
        "nome": "Solana",
        "tags": ["Research", "2022"],
        "texto": "A criptomoeda Solana (Sol) foi lançada em março de 2020, com o objetivo de rivalizar com a Ethereum, focando em capacidade de escalabilidade e com o objetivo de oferecer soluções financeiras de forma descentralizada",
        "link": "https://docs.google.com/document/d/1a6PEjAoEJylOxrx_TA6mwLMgsQtcKZqf/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://www.infomoney.com.br/wp-content/uploads/2021/08/Solana-1024x683-1.png",
    },
    {
        "nome": "Polygon",
        "tags": ["Research", "2022"],
        "texto": "Criada em 2017, a MATIC é a moeda base do ecossistema Polygon, originalmente chamada de Rede Matic",
        "link": "https://docs.google.com/document/d/1HLnSFJ03SrjskQYaBIFhF-9ZY-oADU6e/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://thebuzzly.com/wp-content/uploads/2021/10/CryptoMode-Polygon-DeFi.jpg",
    },
    {
        "nome": "Polkadot",
        "tags": ["Research", "2022"],
        "texto": "Criada em 2016 por Gavin Wood, co-fundador do Ethereum, a Polkadot é uma plataforma que surgiu com o objetivo principal de ser uma rede que conecta diferentes blockchains",
        "link": "https://docs.google.com/document/d/1po8eeRmD1FlXz9PN1W7vF9M1Ckpn-uhO/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://mma.prnewswire.com/media/1712696/Polkadot_Logo.jpg?p=facebook",
    },
    {
        "nome": "Decentraland",
        "tags": ["Research", "2022"],
        "texto": "Decentraland é um software executado na rede Ethereum; projetado para incentivar uma rede global de usuários a operar um mundo virtual compartilhado",
        "link": "https://docs.google.com/document/d/1PJY7SxIGAs4V8hOO6ks8vwT4mr15wLna/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://www.criptofacil.com/wp-content/uploads/2022/03/metaverse-fashion-week-em-decentraland-comeca-hoje-com-token-mana-em-alta.jpg",
    },
    {
        "nome": "Uniswap",
        "tags": ["Research", "2022"],
        "texto": "Criado por Hayden Adams com alguns conselhos de Vitalik Buterin, o protocolo da Uniswap presente na blockchain da Ethereum possui duas funções: ela funciona como uma criptomoeda, o UNI, e também como uma DEX (Decentralized Exchange) que permite trocas entre tokens do tipo ERC-20",
        "link": "https://docs.google.com/document/d/1p35Q9VP11IpgYawmLnRtp6XxlMM68u4q/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
        "image": "https://uniswap.org/images/twitter-card.jpg",
    },
    {
        "nome": "Cardano",
        "tags": ["Research", "2019"],
        "texto": "Cardano é uma plataforma de criptomoedas e contratos inteligentes lançada em setembro de 2017, que se autodenomina como a “terceira geração” das criptomoedas...",
        "link": "https://drive.google.com/file/d/1bp_9Iik_oa23-CZMuMbjjAWWiBxlwhkj/view?usp=sharing",
        "image": "https://media.moneytimes.com.br/uploads/2020/05/cardano-ada-blockchain.jpg",
    },
    {
        "nome": "Chainlink",
        "tags": ["Research", "2019"],
        "texto": "Chainlink é uma rede descentralizada com o objetivo de conectar informações de fora da rede com a blockchain interna, a partir de um sistema oracles...",
        "link": "https://drive.google.com/file/d/180Jjlbytnzzf6CuFurfjVZE8o7dvq-5C/view?usp=sharing",
        "image": "https://suporte.mercadobitcoin.com.br/hc/article_attachments/360079203632/chainlink-combo-logo.png",
    },
    {
        "nome": "Monero",
        "tags": ["Research", "2019"],
        "texto": "Monero é um Fork da Bytecoin, a primeira criptomoeda privada, devido a algumas críticas feitas à moeda original, como a de que em seu início 80% de todas suas moedas já haviam sido mineradas. 7 desenvolvedores forkaram para monero (moeda em esperanto).",
        "link": "https://drive.google.com/file/d/1e3VWdperg6dzuhWvsTBBNQjl6WJhnLSj/view?usp=sharing",
        "image": "https://livecoins.com.br/wp-content/uploads/2018/03/monero-logo.png",
    },
    {
        "nome": "ZCash",
        "tags": ["Research", "2019"],
        "texto": "Zcash (ZEC) é uma criptomoeda descentralizada criada em 2016 pelo programador norte-americano Zooko Wilcox, e mantida pela instituição sem fins lucrativos chamada Fundação Zcash.",
        "link": "https://drive.google.com/file/d/1cFeVojTXAN10x64SInuLzBRBwmBDh7dh/view?usp=sharing",
        "image": "https://0xzx.com/wp-content/uploads/2020/07/zcash-transaction.jpg",
    },
    {
        "nome": "Litecoin",
        "tags": ["Research", "2019"],
        "texto": "O Litecoin foi criado por um ex-engenheiro da Google Charlie Lee, com o objetivo de aumentar a velocidade de transação e escalabilidade da moeda",
        "link": "https://drive.google.com/file/d/1lZ78r0MY6osoh6Mevr1BqGG6PL56wMBA/view?usp=sharing",
        "image": "https://moneyinvest.com.br/wp-content/uploads/2021/05/litcoin.jpeg",
    },
    {
        "nome": "NEO",
        "tags": ["Research", "2019"],
        "texto": "O projeto da NEO começou em fevereiro de 2014, quando o blockchain Antshares, foi criado sendo o primeiro desenvolvido na China.",
        "link": "https://drive.google.com/file/d/1PDIhivRzXI4Kb-QtDoQ9Hd14CZhP8mTN/view?usp=sharing",
        "image": "https://p7z2w8n8.rocketcdn.me/wp-content/uploads/2021/05/neo-o-que-e-como-funciona-vantagens-riscos-e-como-comprar.jpg",
    },
    {
        "nome": "Tezos",
        "tags": ["Research", "2019"],
        "texto": "Tezos é uma criptomoeda baseada em blockchain. Também tem sua própria plataforma de contratos inteligentes (smart contracts) que permite a criação de aplicativos descentralizados (dApps), sendo uma de suas propostas, ser uma plataforma de Security Token Offering (STO). Desse modo, o XTZ é um utility token que permite o acesso a rede blockchain da Tezos.",
        "link": "https://drive.google.com/file/d/1gjvQy92JAsCwSYP8Tgpz28wo07h2mc-E/view?usp=sharing",
        "image": "https://media.moneytimes.com.br/uploads/2020/11/tezos.jpg",
    },
    {
        "nome": "Dogecoin",
        "tags": ["Research", "2019"],
        "texto": "O Dogecoin (DOGE) é uma criptomoeda sem fins lucrativos fundada em dezembro de 2013 pelo australiano Jackson Palmer. O inusitado desta moeda é o fato de seu logotipo ser inspirado do meme “Doge”, a foto de um cachorro da raça Shiba Inu que viralizou na época.",
        "link": "https://drive.google.com/file/d/1KtwSyO8rE-vqVOJVfqKC3o3Y1MIGNbEL/view?usp=sharing",
        "image": "https://s2.glbimg.com/Yu_YuutgYfolZ-h9rW52gH45iuU=/696x390/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/L/F/tLAOX9QCm7171sqJZFCA/075-porzycki-dogecoin210622-npbea-b.jpg",
    },
    {
        "nome": "Ripple",
        "tags": ["Research", "2019"],
        "texto": "Fundado em 2012 por Chris Larsen e Jed McCaleb, o Ripple é tanto uma criptomoeda (XRP), como um protocolo de pagamento distribuído (RippleNet) que busca permitir que instituições financeiras mandem dinheiro de forma segura, instantânea e super barata para qualquer lugar.",
        "link": "https://drive.google.com/file/d/1aYR1DcfPprgULF_1U1XScJMrR0NUATL2/view?usp=sharing",
        "image": "https://mms.businesswire.com/media/20190611005917/pt/726896/23/Ripple_Logo.jpg",
    },
    {
        "nome": "Binance Coin",
        "tags": ["Research", "2019"],
        "texto": "A Binance Coin (BNB) é uma altcoin criada por uma das maiores exchanges de criptoativos, a Binance.",
        "link": "https://drive.google.com/file/d/161w-K0lMqIqkxjG7SyFOu3Cf9gatY8Fw/view?usp=sharing",
        "image": "https://public.bnbstatic.com/image/cms/blog/20210412/3f999b0c-de99-495d-b9bc-634eb7ef4c47.png",
    },
    {
        "nome": "Dash",
        "tags": ["Research", "2019"],
        "texto": "A Dash foi criada em 2014, com o intuito de solucionar alguns problemas do bitcoin, como a velocidade e privacidade das transações.",
        "link": "https://drive.google.com/file/d/1jJEvr_WnAMzcFYbtE0j5DMwMBCuoYY7f/view?usp=sharing",
        "image": "http://media.dash.org/wp-content/uploads/dash-digital-cash.png",
    },
    {
        "nome": "IOTA",
        "tags": ["Research", "2019"],
        "texto": "IOTA é uma das criptomoedas da chamada “terceira geração de blockchains”, que mesmo não utilizando-se de uma blockchain em si, visa resolver os problemas de escalabilidade e rapidez de uma rede blockchain convencional, para assim dar chão para as novas tecnologias e novas demandas advindas da chamada “Internet Of Things”.",
        "link": "https://drive.google.com/file/d/1IsJOcko-whb6qddaU3k4r4XDJjdb7bPS/view?usp=sharing",
        "image": "https://img.ibxk.com.br/2017/12/12/iota-12163208489279.png",
    },
]


# Componente para exibir estatísticas do fundo
def stats_card(title, stat, icon):
    return rx.box(
        rx.flex(
            rx.box(
                rx.text(
                    title,
                    style={
                        "font_weight": "medium",
                        "color": rx.color_mode_cond(light="gray.600", dark="gray.400"),
                    },
                ),
                rx.text(
                    stat,
                    style={
                        "font_size": "1.5rem",
                        "font_weight": "medium",
                        "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    },
                ),
                style={
                    "padding_left": rx.breakpoints(initial="0.5rem", md="1rem"),
                },
            ),
            rx.box(
                icon,
                style={
                    "margin_top": "auto",
                    "margin_bottom": "auto",
                    "color": rx.color_mode_cond(light="gray.800", dark="gray.200"),
                    "align_content": "center",
                },
            ),
            justify_content="space-between",
            style={
                "width": "100%",
            },
        ),
        style={
            "padding_x": rx.breakpoints(initial="0.5rem", md="1rem"),
            "padding_y": "1.25rem",
            "box_shadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            "border": "1px solid",
            "border_color": rx.color_mode_cond(light="gray.800", dark="gray.500"),
            "border_radius": "0.5rem",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "width": "100%",
            "transition": "transform 0.2s",
            "_hover": {
                "transform": "translateY(-5px)",
            },
        },
    )


# Componente de tags para os itens de pesquisa
def blog_tags(tags):
    return rx.hstack(
        *[
            rx.box(
                tag,
                style={
                    "background": rx.color_mode_cond(light="#ED8936", dark="#ED8936"),
                    "color": "white",
                    "font_size": "0.8rem",
                    "padding": "0.25rem 0.5rem",
                    "border_radius": "0.375rem",
                },
            )
            for tag in tags
        ],
        style={"margin_top": "0.75rem"},
    )


# Componente para cada item de pesquisa
def research_item(research):
    return rx.box(
        rx.box(
            rx.link(
                rx.image(
                    src=research["image"],
                    alt=f"Imagem de {research['nome']}",
                    style={
                        "transform": "scale(1.0)",
                        "object_fit": "contain",
                        "width": "100%",
                        "transition": "0.3s ease-in-out",
                        "_hover": {"transform": "scale(1.05)"},
                    },
                ),
                href=research["link"],
                is_external=True,
                style={
                    "text_decoration": "none",
                    "_hover": {"text_decoration": "none"},
                },
            ),
            style={"border_radius": "0.5rem", "overflow": "hidden"},
        ),
        blog_tags(research["tags"]),
        rx.heading(
            rx.link(
                research["nome"],
                href=research["link"],
                is_external=True,
                style={
                    "text_decoration": "none",
                    "_hover": {"text_decoration": "none"},
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
            ),
            style={
                "font_size": "1.25rem",
                "margin_top": "0.5rem",
                "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
            },
            as_="h2",
        ),
        rx.text(
            research["texto"],
            style={
                "font_size": "1rem",
                "margin_top": "0.5rem",
                "color": rx.color_mode_cond(light="gray.700", dark="gray.300"),
            },
        ),
        style={
            "width": "100%",
        },
    )


# Componente de lista de pesquisas
def research_list(researches):
    return rx.box(
        rx.heading(
            "Researches",
            style={
                "font_size": "1.5rem",
                "font_weight": "bold",
                "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
            },
            as_="h2",
        ),
        rx.divider(
            style={
                "margin_top": "1.25rem",
                "margin_bottom": "1.25rem",
                "border_color": rx.color_mode_cond(light="gray.300", dark="gray.600"),
            }
        ),
        rx.flex(
            *[
                rx.box(
                    research_item(research),
                    style={
                        "width": rx.breakpoints(
                            initial="100%", sm="45%", md="45%", lg="30%"
                        ),
                        "margin_bottom": "2rem",
                    },
                )
                for research in researches
            ],
            style={
                "margin_top": "1.25rem",
                "gap": "30px",
                "flex_wrap": "wrap",
                "justify_content": "flex-start",
            },
        ),
        style={
            "max_width": "80rem",
            "margin": "0 auto",
            "padding": "3rem",
        },
    )


def info_fundo(acc_return="--", annual_return="--", num_assets="--"):
    # Ícones para as estatísticas
    bitcoin_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 512 512">
            <path fill="currentColor" d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256S119.033 8 256 8s248 111.033 248 248m-141.651-35.33c4.937-32.999-20.191-50.739-54.55-62.573l11.146-44.702l-27.213-6.781l-10.851 43.524c-7.154-1.783-14.502-3.464-21.803-5.13l10.929-43.81l-27.198-6.781l-11.153 44.686c-5.922-1.349-11.735-2.682-17.377-4.084l.031-.14l-37.53-9.37l-7.239 29.062s20.191 4.627 19.765 4.913c11.022 2.751 13.014 10.044 12.68 15.825l-12.696 50.925c.76.194 1.744.473 2.829.907c-.907-.225-1.876-.473-2.876-.713l-17.796 71.338c-1.349 3.348-4.767 8.37-12.471 6.464c.271.395-19.78-4.937-19.78-4.937l-13.51 31.147l35.414 8.827c6.588 1.651 13.045 3.379 19.4 5.006l-11.262 45.213l27.182 6.781l11.153-44.733a1038 1038 0 0 0 21.687 5.627l-11.115 44.523l27.213 6.781l11.262-45.128c46.404 8.781 81.299 5.239 95.986-36.727c11.836-33.79-.589-53.281-25.004-65.991c17.78-4.098 31.174-15.792 34.747-39.949m-62.177 87.179c-8.41 33.79-65.308 15.523-83.755 10.943l14.944-59.899c18.446 4.603 77.6 13.717 68.811 48.956m8.417-87.667c-7.673 30.736-55.031 15.12-70.393 11.292l13.548-54.327c15.363 3.828 64.836 10.973 56.845 43.035" />
        </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "3.5rem",  # w-10
            "height": "3.5rem",  # h-10
        },
    )

    money_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 512 512">
                <path fill="currentColor" d="M327.027 65.816L229.79 128.23l9.856 5.397l86.51-55.53l146.735 83.116l-84.165 54.023l4.1 2.244v6.848l65.923-42.316l13.836 7.838l-79.76 51.195v11.723l64.633-41.487l15.127 8.57l-79.76 51.195v11.723l64.633-41.487l15.127 8.57l-79.76 51.195v11.723l100.033-64.21l-24.828-14.062l24.827-15.937l-24.828-14.064l24.827-15.937l-23.537-13.333l23.842-15.305zm31.067 44.74c-21.038 10.556-49.06 12.342-68.79 4.383l-38.57 24.757l126.903 69.47l36.582-23.48c-14.41-11.376-13.21-28.35 2.942-41.67zM227.504 147.5l-70.688 46.094l135.61 78.066l1.33-.85c2.5-1.61 6.03-3.89 10.242-6.613c8.42-5.443 19.563-12.66 30.674-19.86c16.002-10.37 24.248-15.72 31.916-20.694zm115.467 1.17a8.583 14.437 82.068 0 1 .003 0a8.583 14.437 82.068 0 1 8.32 1.945a8.583 14.437 82.068 0 1-.87 12.282a8.583 14.437 82.068 0 1-20.273 1.29a8.583 14.437 82.068 0 1 .87-12.28a8.583 14.437 82.068 0 1 11.95-3.237m-218.423 47.115L19.143 263.44l23.537 13.333l-23.842 15.305l24.828 14.063l-24.828 15.938l24.828 14.063l-24.828 15.938l166.135 94.106L285.277 381.8v-11.72l-99.433 63.824L39.11 350.787l14.255-9.15l131.608 74.547L285.277 351.8v-11.72l-99.433 63.824L39.11 320.787l14.255-9.15l131.608 74.547L285.277 321.8v-11.72l-99.433 63.824L39.11 290.787l13.27-8.52l132.9 75.28l99.997-64.188v-5.05l-5.48-3.154l-93.65 60.11l-146.73-83.116l94.76-60.824l-9.63-5.543zm20.46 11.78l-46.92 30.115c14.41 11.374 13.21 28.348-2.942 41.67l59.068 33.46c21.037-10.557 49.057-12.342 68.787-4.384l45.965-29.504l-123.96-71.358zm229.817 32.19c-8.044 5.217-15.138 9.822-30.363 19.688a36222 36222 0 0 1-30.69 19.873c-4.217 2.725-7.755 5.01-10.278 6.632c-.09.06-.127.08-.215.137v85.924l71.547-48.088zm-200.99 17.48a8.583 14.437 82.068 0 1 8.32 1.947a8.583 14.437 82.068 0 1-.87 12.28a8.583 14.437 82.068 0 1-20.27 1.29a8.583 14.437 82.068 0 1 .87-12.28a8.583 14.437 82.068 0 1 11.95-3.236z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "3.5rem",  # w-10
            "height": "3.5rem",  # h-10
        },
    )

    stock_svg = rx.html(
        """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 16 16">
                <path fill="none" stroke="currentColor" stroke-linejoin="round" d="M1.583 4.5L8 1.583L14.417 4.5m-12.834 0L8 7.417M1.583 4.5v6.417L8 14.417m0-7L14.417 4.5M8 7.417v7M14.417 4.5v6.417L8 14.417M10.5 13V9.5m2 2.5V8.5" stroke-width="1" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": "3.5rem",  # w-10
            "height": "3.5rem",  # h-10
        },
    )

    return rx.box(
        # Seção de estatísticas
        rx.box(
            rx.heading(
                "Indicadores",
                style={
                    "text_align": "center",
                    "font_size": "2.25rem",
                    "padding_y": "2.5rem",
                    "font_weight": "bold",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
            ),
            rx.grid(
                stats_card("Retorno acumulado", acc_return, bitcoin_svg),
                stats_card("Retorno anual médio", annual_return, money_svg),
                stats_card("Número de ativos", num_assets, stock_svg),
                columns=rx.breakpoints(initial="1", md="3"),
                gap=rx.breakpoints(initial="1.25rem", lg="2rem"),
                style={
                    "width": "100%",
                },
            ),
            style={
                "max_width": "80rem",
                "margin": "0 auto",
                "padding_top": "1.25rem",
                "padding_x": rx.breakpoints(initial="0.5rem", sm="3rem", md="4.25rem"),
                "margin_bottom": "5rem",
            },
        ),
        # Seção de pesquisas
        research_list(researches),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
