"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from components.Navbar import navbar
from components.Footer import footer
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials


class State(rx.State):
    """The app state."""

    ...


def index():
    # Welcome Page (Index)
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                call_to_action_with_video(),
                features(),
                testimonials(),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.text(
                                "Conhe\u00e7a nossas \u00e1reas! Estamos estruturados em \u00e1reas de estudo e \u00e1reas administrativas",
                                class_name="chakra-text css-y5rwul",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.el.button(
                                        "Nossas \u00e1reas",
                                        type="button",
                                        class_name="chakra-button css-1onh796",
                                    ),
                                    class_name="chakra-link css-f4h6uy",
                                    href="#/areas",
                                ),
                                class_name="chakra-stack css-x9juev",
                            ),
                            class_name="chakra-stack css-7nla9k",
                        ),
                        class_name="chakra-stack css-13v4fef",
                    ),
                    class_name="css-1utqpha",
                ),
                footer(),
                id="root",
            )
        )
    )


def processo_seletivo():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.heading(
                                    "Nosso Processo Seletivo chegou!",
                                    class_name="css-kttl9l",
                                    as_="h2",
                                    size="6",
                                ),
                                rx.el.a(
                                    rx.el.button(
                                        "Inscrever-se",
                                        type="button",
                                        class_name="chakra-button css-b85hn3",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-f4h6uy",
                                    href="https://docs.google.com/forms/d/e/1FAIpQLScQyW4RGcwtcNAAVtYj3iFJdgJ4Khq07rSluQo5tWROKWYxow/viewform",
                                ),
                                rx.el.a(
                                    rx.el.button(
                                        rx.text.span(
                                            rx.el.svg(
                                                rx.el.svg.path(
                                                    d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4447.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785-.037 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0943.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0105c3.9278 1.7933 8.18 1.7933 12.0614 0a.0739.0739 0 01.0785.0095c.1202.099.246.1981.3728.2924a.077.077 0 01-.0066.1276 12.2986 12.2986 0 01-1.873.8914.0766.0766 0 00-.0407.1067c.3604.698.7719 1.3628 1.225 1.9932a.076.076 0 00.0842.0286c1.961-.6067 3.9495-1.5219 6.0023-3.0294a.077.077 0 00.0313-.0552c.5004-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0 00-.0312-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 2.1569-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.946 2.4189-2.1568 2.4189Z"
                                                ),
                                                stroke="currentColor",
                                                fill="currentColor",
                                                stroke_width="0",
                                                role="img",
                                                viewbox="0 0 24 24",
                                                aria_hidden="true",
                                                focusable="false",
                                                height="1em",
                                                width="1em",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            class_name="chakra-button__icon css-1wh2kri",
                                        ),
                                        "Discord",
                                        type="button",
                                        class_name="chakra-button css-a6md8f",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-f4h6uy",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                class_name="chakra-stack css-1lpczhs",
                            ),
                            class_name="css-zd4of5",
                        ),
                        rx.box(
                            rx.box(
                                rx.text(
                                    "O maior experimento financeiro e sociol\u00f3gico do s\u00e9culo XXI, o Bitcoin veio solucionar diversos problemas antes sem solu\u00e7\u00e3o. A Blockchain Insper vai te dar base para entender o que est\u00e1 por tr\u00e1s da constru\u00e7\u00e3o do protocolo e o que motivou Satoshi Nakamoto a desenvolv\u00ea-lo, entre muitas outras coisas que rondam essa tecnologia que est\u00e1 revolucionando a economia mundial. Al\u00e9m disso, temos parcerias com as maiores empresas do mercado para, al\u00e9m de ganhar conhecimento, saber como funcionam os projetos na pr\u00e1tica.",
                                    class_name="css-0",
                                ),
                                class_name="css-k008qs",
                            ),
                            class_name="css-0",
                        ),
                        class_name="css-1xb0s7",
                    ),
                    rx.divider(
                        aria_orientation="horizontal",
                        class_name="chakra-divider css-gir5mk",
                    ),
                    rx.box(
                        rx.box(
                            rx.heading(
                                "Primeira Fase",
                                class_name="css-vv36la",
                                as_="h3",
                                size="4",
                            ),
                            rx.text(
                                "Preenchimento de um Forms com detalhes pessoais e perguntas de car\u00e1ter opinativo.",
                                class_name="css-0",
                            ),
                            class_name="css-0",
                        ),
                        rx.box(
                            rx.heading(
                                "Segunda Fase",
                                class_name="css-vv36la",
                                as_="h3",
                                size="4",
                            ),
                            rx.text(
                                "Resolu\u00e7\u00e3o de um case elaborado em parceria com o BTG e com a Mynt.",
                                class_name="css-0",
                            ),
                            class_name="css-0",
                        ),
                        rx.box(
                            rx.heading(
                                "Terceira Fase",
                                class_name="css-vv36la",
                                as_="h3",
                                size="4",
                            ),
                            rx.text(
                                "Entrevista individual para conhecer melhor o candidato com perguntas pessoais e possivelmente t\u00e9cnicas.",
                                class_name="css-0",
                            ),
                            class_name="css-0",
                        ),
                        rx.box(
                            rx.heading(
                                "Programa de Trainees",
                                class_name="css-vv36la",
                                as_="h3",
                                size="4",
                            ),
                            rx.text(
                                "Desempenho no Curso de Introdu\u00e7\u00e3o \u00e0 Blockchain e Projeto Interno Aplicado (nessa fase, os candidatos j\u00e1 ganham entre 5 e 10 horas complementares).",
                                class_name="css-0",
                            ),
                            class_name="css-0",
                        ),
                        class_name="css-1gmb2s4",
                    ),
                    rx.divider(
                        aria_orientation="horizontal",
                        class_name="chakra-divider css-gir5mk",
                    ),
                    class_name="chakra-container css-1x6bs2p",
                ),
                rx.box(
                    rx.box(
                        rx.el.a(
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zm-141.651-35.33c4.937-32.999-20.191-50.739-54.55-62.573l11.146-44.702-27.213-6.781-10.851 43.524c-7.154-1.783-14.502-3.464-21.803-5.13l10.929-43.81-27.198-6.781-11.153 44.686c-5.922-1.349-11.735-2.682-17.377-4.084l.031-.14-37.53-9.37-7.239 29.062s20.191 4.627 19.765 4.913c11.022 2.751 13.014 10.044 12.68 15.825l-12.696 50.925c.76.194 1.744.473 2.829.907-.907-.225-1.876-.473-2.876-.713l-17.796 71.338c-1.349 3.348-4.767 8.37-12.471 6.464.271.395-19.78-4.937-19.78-4.937l-13.51 31.147 35.414 8.827c6.588 1.651 13.045 3.379 19.4 5.006l-11.262 45.213 27.182 6.781 11.153-44.733a1038.209 1038.209 0 0 0 21.687 5.627l-11.115 44.523 27.213 6.781 11.262-45.128c46.404 8.781 81.299 5.239 95.986-36.727 11.836-33.79-.589-53.281-25.004-65.991 17.78-4.098 31.174-15.792 34.747-39.949zm-62.177 87.179c-8.41 33.79-65.308 15.523-83.755 10.943l14.944-59.899c18.446 4.603 77.6 13.717 68.811 48.956zm8.417-87.667c-7.673 30.736-55.031 15.12-70.393 11.292l13.548-54.327c15.363 3.828 64.836 10.973 56.845 43.035z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 512 512",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1x6efgi",
                                ),
                                rx.box(
                                    rx.text(
                                        "N\u00facleos",
                                        class_name="chakra-text css-1jnffv6",
                                    ),
                                    rx.box(
                                        "Clique aqui para conhecer nossas \u00e1reas de estudos",
                                        class_name="css-9826r4",
                                    ),
                                    class_name="chakra-stack css-46p1lt",
                                ),
                                class_name="chakra-stack css-v3nyow",
                            ),
                            class_name="chakra-link css-f4h6uy",
                            href="#/areas",
                        ),
                        rx.el.a(
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                                        rx.el.svg.path(
                                            d="M17 11V3H7v4H3v14h8v-4h2v4h8V11h-4zM7 19H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V9h2v2zm4 4H9v-2h2v2zm0-4H9V9h2v2zm0-4H9V5h2v2zm4 8h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2zm4 12h-2v-2h2v2zm0-4h-2v-2h2v2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 24 24",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1x6efgi",
                                ),
                                rx.box(
                                    rx.text(
                                        "Parceiros",
                                        class_name="chakra-text css-1jnffv6",
                                    ),
                                    rx.box(
                                        "Clique aqui para conhecer nossos parceiros",
                                        class_name="css-9826r4",
                                    ),
                                    class_name="chakra-stack css-46p1lt",
                                ),
                                class_name="chakra-stack css-v3nyow",
                            ),
                            class_name="chakra-link css-f4h6uy",
                            href="#/partnerships",
                        ),
                        rx.el.a(
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.defs(),
                                        rx.el.svg.path(
                                            d="M312.1 591.5c3.1 3.1 8.2 3.1 11.3 0l101.8-101.8 86.1 86.2c3.1 3.1 8.2 3.1 11.3 0l226.3-226.5c3.1-3.1 3.1-8.2 0-11.3l-36.8-36.8c-3.1-3.1-8.2-3.1-11.3 0L517 485.3l-86.1-86.2c-3.1-3.1-8.2-3.1-11.3 0L275.3 543.4c-3.1 3.1-3.1 8.2 0 11.3l36.8 36.8z"
                                        ),
                                        rx.el.svg.path(
                                            d="M904 160H548V96c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H120c-17.7 0-32 14.3-32 32v520c0 17.7 14.3 32 32 32h356.4v32L311.6 884.1c-3.7 2.4-4.7 7.3-2.3 11l30.3 47.2v0.1c2.4 3.7 7.4 4.7 11.1 2.3L512 838.9l161.3 105.8c3.7 2.4 8.7 1.4 11.1-2.3v-0.1l30.3-47.2c2.4-3.7 1.3-8.6-2.3-11L548 776.3V744h356c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32z m-40 512H160V232h704v440z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        t="1569683753031",
                                        viewbox="0 0 1024 1024",
                                        version="1.1",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1x6efgi",
                                ),
                                rx.box(
                                    rx.text(
                                        "Projetos", class_name="chakra-text css-1jnffv6"
                                    ),
                                    rx.box(
                                        "Clique aqui para conhecer nossos alguns dos nossos melhores projetos",
                                        class_name="css-9826r4",
                                    ),
                                    class_name="chakra-stack css-46p1lt",
                                ),
                                class_name="chakra-stack css-v3nyow",
                            ),
                            class_name="chakra-link css-f4h6uy",
                            href="#/projects",
                        ),
                        class_name="css-sj7xet",
                    ),
                    class_name="css-1u3waxk",
                ),
                footer(),
                id="root",
            )
        )
    )


