import reflex as rx
from App.Template import template
from components.curso_intro.Materiais import materiais
from components.curso_intro.Videos import videos

# Dados para as seções de material
materiais1 = [
    {
        "nome": "Symmetric vs Asymmetric encryption",
        "link": "https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences",
    }
]

materiais2 = [
    {
        "nome": "Explaining public-key cryptography to non-geeks",
        "link": "https://medium.com/@vrypan/explaining-public-key-cryptography-to-non-geeks-f0994b3c2d5",
    }
]

videos2 = [
    {"link": "https://www.youtube.com/embed/AQDCe585Lnc"},
    {"link": "https://www.youtube.com/embed/GSTiKjnBaes"},
    {"link": "https://www.youtube.com/embed/GSIDS_lvRv4"},
    {"link": "https://www.youtube.com/embed/vsXMMT2CqqE"},
    {"link": "https://www.youtube.com/embed/pgzWxOtk1zg"},
    {"link": "https://www.youtube.com/embed/dut9EnbFym0"},
]


videos3 = [
    {"link": "https://www.youtube.com/embed/s22eJ1eVLTU"},
    {"link": "https://www.youtube.com/embed/Aq3a-_O2NcI"},
]

materiais4 = [
    {
        "nome": "Understanding Bitcoin Market Participants – Vulnerabilities in the Price of Bitcoin Driven by Miners",
        "link": "https://www.blockwaresolutions.com/research-and-publications/2020-halving-analysis",
    }
]

videos4 = [
    {"link": "https://www.youtube.com/embed/d4xXJh677J0"},
    {"link": "https://www.youtube.com/embed/L-Qhv8kLESY"},
]

materiais5 = [
    {
        "nome": "Why is Diffie-Hellman considered in the context of public key cryptography?",
        "link": "https://crypto.stackexchange.com/questions/6307/why-is-diffie-hellman-considered-in-the-context-of-public-key-cryptography",
    }
]

videos5 = [
    {"link": "https://www.youtube.com/embed/NmM9HA2MQGI"},
    {"link": "https://www.youtube.com/embed/Yjrfm_oRO0w"},
]

materiais6 = [
    {
        "nome": "Cryptographic Hash Function",
        "link": "https://www.lifewire.com/cryptographic-hash-function-2625832",
    }
]

videos6 = [
    {"link": "https://www.youtube.com/embed/DMtFhACPnTY"},
    {"link": "https://www.youtube.com/embed/b4b8ktEV4Bg"},
    {"link": "https://www.youtube.com/embed/S9JGmA5_unY"},
    {"link": "https://www.youtube.com/embed/8ZtInClXe1Q"},
    {"link": "https://www.youtube.com/embed/0WiTaBI82Mc"},
]

videos7 = [
    {"link": "https://www.youtube.com/embed/JD72Ry60eP4"},
]

materiais8 = [
    {
        "nome": "What is the math behind elliptic curve cryptography?",
        "link": "https://hackernoon.com/what-is-the-math-behind-elliptic-curve-cryptography-f61b25253da3",
    }
]

videos8 = [
    {"link": "https://www.youtube.com/embed/NF1pwjL9-DE"},
    {"link": "https://www.youtube.com/embed/nybVFJVXbww"},
    {"link": "https://www.youtube.com/embed/dCvB-mhkT0w"},
]

videos9 = [
    {"link": "https://www.youtube.com/embed/O4xNJsjtN6E"},
]

materiais10 = [
    {
        "nome": "Myths about /dev/urandom",
        "link": "https://www.2uo.de/myths-about-urandom/",
    }
]

videos10 = [
    {"link": "https://www.youtube.com/embed/SxP30euw3-0"},
    {"link": "https://www.youtube.com/embed/LDPMpc-ENqY"},
]

materiais11 = [
    {
        "nome": "O efeito da supremacia quântica no futuro da criptografia",
        "link": "https://medium.com/brunoartc/o-efeito-da-supremacia-qu%C3%A2ntica-no-futuro-da-criptografia-cd00dc049d5b",
    }
]

videos11 = [
    {"link": "https://www.youtube.com/embed/MjwXDuuMW0s"},
    {"link": "https://www.youtube.com/embed/hbiKHELmzuc"},
]

videos12 = [
    {"link": "https://www.youtube.com/embed/MVPvrGbBKF8"},
]


@rx.page(route="/learn/curso-intro/tecnologia")
@template
def tecnologia():
    return rx.box(
        # Criptografia simétrica
        materiais(materiais1, "Criptografia simétrica"),
        # Criptografia assimétrica
        materiais(materiais2, "Criptografia assimétrica"),
        videos(videos2, "Criptografia assimétrica: Vídeos"),
        # Assinaturas Digitais
        videos(videos3, "Assinaturas Digitais: Vídeos"),
        # Consenso
        materiais(materiais4, "Consenso"),
        videos(videos4, "Consenso: Vídeos"),
        # Diffie-Hellman
        materiais(materiais5, "Diffie-Hellman"),
        videos(videos5, "Diffie-Hellman: Vídeos"),
        # Hash functions
        materiais(materiais6, "Hash functions"),
        videos(videos6, "Hash functions: Vídeos"),
        # RSA
        videos(videos7, "RSA: Vídeos"),
        # Curvas elípticas
        materiais(materiais8, "Curvas elípticas (ECC)"),
        videos(videos8, "Curvas elípticas (ECC): Vídeos"),
        # AES
        videos(videos9, "AES: Vídeos"),
        # Pseudo-random / random
        materiais(materiais10, "Pseudo-random / random"),
        videos(videos10, "Pseudo-random / random: Vídeos"),
        # Criptografia Quântica
        materiais(materiais11, "Criptografia Quântica"),
        videos(videos11, "Criptografia Quântica: Vídeos"),
        # Aula Tech Blockchain Insper
        videos(videos12, "Aula Tech Blockchain Insper 2020.2"),
        style={
            "width": "100%",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
