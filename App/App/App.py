"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
# from pages.Home import home


class State(rx.State):
    """The app state."""

    ...


def index():
    # Welcome Page (Index)
    return rx.fragment(
        rx.el.link(rel="icon", href="/favicon.png"),
        rx.el.link(rel="apple-touch-icon", href="/logo192.png"),
        rx.el.link(rel="manifest", href="/manifest.json"),
        rx.el.link(href="/static/css/main.a67c64bb.chunk.css", rel="stylesheet"),
        rx.el.style(custom_attrs={"data-emotion": "css-global", "data-s": ""}),
        rx.el.style(custom_attrs={"data-emotion": "css-global", "data-s": ""}),
        rx.el.style(custom_attrs={"data-emotion": "css-global", "data-s": ""}),
        rx.el.style(custom_attrs={"data-emotion": "css", "data-s": ""}),
        rx.box(
            rx.el.noscript("You need to enable JavaScript to run this app."),
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        fill="currentColor",
                                        d="M 3 5 A 1.0001 1.0001 0 1 0 3 7 L 21 7 A 1.0001 1.0001 0 1 0 21 5 L 3 5 z M 3 11 A 1.0001 1.0001 0 1 0 3 13 L 21 13 A 1.0001 1.0001 0 1 0 21 11 L 3 11 z M 3 17 A 1.0001 1.0001 0 1 0 3 19 L 21 19 A 1.0001 1.0001 0 1 0 21 17 L 3 17 z",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-bokek7",
                                    aria_hidden="true",
                                ),
                                type="button",
                                class_name="chakra-button css-f59olw",
                                aria_label="Toggle Navigation",
                            ),
                            class_name="css-1twb9xo",
                        ),
                        rx.box(
                            rx.el.a(
                                rx.image(
                                    src="/static/media/logo-dark.537e082d.svg",
                                    class_name="chakra-image css-v7v99c",
                                ),
                                class_name="chakra-link css-f4h6uy",
                                href="/",
                            ),
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Processo Seletivo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/ps",
                                            id="popover-trigger-3",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-3",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Time",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/members/actual",
                                            id="popover-trigger-5",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-5",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Alumni",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a nossos ex-membros",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/members/alumni",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-5",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "N\u00facleos",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/areas",
                                            id="popover-trigger-7",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-7",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Projetos",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a alguns dos nossos melhores projetos",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/projects",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-7",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Fundo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/fund",
                                            id="popover-trigger-9",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-9",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Parceiros",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/partnerships",
                                            id="popover-trigger-11",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-11",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Aprenda",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/learn",
                                            id="popover-trigger-13",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-13",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Contato",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/contact",
                                            id="popover-trigger-15",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-15",
                                        ),
                                        class_name="css-0",
                                    ),
                                    class_name="chakra-stack css-nd8846",
                                ),
                                class_name="css-1ynfsgs",
                            ),
                            class_name="css-1ef8uzr",
                        ),
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.a(
                                        rx.el.svg.circle(cx="12", cy="12", r="5"),
                                        rx.el.svg.path(d="M12 1v2"),
                                        rx.el.svg.path(d="M12 21v2"),
                                        rx.el.svg.path(d="M4.22 4.22l1.42 1.42"),
                                        rx.el.svg.path(d="M18.36 18.36l1.42 1.42"),
                                        rx.el.svg.path(d="M1 12h2"),
                                        rx.el.svg.path(d="M21 12h2"),
                                        rx.el.svg.path(d="M4.22 19.78l1.42-1.42"),
                                        rx.el.svg.path(d="M18.36 5.64l1.42-1.42"),
                                        stroke_linejoin="round",
                                        stroke_linecap="round",
                                        stroke_width="2",
                                        fill="none",
                                        stroke="currentColor",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-onkibi",
                                ),
                                type="button",
                                class_name="chakra-button css-73pxpg",
                            ),
                            class_name="chakra-stack css-uiyb8i",
                        ),
                        class_name="css-1553k70",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Processo Seletivo",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/ps",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Time", class_name="chakra-text css-13xtz7x"
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/members/actual",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Alumni",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/members/alumni",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "N\u00facleos",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/areas",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Projetos",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/projects",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Fundo", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/fund",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Parceiros",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/partnerships",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Aprenda", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/learn",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Contato", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/contact",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            class_name="chakra-stack css-1delute",
                        ),
                        class_name="chakra-collapse",
                        overflow="hidden",
                        display="none",
                        opacity="0",
                        height="0px",
                    ),
                    class_name="css-0",
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.heading(
                                rx.text.span(
                                    "Venha conhecer",
                                    class_name="chakra-text css-1qzs2a5",
                                ),
                                rx.el.br(),
                                rx.text.span(
                                    "nosso trabalho!",
                                    class_name="chakra-text css-10tibwi",
                                ),
                                class_name="chakra-heading css-190rmj2",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Criada em setembro de 2017, a Blockchain Insper \u00e9 a primeira organiza\u00e7\u00e3o estudantil da Am\u00e9rica Latina focada em estudo de tecnologias blockchain. Derivada de uma iniciativa universit\u00e1ria, que re\u00fane estudantes de administra\u00e7\u00e3o, economia, engenharias e direito a entidade est\u00e1 dividida em tr\u00eas \u00e1reas de estudo: Business, Finance e Tecnologia.",
                                class_name="chakra-text css-oztxm7",
                            ),
                            rx.box(
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
                                        class_name="chakra-button css-19ss788",
                                    ),
                                    target="_blank",
                                    rel="noopener noreferrer",
                                    class_name="chakra-link css-f4h6uy",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                class_name="chakra-stack css-19hw9x9",
                            ),
                            class_name="chakra-stack css-p4fh8y",
                        ),
                        rx.box(
                            rx.el.svg(
                                rx.el.svg.path(
                                    fill_rule="evenodd",
                                    clip_rule="evenodd",
                                    d="M239.184 439.443c-55.13-5.419-110.241-21.365-151.074-58.767C42.307 338.722-7.478 282.729.938 221.217c8.433-61.644 78.896-91.048 126.871-130.712 34.337-28.388 70.198-51.348 112.004-66.78C282.34 8.024 325.382-3.369 370.518.904c54.019 5.115 112.774 10.886 150.881 49.482 39.916 40.427 49.421 100.753 53.385 157.402 4.13 59.015 11.255 128.44-30.444 170.44-41.383 41.683-111.6 19.106-169.213 30.663-46.68 9.364-88.56 35.21-135.943 30.551z",
                                    fill="currentColor",
                                ),
                                viewbox="0 0 578 440",
                                focusable="false",
                                class_name="chakra-icon css-1lqb88r",
                                xmlns="http://www.w3.org/2000/svg",
                            ),
                            rx.box(
                                rx.el.iframe(
                                    title="Teste",
                                    alt="Bitcoin Video",
                                    src="https://www.youtube.com/embed/P3gAHRgNrEE",
                                    allowfullscreen=True,
                                ),
                                class_name="chakra-aspect-ratio css-72bqyg",
                            ),
                            class_name="css-n8pbor",
                        ),
                        class_name="chakra-stack css-1ttgn56",
                    ),
                    class_name="chakra-container css-1vsk1kk",
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.heading(
                                "Reavaliando o presente e construindo o futuro",
                                class_name="chakra-heading css-1dklj6k",
                                as_="h2",
                                size="6",
                            ),
                            rx.text(
                                "Buscamos criar um time altamente engajado e preparado para enfrentar a nova onda de tecnologia no mercado de trabalho. Seguimos com o objetivo de estimular o estudo e a ado\u00e7\u00e3o dessa tecnologia no Brasil, criando conhecimento n\u00e3o apenas para o agora, como tamb\u00e9m para o futuro.",
                                class_name="chakra-text css-ef8b8e",
                            ),
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.box(
                                            rx.el.svg(
                                                rx.el.svg.path(
                                                    fill="none",
                                                    stroke_linecap="round",
                                                    stroke_linejoin="round",
                                                    stroke_width="32",
                                                    d="M461.81 53.81a4.4 4.4 0 00-3.3-3.39c-54.38-13.3-180 34.09-248.13 102.17a294.9 294.9 0 00-33.09 39.08c-21-1.9-42-.3-59.88 7.5-50.49 22.2-65.18 80.18-69.28 105.07a9 9 0 009.8 10.4l81.07-8.9a180.29 180.29 0 001.1 18.3 18.15 18.15 0 005.3 11.09l31.39 31.39a18.15 18.15 0 0011.1 5.3 179.91 179.91 0 0018.19 1.1l-8.89 81a9 9 0 0010.39 9.79c24.9-4 83-18.69 105.07-69.17 7.8-17.9 9.4-38.79 7.6-59.69a293.91 293.91 0 0039.19-33.09c68.38-68 115.47-190.86 102.37-247.95zM298.66 213.67a42.7 42.7 0 1160.38 0 42.65 42.65 0 01-60.38 0z",
                                                ),
                                                rx.el.svg.path(
                                                    fill="none",
                                                    stroke_linecap="round",
                                                    stroke_linejoin="round",
                                                    stroke_width="32",
                                                    d="M109.64 352a45.06 45.06 0 00-26.35 12.84C65.67 382.52 64 448 64 448s65.52-1.67 83.15-19.31A44.73 44.73 0 00160 402.32",
                                                ),
                                                stroke="currentColor",
                                                fill="currentColor",
                                                stroke_width="0",
                                                viewbox="0 0 512 512",
                                                focusable="false",
                                                class_name="chakra-icon css-1lbb8sh",
                                                height="1em",
                                                width="1em",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            class_name="css-1d7t0og",
                                        ),
                                        rx.text(
                                            "Nossa Miss\u00e3o",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        class_name="chakra-stack css-84zodg",
                                    ),
                                    rx.text(
                                        "Fomentar o desenvolvimento do ecossistema brasileiro em torno da tecnologia blockchain, criando um futuro mais eficiente atrav\u00e9s da tecnologia.",
                                        class_name="chakra-text css-1tngv1n",
                                    ),
                                    class_name="css-0",
                                ),
                                rx.box(class_name="chakra-stack__divider css-1uymzum"),
                                rx.box(
                                    rx.box(
                                        rx.box(
                                            rx.el.svg(
                                                rx.el.svg.circle(
                                                    cx="256", cy="256", r="64"
                                                ),
                                                rx.el.svg.path(
                                                    d="M490.84 238.6c-26.46-40.92-60.79-75.68-99.27-100.53C349 110.55 302 96 255.66 96c-42.52 0-84.33 12.15-124.27 36.11-40.73 24.43-77.63 60.12-109.68 106.07a31.92 31.92 0 00-.64 35.54c26.41 41.33 60.4 76.14 98.28 100.65C162 402 207.9 416 255.66 416c46.71 0 93.81-14.43 136.2-41.72 38.46-24.77 72.72-59.66 99.08-100.92a32.2 32.2 0 00-.1-34.76zM256 352a96 96 0 1196-96 96.11 96.11 0 01-96 96z"
                                                ),
                                                stroke="currentColor",
                                                fill="currentColor",
                                                stroke_width="0",
                                                viewbox="0 0 512 512",
                                                focusable="false",
                                                class_name="chakra-icon css-1oovkcf",
                                                height="1em",
                                                width="1em",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            class_name="css-98kz1g",
                                        ),
                                        rx.text(
                                            "Nossa Vis\u00e3o",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        class_name="chakra-stack css-84zodg",
                                    ),
                                    rx.text(
                                        "Capacitar os alunos com o melhor conte\u00fado e conect\u00e1-los ao mercado, no intuito de incluir nosso pa\u00eds nesse cen\u00e1rio de inova\u00e7\u00e3o.",
                                        class_name="chakra-text css-1tngv1n",
                                    ),
                                    class_name="css-0",
                                ),
                                rx.box(class_name="chakra-stack__divider css-1uymzum"),
                                rx.box(
                                    rx.box(
                                        rx.box(
                                            rx.el.svg(
                                                rx.el.svg.circle(
                                                    cx="256", cy="256", r="24"
                                                ),
                                                rx.el.svg.path(
                                                    d="M256 48C141.31 48 48 141.31 48 256s93.31 208 208 208 208-93.31 208-208S370.69 48 256 48zm105.07 113.33l-46.88 117.2a64 64 0 01-35.66 35.66l-117.2 46.88a8 8 0 01-10.4-10.4l46.88-117.2a64 64 0 0135.66-35.66l117.2-46.88a8 8 0 0110.4 10.4z"
                                                ),
                                                stroke="currentColor",
                                                fill="currentColor",
                                                stroke_width="0",
                                                viewbox="0 0 512 512",
                                                focusable="false",
                                                class_name="chakra-icon css-7gskat",
                                                height="1em",
                                                width="1em",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            class_name="css-izs6lo",
                                        ),
                                        rx.text(
                                            "Nossos Valores",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        class_name="chakra-stack css-84zodg",
                                    ),
                                    rx.text(
                                        "Alto comprometimento, proatividade, inova\u00e7\u00e3o, trabalho em equipe, multidisciplinaridade, excel\u00eancia e efici\u00eancia.",
                                        class_name="chakra-text css-1tngv1n",
                                    ),
                                    class_name="css-0",
                                ),
                                class_name="chakra-stack css-j7qwjs",
                            ),
                            class_name="chakra-stack css-egoftb",
                        ),
                        rx.box(
                            rx.image(
                                alt="feature image",
                                src="/static/media/insper.938cda6f.jpg",
                                class_name="chakra-image css-b85nkz",
                            ),
                            class_name="css-k008qs",
                        ),
                        class_name="css-lfcvwb",
                    ),
                    class_name="chakra-container css-16vsuek",
                ),
                rx.box(
                    rx.box(
                        rx.box(
                            rx.heading(
                                "Depoimentos de nossos membros",
                                class_name="chakra-heading css-1dklj6k",
                                as_="h2",
                                size="6",
                            ),
                            class_name="chakra-stack css-jp20jv",
                        ),
                        rx.box(
                            rx.box(
                                rx.box(
                                    rx.text(
                                        "Hoje acredito que a entidade se tornou algo muito mais pr\u00f3ximo do que imagin\u00e1vamos quando foi fundada, um organismo que funciona de maneira independente de qualquer membro espec\u00edfico. Al\u00e9m da possibilidade de aprender e debater com pessoas inteligentes sobre caminhos futuros para a sociedade por meio da tecnologia, os membros tem a oportunidade de aplicar essas ideias na pr\u00e1tica nas \u00e1reas internas e tamb\u00e9m em projetos com as principais empresas do pa\u00eds como Ambev e BTG Pactual.",
                                        class_name="chakra-text css-16ozagw",
                                    ),
                                    class_name="chakra-stack css-1ahniv6",
                                ),
                                rx.box(
                                    rx.text.span(
                                        rx.image(
                                            src="/static/media/felipe.b7224a86.jpeg",
                                            class_name="chakra-avatar__img css-3a5bz2",
                                        ),
                                        alt="Felipe Santos",
                                        class_name="chakra-avatar css-in8e35",
                                    ),
                                    rx.box(
                                        rx.text(
                                            "Felipe Santos",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        rx.text(
                                            "Co-fundador e Ex-membro",
                                            class_name="chakra-text css-zgbaaa",
                                        ),
                                        class_name="chakra-stack css-130k5dj",
                                    ),
                                    class_name="css-1p6ys5y",
                                ),
                                class_name="css-0",
                            ),
                            rx.box(
                                rx.box(
                                    rx.text(
                                        "Quando me chamaram e disseram que estavam fazendo uma entidade relacionada a isso eu vi uma oportunidade de disseminar o conhecimento nem que fosse dentro do pr\u00f3prio insper Foi ent\u00e3o que me juntei ao time de fundadores da entidade. Com uma miss\u00e3o de difundir o conhecimento e fazer com que as pessoas gostem de aprender e tenham as melhores ferramentas a sua disposi\u00e7\u00e3o. Por isso decido fazer v\u00e1rios projetos para que eu possa levar o conhecimento que fui adquirindo para os outros seja na forma de aulas, ou at\u00e9 mesmo mentira do um projeto proposto.",
                                        class_name="chakra-text css-16ozagw",
                                    ),
                                    class_name="chakra-stack css-1ahniv6",
                                ),
                                rx.box(
                                    rx.text.span(
                                        rx.image(
                                            src="/static/media/bruno.34122a46.jpeg",
                                            class_name="chakra-avatar__img css-3a5bz2",
                                        ),
                                        alt="Bruno Arthur",
                                        class_name="chakra-avatar css-in8e35",
                                    ),
                                    rx.box(
                                        rx.text(
                                            "Bruno Arthur",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        rx.text(
                                            "Co-fundador e Ex-membro",
                                            class_name="chakra-text css-zgbaaa",
                                        ),
                                        class_name="chakra-stack css-130k5dj",
                                    ),
                                    class_name="css-1p6ys5y",
                                ),
                                class_name="css-0",
                            ),
                            rx.box(
                                rx.box(
                                    rx.text(
                                        "Fundar a B.I. foi um desafio \u00edmpar. Estudar uma tecnologia t\u00e3o latente e nova trouxe desafios extras, mas ao mesmo tempo diferenciais competitivos em nossos curr\u00edculos, logo no in\u00edcio de nossas carreiras. Habilidades de aprendizado, gest\u00e3o de equipe, resolu\u00e7\u00e3o de conflitos, entendimento de viabilidade de projetos e tomada de decis\u00e3o, eram desenvolvidas a cada dia. Hoje posso falar que a entidade teve papel fundamental em meu desenvolvimento profissional e na posi\u00e7\u00e3o que ocupo hoje.",
                                        class_name="chakra-text css-16ozagw",
                                    ),
                                    class_name="chakra-stack css-1ahniv6",
                                ),
                                rx.box(
                                    rx.text.span(
                                        rx.image(
                                            src="/static/media/joao.8543876f.jpeg",
                                            class_name="chakra-avatar__img css-3a5bz2",
                                        ),
                                        alt="Jo\u00e3o P. J. M. Perpetuo",
                                        class_name="chakra-avatar css-in8e35",
                                    ),
                                    rx.box(
                                        rx.text(
                                            "Jo\u00e3o P. J. M. Perpetuo",
                                            class_name="chakra-text css-35ezg3",
                                        ),
                                        rx.text(
                                            "Co-fundador e Ex-membro",
                                            class_name="chakra-text css-zgbaaa",
                                        ),
                                        class_name="chakra-stack css-130k5dj",
                                    ),
                                    class_name="css-1p6ys5y",
                                ),
                                class_name="css-0",
                            ),
                            class_name="chakra-stack css-1k0eqqv",
                        ),
                        class_name="chakra-container chakra-stack css-1cvohfv",
                    ),
                    class_name="css-1cozlc8",
                ),
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
                rx.box(
                    rx.box(
                        rx.box(
                            rx.image(
                                src="/static/media/logo-dark.537e082d.svg",
                                class_name="chakra-image css-v7v99c",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 640 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Discord",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="LinkedIn",
                                    href="https://www.linkedin.com/company/blockchain-insper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Instagram",
                                    href="https://www.instagram.com/blockchainsper/",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 496 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="GitHub",
                                    href="https://github.com/BlockchainInsper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                                        rx.el.svg.path(
                                            d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 24 24",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Email",
                                    href="mailto:blockchainsper@gmail.com",
                                ),
                                role="group",
                                class_name="chakra-button__group css-1bdsol1",
                            ),
                            class_name="chakra-stack css-3ivhej",
                        ),
                        rx.text(
                            "\u00a9 2025 Blockchain Insper. All rights reserved.",
                            class_name="chakra-text css-1kfduyp",
                        ),
                        class_name="chakra-stack css-n21gh5",
                    ),
                    role="contentinfo",
                    class_name="css-1xi056f",
                ),
                id="root",
            ),
            class_name="chakra-ui-dark",
        ),
    )


