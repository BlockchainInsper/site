import reflex as rx


def call_to_action_with_video():
    return (
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
    )
