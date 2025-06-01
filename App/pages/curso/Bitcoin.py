import reflex as rx
from App.Template import template
from components.curso_intro.Materiais import materiais
from components.curso_intro.Videos import videos

# Dados para materiais e vídeos
materiais1 = [
    {
        "nome": "What is Bitcoin?",
        "link": "https://www.investopedia.com/terms/b/bitcoin.asp",
    },
    {
        "nome": "Bitcoin and the Rise of the Cypherpunks - CoinDesk",
        "link": "https://www.coindesk.com/the-rise-of-the-cypherpunks/",
    },
    {
        "nome": "What is the Genesis Block in Bitcoin Terms?",
        "link": "https://www.investopedia.com/news/what-genesis-block-bitcoin-terms/",
    },
    {
        "nome": "Bitcoin X Gold X US Dollar",
        "link": "https://www.fool.com/investing/2017/08/17/how-does-bitcoins-market-cap-stack-up-next-to-gold.aspx",
    },
    {"nome": "Bitcoin White-Paper", "link": "https://bitcoin.org/bitcoin.pdf"},
]

videos1 = [
    {"link": "https://www.youtube.com/embed/Ur037LYsb8M"},
    {"link": "https://www.youtube.com/embed/Lx9zgZCMqXE"},
]

materiais2 = [
    {
        "nome": "Byzantine Generals Problem Explained",
        "link": "https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419",
    },
    {
        "nome": "What is Double Spending & How Does Bitcoin Handle It?",
        "link": "https://coinsutra.com/bitcoin-double-spending/",
    },
    {
        "nome": "Bitcoin Transaction Inputs and Outputs?",
        "link": "https://www.cryptocompare.com/mining/guides/bitcoin-transaction-inputs-and-outputs/",
    },
]

videos2 = [
    {"link": "https://www.youtube.com/embed/DhYegGIS3do"},
    {"link": "https://www.youtube.com/embed/cOc7V64HUDQ"},
    {"link": "https://www.youtube.com/embed/q5GWwTgRIT4"},
]

materiais3 = [
    {
        "nome": "What Is a Blockchain Consensus Algorithm?",
        "link": "https://academy.binance.com/en/articles/what-is-a-blockchain-consensus-algorithm",
    },
    {
        "nome": "Proof of Work",
        "link": "https://tokens-economy.gitbook.io/consensus/chain-based-proof-of-work/proof-of-work-pow-1",
    },
    {
        "nome": "Bitcoin Hash Functions Explained - CoinDesk",
        "link": "https://www.coindesk.com/bitcoin-hash-functions-explained/",
    },
    {
        "nome": "Bitcoin: Cryptographic hash functions",
        "link": "https://www.khanacademy.org/economics-finance-domain/core-finance/money-and-banking/bitcoin/v/bitcoin-cryptographic-hash-function",
    },
    {
        "nome": "Bitcoin: Digital signatures",
        "link": "https://pt.khanacademy.org/economics-finance-domain/core-finance/money-and-banking/bitcoin/v/bitcoin-digital-signatures",
    },
]

videos3 = [
    {"link": "https://www.youtube.com/embed/9V1bipPkCTU"},
    {"link": "https://www.youtube.com/embed/UAQniUSL2Lo"},
]

materiais4 = [
    {
        "nome": "Bitcoin Wallets for Beginners: Everything You Need to Know",
        "link": "https://cointelegraph.com/bitcoin-for-beginners/what-is-bitcoin-wallets",
    },
    {
        "nome": "A melhor Wallet para você",
        "link": "https://bitcoin.org/en/choose-your-wallet",
    },
    {
        "nome": "Explaining public-key cryptography to non-geeks – Panayotis Vryonis – Medium",
        "link": "https://medium.com/@vrypan/explaining-public-key-cryptography-to-non-geeks-f0994b3c2d5",
    },
    {
        "nome": "What is a Bitcoin wallet and Bitcoin address - Bitcoin Whiteboard Tuesday #3",
        "link": "https://steemit.com/wallet/@omerhar206/662exr-how-digital-signatures-work-on-the-cryptocurrency-wallets",
    },
]

materiais5 = [
    {
        "nome": "What a Bitcoin Fork is",
        "link": "http://news.bitcoin.com/a-guide-to-what-a-bitcoin-fork-is-and-why-they-happen/",
    },
    {
        "nome": "The Great Bitcoin Scaling Debate — A Timeline – Hacker Noon",
        "link": "https://hackernoon.com/the-great-bitcoin-scaling-debate-a-timeline-6108081dbada",
    },
]

videos5 = [
    {"link": "https://www.youtube.com/embed/pdaXY1OOiWQ"},
    {"link": "https://www.youtube.com/embed/XCo6yyutYAM"},
]

materiais6 = [
    {
        "nome": "O que é o Halving do Bitcoin e como ele afeta o mercado",
        "link": "https://www.infomoney.com.br/mercados/o-que-e-o-halving-do-bitcoin-e-como-ele-afeta-o-mercado-da-criptomoeda/",
    },
    {
        "nome": "Bitcoin Halving",
        "link": "https://www.investopedia.com/bitcoin-halving-4843769",
    },
    {
        "nome": "What Happens to Bitcoin After All 21 Million Are Mined?",
        "link": "https://www.investopedia.com/tech/what-happens-bitcoin-after-21-million-mined/",
    },
]

materiais7 = [
    {
        "nome": "Mastering Bitcoin 2nd Edition",
        "link": "https://unglueit-files.s3.amazonaws.com/ebf/05db7df4f31840f0a873d6ea14dcc28d.pdf",
    },
    {"nome": "BitcoinBook", "link": "https://github.com/bitcoinbook/bitcoinbook"},
    {
        "nome": "Bitcoin para Programadores",
        "link": "https://itsrio.org/wp-content/uploads/2018/06/bitcoin-para-programadores.pdf",
    },
    {
        "nome": "Bitcoin and Cryptocurrency Technologies - Princeton",
        "link": "https://www.coursera.org/learn/cryptocurrency?ranMID=40328&ranEAID=SAyYsTvLiGQ&ranSiteID=SAyYsTvLiGQ-7F1vKwRzA9FOUjjF.CFkCw&siteID=SAyYsTvLiGQ-7F1vKwRzA9FOUjjF.CFkCw&utm_content=10&utm_medium=partners&utm_source=linkshare&utm_campaign=SAyYsTvLiGQ",
    },
    {
        "nome": "Bitcoin and Cryptocurrency Technologies - Free Online Course",
        "link": "https://www.classcentral.com/course/bitcointech-3655?utm_source=fcc_medium&utm_medium=web&utm_campaign=ivy_league_courses_2020",
    },
    {
        "nome": "Bitcoin and Cryptocurrencies",
        "link": "https://www.edx.org/course/bitcoin-and-cryptocurrencies",
    },
]


@template
def bitcoin():
    return rx.box(
        materiais(materiais1, "Introdução e História"),
        videos(videos1, "Introdução e História: Vídeos"),
        materiais(materiais2, "Problema do Gasto Duplo"),
        videos(videos2, "Problema do Gasto Duplo: Vídeos"),
        materiais(materiais3, "Protocolo de Consenso (Proof of Work)"),
        videos(videos3, "Protocolo de Consenso (Proof of Work): Vídeos"),
        materiais(materiais4, "O que são Wallets?"),
        materiais(materiais5, "O que são Forks e como funcionam?"),
        videos(videos5, "O que são Forks e como funcionam?: Vídeos"),
        materiais(materiais6, "O que é o Halving e quando ele ocorre?"),
        materiais(materiais7, "Livros e Cursos"),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