def time():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Conhe\u00e7a nosso time ",
                            rx.text.span(
                                "2022.1", class_name="chakra-text css-1jkapds"
                            ),
                            class_name="chakra-heading css-124aq96",
                            as_="h2",
                            size="6",
                        ),
                        class_name="chakra-stack css-1tcwzuj",
                    ),
                    class_name="chakra-container css-1a3ltpp",
                ),
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
                footer(),
                id="root",
            )
        )
    )


def nucleos():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.el.svg(
                        rx.el.a(
                            rx.el.svg.path(
                                d="M11,44H9c-0.6,0-1-0.4-1-1v-2h4v2C12,43.6,11.6,44,11,44z"
                            ),
                            rx.el.svg.path(
                                d="M39,44h-2c-0.6,0-1-0.4-1-1v-2h4v2C40,43.6,39.6,44,39,44z"
                            ),
                            fill="#263238",
                        ),
                        rx.el.svg.path(
                            fill="#37474F",
                            d="M27,7h-6c-1.7,0-3,1.3-3,3v3h2v-3c0-0.6,0.4-1,1-1h6c0.6,0,1,0.4,1,1v3h2v-3C30,8.3,28.7,7,27,7z",
                        ),
                        rx.el.svg.path(
                            fill="#78909C",
                            d="M40,43H8c-2.2,0-4-1.8-4-4V15c0-2.2,1.8-4,4-4h32c2.2,0,4,1.8,4,4v24C44,41.2,42.2,43,40,43z",
                        ),
                        stroke="currentColor",
                        fill="currentColor",
                        stroke_width="0",
                        version="1",
                        viewbox="0 0 48 48",
                        enable_background="new 0 0 48 48",
                        focusable="false",
                        class_name="chakra-icon css-10xmb8f",
                        height="1em",
                        width="1em",
                        xmlns="http://www.w3.org/2000/svg",
                    ),
                    rx.heading(
                        "Business",
                        class_name="chakra-heading css-1wib1wc",
                        as_="h2",
                        size="6",
                    ),
                    rx.text(
                        "Estudo das aplica\u00e7\u00f5es da tecnologia blockchain, atua\u00e7\u00f5es nas diversas \u00e1reas e empresas e elabora\u00e7\u00e3o de poss\u00edveis real cases.",
                        class_name="chakra-text css-q9k0mw",
                    ),
                    class_name="css-74le4x",
                ),
                rx.box(
                    rx.el.svg(
                        rx.el.a(
                            rx.el.svg.rect(x="38", y="4", width="2", height="20"),
                            rx.el.svg.rect(x="15", y="7", width="2", height="17"),
                            rx.el.svg.rect(x="8", y="27", width="2", height="17"),
                            rx.el.svg.rect(x="28", y="19", width="2", height="22"),
                            fill="#546E7A",
                        ),
                        rx.el.svg.path(
                            fill="#4CAF50",
                            d="M36,7h6c1.1,0,2,0.9,2,2v10c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2V9C34,7.9,34.9,7,36,7z",
                        ),
                        rx.el.svg.path(
                            fill="#4CAF50",
                            d="M13,10h6c1.1,0,2,0.9,2,2v7c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2v-7C11,10.9,11.9,10,13,10z",
                        ),
                        rx.el.svg.path(
                            fill="#F44336",
                            d="M6,30h6c1.1,0,2,0.9,2,2v7c0,1.1-0.9,2-2,2H6c-1.1,0-2-0.9-2-2v-7C4,30.9,4.9,30,6,30z",
                        ),
                        rx.el.svg.path(
                            fill="#F44336",
                            d="M26,22h6c1.1,0,2,0.9,2,2v12c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2V24C24,22.9,24.9,22,26,22z",
                        ),
                        stroke="currentColor",
                        fill="currentColor",
                        stroke_width="0",
                        version="1",
                        viewbox="0 0 48 48",
                        enable_background="new 0 0 48 48",
                        focusable="false",
                        class_name="chakra-icon css-10xmb8f",
                        height="1em",
                        width="1em",
                        xmlns="http://www.w3.org/2000/svg",
                    ),
                    rx.heading(
                        "Finance",
                        class_name="chakra-heading css-1wib1wc",
                        as_="h2",
                        size="6",
                    ),
                    rx.text(
                        "Estudo do mercado de criptoativos, tecnologia blockchain no mercado financeiro e poss\u00edveis estrat\u00e9gias elaboradas.",
                        class_name="chakra-text css-q9k0mw",
                    ),
                    class_name="css-74le4x",
                ),
                rx.box(
                    rx.el.svg(
                        rx.el.a(
                            rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                            rx.el.svg.path(
                                d="M13 18v2h4v2H7v-2h4v-2H2.992A.998.998 0 0 1 2 16.993V4.007C2 3.451 2.455 3 2.992 3h18.016c.548 0 .992.449.992 1.007v12.986c0 .556-.455 1.007-.992 1.007H13z"
                            ),
                        ),
                        stroke="currentColor",
                        fill="currentColor",
                        stroke_width="0",
                        viewbox="0 0 24 24",
                        focusable="false",
                        class_name="chakra-icon css-10xmb8f",
                        height="1em",
                        width="1em",
                        xmlns="http://www.w3.org/2000/svg",
                    ),
                    rx.heading(
                        "Tech",
                        class_name="chakra-heading css-1wib1wc",
                        as_="h2",
                        size="6",
                    ),
                    rx.text(
                        "Estudo da tecnologia blockchain na parte t\u00e9cnica, smart-contracts, dApps, softwares e criptografia.",
                        class_name="chakra-text css-q9k0mw",
                    ),
                    class_name="css-74le4x",
                ),
                footer(),
                id="root",
            )
        )
    )


