import reflex as rx
from components.icons.icons import bitcoin_icon, money_icon, stock_icon


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
                stats_card("Retorno acumulado", acc_return, bitcoin_icon(3.5, 60)),
                stats_card("Retorno anual médio", annual_return, money_icon(3.5, 60)),
                stats_card("Número de ativos", num_assets, stock_icon(3.5, 60)),
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