def processo_seletivo():
    return rx.fragment(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        fill="currentColor",
                                        d="M 3 5 A 1.0001 1.0001 0 1 0 3 7 L 21 7 A 1.0001 1.0001 0 1 0 21 5 L 3 5 z M 3 11 A 1.0001 1.0001 0 1 0 3 13 L 21 13 A 1.0001 1.0001 0 1 0 21 11 L 3 11 z M 3 17 A 1.0001 1.0001 0 1 0 3 19 L 21 19 A 1.0001 1.0001 0 1 0 21 17 L 3 17 z",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-bokek7",
                                    aria_hidden="true",
                                ),
                                type="button",
                                class_name="chakra-button css-f59olw",
                                aria_label="Toggle Navigation",
                            ),
                            class_name="css-1twb9xo",
                        ),
                        rx.box(
                            rx.el.a(
                                rx.image(
                                    src="/static/media/logo-dark.537e082d.svg",
                                    class_name="chakra-image css-v7v99c",
                                ),
                                class_name="chakra-link css-f4h6uy",
                                href="/",
                            ),
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Processo Seletivo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/ps",
                                            id="popover-trigger-3",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-3",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Time",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/members/actual",
                                            id="popover-trigger-5",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-5",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Alumni",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a nossos ex-membros",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/members/alumni",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-5",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "N\u00facleos",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/areas",
                                            id="popover-trigger-7",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-7",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Projetos",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a alguns dos nossos melhores projetos",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/projects",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-7",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Fundo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/fund",
                                            id="popover-trigger-9",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-9",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Parceiros",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/partnerships",
                                            id="popover-trigger-11",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-11",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Aprenda",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/learn",
                                            id="popover-trigger-13",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-13",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Contato",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/contact",
                                            id="popover-trigger-15",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-15",
                                        ),
                                        class_name="css-0",
                                    ),
                                    class_name="chakra-stack css-nd8846",
                                ),
                                class_name="css-1ynfsgs",
                            ),
                            class_name="css-1ef8uzr",
                        ),
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.a(
                                        rx.el.svg.circle(cx="12", cy="12", r="5"),
                                        rx.el.svg.path(d="M12 1v2"),
                                        rx.el.svg.path(d="M12 21v2"),
                                        rx.el.svg.path(d="M4.22 4.22l1.42 1.42"),
                                        rx.el.svg.path(d="M18.36 18.36l1.42 1.42"),
                                        rx.el.svg.path(d="M1 12h2"),
                                        rx.el.svg.path(d="M21 12h2"),
                                        rx.el.svg.path(d="M4.22 19.78l1.42-1.42"),
                                        rx.el.svg.path(d="M18.36 5.64l1.42-1.42"),
                                        stroke_linejoin="round",
                                        stroke_linecap="round",
                                        stroke_width="2",
                                        fill="none",
                                        stroke="currentColor",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-onkibi",
                                ),
                                type="button",
                                class_name="chakra-button css-73pxpg",
                            ),
                            class_name="chakra-stack css-uiyb8i",
                        ),
                        class_name="css-1553k70",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Processo Seletivo",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/ps",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Time", class_name="chakra-text css-13xtz7x"
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/members/actual",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Alumni",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/members/alumni",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "N\u00facleos",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/areas",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Projetos",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/projects",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Fundo", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/fund",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Parceiros",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/partnerships",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Aprenda", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/learn",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Contato", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/contact",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            class_name="chakra-stack css-1delute",
                        ),
                        class_name="chakra-collapse",
                        overflow="hidden",
                        display="none",
                        opacity="0",
                        height="0px",
                    ),
                    class_name="css-0",
                ),
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
                rx.box(
                    rx.box(
                        rx.box(
                            rx.image(
                                src="/static/media/logo-dark.537e082d.svg",
                                class_name="chakra-image css-v7v99c",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 640 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Discord",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="LinkedIn",
                                    href="https://www.linkedin.com/company/blockchain-insper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Instagram",
                                    href="https://www.instagram.com/blockchainsper/",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 496 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="GitHub",
                                    href="https://github.com/BlockchainInsper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                                        rx.el.svg.path(
                                            d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 24 24",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Email",
                                    href="mailto:blockchainsper@gmail.com",
                                ),
                                role="group",
                                class_name="chakra-button__group css-1bdsol1",
                            ),
                            class_name="chakra-stack css-3ivhej",
                        ),
                        rx.text(
                            "\u00a9 2025 Blockchain Insper. All rights reserved.",
                            class_name="chakra-text css-1kfduyp",
                        ),
                        class_name="chakra-stack css-n21gh5",
                    ),
                    role="contentinfo",
                    class_name="css-1xi056f",
                ),
                id="root",
            )
        )
    )


