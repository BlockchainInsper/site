import reflex as rx
from components.home.Hero import call_to_action_with_video
from components.home.Features import features
from components.home.Testimonials import testimonials
from App.Template import template


def with_background_image():
    return rx.flex(
        # Container principal centralizado horizontalmente
        rx.flex(
            # Stack vertical com texto e botão
            rx.vstack(
                # Texto alinhado à esquerda
                rx.text(
                    "Conheça nossas áreas! Estamos estruturados em áreas de estudo e áreas administrativas",
                    class_name="font-bold leading-tight text-3xl md:text-4xl text-left text-white",
                ),
                # Botão alinhado à esquerda
                rx.button(
                    "Nossas áreas",
                    class_name="bg-[#f68b23] rounded-full text-white hover:bg-[#f68b70]",
                    on_click=rx.redirect("/areas"),
                ),
                # Configuração do vstack
                spacing="6",
                class_name="items-start w-full",  # Alinha os itens à esquerda
            ),
            # Configuração do flex container
            class_name="max-w-2xl w-full justify-center",
        ),
        # Configuração do flex principal com cor de fundo
        class_name="w-full h-[30vh] bg-[#1A202C] flex justify-center items-center px-4",
    )


@rx.page(route="/")
@template
def home():
    return rx.vstack(
        call_to_action_with_video(),
        features(),
        testimonials(),
        with_background_image(),
    )
