import reflex as rx
from App.Template import template
from components.curso_intro.Materiais import materiais
from components.curso_intro.Videos import videos

# Dados para os materiais
materiais_list = [
    {
        "nome": "Carta: Bitcoin by Satoshi Nakamoto",
        "link": "http://p2pfoundation.ning.com/forum/topics/bitcoin-open-source",
    },
    {"nome": "Documentário: Banking on Bitcoin", "link": "https://vimeo.com/226777744"},
]

# Dados para os vídeos
videos_list = [
    {"link": "https://www.youtube.com/embed/DyAufA2lWn0"},
    {"link": "https://www.youtube.com/embed/bBC-nXj3Ng4"},
]


@rx.page(route="/learn/curso-intro/introducao", title="Blockchain Insper")
@template
def introducao():
    return rx.box(
        videos(videos_list, "Introdução"),
        materiais(materiais_list, "Essenciais"),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
