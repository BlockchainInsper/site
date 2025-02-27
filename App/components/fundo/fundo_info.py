import reflex as rx


def info_fundo():
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.el.svg(
                        rx.el.svg.circle(
                            cx="50",
                            cy="50",
                            r="42",
                            stroke_width="10px",
                            class_name="chakra-progress__track css-ol3i12",
                        ),
                        rx.el.svg.circle(
                            cx="50",
                            cy="50",
                            r="42",
                            stroke_width="10px",
                            class_name="chakra-progress__indicator css-sp5bsz",
                        ),
                        viewbox="0 0 100 100",
                        class_name="css-jf70f3",
                    ),
                    class_name="chakra-progress css-120wkjd",
                    aria_valuemax="100",
                    aria_valuemin="0",
                    role="progressbar",
                    custom_attrs={"data-indeterminate": ""},
                ),
                class_name="css-gmuwbf",
            ),
            class_name="css-ilwvj3",
        ),
        rx.box(
            rx.heading("Indicadores", class_name="css-1b10ebd", as_="h1", size="8"),
            rx.box(
                rx.box(
                    rx.el.dl(
                        rx.box(
                            rx.box(
                                rx.el.dt(
                                    "Retorno acumulado",
                                    class_name="chakra-stat__label css-1or5rq5",
                                ),
                                rx.el.dd(class_name="chakra-stat__number css-2u1up0"),
                                class_name="css-1sgy36a",
                            ),
                            rx.box(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zm-141.651-35.33c4.937-32.999-20.191-50.739-54.55-62.573l11.146-44.702-27.213-6.781-10.851 43.524c-7.154-1.783-14.502-3.464-21.803-5.13l10.929-43.81-27.198-6.781-11.153 44.686c-5.922-1.349-11.735-2.682-17.377-4.084l.031-.14-37.53-9.37-7.239 29.062s20.191 4.627 19.765 4.913c11.022 2.751 13.014 10.044 12.68 15.825l-12.696 50.925c.76.194 1.744.473 2.829.907-.907-.225-1.876-.473-2.876-.713l-17.796 71.338c-1.349 3.348-4.767 8.37-12.471 6.464.271.395-19.78-4.937-19.78-4.937l-13.51 31.147 35.414 8.827c6.588 1.651 13.045 3.379 19.4 5.006l-11.262 45.213 27.182 6.781 11.153-44.733a1038.209 1038.209 0 0 0 21.687 5.627l-11.115 44.523 27.213 6.781 11.262-45.128c46.404 8.781 81.299 5.239 95.986-36.727 11.836-33.79-.589-53.281-25.004-65.991 17.78-4.098 31.174-15.792 34.747-39.949zm-62.177 87.179c-8.41 33.79-65.308 15.523-83.755 10.943l14.944-59.899c18.446 4.603 77.6 13.717 68.811 48.956zm8.417-87.667c-7.673 30.736-55.031 15.12-70.393 11.292l13.548-54.327c15.363 3.828 64.836 10.973 56.845 43.035z"
                                    ),
                                    stroke="currentColor",
                                    fill="currentColor",
                                    stroke_width="0",
                                    viewbox="0 0 512 512",
                                    height="3em",
                                    width="3em",
                                    xmlns="http://www.w3.org/2000/svg",
                                ),
                                class_name="css-fjkyuu",
                            ),
                            class_name="css-gg4vpm",
                        )
                    ),
                    class_name="chakra-stat css-qp8lnl",
                ),
                rx.box(
                    rx.el.dl(
                        rx.box(
                            rx.box(
                                rx.el.dt(
                                    "Retorno anual m\u00e9dio",
                                    class_name="chakra-stat__label css-1or5rq5",
                                ),
                                rx.el.dd(class_name="chakra-stat__number css-2u1up0"),
                                class_name="css-1sgy36a",
                            ),
                            rx.box(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        d="M327.027 65.816L229.79 128.23l9.856 5.397 86.51-55.53 146.735 83.116-84.165 54.023 4.1 2.244v6.848l65.923-42.316 13.836 7.838-79.76 51.195v11.723l64.633-41.487 15.127 8.57-79.76 51.195v11.723l64.633-41.487 15.127 8.57-79.76 51.195v11.723l100.033-64.21-24.828-14.062 24.827-15.937-24.828-14.064 24.827-15.937-23.537-13.333 23.842-15.305-166.135-94.106zm31.067 44.74c-21.038 10.556-49.06 12.342-68.79 4.383l-38.57 24.757 126.903 69.47 36.582-23.48c-14.41-11.376-13.21-28.35 2.942-41.67l-59.068-33.46zM227.504 147.5l-70.688 46.094 135.61 78.066 1.33-.85c2.5-1.61 6.03-3.89 10.242-6.613 8.42-5.443 19.563-12.66 30.674-19.86 16.002-10.37 24.248-15.72 31.916-20.694L227.504 147.5zm115.467 1.17a8.583 14.437 82.068 0 1 .003 0 8.583 14.437 82.068 0 1 8.32 1.945 8.583 14.437 82.068 0 1-.87 12.282 8.583 14.437 82.068 0 1-20.273 1.29 8.583 14.437 82.068 0 1 .87-12.28 8.583 14.437 82.068 0 1 11.95-3.237zm-218.423 47.115L19.143 263.44l23.537 13.333-23.842 15.305 24.828 14.063-24.828 15.938 24.828 14.063-24.828 15.938 166.135 94.106L285.277 381.8V370.08l-99.433 63.824L39.11 350.787l14.255-9.15 131.608 74.547L285.277 351.8V340.08l-99.433 63.824L39.11 320.787l14.255-9.15 131.608 74.547L285.277 321.8V310.08l-99.433 63.824L39.11 290.787l13.27-8.52 132.9 75.28 99.997-64.188v-5.05l-5.48-3.154-93.65 60.11-146.73-83.116 94.76-60.824-9.63-5.543zm20.46 11.78l-46.92 30.115c14.41 11.374 13.21 28.348-2.942 41.67l59.068 33.46c21.037-10.557 49.057-12.342 68.787-4.384l45.965-29.504-123.96-71.358zm229.817 32.19c-8.044 5.217-15.138 9.822-30.363 19.688-11.112 7.203-22.258 14.42-30.69 19.873-4.217 2.725-7.755 5.01-10.278 6.632-.09.06-.127.08-.215.137v85.924l71.547-48.088v-84.166zm-200.99 17.48a8.583 14.437 82.068 0 1 8.32 1.947 8.583 14.437 82.068 0 1-.87 12.28 8.583 14.437 82.068 0 1-20.27 1.29 8.583 14.437 82.068 0 1 .87-12.28 8.583 14.437 82.068 0 1 11.95-3.236z"
                                    ),
                                    stroke="currentColor",
                                    fill="currentColor",
                                    stroke_width="0",
                                    viewbox="0 0 512 512",
                                    height="3em",
                                    width="3em",
                                    xmlns="http://www.w3.org/2000/svg",
                                ),
                                class_name="css-fjkyuu",
                            ),
                            class_name="css-gg4vpm",
                        )
                    ),
                    class_name="chakra-stat css-qp8lnl",
                ),
                rx.box(
                    rx.el.dl(
                        rx.box(
                            rx.box(
                                rx.el.dt(
                                    "N\u00famero de ativos",
                                    class_name="chakra-stat__label css-1or5rq5",
                                ),
                                rx.el.dd(class_name="chakra-stat__number css-2u1up0"),
                                class_name="css-1sgy36a",
                            ),
                            rx.box(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        d="M904 747H120c-4.4 0-8 3.6-8 8v56c0 4.4 3.6 8 8 8h784c4.4 0 8-3.6 8-8v-56c0-4.4-3.6-8-8-8zM165.7 621.8l39.7 39.5c3.1 3.1 8.2 3.1 11.3 0l234.7-233.9 97.6 97.3a32.11 32.11 0 0 0 45.2 0l264.2-263.2c3.1-3.1 3.1-8.2 0-11.3l-39.7-39.6a8.03 8.03 0 0 0-11.3 0l-235.7 235-97.7-97.3a32.11 32.11 0 0 0-45.2 0L165.7 610.5a7.94 7.94 0 0 0 0 11.3z"
                                    ),
                                    stroke="currentColor",
                                    fill="currentColor",
                                    stroke_width="0",
                                    viewbox="0 0 1024 1024",
                                    height="3em",
                                    width="3em",
                                    xmlns="http://www.w3.org/2000/svg",
                                ),
                                class_name="css-fjkyuu",
                            ),
                            class_name="css-gg4vpm",
                        )
                    ),
                    class_name="chakra-stat css-qp8lnl",
                ),
                class_name="css-1mzkwiw",
            ),
            class_name="css-h5yg1p",
        ),
        rx.box(
            rx.heading(
                "Researches",
                class_name="chakra-heading css-1dklj6k",
                as_="h2",
                size="6",
            ),
            rx.divider(
                aria_orientation="horizontal",
                class_name="chakra-divider css-14mxqfx",
            ),
            rx.box(
                rx.list(
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://media.seudinheiro.com/uploads/2021/11/avalanche-avax-criptomoeda-logotipo.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1elHJm_2-mVJG-Kll-drSWQPqbuYEthND/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Avalanche",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "A Avalanche \u00e9 uma plataforma p\u00fablica e open-source que conta com uma blockchain layer 1 que suporta tanto smart contracts como redes personaliz\u00e1veis.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://www.infomoney.com.br/wp-content/uploads/2021/08/Solana-1024x683-1.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1a6PEjAoEJylOxrx_TA6mwLMgsQtcKZqf/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Solana",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "A criptomoeda Solana (Sol) foi lan\u00e7ada em mar\u00e7o de 2020, com o objetivo de rivalizar com a Ethereum, focando em capacidade de escalabilidade e com o objetivo de oferecer solu\u00e7\u00f5es financeiras de forma descentralizada",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://thebuzzly.com/wp-content/uploads/2021/10/CryptoMode-Polygon-DeFi.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1HLnSFJ03SrjskQYaBIFhF-9ZY-oADU6e/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Polygon",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Criada em 2017, a MATIC \u00e9 a moeda base do ecossistema Polygon, originalmente chamada de Rede Matic",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://mma.prnewswire.com/media/1712696/Polkadot_Logo.jpg?p=facebook",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1po8eeRmD1FlXz9PN1W7vF9M1Ckpn-uhO/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Polkadot",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Criada em 2016 por Gavin Wood, co-fundador do Ethereum, a Polkadot \u00e9 uma plataforma que surgiu com o objetivo principal de ser uma rede que conecta diferentes blockchains",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://www.criptofacil.com/wp-content/uploads/2022/03/metaverse-fashion-week-em-decentraland-comeca-hoje-com-token-mana-em-alta.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1PJY7SxIGAs4V8hOO6ks8vwT4mr15wLna/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Decentraland",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Decentraland \u00e9 um software executado na rede Ethereum; projetado para incentivar uma rede global de usu\u00e1rios a operar um mundo virtual compartilhado",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://uniswap.org/images/twitter-card.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://docs.google.com/document/d/1p35Q9VP11IpgYawmLnRtp6XxlMM68u4q/edit?usp=sharing&ouid=116176718830297613713&rtpof=true&sd=true",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2022", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Uniswap",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Criado por Hayden Adams com alguns conselhos de Vitalik Buterin, o protocolo da Uniswap presente na blockchain da Ethereum possui duas fun\u00e7\u00f5es: ela funciona como uma criptomoeda, o UNI, e tamb\u00e9m como uma DEX (Decentralized Exchange) que permite trocas entre tokens do tipo ERC-20",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://media.moneytimes.com.br/uploads/2020/05/cardano-ada-blockchain.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1bp_9Iik_oa23-CZMuMbjjAWWiBxlwhkj/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Cardano",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Cardano \u00e9 uma plataforma de criptomoedas e contratos inteligentes lan\u00e7ada em setembro de 2017, que se autodenomina como a \u201cterceira gera\u00e7\u00e3o\u201d das criptomoedas...",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://suporte.mercadobitcoin.com.br/hc/article_attachments/360079203632/chainlink-combo-logo.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/180Jjlbytnzzf6CuFurfjVZE8o7dvq-5C/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Chainlink",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Chainlink \u00e9 uma rede descentralizada com o objetivo de conectar informa\u00e7\u00f5es de fora da rede com a blockchain interna, a partir de um sistema oracles...",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://livecoins.com.br/wp-content/uploads/2018/03/monero-logo.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1e3VWdperg6dzuhWvsTBBNQjl6WJhnLSj/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Monero",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Monero \u00e9 um Fork da Bytecoin, a primeira criptomoeda privada, devido a algumas cr\u00edticas feitas \u00e0 moeda original, como a de que em seu in\u00edcio 80% de todas suas moedas j\u00e1 haviam sido mineradas. 7 desenvolvedores forkaram para monero (moeda em esperanto).",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://0xzx.com/wp-content/uploads/2020/07/zcash-transaction.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1cFeVojTXAN10x64SInuLzBRBwmBDh7dh/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "ZCash",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Zcash (ZEC) \u00e9 uma criptomoeda descentralizada criada em 2016 pelo programador norte-americano Zooko Wilcox, e mantida pela institui\u00e7\u00e3o sem fins lucrativos chamada Funda\u00e7\u00e3o Zcash.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://moneyinvest.com.br/wp-content/uploads/2021/05/litcoin.jpeg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1lZ78r0MY6osoh6Mevr1BqGG6PL56wMBA/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Litecoin",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "O Litecoin foi criado por um ex-engenheiro da Google Charlie Lee, com o objetivo de aumentar a velocidade de transa\u00e7\u00e3o e escalabilidade da moeda",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://p7z2w8n8.rocketcdn.me/wp-content/uploads/2021/05/neo-o-que-e-como-funciona-vantagens-riscos-e-como-comprar.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1PDIhivRzXI4Kb-QtDoQ9Hd14CZhP8mTN/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a("NEO", class_name="chakra-link css-10qsrqw"),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "O projeto da NEO come\u00e7ou em fevereiro de 2014, quando o blockchain Antshares, foi criado sendo o primeiro desenvolvido na China.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://media.moneytimes.com.br/uploads/2020/11/tezos.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1gjvQy92JAsCwSYP8Tgpz28wo07h2mc-E/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Tezos",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Tezos \u00e9 uma criptomoeda baseada em blockchain. Tamb\u00e9m tem sua pr\u00f3pria plataforma de contratos inteligentes (smart contracts) que permite a cria\u00e7\u00e3o de aplicativos descentralizados (dApps), sendo uma de suas propostas, ser uma plataforma de Security Token Offering (STO). Desse modo, o XTZ \u00e9 um utility token que permite o acesso a rede blockchain da Tezos.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://s2.glbimg.com/Yu_YuutgYfolZ-h9rW52gH45iuU=/696x390/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2021/L/F/tLAOX9QCm7171sqJZFCA/075-porzycki-dogecoin210622-npbea-b.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1KtwSyO8rE-vqVOJVfqKC3o3Y1MIGNbEL/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Dogecoin",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "O Dogecoin (DOGE) \u00e9 uma criptomoeda sem fins lucrativos fundada em dezembro de 2013 pelo australiano Jackson Palmer. O inusitado desta moeda \u00e9 o fato de seu logotipo ser inspirado do meme \u201cDoge\u201d, a foto de um cachorro da ra\u00e7a Shiba Inu que viralizou na \u00e9poca.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://mms.businesswire.com/media/20190611005917/pt/726896/23/Ripple_Logo.jpg",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1aYR1DcfPprgULF_1U1XScJMrR0NUATL2/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Ripple",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Fundado em 2012 por Chris Larsen e Jed McCaleb, o Ripple \u00e9 tanto uma criptomoeda (XRP), como um protocolo de pagamento distribu\u00eddo (RippleNet) que busca permitir que institui\u00e7\u00f5es financeiras mandem dinheiro de forma segura, instant\u00e2nea e super barata para qualquer lugar.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://public.bnbstatic.com/image/cms/blog/20210412/3f999b0c-de99-495d-b9bc-634eb7ef4c47.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/161w-K0lMqIqkxjG7SyFOu3Cf9gatY8Fw/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Binance Coin",
                                    class_name="chakra-link css-10qsrqw",
                                ),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "A Binance Coin (BNB) \u00e9 uma altcoin criada por uma das maiores exchanges de criptoativos, a Binance.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="http://media.dash.org/wp-content/uploads/dash-digital-cash.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1jJEvr_WnAMzcFYbtE0j5DMwMBCuoYY7f/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a("Dash", class_name="chakra-link css-10qsrqw"),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "A Dash foi criada em 2014, com o intuito de solucionar alguns problemas do bitcoin, como a velocidade e privacidade das transa\u00e7\u00f5es.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    rx.el.li(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some text",
                                        src="https://img.ibxk.com.br/2017/12/12/iota-12163208489279.png",
                                        class_name="chakra-image css-mib21k",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1IsJOcko-whb6qddaU3k4r4XDJjdb7bPS/view?usp=sharing",
                                ),
                                class_name="css-1vqsgbx",
                            ),
                            rx.box(
                                rx.text.span("Research", class_name="css-1s4b4jw"),
                                rx.text.span("2019", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-qn174q",
                            ),
                            rx.heading(
                                rx.el.a("IOTA", class_name="chakra-link css-10qsrqw"),
                                class_name="chakra-heading css-3frrbh",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "IOTA \u00e9 uma das criptomoedas da chamada \u201cterceira gera\u00e7\u00e3o de blockchains\u201d, que mesmo n\u00e3o utilizando-se de uma blockchain em si, visa resolver os problemas de escalabilidade e rapidez de uma rede blockchain convencional, para assim dar ch\u00e3o para as novas tecnologias e novas demandas advindas da chamada \u201cInternet Of Things\u201d.",
                                class_name="chakra-text css-119hn4q",
                            ),
                            class_name="css-8atqhb",
                        ),
                        class_name="chakra-wrap__listitem css-drcqdj",
                    ),
                    class_name="chakra-wrap__list css-ncyfy7",
                ),
                class_name="chakra-wrap css-17qnj1m",
            ),
            class_name="chakra-container css-1oamxn5",
        ),
    )
