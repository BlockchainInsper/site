"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from App.States import ContactFormState
from pages.Home import home
from pages.ProcessoSeletivo import processo_seletivo
from pages.MembrosAtuais import membros_atuais
from pages.MembrosAlumni import membros_alumni
from pages.Areas import nucleos
from pages.Projetos import projetos_page
from pages.Fundo import fundo
from pages.Parcerias import parceiros
from pages.Aprenda import aprenda
from pages.Contato import contato
from pages.CursoIntro import curso_intro
from pages.curso.Introducao import introducao
from pages.curso.Bitcoin import bitcoin
from pages.curso.Blockchain import blockchain
from pages.curso.CryptoAssets import crypto_assets
from pages.curso.Chains import chains
from pages.curso.Tecnologia import tecnologia

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
    style={
        "fontFamily": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'",
        "transitionProperty": "background-color",
        "transitionDuration": "200ms",
        "lineHeight": "1.5",
        "minHeight": "100vh",
    },
)
app.add_page(home, route="/")
app.add_page(processo_seletivo, route="/ps")
app.add_page(membros_atuais, route="/members/actual")
app.add_page(membros_alumni, route="/members/alumni")
app.add_page(nucleos, route="/areas")
app.add_page(projetos_page, route="/projects")
app.add_page(fundo, route="/fund")
app.add_page(parceiros, route="/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contato, route="/contact")
app.add_page(curso_intro, route="/learn/curso-intro")
app.add_page(introducao, route="/learn/curso-intro/introducao")
app.add_page(bitcoin, route="/learn/curso-intro/bitcoin")
app.add_page(blockchain, route="/learn/curso-intro/blockchain")
app.add_page(crypto_assets, route="/learn/curso-intro/crypto-assets")
app.add_page(chains, route="/learn/curso-intro/chains")
app.add_page(tecnologia, route="/learn/curso-intro/tecnologia")