def fundo():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Fundo Blockchain Insper",
                            class_name="chakra-heading css-1f48gq8",
                            as_="h2",
                            size="6",
                        ),
                        rx.text(
                            "Nossa tese de investimento consiste em analisar os whitepapers de diversas criptomoedas, a partir disso avaliando sua aplicabilidade, escalabilidade e potencial de crescimento futuro. Dessa forma, realizamos a aloca\u00e7\u00e3o de ativos do nosso fundo simulado.",
                            class_name="chakra-text css-qx8l5f",
                        ),
                        class_name="css-1frzi1b",
                    ),
                    class_name="css-0",
                ),
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
                    rx.heading(
                        "Indicadores", class_name="css-1b10ebd", as_="h1", size="8"
                    ),
                    rx.box(
                        rx.box(
                            rx.el.dl(
                                rx.box(
                                    rx.box(
                                        rx.el.dt(
                                            "Retorno acumulado",
                                            class_name="chakra-stat__label css-1or5rq5",
                                        ),
                                        rx.el.dd(
                                            class_name="chakra-stat__number css-2u1up0"
                                        ),
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
                                        rx.el.dd(
                                            class_name="chakra-stat__number css-2u1up0"
                                        ),
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
                                        rx.el.dd(
                                            class_name="chakra-stat__number css-2u1up0"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
                                        rx.text.span("2019", class_name="css-1s4b4jw"),
                                        class_name="chakra-stack css-qn174q",
                                    ),
                                    rx.heading(
                                        rx.el.a(
                                            "NEO", class_name="chakra-link css-10qsrqw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
                                        rx.text.span("2019", class_name="css-1s4b4jw"),
                                        class_name="chakra-stack css-qn174q",
                                    ),
                                    rx.heading(
                                        rx.el.a(
                                            "Dash", class_name="chakra-link css-10qsrqw"
                                        ),
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
                                        rx.text.span(
                                            "Research", class_name="css-1s4b4jw"
                                        ),
                                        rx.text.span("2019", class_name="css-1s4b4jw"),
                                        class_name="chakra-stack css-qn174q",
                                    ),
                                    rx.heading(
                                        rx.el.a(
                                            "IOTA", class_name="chakra-link css-10qsrqw"
                                        ),
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
                footer(),
                id="root",
            )
        )
    )


def parceiros():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Parceiros",
                            class_name="chakra-heading css-1f48gq8",
                            as_="h2",
                            size="6",
                        ),
                        rx.text(
                            "Aqui voc\u00ea encontrar\u00e1 todos os parceiros da Blockchain Insper",
                            class_name="chakra-text css-qx8l5f",
                        ),
                        class_name="css-9sg3e1",
                    ),
                    class_name="css-0",
                ),
                rx.box(
                    rx.list(
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/insper.f3f3d55a.png",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Insper",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.insper.edu.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/mercadobtc.015a99b6.jpg",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Mercado Bitcoin",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.mercadobitcoin.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/ambev.6a765a10.jfif",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Ambev",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.ambev.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/itau.4d5bdeb4.webp",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Ita\u00fa",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.itau.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/dotz.cfd1cd74.png",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Dotz",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.dotz.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/gcb.3f537b98.jfif",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "GCB Investimentos",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://gcbinvestimentos.com/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="data:image/png;base64,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",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Peer BR",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://peerbr.com/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/coins.072a326e.jfif",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Coins",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://coins.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/ulrich.39a00847.jpg",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Fernando Ulrich",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.linkedin.com/in/fernando-ulrich-aa805821/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/blockchainberkeley.0b66e30a.png",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Blockchain Berkeley",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://blockchain.berkeley.edu/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/beetech.b984b850.jpeg",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "BeeTech",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://beetech.global/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/blockmaster.4d8f4d23.jpg",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Block Master",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.blockmaster.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="data:image/png;base64,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",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "iCoLab",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://icolab.org.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="data:image/png;base64,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",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Mar Ventures",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://www.mar.ventures/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        rx.el.li(
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.image(
                                            src="/static/media/portaldobtc.9e6f584d.webp",
                                            class_name="chakra-image css-1gqsic3",
                                        ),
                                        class_name="css-ox58qu",
                                    ),
                                    rx.box(
                                        rx.heading(
                                            "Portal do Bitcoin",
                                            class_name="chakra-heading css-mr4omx",
                                            as_="h2",
                                            size="6",
                                        ),
                                        rx.el.a(
                                            rx.el.button(
                                                "Mais informa\u00e7\u00f5es",
                                                type="button",
                                                class_name="chakra-button css-asn4yg",
                                            ),
                                            target="_blank",
                                            rel="noopener noreferrer",
                                            class_name="chakra-link css-f4h6uy",
                                            href="https://portaldobitcoin.uol.com.br/",
                                        ),
                                        class_name="chakra-stack css-160hj0l",
                                    ),
                                    role="group",
                                    class_name="css-1re1swf",
                                ),
                                class_name="css-x5opt7",
                            ),
                            class_name="chakra-wrap__listitem css-1yp4ln",
                        ),
                        class_name="chakra-wrap__list css-krk3di",
                    ),
                    class_name="chakra-wrap css-1qn7hqg",
                ),
                footer(),
                id="root",
            )
        )
    )


