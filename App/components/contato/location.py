import reflex as rx


def location_info():
    return (
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
    )