def time():
    return rx.fragment(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        fill="currentColor",
                                        d="M 3 5 A 1.0001 1.0001 0 1 0 3 7 L 21 7 A 1.0001 1.0001 0 1 0 21 5 L 3 5 z M 3 11 A 1.0001 1.0001 0 1 0 3 13 L 21 13 A 1.0001 1.0001 0 1 0 21 11 L 3 11 z M 3 17 A 1.0001 1.0001 0 1 0 3 19 L 21 19 A 1.0001 1.0001 0 1 0 21 17 L 3 17 z",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-bokek7",
                                    aria_hidden="true",
                                ),
                                type="button",
                                class_name="chakra-button css-f59olw",
                                aria_label="Toggle Navigation",
                            ),
                            class_name="css-1twb9xo",
                        ),
                        rx.box(
                            rx.el.a(
                                rx.image(
                                    src="/static/media/logo-dark.537e082d.svg",
                                    class_name="chakra-image css-v7v99c",
                                ),
                                class_name="chakra-link css-f4h6uy",
                                href="/",
                            ),
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Processo Seletivo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/ps",
                                            id="popover-trigger-3",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-3",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Time",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/members/actual",
                                            id="popover-trigger-5",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-5",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Alumni",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a nossos ex-membros",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/members/alumni",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-5",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                            margin="0px",
                                            transform="translate(298.4px, 52.8px)",
                                            __popper_transform_origin="top left",
                                            custom_attrs={
                                                "data-popper-placement": "bottom-start"
                                            },
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "N\u00facleos",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/areas",
                                            id="popover-trigger-7",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-7",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Projetos",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a alguns dos nossos melhores projetos",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/projects",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-7",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Fundo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/fund",
                                            id="popover-trigger-9",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-9",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Parceiros",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/partnerships",
                                            id="popover-trigger-11",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-11",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Aprenda",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/learn",
                                            id="popover-trigger-13",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-13",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Contato",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/contact",
                                            id="popover-trigger-15",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-15",
                                        ),
                                        class_name="css-0",
                                    ),
                                    class_name="chakra-stack css-nd8846",
                                ),
                                class_name="css-1ynfsgs",
                            ),
                            class_name="css-1ef8uzr",
                        ),
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.a(
                                        rx.el.svg.circle(cx="12", cy="12", r="5"),
                                        rx.el.svg.path(d="M12 1v2"),
                                        rx.el.svg.path(d="M12 21v2"),
                                        rx.el.svg.path(d="M4.22 4.22l1.42 1.42"),
                                        rx.el.svg.path(d="M18.36 18.36l1.42 1.42"),
                                        rx.el.svg.path(d="M1 12h2"),
                                        rx.el.svg.path(d="M21 12h2"),
                                        rx.el.svg.path(d="M4.22 19.78l1.42-1.42"),
                                        rx.el.svg.path(d="M18.36 5.64l1.42-1.42"),
                                        stroke_linejoin="round",
                                        stroke_linecap="round",
                                        stroke_width="2",
                                        fill="none",
                                        stroke="currentColor",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-onkibi",
                                ),
                                type="button",
                                class_name="chakra-button css-73pxpg",
                            ),
                            class_name="chakra-stack css-uiyb8i",
                        ),
                        class_name="css-1553k70",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Processo Seletivo",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/ps",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Time", class_name="chakra-text css-13xtz7x"
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/members/actual",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Alumni",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/members/alumni",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "N\u00facleos",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/areas",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Projetos",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/projects",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Fundo", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/fund",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Parceiros",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/partnerships",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Aprenda", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/learn",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Contato", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/contact",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            class_name="chakra-stack css-1delute",
                        ),
                        class_name="chakra-collapse",
                        overflow="hidden",
                        display="none",
                        opacity="0",
                        height="0px",
                    ),
                    class_name="css-0",
                ),
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
                rx.box(
                    rx.box(
                        rx.box(
                            rx.image(
                                src="/static/media/logo-dark.537e082d.svg",
                                class_name="chakra-image css-v7v99c",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 640 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Discord",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="LinkedIn",
                                    href="https://www.linkedin.com/company/blockchain-insper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Instagram",
                                    href="https://www.instagram.com/blockchainsper/",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 496 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="GitHub",
                                    href="https://github.com/BlockchainInsper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                                        rx.el.svg.path(
                                            d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 24 24",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Email",
                                    href="mailto:blockchainsper@gmail.com",
                                ),
                                role="group",
                                class_name="chakra-button__group css-1bdsol1",
                            ),
                            class_name="chakra-stack css-3ivhej",
                        ),
                        rx.text(
                            "\u00a9 2025 Blockchain Insper. All rights reserved.",
                            class_name="chakra-text css-1kfduyp",
                        ),
                        class_name="chakra-stack css-n21gh5",
                    ),
                    role="contentinfo",
                    class_name="css-1xi056f",
                ),
                id="root",
            )
        )
    )


