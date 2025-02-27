import reflex as rx


def contato_info():
    return (
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
    )
