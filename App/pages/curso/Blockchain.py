import reflex as rx
from App.Template import template
from components.curso_intro.Materiais import materiais
from components.curso_intro.Videos import videos

# Dados para materiais e vídeos
materiais1 = [
    {
        "nome": "What is Blockchain Technology? - IBM",
        "link": "https://www.ibm.com/br-pt/topics/what-is-blockchain",
    },
    {
        "nome": "How Does Blockchain Technology Work? - Investopedia",
        "link": "https://www.investopedia.com/terms/b/blockchain.asp",
    },
    {
        "nome": "Blockchain: One of History's Greatest Inventions?",
        "link": "https://www.investopedia.com/tech/blockchain-one-historys-greatest-inventions/",
    },
    {
        "nome": "Forget Bitcoin: Blockchain is the Future",
        "link": "https://www.investopedia.com/tech/forget-bitcoin-blockchain-future/",
    },
    {
        "nome": "Blockchain: entenda a tecnologia",
        "link": "https://epocanegocios.globo.com/Tecnologia/noticia/2019/01/blockchain-entenda-tecnologia-que-passa-fazer-parte-da-vida-de-empresas-governos-e-individuos.html?utm_source=facebook&utm_medium=social&utm_campaign=post",
    },
    {
        "nome": "On Public and Private Blockchains - Ethereum Blog",
        "link": "https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/",
    },
]

videos1 = [
    {"link": "https://www.youtube.com/embed/Pl8OlkkwRpc"},
    {"link": "https://www.youtube.com/embed/2iF73cybTBs"},
]

materiais2 = [
    {"nome": "IBM Hyperledger", "link": "https://www.ibm.com/br-pt/topics/hyperledger"},
    {
        "nome": "Hyperledger: um blockchain para empresas | Blockchain Insper",
        "link": "https://medium.com/blockchain-insper/hyperledger-um-blockchain-para-empresas-bf393dc6cedd",
    },
    {
        "nome": "Hyperledger: What is it, what's it good for, and wasn't it in Spaceballs?",
        "link": "https://medium.com/coinmonks/hyperledger-what-is-it-whats-it-good-for-and-wasn-t-it-in-spaceballs-522d8b3857c8",
    },
    {"nome": "Corda: Frictionless Commerce", "link": "https://www.corda.net/"},
    {
        "nome": "Hyperledger Vs Corda Vs Ethereum: The Ultimate Comparison",
        "link": "https://101blockchains.com/hyperledger-vs-corda-r3-vs-ethereum/",
    },
]

videos2 = [
    {"link": "https://www.youtube.com/embed/ZFC-5d9iUQ0"},
    {"link": "https://www.youtube.com/embed/oC5CasmGnJQ"},
]

materiais3 = [
    {
        "nome": "Ethereum, o protocolo que possibilitou ao blockchain voos mais altos",
        "link": "https://medium.com/blockchain-insper/o-protocolo-que-possibilitou-ao-blockchain-voos-mais-altos-de1407efd90c",
    },
    {
        "nome": "An Introduction to Ethereum and Smart Contracts: a Programmable Blockchain",
        "link": "https://auth0.com/blog/an-introduction-to-ethereum-and-smart-contracts-part-2/",
    },
    {
        "nome": "What is a dApp? Decentralized Application on the Blockchain",
        "link": "https://blockchainhub.net/decentralized-applications-dapps/",
    },
    {
        "nome": "O que são Smart-Contracts?",
        "link": "https://medium.com/mosaicouniversity/o-que-s%C3%A3o-smart-contracts-9d9e69d6377c",
    },
    {
        "nome": "What Are Dapps? The New Decentralized Future",
        "link": "https://blockgeeks.com/guides/dapps/",
    },
]


videos3 = [
    {"link": "https://www.youtube.com/embed/r0S4qIMf4Pg"},
    {"link": "https://www.youtube.com/embed/WSN5BaCzsbo"},
    {"link": "https://www.youtube.com/embed/pWGLtjG-F5c"},
    {"link": "https://www.youtube.com/embed/Yh8cHUB-KoU"},
    {"link": "https://www.youtube.com/embed/2jisWLxf38E"},
    {"link": "https://www.youtube.com/embed/MGemhK9t44Q"},
    {"link": "https://www.youtube.com/embed/3x1b_S6Qp2Q"},
]

materiais4 = [
    {
        "nome": "Proof of Work vs Proof of Stake",
        "link": "https://hackernoon.com/consensus-mechanisms-explained-pow-vs-pos-89951c66ae10",
    },
    {
        "nome": "Proof of Stake",
        "link": "https://tokens-economy.gitbook.io/consensus/chain-based-proof-of-stake/proof-of-stake-pos",
    },
]

videos4 = [
    {"link": "https://www.youtube.com/embed/aRiUG2UeUBc"},
]

materiais5 = [
    {
        "nome": "Eleições comprometidas? Entenda como as novas tecnologias podem impactá-las",
        "link": "https://medium.com/blockchain-insper/elei%C3%A7%C3%B5es-comprometidas-entenda-como-as-novas-tecnologias-podem-impact%C3%A1-las-1413b50d0e90",
    },
    {
        "nome": "Ecossistema brasileiro",
        "link": "https://guiadobitcoin.com.br/noticias/conheca-o-ecossistema-brasileiro-de-blockchain-e-criptomoedas/",
    },
    {
        "nome": "Crypto Thesis Open Financial Systems",
        "link": "https://medium.com/@PanteraCapital/a-crypto-thesis-47eaacf861ca",
    },
]

materiais6 = [
    {
        "nome": "Blockchain For Dummies - IBM",
        "link": "https://www.ibm.com/downloads/cas/36KBMBOG",
    },
    {
        "nome": "Blockchain Technology",
        "link": "https://www.edx.org/course/blockchain-technology",
    },
]


@rx.page(route="/learn/curso-intro/blockchain")
@template
def blockchain():
    return rx.box(
        materiais(materiais1, "Introdução"),
        videos(videos1, "Introdução: Vídeos"),
        materiais(materiais2, "Blockchain Público e Privado"),
        videos(videos2, "Blockchain Público e Privado: Vídeos"),
        materiais(materiais3, "Ethereum, Smart Contracts e dApps (decentralized apps)"),
        videos(
            videos3, "Ethereum, Smart Contracts e dApps (decentralized apps): Vídeos"
        ),
        materiais(materiais4, "Proof of Stake"),
        videos(videos4, "Proof of Stake: Vídeos"),
        materiais(materiais5, "Ecossistema - Blockchain/Crypto"),
        materiais(materiais6, "Livros e Cursos"),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
