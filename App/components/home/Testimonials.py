import reflex as rx


def testimonial_content(text: str) -> rx.Component:
    """Balão de depoimento com pseudo-elemento de triângulo."""
    return rx.box(
        rx.text(
            text,
            style={
                "text_align": "center",
                "color": rx.color_mode_cond(
                    light="rgb(107, 114, 128)",  # gray-600
                    dark="rgb(156, 163, 175)",  # gray-400
                ),
                "font_size": "0.875rem",  # text-sm
                "line_height": "1.5rem",
            },
        ),
        style={
            "background": rx.color_mode_cond(
                light="white",
                dark="rgb(31, 41, 55)",  # gray-800
            ),
            "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1)",
            "padding": "2rem",
            "border_radius": "0.75rem",
            "position": "relative",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "width": "400px",  # Largura fixa maior
            "_after": {
                "content": "''",
                "position": "absolute",
                "width": "0",
                "height": "0",
                "border_left": "16px solid transparent",
                "border_right": "16px solid transparent",
                "border_top": rx.color_mode_cond(
                    light="16px solid white", dark="16px solid rgb(31, 41, 55)"
                ),
                "bottom": "-16px",
                "left": "50%",
                "transform": "translateX(-50%)",
            },
        },
    )


def testimonial_avatar(src: str, name: str, title: str) -> rx.Component:
    """Avatar com nome e título do depoente."""
    return rx.box(
        rx.box(
            rx.avatar(src=src, alt=name, style={"width": "3rem", "height": "3rem"}),
            style={"display": "flex", "justify_content": "center", "width": "100%"},
        ),
        rx.box(
            rx.text(name, style={"font_weight": "600", "text_align": "center"}),
            style={"text_align": "center", "width": "100%", "margin_top": "0.5rem"},
        ),
        rx.box(
            rx.text(
                title,
                style={
                    "font_size": "0.875rem",
                    "color": rx.color_mode_cond(
                        light="rgb(107, 114, 128)",  # gray-600
                        dark="rgb(156, 163, 175)",  # gray-400
                    ),
                },
            ),
            style={"text_align": "center", "width": "100%"},
        ),
        style={"margin_top": "2rem", "width": "100%"},
    )


def testimonial(content: str, src: str, name: str, title: str) -> rx.Component:
    """Componente completo de um depoimento."""
    return rx.box(
        testimonial_content(content),
        testimonial_avatar(src, name, title),
        style={"width": "100%"},
    )


def testimonials() -> rx.Component:
    """Componente principal de depoimentos."""
    return rx.box(
        rx.box(
            rx.vstack(  # Usando vstack para organizar verticalmente
                rx.vstack(  # Stack para o título
                    rx.heading(
                        "Depoimentos de nossos membros",
                        style={
                            "font_size": "2.25rem",
                            "font_weight": "700",
                            "text_align": "center",
                            "color": rx.color_mode_cond(
                                light="#1A202C", dark="rgba(255, 255, 255, 0.92)"
                            ),
                        },
                    ),
                    style={
                        "spacing": "0",
                        "align_items": "center",
                        "margin_bottom": "3rem",
                        "width": "100%",  # Garante que o vstack ocupe toda a largura
                        "display": "flex",
                        "justify_content": "center",  # Centraliza horizontalmente
                    },
                ),
                rx.grid(
                    testimonial(
                        "Hoje acredito que a entidade se tornou algo muito mais próximo do que imaginávamos quando "
                        "foi fundada, um organismo que funciona de maneira independente de qualquer membro "
                        "específico. Além da possibilidade de aprender e debater com pessoas inteligentes sobre "
                        "caminhos futuros para a sociedade por meio da tecnologia, os membros tem a oportunidade "
                        "de aplicar essas ideias na prática nas áreas internas e também em projetos com as "
                        "principais empresas do país como Ambev e BTG Pactual.",
                        "/felipe.jpeg",
                        "Felipe Santos",
                        "Co-fundador e Ex-membro",
                    ),
                    testimonial(
                        "Quando me chamaram e disseram que estavam fazendo uma entidade relacionada a isso eu vi "
                        "uma oportunidade de disseminar o conhecimento nem que fosse dentro do próprio insper "
                        "Foi então que me juntei ao time de fundadores da entidade. Com uma missão de difundir o "
                        "conhecimento e fazer com que as pessoas gostem de aprender e tenham as melhores "
                        "ferramentas a sua disposição. Por isso decido fazer vários projetos para que eu possa "
                        "levar o conhecimento que fui adquirindo para os outros seja na forma de aulas, ou até "
                        "mesmo mentira do um projeto proposto.",
                        "/bruno.jpeg",
                        "Bruno Arthur",
                        "Co-fundador e Ex-membro",
                    ),
                    testimonial(
                        "Fundar a B.I. foi um desafio ímpar. Estudar uma tecnologia tão latente e nova trouxe "
                        "desafios extras, mas ao mesmo tempo diferenciais competitivos em nossos currículos, logo "
                        "no início de nossas carreiras. Habilidades de aprendizado, gestão de equipe, resolução "
                        "de conflitos, entendimento de viabilidade de projetos e tomada de decisão, eram "
                        "desenvolvidas a cada dia. Hoje posso falar que a entidade teve papel fundamental em meu "
                        "desenvolvimento profissional e na posição que ocupo hoje.",
                        "/joao.jpeg",
                        "João P. J. M. Perpetuo",
                        "Co-fundador e Ex-membro",
                    ),
                    style={
                        "display": "grid",
                        "grid_template_columns": rx.breakpoints(
                            initial="1fr", md="repeat(3, 1fr)"
                        ),
                        "gap": "2.5rem",
                        "width": "100%",
                    },
                ),
                style={
                    "spacing": "3rem",
                    "width": "100%",
                },
            ),
            style={
                "max_width": "80rem",  # Equivalente ao 7xl do Chakra
                "padding_y": "4rem",
                "margin": "0 auto",
                "width": "100%",
            },
        ),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(
                light="rgb(243, 244, 246)",  # gray-100
                dark="rgb(55, 65, 81)",  # gray-700
            ),
        },
    )
