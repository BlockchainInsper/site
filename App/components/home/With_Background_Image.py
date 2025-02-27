import reflex as rx


def with_background_image():
    return (
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
    )
