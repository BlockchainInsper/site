import reflex as rx


def navbar():
    return rx.box(
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
                        src="/logo-dark.svg",
                        class_name="chakra-image css-v7v99c",
                        width="100px",
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
                                href="/ps",
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
                                href="/members/actual",
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
                                            href="/members/alumni",
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
                                            href="/projects",
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
                                href="/fund",
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
                                href="/partnerships",
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
                                href="/learn",
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
                                href="/contact",
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
                            "Processo Seletivo",  # PARECE CÓDIGO DUPLICADO
                            class_name="chakra-text css-13xtz7x",
                        ),
                        class_name="chakra-link css-ryc07z",
                        href="/ps",
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
                            "Time",
                            class_name="chakra-text css-13xtz7x",  # PARECE CÓDIGO DUPLICADO
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
                        href="/members/actual",
                    ),
                    rx.box(
                        rx.box(
                            rx.el.a(
                                "Alumni",  # PARECE CÓDIGO DUPLICADO
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
                            "N\u00facleos",  # PARECE CÓDIGO DUPLICADO
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
                        href="/areas",
                    ),
                    rx.box(
                        rx.box(
                            rx.el.a(
                                "Projetos",  # PARECE CÓDIGO DUPLICADO
                                class_name="chakra-link css-1i05af6",
                                href="/projects",
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
                            "Fundo",  # PARECE CÓDIGO DUPLICADO
                            class_name="chakra-text css-13xtz7x",
                        ),
                        class_name="chakra-link css-ryc07z",
                        href="/fund",
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
                            "Parceiros",  # PARECE CÓDIGO DUPLICADO
                            class_name="chakra-text css-13xtz7x",
                        ),
                        class_name="chakra-link css-ryc07z",
                        href="/partnerships",
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
                            "Aprenda",  # PARECE CÓDIGO DUPLICADO
                            class_name="chakra-text css-13xtz7x",
                        ),
                        class_name="chakra-link css-ryc07z",
                        href="/learn",
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
                            "Contato",  # PARECE CÓDIGO DUPLICADO
                            class_name="chakra-text css-13xtz7x",
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
    )