def aprenda():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.heading(
                        "Pilares do Conhecimento",
                        class_name="css-1kiqah5",
                        as_="h1",
                        size="8",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.circle(
                                            fill="#FFF59D", cx="24", cy="22", r="20"
                                        ),
                                        rx.el.svg.path(
                                            fill="#FBC02D",
                                            d="M37,22c0-7.7-6.6-13.8-14.5-12.9c-6,0.7-10.8,5.5-11.4,11.5c-0.5,4.6,1.4,8.7,4.6,11.3 c1.4,1.2,2.3,2.9,2.3,4.8V37h12v-0.1c0-1.8,0.8-3.6,2.2-4.8C35.1,29.7,37,26.1,37,22z",
                                        ),
                                        rx.el.svg.path(
                                            fill="#FFF59D",
                                            d="M30.6,20.2l-3-2c-0.3-0.2-0.8-0.2-1.1,0L24,19.8l-2.4-1.6c-0.3-0.2-0.8-0.2-1.1,0l-3,2 c-0.2,0.2-0.4,0.4-0.4,0.7s0,0.6,0.2,0.8l3.8,4.7V37h2V26c0-0.2-0.1-0.4-0.2-0.6l-3.3-4.1l1.5-1l2.4,1.6c0.3,0.2,0.8,0.2,1.1,0 l2.4-1.6l1.5,1l-3.3,4.1C25.1,25.6,25,25.8,25,26v11h2V26.4l3.8-4.7c0.2-0.2,0.3-0.5,0.2-0.8S30.8,20.3,30.6,20.2z",
                                        ),
                                        rx.el.svg.circle(
                                            fill="#5C6BC0", cx="24", cy="44", r="3"
                                        ),
                                        rx.el.svg.path(
                                            fill="#9FA8DA",
                                            d="M26,45h-4c-2.2,0-4-1.8-4-4v-5h12v5C30,43.2,28.2,45,26,45z",
                                        ),
                                        rx.el.a(
                                            rx.el.svg.path(
                                                d="M30,41l-11.6,1.6c0.3,0.7,0.9,1.4,1.6,1.8l9.4-1.3C29.8,42.5,30,41.8,30,41z"
                                            ),
                                            rx.el.svg.polygon(
                                                points="18,38.7 18,40.7 30,39 30,37"
                                            ),
                                            fill="#5C6BC0",
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        version="1",
                                        viewbox="0 0 48 48",
                                        enable_background="new 0 0 48 48",
                                        focusable="false",
                                        class_name="chakra-icon css-n17ngm",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1motzux",
                                ),
                                rx.text(
                                    "Aprender a conhecer",
                                    class_name="chakra-text css-35ezg3",
                                ),
                                rx.text(
                                    "Esse aprendizado pretende que cada pessoa possa conhecer o mundo que a rodeia, conseguindo assim viver dignamente, desenvolver capacidades profissionais e se comunicar.",
                                    class_name="chakra-text css-q9k0mw",
                                ),
                                class_name="chakra-stack css-n21gh5",
                            ),
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="#1565C0",
                                            d="M25,22h13l6,6V11c0-2.2-1.8-4-4-4H25c-2.2,0-4,1.8-4,4v7C21,20.2,22.8,22,25,22z",
                                        ),
                                        rx.el.svg.path(
                                            fill="#2196F3",
                                            d="M23,19H10l-6,6V8c0-2.2,1.8-4,4-4h15c2.2,0,4,1.8,4,4v7C27,17.2,25.2,19,23,19z",
                                        ),
                                        rx.el.a(
                                            rx.el.svg.circle(cx="12", cy="31", r="5"),
                                            rx.el.svg.circle(cx="36", cy="31", r="5"),
                                            fill="#FFA726",
                                        ),
                                        rx.el.a(
                                            rx.el.svg.path(
                                                d="M20,42c0,0-2.2-4-8-4s-8,4-8,4v2h16V42z"
                                            ),
                                            rx.el.svg.path(
                                                d="M44,42c0,0-2.2-4-8-4s-8,4-8,4v2h16V42z"
                                            ),
                                            fill="#607D8B",
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        version="1",
                                        viewbox="0 0 48 48",
                                        enable_background="new 0 0 48 48",
                                        focusable="false",
                                        class_name="chakra-icon css-n17ngm",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1motzux",
                                ),
                                rx.text(
                                    "Aprender a fazer",
                                    class_name="chakra-text css-35ezg3",
                                ),
                                rx.text(
                                    "Ele se refere \u00e0 forma\u00e7\u00e3o do profissional. Fala sobre como conseguir usar os conhecimentos adquiridos na pr\u00e1tica, no mercado de trabalho, criando qualifica\u00e7\u00e3o profissional e experi\u00eancia.",
                                    class_name="chakra-text css-q9k0mw",
                                ),
                                class_name="chakra-stack css-n21gh5",
                            ),
                            rx.box(
                                rx.box(
                                    rx.el.svg(
                                        rx.el.svg.polygon(
                                            fill="#FF9800",
                                            points="24,37 19,31 19,25 29,25 29,31",
                                        ),
                                        rx.el.a(
                                            rx.el.svg.circle(cx="33", cy="19", r="2"),
                                            rx.el.svg.circle(cx="15", cy="19", r="2"),
                                            fill="#FFA726",
                                        ),
                                        rx.el.svg.path(
                                            fill="#FFB74D",
                                            d="M33,13c0-7.6-18-5-18,0c0,1.1,0,5.9,0,7c0,5,4,9,9,9s9-4,9-9C33,18.9,33,14.1,33,13z",
                                        ),
                                        rx.el.svg.path(
                                            fill="#424242",
                                            d="M24,4c-6.1,0-10,4.9-10,11c0,0.8,0,2.3,0,2.3l2,1.7v-5l12-4l4,4v5l2-1.7c0,0,0-1.5,0-2.3c0-4-1-8-6-9l-1-2 H24z",
                                        ),
                                        rx.el.a(
                                            rx.el.svg.circle(cx="28", cy="19", r="1"),
                                            rx.el.svg.circle(cx="20", cy="19", r="1"),
                                            fill="#784719",
                                        ),
                                        rx.el.svg.polygon(
                                            fill="#fff",
                                            points="24,43 19,31 24,32 29,31",
                                        ),
                                        rx.el.svg.polygon(
                                            fill="#D32F2F",
                                            points="23,35 22.3,39.5 24,43.5 25.7,39.5 25,35 26,34 24,32 22,34",
                                        ),
                                        rx.el.svg.path(
                                            fill="#546E7A",
                                            d="M29,31L29,31l-5,12l-5-12c0,0-11,2-11,13h32C40,33,29,31,29,31z",
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        version="1",
                                        viewbox="0 0 48 48",
                                        enable_background="new 0 0 48 48",
                                        focusable="false",
                                        class_name="chakra-icon css-n17ngm",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="css-1motzux",
                                ),
                                rx.text(
                                    "Aprender a ser",
                                    class_name="chakra-text css-35ezg3",
                                ),
                                rx.text(
                                    "Ele defende que o ser humano precisa se tornar apto a pensar de forma aut\u00f4noma e cr\u00edtica, sendo capaz de formular o pr\u00f3prio ju\u00edzo de valor e sabendo que atitudes tomar ante as circunst\u00e2ncias da vida.",
                                    class_name="chakra-text css-q9k0mw",
                                ),
                                class_name="chakra-stack css-n21gh5",
                            ),
                            class_name="css-p92pfp",
                        ),
                        class_name="css-h94677",
                    ),
                    class_name="css-11csr4g",
                ),
                rx.box(
                    rx.box(
                        rx.heading(
                            "Aprenda blockchain ",
                            rx.el.br(),
                            rx.text.span("agora", class_name="chakra-text css-10tibwi"),
                            class_name="chakra-heading css-1xb57ov",
                            as_="h2",
                            size="6",
                        ),
                        rx.text(
                            "A Blockchain Insper tem o prazer de apresentar o Curso de Introdu\u00e7\u00e3o \u00e0 Blockchain! Na linha de contribuir para o acesso \u00e0 informa\u00e7\u00e3o e o fomento do estudo das novas tecnologias, o curso \u00e9 realizado no formato online, e \u00e9 aberto para qualquer pessoa. Os conte\u00fados foram escolhidos pelos membros da entidade, abordando desde contexto hist\u00f3rico at\u00e9 futuras perspectivas da tecnologia.",
                            class_name="chakra-text css-q9k0mw",
                        ),
                        rx.box(
                            rx.el.a(
                                rx.el.button(
                                    "Vamos come\u00e7ar!",
                                    type="button",
                                    class_name="chakra-button css-1f8g3n5",
                                ),
                                class_name="chakra-link css-f4h6uy",
                                href="#/learn/curso-intro",
                            ),
                            class_name="chakra-stack css-grmpig",
                        ),
                        class_name="chakra-stack css-ab1nhi",
                    ),
                    class_name="chakra-container css-1a3l159",
                ),
                rx.box(
                    rx.heading(
                        "Aprenda na pr\u00e1tica",
                        class_name="chakra-heading css-1dklj6k",
                        as_="h1",
                        size="8",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some good alt text",
                                        src="/static/media/arteAgro.f232cae3.png",
                                        class_name="chakra-image css-1q7mro",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1zlmy-Juu6i6HVZw7WCYQs_rC4CEDZSFy/view",
                                ),
                                class_name="css-wo9i0v",
                            ),
                            rx.box(
                                rx.box(class_name="css-504s85"), class_name="css-bm0zes"
                            ),
                            class_name="css-1r21lrd",
                        ),
                        rx.box(
                            rx.box(
                                rx.text.span(
                                    "Agropecu\u00e1ria", class_name="css-1s4b4jw"
                                ),
                                rx.text.span("Report", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-g9cw6v",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Report do setor Agropecu\u00e1rio",
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1zlmy-Juu6i6HVZw7WCYQs_rC4CEDZSFy/view",
                                ),
                                class_name="chakra-heading css-15loomw",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "O setor agropecu\u00e1rio \u00e9 um dos principais setores econ\u00f4micos do Brasil, representando uma parcela de 21% do PIB nacional. Atualmente, ele encontra diversos problemas estruturais, os quais poderiam ser solucionados atrav\u00e9s da tecnologia blockchain. No report a seguir esses t\u00f3picos ser\u00e3o abordados e discutidos.",
                                class_name="chakra-text css-bjugk0",
                            ),
                            class_name="css-fu5aqi",
                        ),
                        class_name="css-1tvbi2x",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.text.span("Sa\u00fade", class_name="css-1s4b4jw"),
                                rx.text.span("Report", class_name="css-1s4b4jw"),
                                class_name="chakra-stack css-g9cw6v",
                            ),
                            rx.heading(
                                rx.el.a(
                                    "Report do setor da Sa\u00fade",
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1KzcVDm7Ipq4yGfkN1DBzlBwWOwS-DfYz/view",
                                ),
                                class_name="chakra-heading css-15loomw",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Sendo o assunto de maior import\u00e2ncia recentemente, o setor de sa\u00fade aparece como enfoque de 2020 pela situa\u00e7\u00e3o vivida com a pandemia do COVID-19. Nesse ano, foi poss\u00edvel notar a import\u00e2ncia e os benef\u00edcios de um sistema de sa\u00fade bem estruturado. No report a seguir esses t\u00f3picos ser\u00e3o abordados e discutidos.",
                                class_name="chakra-text css-bjugk0",
                            ),
                            class_name="css-fu5aqi",
                        ),
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.image(
                                        alt="some good alt text",
                                        src="/static/media/arteHealth.aabf715a.png",
                                        class_name="chakra-image css-1q7mro",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-10qsrqw",
                                    href="https://drive.google.com/file/d/1KzcVDm7Ipq4yGfkN1DBzlBwWOwS-DfYz/view",
                                ),
                                class_name="css-wo9i0v",
                            ),
                            rx.box(
                                rx.box(class_name="css-504s85"), class_name="css-bm0zes"
                            ),
                            class_name="css-1r21lrd",
                        ),
                        class_name="css-1tvbi2x",
                    ),
                    class_name="chakra-container css-1oamxn5",
                ),
                footer(),
                id="root",
            )
        )
    )