def nucleos():
    return rx.fragment(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.svg.path(
                                        fill="currentColor",
                                        d="M 3 5 A 1.0001 1.0001 0 1 0 3 7 L 21 7 A 1.0001 1.0001 0 1 0 21 5 L 3 5 z M 3 11 A 1.0001 1.0001 0 1 0 3 13 L 21 13 A 1.0001 1.0001 0 1 0 21 11 L 3 11 z M 3 17 A 1.0001 1.0001 0 1 0 3 19 L 21 19 A 1.0001 1.0001 0 1 0 21 17 L 3 17 z",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-bokek7",
                                    aria_hidden="true",
                                ),
                                type="button",
                                class_name="chakra-button css-f59olw",
                                aria_label="Toggle Navigation",
                            ),
                            class_name="css-1twb9xo",
                        ),
                        rx.box(
                            rx.el.a(
                                rx.image(
                                    src="/static/media/logo-dark.537e082d.svg",
                                    class_name="chakra-image css-v7v99c",
                                ),
                                class_name="chakra-link css-f4h6uy",
                                href="/",
                            ),
                            rx.box(
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Processo Seletivo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/ps",
                                            id="popover-trigger-3",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-3",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Time",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/members/actual",
                                            id="popover-trigger-5",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-5",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Alumni",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a nossos ex-membros",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/members/alumni",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-5",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            position="absolute",
                                            min_width="max-content",
                                            inset="0px auto auto 0px",
                                            margin="0px",
                                            transform="translate(298.4px, 52.8px)",
                                            __popper_transform_origin="top left",
                                            custom_attrs={
                                                "data-popper-placement": "bottom-start"
                                            },
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "N\u00facleos",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/areas",
                                            id="popover-trigger-7",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-7",
                                        ),
                                        rx.box(
                                            rx.box(
                                                rx.box(
                                                    rx.el.a(
                                                        rx.box(
                                                            rx.box(
                                                                rx.text(
                                                                    "Projetos",
                                                                    class_name="chakra-text css-cugd40",
                                                                ),
                                                                rx.text(
                                                                    "Conhe\u00e7a alguns dos nossos melhores projetos",
                                                                    class_name="chakra-text css-itvw0n",
                                                                ),
                                                                class_name="css-0",
                                                            ),
                                                            rx.box(
                                                                rx.el.svg(
                                                                    rx.el.svg.path(
                                                                        fill="currentColor",
                                                                        d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z",
                                                                    ),
                                                                    viewbox="0 0 24 24",
                                                                    focusable="false",
                                                                    class_name="chakra-icon css-1b471nl",
                                                                ),
                                                                class_name="css-2gz105",
                                                            ),
                                                            class_name="chakra-stack css-84zodg",
                                                        ),
                                                        class_name="chakra-link css-v8ajqy",
                                                        href="#/projects",
                                                        role="group",
                                                    ),
                                                    class_name="chakra-stack css-n21gh5",
                                                ),
                                                id="popover-content-7",
                                                tabindex="-1",
                                                role="tooltip",
                                                class_name="chakra-popover__content css-c440zk",
                                                transform_origin="var(--popper-transform-origin)",
                                                opacity="0",
                                                visibility="hidden",
                                                transform="scale(0.95) translateZ(0px)",
                                            ),
                                            class_name="chakra-popover__popper css-1qq679y",
                                            visibility="hidden",
                                            min_width="max-content",
                                            margin="0px",
                                            __popper_transform_origin="top left",
                                            position="absolute",
                                            inset="0px auto auto 0px",
                                            transform="translate(360.8px, 52.8px)",
                                            custom_attrs={
                                                "data-popper-placement": "bottom-start"
                                            },
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Fundo",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/fund",
                                            id="popover-trigger-9",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-9",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Parceiros",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/partnerships",
                                            id="popover-trigger-11",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-11",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Aprenda",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/learn",
                                            id="popover-trigger-13",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-13",
                                        ),
                                        class_name="css-0",
                                    ),
                                    rx.box(
                                        rx.el.a(
                                            "Contato",
                                            class_name="chakra-link css-p92xmu",
                                            href="#/contact",
                                            id="popover-trigger-15",
                                            aria_haspopup="dialog",
                                            aria_expanded="false",
                                            aria_controls="popover-content-15",
                                        ),
                                        class_name="css-0",
                                    ),
                                    class_name="chakra-stack css-nd8846",
                                ),
                                class_name="css-1ynfsgs",
                            ),
                            class_name="css-1ef8uzr",
                        ),
                        rx.box(
                            rx.el.button(
                                rx.el.svg(
                                    rx.el.a(
                                        rx.el.svg.circle(cx="12", cy="12", r="5"),
                                        rx.el.svg.path(d="M12 1v2"),
                                        rx.el.svg.path(d="M12 21v2"),
                                        rx.el.svg.path(d="M4.22 4.22l1.42 1.42"),
                                        rx.el.svg.path(d="M18.36 18.36l1.42 1.42"),
                                        rx.el.svg.path(d="M1 12h2"),
                                        rx.el.svg.path(d="M21 12h2"),
                                        rx.el.svg.path(d="M4.22 19.78l1.42-1.42"),
                                        rx.el.svg.path(d="M18.36 5.64l1.42-1.42"),
                                        stroke_linejoin="round",
                                        stroke_linecap="round",
                                        stroke_width="2",
                                        fill="none",
                                        stroke="currentColor",
                                    ),
                                    viewbox="0 0 24 24",
                                    focusable="false",
                                    class_name="chakra-icon css-onkibi",
                                ),
                                type="button",
                                class_name="chakra-button css-73pxpg",
                            ),
                            class_name="chakra-stack css-uiyb8i",
                        ),
                        class_name="css-1553k70",
                    ),
                    rx.box(
                        rx.box(
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Processo Seletivo",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/ps",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Time", class_name="chakra-text css-13xtz7x"
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/members/actual",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Alumni",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/members/alumni",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "N\u00facleos",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            fill="currentColor",
                                            d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z",
                                        ),
                                        viewbox="0 0 24 24",
                                        focusable="false",
                                        class_name="chakra-icon css-1twc07j",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/areas",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.el.a(
                                            "Projetos",
                                            class_name="chakra-link css-1i05af6",
                                            href="#/projects",
                                        ),
                                        class_name="chakra-stack css-1xmht12",
                                    ),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Fundo", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/fund",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Parceiros",
                                        class_name="chakra-text css-13xtz7x",
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/partnerships",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Aprenda", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/learn",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.text(
                                        "Contato", class_name="chakra-text css-13xtz7x"
                                    ),
                                    class_name="chakra-link css-ryc07z",
                                    href="#/contact",
                                ),
                                rx.box(
                                    rx.box(class_name="chakra-stack css-1xmht12"),
                                    class_name="chakra-collapse",
                                    overflow="hidden",
                                    display="none",
                                    opacity="0",
                                    height="0px",
                                ),
                                class_name="chakra-stack css-egoftb",
                            ),
                            class_name="chakra-stack css-1delute",
                        ),
                        class_name="chakra-collapse",
                        overflow="hidden",
                        display="none",
                        opacity="0",
                        height="0px",
                    ),
                    class_name="css-0",
                ),
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
                rx.box(
                    rx.box(
                        rx.box(
                            rx.image(
                                src="/static/media/logo-dark.537e082d.svg",
                                class_name="chakra-image css-v7v99c",
                            ),
                            rx.box(
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M524.531,69.836a1.5,1.5,0,0,0-.764-.7A485.065,485.065,0,0,0,404.081,32.03a1.816,1.816,0,0,0-1.923.91,337.461,337.461,0,0,0-14.9,30.6,447.848,447.848,0,0,0-134.426,0,309.541,309.541,0,0,0-15.135-30.6,1.89,1.89,0,0,0-1.924-.91A483.689,483.689,0,0,0,116.085,69.137a1.712,1.712,0,0,0-.788.676C39.068,183.651,18.186,294.69,28.43,404.354a2.016,2.016,0,0,0,.765,1.375A487.666,487.666,0,0,0,176.02,479.918a1.9,1.9,0,0,0,2.063-.676A348.2,348.2,0,0,0,208.12,430.4a1.86,1.86,0,0,0-1.019-2.588,321.173,321.173,0,0,1-45.868-21.853,1.885,1.885,0,0,1-.185-3.126c3.082-2.309,6.166-4.711,9.109-7.137a1.819,1.819,0,0,1,1.9-.256c96.229,43.917,200.41,43.917,295.5,0a1.812,1.812,0,0,1,1.924.233c2.944,2.426,6.027,4.851,9.132,7.16a1.884,1.884,0,0,1-.162,3.126,301.407,301.407,0,0,1-45.89,21.83,1.875,1.875,0,0,0-1,2.611,391.055,391.055,0,0,0,30.014,48.815,1.864,1.864,0,0,0,2.063.7A486.048,486.048,0,0,0,610.7,405.729a1.882,1.882,0,0,0,.765-1.352C623.729,277.594,590.933,167.465,524.531,69.836ZM222.491,337.58c-28.972,0-52.844-26.587-52.844-59.239S193.056,219.1,222.491,219.1c29.665,0,53.306,26.82,52.843,59.239C275.334,310.993,251.924,337.58,222.491,337.58Zm195.38,0c-28.971,0-52.843-26.587-52.843-59.239S388.437,219.1,417.871,219.1c29.667,0,53.307,26.82,52.844,59.239C470.715,310.993,447.538,337.58,417.871,337.58Z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 640 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Discord",
                                    href="https://discord.gg/jdK5yB48Mm",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="LinkedIn",
                                    href="https://www.linkedin.com/company/blockchain-insper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 448 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Instagram",
                                    href="https://www.instagram.com/blockchainsper/",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(
                                            d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 496 512",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="GitHub",
                                    href="https://github.com/BlockchainInsper",
                                ),
                                rx.el.a(
                                    rx.el.svg(
                                        rx.el.svg.path(fill="none", d="M0 0h24v24H0z"),
                                        rx.el.svg.path(
                                            d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"
                                        ),
                                        stroke="currentColor",
                                        fill="currentColor",
                                        stroke_width="0",
                                        viewbox="0 0 24 24",
                                        font_size="20px",
                                        aria_hidden="true",
                                        focusable="false",
                                        height="1em",
                                        width="1em",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    class_name="chakra-button css-12su4ed",
                                    aria_label="Email",
                                    href="mailto:blockchainsper@gmail.com",
                                ),
                                role="group",
                                class_name="chakra-button__group css-1bdsol1",
                            ),
                            class_name="chakra-stack css-3ivhej",
                        ),
                        rx.text(
                            "\u00a9 2025 Blockchain Insper. All rights reserved.",
                            class_name="chakra-text css-1kfduyp",
                        ),
                        class_name="chakra-stack css-n21gh5",
                    ),
                    role="contentinfo",
                    class_name="css-1xi056f",
                ),
                id="root",
            )
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(processo_seletivo, "/#/ps")
app.add_page(time, "/#/members/actual")
app.add_page(nucleos, "/#/areas")
