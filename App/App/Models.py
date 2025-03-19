import reflex as rx


class Contact(rx.Model, table=True):
    name: str
    email: str
    subject: str
    message: str
