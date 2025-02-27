import reflex as rx


def curso():
    return (
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
    )
