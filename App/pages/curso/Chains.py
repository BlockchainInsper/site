import reflex as rx
from App.Template import template
from components.curso_intro.Materiais import materiais
from components.curso_intro.Videos import videos

# Dados para materiais e vídeos
materiais1 = [
    {
        "nome": "Path for Network Adoption",
        "link": "https://www.coindesk.com/state-of-lightning-whats-the-path-for-network-adoption-in-2019",
    }
]

videos1 = [
    {"link": "https://www.youtube.com/embed/rrr_zPmEiME"},
    {"link": "https://www.youtube.com/embed/pBh4DcM-0pg"},
    {"link": "https://www.youtube.com/embed/8zVzw912wPo"},
    {"link": "https://www.youtube.com/embed/c4TjfaLgzj4"},
]

videos2 = [
    {"link": "https://www.youtube.com/embed/ctzGr58_jeI"},
    {"link": "https://www.youtube.com/embed/XW0QZmtbjvs"},
]

materiais3 = [
    {
        "nome": "Binance Smart Chain: a blockchain que pode roubar o trono da Ethereum",
        "link": "https://esportes.yahoo.com/noticias/binance-smart-chain-blockchain-que-141600097.html",
    }
]

videos3 = [
    {"link": "https://www.youtube.com/embed/iJDoc0kvXLc"},
    {"link": "https://www.youtube.com/embed/pA2SZmqZeRc"},
]

materiais4 = [{"nome": "Chainlink", "link": "https://chain.link/solutions"}]

videos4 = [
    {"link": "https://www.youtube.com/embed/tIUHQ7sDoaU"},
    {"link": "https://www.youtube.com/embed/lRba55HTK0Q"},
    {"link": "https://www.youtube.com/embed/TPXTmVdlyoc"},
]

videos5 = [
    {"link": "https://www.youtube.com/embed/Do8rHvr65ZA"},
    {"link": "https://www.youtube.com/embed/Elwv7Itr1qA"},
    {"link": "https://www.youtube.com/embed/Z2JlxAz3Mvg"},
    {"link": "https://www.youtube.com/embed/FKh8hjJNhWc"},
]

videos6 = [
    {"link": "https://www.youtube.com/embed/IijtdpAtOt0"},
    {"link": "https://www.youtube.com/embed/f7F67ZP9fsE"},
]

videos7 = [
    {"link": "https://www.youtube.com/embed/JeJzwZgxF50"},
]


@rx.page(route="/learn/curso-intro/chains", title="Blockchain Insper")
@template
def chains():
    return rx.box(
        materiais(materiais1, "Bitcoin Lightning Network"),
        videos(videos1, "Bitcoin Lightning Network: Vídeos"),
        videos(videos2, "Ethereum 2: Vídeos"),
        materiais(materiais3, "Binance Smart Chain"),
        videos(videos3, "Binance Smart Chain: Vídeos"),
        materiais(materiais4, "Chainlink"),
        videos(videos4, "Chainlink: Vídeos"),
        videos(videos5, "Cardano: Vídeos"),
        videos(videos6, "Polygon: Vídeos"),
        videos(videos7, "Outras soluções de escalabilidade e privacidade: Vídeos"),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
