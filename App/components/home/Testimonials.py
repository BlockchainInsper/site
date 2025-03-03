import reflex as rx


def testimonial_content(text):
    """Balão de depoimento com pseudo-elemento de triângulo."""
    return rx.box(
        rx.text(
            text,
            class_name="text-center text-gray-600 dark:text-gray-400 text-sm",
        ),
        class_name="bg-white dark:bg-gray-800 shadow-lg p-8 rounded-xl relative h-[320px] flex items-center justify-center after:content-[''] after:absolute after:w-0 after:h-0 after:border-l-[16px] after:border-l-transparent after:border-r-[16px] after:border-r-transparent after:border-t-[16px] after:border-t-white dark:after:border-t-gray-800 after:bottom-[-16px] after:left-1/2 after:-translate-x-1/2",
    )


def testimonial_avatar(src, name, title):
    """Avatar com nome e título do depoente."""
    return rx.box(
        # Box para centralizar o avatar
        rx.box(
            rx.avatar(
                src=src,
                alt=name,
                class_name="w-12 h-12",
            ),
            class_name="flex justify-center w-full",
        ),
        # Box para centralizar o nome
        rx.box(
            rx.text(
                name,
                class_name="font-semibold text-center",
            ),
            class_name="text-center w-full mt-2",
        ),
        # Box para centralizar o título
        rx.box(
            rx.text(
                title,
                class_name="text-sm text-gray-600 dark:text-gray-400",
            ),
            class_name="text-center w-full",
        ),
        class_name="mt-8 w-full",
    )


def testimonial(content, src, name, title):
    """Componente completo de um depoimento."""
    return rx.box(
        testimonial_content(content),
        testimonial_avatar(src, name, title),
        class_name="w-full",
    )


def testimonials():
    """Componente principal de depoimentos."""
    return rx.box(
        # Container principal
        rx.container(
            # Título centralizado
            rx.heading(
                "Depoimentos de nossos membros",
                class_name="text-3xl font-bold text-center mb-12",
            ),
            # Grid para os depoimentos
            rx.grid(
                # Depoimento 1
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
                # Depoimento 2
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
                # Depoimento 3
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
                # Grid responsivo - 1 coluna em mobile, 3 em desktop
                class_name="grid grid-cols-1 md:grid-cols-3 gap-10",
            ),
            class_name="w-full py-16 px-6",
        ),
        class_name="w-full bg-gray-100 dark:bg-gray-700",
    )
