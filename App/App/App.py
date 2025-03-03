"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from pages.Home import home
from pages.ProcessoSeletivo import processo_seletivo
from pages.MembrosAtuais import membros_atuais
from pages.MembrosAlumni import membros_alumni
from pages.Areas import nucleos
from pages.Projetos import projetos
from pages.Fundo import fundo
from pages.Parcerias import parceiros
from pages.Aprenda import aprenda
from pages.Contato import contato

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    ),
)
app.add_page(home, route="/")
app.add_page(processo_seletivo, route="/ps")
app.add_page(membros_atuais, route="/members/actual")
app.add_page(membros_alumni, route="/members/alumni")
app.add_page(nucleos, route="/areas")
app.add_page(projetos, route="/projects")
app.add_page(fundo, route="/fund")
app.add_page(parceiros, route="/partnerships")
app.add_page(aprenda, route="/learn")
app.add_page(contato, route="/contact")
