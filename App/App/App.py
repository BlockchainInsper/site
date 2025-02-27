"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from components.Navbar import navbar
from components.Footer import footer
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials
from components.home.With_Background_Image import with_background_image
from components.processo_seletivo.Intro import intro
from components.processo_seletivo.Summary import summary
from pages.Areas import areas
from components.fundo.intro import intro_fundo
from components.fundo.fundo_info import info_fundo
from components.parcerias.intro import intro_partnerships
from components.parcerias.Card import render_cards


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
                with_background_image(),
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
                intro(),
                summary(),
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


def alumni():
    pass


def nucleos():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                areas(),
                footer(),
                id="root",
            )
        )
    )


def projetos():
    pass


def fundo():
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                intro_fundo(),
                info_fundo(),
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
                intro_partnerships(),
                render_cards(),
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
app.add_page(parceiros, route="/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contato, route="/contact")
