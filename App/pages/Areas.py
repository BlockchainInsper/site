import reflex as rx
from App.Template import template


# Definição dos ícones SVG para reutilização
def business_icon():
    return rx.el.svg(
        rx.el.a(
            rx.el.svg.path(d="M11,44H9c-0.6,0-1-0.4-1-1v-2h4v2C12,43.6,11.6,44,11,44z"),
            rx.el.svg.path(
                d="M39,44h-2c-0.6,0-1-0.4-1-1v-2h4v2C40,43.6,39.6,44,39,44z"
            ),
            fill="#263238",
        ),
        rx.el.svg.path(
            fill="#37474F",
            d="M27,7h-6c-1.7,0-3,1.3-3,3v3h2v-3c0-0.6,0.4-1,1-1h6c0.6,0,1,0.4,1,1v3h2v-3C30,8.3,28.7,7,27,7z",
        ),
        rx.el.svg.path(
            fill="#78909C",
            d="M40,43H8c-2.2,0-4-1.8-4-4V15c0-2.2,1.8-4,4-4h32c2.2,0,4,1.8,4,4v24C44,41.2,42.2,43,40,43z",
        ),
        stroke="currentColor",
        fill="currentColor",
        stroke_width="0",
        version="1",
        viewbox="0 0 48 48",
        enable_background="new 0 0 48 48",
        focusable="false",
        style={
            "width": "50px",
            "height": "50px",
            "color": rx.color_mode_cond(light="#0B69FF", dark="#63B3ED"),
        },
    )


def finance_icon():
    return rx.el.svg(
        rx.el.a(
            rx.el.svg.rect(x="38", y="4", width="2", height="20"),
            rx.el.svg.rect(x="15", y="7", width="2", height="17"),
            rx.el.svg.rect(x="8", y="27", width="2", height="17"),
            rx.el.svg.rect(x="28", y="19", width="2", height="22"),
            fill="#546E7A",
        ),
        rx.el.svg.path(
            fill="#4CAF50",
            d="M36,7h6c1.1,0,2,0.9,2,2v10c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2V9C34,7.9,34.9,7,36,7z",
        ),
        rx.el.svg.path(
            fill="#4CAF50",
            d="M13,10h6c1.1,0,2,0.9,2,2v7c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2v-7C11,10.9,11.9,10,13,10z",
        ),
        rx.el.svg.path(
            fill="#F44336",
            d="M6,30h6c1.1,0,2,0.9,2,2v7c0,1.1-0.9,2-2,2H6c-1.1,0-2-0.9-2-2v-7C4,30.9,4.9,30,6,30z",
        ),
        rx.el.svg.path(
            fill="#F44336",
            d="M26,22h6c1.1,0,2,0.9,2,2v12c0,1.1-0.9,2-2,2h-6c-1.1,0-2-0.9-2-2V24C24,22.9,24.9,22,26,22z",
        ),
        stroke="currentColor",
        fill="currentColor",
        stroke_width="0",
        version="1",
        viewbox="0 0 48 48",
        enable_background="new 0 0 48 48",
        focusable="false",
        style={
            "width": "50px",
            "height": "50px",
            "color": rx.color_mode_cond(light="#0B69FF", dark="#63B3ED"),
        },
    )


def tech_icon():
    return rx.el.svg(
        rx.el.a(
            rx.el.svg.rect(
                width="36", height="28", x="6", y="6", fill="currentColor", rx="3"
            ),
            rx.el.svg.path(stroke_linecap="round", d="M14 42h20m-10-8v8"),
            fill="none",
            stroke="currentColor",
            stroke_linejoin="round",
            stroke_width="4",
        ),
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 48 48",
        style={
            "width": "50px",
            "height": "50px",
            "color": rx.color_mode_cond(
                light="#1A202C", dark="rgba(255, 255, 255, 0.92)"
            ),
        },
    )


# Função para criar uma área com ícone e descrição
def area_box(icon, title, description):
    return rx.flex(
        # Layout vertical com centralização
        rx.vstack(
            # Ícone centralizado no topo
            icon,
            # Heading centralizado
            rx.heading(
                title,
                as_="h2",
                style={
                    "font_size": "2rem",  # Tamanho ajustado para evitar overflow
                    "font_weight": "bold",
                    "margin_top": "0.75rem",  # Reduzido para economizar espaço vertical
                    "margin_bottom": "0.5rem",  # Reduzido para economizar espaço
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                    "text_align": "center",
                },
            ),
            # Texto centralizado abaixo
            rx.text(
                description,
                style={
                    "color": rx.color_mode_cond(light="gray.600", dark="gray.300"),
                    "text_align": "center",
                    "max_width": "500px",
                    "line_height": "1.4",  # Reduzido para economizar espaço vertical
                    "font_size": "0.95rem",  # Tamanho levemente reduzido
                },
            ),
            # Configuração do vstack
            style={
                "align_items": "center",
                "width": "100%",
                "justify_content": "center",
                "padding": "1rem",  # Reduzido para economizar espaço
                "gap": "0.5rem",  # Espaço reduzido entre elementos
            },
        ),
        # Configuração do flex container
        style={
            "width": "100%",
            # Ajustado para garantir que caiba com a navbar e footer
            "height": "calc((100vh - 220px) / 3)",  # Considera espaço para navbar e footer
            "justify_content": "center",
            "align_items": "center",
            "border_bottom": rx.color_mode_cond(
                light="1px solid rgba(0,0,0,0.1)",
                dark="1px solid rgba(255,255,255,0.1)",
            ),
            "transition": "background-color 0.2s",
            "_hover": {
                "background": rx.color_mode_cond(
                    light="rgba(0,0,0,0.02)", dark="rgba(255,255,255,0.02)"
                )
            },
        },
    )


@rx.page(route="/areas")
@template
def nucleos():
    return rx.box(
        # Contêiner principal que ocupa toda a altura disponível
        rx.vstack(
            area_box(
                business_icon(),
                "Business",
                "Estudo das aplicações da tecnologia blockchain, atuações nas diversas áreas e empresas e elaboração de possíveis real cases.",
            ),
            area_box(
                finance_icon(),
                "Finance",
                "Estudo do mercado de criptoativos, tecnologia blockchain no mercado financeiro e possíveis estratégias elaboradas.",
            ),
            area_box(
                tech_icon(),
                "Tech",
                "Estudo da tecnologia blockchain na parte técnica, smart-contracts, dApps, softwares e criptografia.",
            ),
            style={
                "width": "100%",
                "height": "calc(100vh - 220px)",  # Altura exata considerando navbar e footer
                "align_items": "stretch",
                "spacing": "0",
                "padding": "0",
                "margin": "0",
                "overflow_y": "hidden",  # Impede scroll vertical
            },
        ),
        style={
            "width": "100%",
            "max_width": "100%",
            "overflow": "hidden",  # Impede qualquer scroll
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            "padding": "0",
            "margin": "0",
            "height": "calc(100vh - 220px)",  # Altura exata considerando navbar e footer
        },
    )
