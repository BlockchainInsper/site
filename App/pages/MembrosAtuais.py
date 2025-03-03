import reflex as rx
from App.Template import template


@rx.page(route="/members/actual")
@template
def membros_atuais():
    return rx.vstack(
        rx.box(
            rx.box(
                rx.heading(
                    "Conhe\u00e7a nosso time ",
                    rx.text.span("2022.1", class_name="chakra-text css-1jkapds"),
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
        id="root",
    )