def contato():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.box(
                                    rx.list(
                                        rx.el.li(
                                            rx.box(
                                                rx.heading(
                                                    "Entre em Contato",
                                                    class_name="chakra-heading css-1dklj6k",
                                                    as_="h2",
                                                    size="6",
                                                ),
                                                rx.box(
                                                    rx.text(
                                                        "Caso queira fazer contato conosco, acesse o Linkedin de algum dos nossos diretores/presidente. Se isso n\u00e3o for poss\u00edvel, mande um email para n\u00f3s!",
                                                        class_name="chakra-text css-0",
                                                    ),
                                                    class_name="css-dkdl1p",
                                                ),
                                                rx.box(
                                                    rx.el.a(
                                                        rx.el.button(
                                                            rx.el.svg(
                                                                rx.el.svg.path(
                                                                    d="M6.552 6.712c-.456 0-.816.4-.816.888s.368.888.816.888c.456 0 .816-.4.816-.888.008-.488-.36-.888-.816-.888zm2.92 0c-.456 0-.816.4-.816.888s.368.888.816.888c.456 0 .816-.4.816-.888s-.36-.888-.816-.888z"
                                                                ),
                                                                rx.el.svg.path(
                                                                    d="M13.36 0H2.64C1.736 0 1 .736 1 1.648v10.816c0 .912.736 1.648 1.64 1.648h9.072l-.424-1.48 1.024.952.968.896L15 16V1.648C15 .736 14.264 0 13.36 0zm-3.088 10.448s-.288-.344-.528-.648c1.048-.296 1.448-.952 1.448-.952-.328.216-.64.368-.92.472-.4.168-.784.28-1.16.344a5.604 5.604 0 0 1-2.072-.008 6.716 6.716 0 0 1-1.176-.344 4.688 4.688 0 0 1-.584-.272c-.024-.016-.048-.024-.072-.04-.016-.008-.024-.016-.032-.024-.144-.08-.224-.136-.224-.136s.384.64 1.4.944c-.24.304-.536.664-.536.664-1.768-.056-2.44-1.216-2.44-1.216 0-2.576 1.152-4.664 1.152-4.664 1.152-.864 2.248-.84 2.248-.84l.08.096c-1.44.416-2.104 1.048-2.104 1.048s.176-.096.472-.232c.856-.376 1.536-.48 1.816-.504.048-.008.088-.016.136-.016a6.521 6.521 0 0 1 4.024.752s-.632-.6-1.992-1.016l.112-.128s1.096-.024 2.248.84c0 0 1.152 2.088 1.152 4.664 0 0-.68 1.16-2.448 1.216z"
                                                                ),
                                                                stroke="currentColor",
                                                                fill="currentColor",
                                                                stroke_width="0",
                                                                viewbox="0 0 16 16",
                                                                aria_hidden="true",
                                                                focusable="false",
                                                                height="28px",
                                                                width="28px",
                                                                xmlns="http://www.w3.org/2000/svg",
                                                            ),
                                                            type="button",
                                                            class_name="chakra-button css-18155x9",
                                                            aria_label="discord",
                                                        ),
                                                        target="_blank",
                                                        rel="noopener noreferrer",
                                                        class_name="chakra-link css-f4h6uy",
                                                        href="https://discord.gg/jdK5yB48Mm",
                                                    ),
                                                    rx.el.a(
                                                        rx.el.button(
                                                            rx.el.svg(
                                                                rx.el.svg.path(
                                                                    fill="none",
                                                                    d="M0 0h24v24H0V0z",
                                                                ),
                                                                rx.el.svg.path(
                                                                    d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zm-2 0l-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z"
                                                                ),
                                                                stroke="currentColor",
                                                                fill="currentColor",
                                                                stroke_width="0",
                                                                viewbox="0 0 24 24",
                                                                aria_hidden="true",
                                                                focusable="false",
                                                                height="28px",
                                                                width="28px",
                                                                xmlns="http://www.w3.org/2000/svg",
                                                            ),
                                                            type="button",
                                                            class_name="chakra-button css-18155x9",
                                                            aria_label="github",
                                                        ),
                                                        target="_blank",
                                                        rel="noopener noreferrer",
                                                        class_name="chakra-link css-f4h6uy",
                                                        href="mailto:blockchainsper@gmail.com",
                                                    ),
                                                    rx.el.a(
                                                        rx.el.button(
                                                            rx.el.svg(
                                                                rx.el.svg.path(
                                                                    d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"
                                                                ),
                                                                stroke="currentColor",
                                                                fill="currentColor",
                                                                stroke_width="0",
                                                                viewbox="0 0 16 16",
                                                                aria_hidden="true",
                                                                focusable="false",
                                                                height="28px",
                                                                width="28px",
                                                                xmlns="http://www.w3.org/2000/svg",
                                                            ),
                                                            type="button",
                                                            class_name="chakra-button css-18155x9",
                                                            aria_label="discord",
                                                        ),
                                                        target="_blank",
                                                        rel="noopener noreferrer",
                                                        class_name="chakra-link css-f4h6uy",
                                                        href="https://www.linkedin.com/company/blockchain-insper/",
                                                    ),
                                                    rx.el.a(
                                                        rx.el.button(
                                                            rx.el.svg(
                                                                rx.el.svg.path(
                                                                    d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"
                                                                ),
                                                                stroke="currentColor",
                                                                fill="currentColor",
                                                                stroke_width="0",
                                                                viewbox="0 0 16 16",
                                                                aria_hidden="true",
                                                                focusable="false",
                                                                height="28px",
                                                                width="28px",
                                                                xmlns="http://www.w3.org/2000/svg",
                                                            ),
                                                            type="button",
                                                            class_name="chakra-button css-18155x9",
                                                            aria_label="facebook",
                                                        ),
                                                        target="_blank",
                                                        rel="noopener noreferrer",
                                                        class_name="chakra-link css-f4h6uy",
                                                        href="https://www.instagram.com/blockchainsper/",
                                                    ),
                                                    class_name="chakra-stack css-14lxv93",
                                                ),
                                                class_name="css-0",
                                            ),
                                            class_name="chakra-wrap__listitem css-1yp4ln",
                                        ),
                                        class_name="chakra-wrap__list css-1fewj3v",
                                    ),
                                    class_name="chakra-wrap css-0",
                                ),
                                class_name="css-h94677",
                            ),
                            class_name="css-1oprkzw",
                        ),
                        class_name="css-k008qs",
                    ),
                    class_name="chakra-container css-1n1v2nz",
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.el.iframe(
                                title="Teste",
                                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1828.0847263800329!2d-46.67881990221802!3d-23.598254999967665!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce575374b7481f%3A0x50e5aad2656c43ed!2sInsper%20Learning%20Institution!5e0!3m2!1sen!2sbr!4v1586359937804!5m2!1sen!2sbr",
                                alt="demo",
                            ),
                            class_name="chakra-aspect-ratio css-1m7tg19",
                        ),
                        class_name="css-1hz88l4",
                    ),
                    rx.box(
                        rx.box(
                            rx.heading(
                                rx.text.span(
                                    "Venha conhecer a Blockchain Insper e o Insper!",
                                    class_name="chakra-text css-1wd7fno",
                                ),
                                rx.el.br(),
                                rx.text.span(class_name="chakra-text css-10tibwi"),
                                class_name="chakra-heading css-13cmyfy",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Aberto de Segunda \u00e0 Sexta das 07:00 \u00e0s 23:00",
                                class_name="chakra-text css-oztxm7",
                            ),
                            class_name="chakra-stack css-n21gh5",
                        ),
                        class_name="css-gmuwbf",
                    ),
                    class_name="css-x8vryw",
                ),
                footer(),
                id="root",
            )
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(processo_seletivo, route="/ps")
app.add_page(time, route="/members/actual")
app.add_page(nucleos, route="/areas")
app.add_page(fundo, route="/fund")
app.add_page(parceiros, route="/#/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contato, route="/contact")
