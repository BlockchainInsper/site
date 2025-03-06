import reflex as rx
from Models import Contact


class ContactFormState(rx.State):
    @rx.event
    def handle_submit(self, form_data: dict):
        with rx.session() as session:
            contact = Contact(
                name=form_data["name"],
                email=form_data["email"],
                subject=form_data["subject"],
                message=form_data["message"],
            )
            session.add(contact)
            session.commit()
