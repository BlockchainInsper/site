import reflex as rx
from App.Models import Contact


class ContactFormState(rx.State):
    # Defina as variáveis de estado para armazenar os valores do formulário
    name: str = ""
    email: str = ""
    subject: str = ""  # Certifique-se de que esta variável existe
    message: str = ""

    @rx.event(background=True)
    async def handle_submit(self, form_data: dict):
        with rx.session() as session:
            contact = Contact(
                name=form_data["name"],
                email=form_data["email"],
                subject=form_data["subject"],
                message=form_data["message"],
            )
            session.add(contact)
            session.commit()
            return rx.window_alert("Mensagem enviada! Entraremos em contato em breve.")
