import reflex as rx


def areas():
    return rx.box(
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
    )
