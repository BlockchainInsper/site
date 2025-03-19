import reflex as rx


def bitcoin_icon(size, size_html):
    bitcoin_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 512 512">
                <path fill="currentColor" d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256S119.033 8 256 8s248 111.033 248 248m-141.651-35.33c4.937-32.999-20.191-50.739-54.55-62.573l11.146-44.702l-27.213-6.781l-10.851 43.524c-7.154-1.783-14.502-3.464-21.803-5.13l10.929-43.81l-27.198-6.781l-11.153 44.686c-5.922-1.349-11.735-2.682-17.377-4.084l.031-.14l-37.53-9.37l-7.239 29.062s20.191 4.627 19.765 4.913c11.022 2.751 13.014 10.044 12.68 15.825l-12.696 50.925c.76.194 1.744.473 2.829.907c-.907-.225-1.876-.473-2.876-.713l-17.796 71.338c-1.349 3.348-4.767 8.37-12.471 6.464c.271.395-19.78-4.937-19.78-4.937l-13.51 31.147l35.414 8.827c6.588 1.651 13.045 3.379 19.4 5.006l-11.262 45.213l27.182 6.781l11.153-44.733a1038 1038 0 0 0 21.687 5.627l-11.115 44.523l27.213 6.781l11.262-45.128c46.404 8.781 81.299 5.239 95.986-36.727c11.836-33.79-.589-53.281-25.004-65.991c17.78-4.098 31.174-15.792 34.747-39.949m-62.177 87.179c-8.41 33.79-65.308 15.523-83.755 10.943l14.944-59.899c18.446 4.603 77.6 13.717 68.811 48.956m8.417-87.667c-7.673 30.736-55.031 15.12-70.393 11.292l13.548-54.327c15.363 3.828 64.836 10.973 56.845 43.035" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return bitcoin_svg


def money_icon(size, size_html):
    money_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 512 512">
                <path fill="currentColor" d="M327.027 65.816L229.79 128.23l9.856 5.397l86.51-55.53l146.735 83.116l-84.165 54.023l4.1 2.244v6.848l65.923-42.316l13.836 7.838l-79.76 51.195v11.723l64.633-41.487l15.127 8.57l-79.76 51.195v11.723l64.633-41.487l15.127 8.57l-79.76 51.195v11.723l100.033-64.21l-24.828-14.062l24.827-15.937l-24.828-14.064l24.827-15.937l-23.537-13.333l23.842-15.305zm31.067 44.74c-21.038 10.556-49.06 12.342-68.79 4.383l-38.57 24.757l126.903 69.47l36.582-23.48c-14.41-11.376-13.21-28.35 2.942-41.67zM227.504 147.5l-70.688 46.094l135.61 78.066l1.33-.85c2.5-1.61 6.03-3.89 10.242-6.613c8.42-5.443 19.563-12.66 30.674-19.86c16.002-10.37 24.248-15.72 31.916-20.694zm115.467 1.17a8.583 14.437 82.068 0 1 .003 0a8.583 14.437 82.068 0 1 8.32 1.945a8.583 14.437 82.068 0 1-.87 12.282a8.583 14.437 82.068 0 1-20.273 1.29a8.583 14.437 82.068 0 1 .87-12.28a8.583 14.437 82.068 0 1 11.95-3.237m-218.423 47.115L19.143 263.44l23.537 13.333l-23.842 15.305l24.828 14.063l-24.828 15.938l24.828 14.063l-24.828 15.938l166.135 94.106L285.277 381.8v-11.72l-99.433 63.824L39.11 350.787l14.255-9.15l131.608 74.547L285.277 351.8v-11.72l-99.433 63.824L39.11 320.787l14.255-9.15l131.608 74.547L285.277 321.8v-11.72l-99.433 63.824L39.11 290.787l13.27-8.52l132.9 75.28l99.997-64.188v-5.05l-5.48-3.154l-93.65 60.11l-146.73-83.116l94.76-60.824l-9.63-5.543zm20.46 11.78l-46.92 30.115c14.41 11.374 13.21 28.348-2.942 41.67l59.068 33.46c21.037-10.557 49.057-12.342 68.787-4.384l45.965-29.504l-123.96-71.358zm229.817 32.19c-8.044 5.217-15.138 9.822-30.363 19.688a36222 36222 0 0 1-30.69 19.873c-4.217 2.725-7.755 5.01-10.278 6.632c-.09.06-.127.08-.215.137v85.924l71.547-48.088zm-200.99 17.48a8.583 14.437 82.068 0 1 8.32 1.947a8.583 14.437 82.068 0 1-.87 12.28a8.583 14.437 82.068 0 1-20.27 1.29a8.583 14.437 82.068 0 1 .87-12.28a8.583 14.437 82.068 0 1 11.95-3.236z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return money_svg


def stock_icon(size, size_html):
    stock_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 16 16">
                <path fill="none" stroke="currentColor" stroke-linejoin="round" d="M1.583 4.5L8 1.583L14.417 4.5m-12.834 0L8 7.417M1.583 4.5v6.417L8 14.417m0-7L14.417 4.5M8 7.417v7M14.417 4.5v6.417L8 14.417M10.5 13V9.5m2 2.5V8.5" stroke-width="1" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return stock_svg


def idea_icon(size, size_html):
    idea_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 48 48">
                <circle cx="24" cy="22" r="20" fill="#fff59d" stroke-width="1" stroke="#fff59d" />
                <path fill="#fbc02d" d="M37 22c0-7.7-6.6-13.8-14.5-12.9c-6 .7-10.8 5.5-11.4 11.5c-.5 4.6 1.4 8.7 4.6 11.3c1.4 1.2 2.3 2.9 2.3 4.8v.3h12v-.1c0-1.8.8-3.6 2.2-4.8c2.9-2.4 4.8-6 4.8-10.1" stroke-width="1" stroke="#fbc02d" />
                <path fill="#fff59d" d="m30.6 20.2l-3-2c-.3-.2-.8-.2-1.1 0L24 19.8l-2.4-1.6c-.3-.2-.8-.2-1.1 0l-3 2c-.2.2-.4.4-.4.7s0 .6.2.8l3.8 4.7V37h2V26c0-.2-.1-.4-.2-.6l-3.3-4.1l1.5-1l2.4 1.6c.3.2.8.2 1.1 0l2.4-1.6l1.5 1l-3.3 4.1c-.1.2-.2.4-.2.6v11h2V26.4l3.8-4.7c.2-.2.3-.5.2-.8s-.2-.6-.4-.7" stroke-width="1" stroke="#fff59d" />
                <circle cx="24" cy="44" r="3" fill="#5c6bc0" stroke-width="1" stroke="#5c6bc0" />
                <path fill="#9fa8da" d="M26 45h-4c-2.2 0-4-1.8-4-4v-5h12v5c0 2.2-1.8 4-4 4" stroke-width="1" stroke="#9fa8da" />
                <path fill="#5c6bc0" d="m30 41l-11.6 1.6c.3.7.9 1.4 1.6 1.8l9.4-1.3q.6-.9.6-2.1m-12-2.3v2L30 39v-2z" stroke-width="1" stroke="#5c6bc0" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return idea_svg


def collaboration_icon(size, size_html):
    collaboration_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 48 48">
                <path fill="#1565c0" d="M25 22h13l6 6V11c0-2.2-1.8-4-4-4H25c-2.2 0-4 1.8-4 4v7c0 2.2 1.8 4 4 4" stroke-width="1" stroke="#1565c0" />
                <path fill="#2196f3" d="M23 19H10l-6 6V8c0-2.2 1.8-4 4-4h15c2.2 0 4 1.8 4 4v7c0 2.2-1.8 4-4 4" stroke-width="1" stroke="#2196f3" />
                <g fill="#ffa726" stroke-width="1" stroke="#ffa726">
                    <circle cx="12" cy="31" r="5" />
                    <circle cx="36" cy="31" r="5" />
                </g>
                <path fill="#607d8b" d="M20 42s-2.2-4-8-4s-8 4-8 4v2h16zm24 0s-2.2-4-8-4s-8 4-8 4v2h16z" stroke-width="1" stroke="#607d8b" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return collaboration_svg


def businessman_icon(size, size_html):
    businessman_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 48 48">
                <path fill="#ff9800" d="m24 37l-5-6v-6h10v6z" stroke-width="1" stroke="#ff9800" />
                <g fill="#ffa726" stroke-width="1" stroke="#ffa726">
                    <circle cx="33" cy="19" r="2" />
                    <circle cx="15" cy="19" r="2" />
                </g>
                <path fill="#ffb74d" d="M33 13c0-7.6-18-5-18 0v7c0 5 4 9 9 9s9-4 9-9z" stroke-width="1" stroke="#ffb74d" />
                <path fill="#424242" d="M24 4c-6.1 0-10 4.9-10 11v2.3l2 1.7v-5l12-4l4 4v5l2-1.7V15c0-4-1-8-6-9l-1-2z" stroke-width="1" stroke="#424242" />
                <g fill="#784719" stroke-width="1" stroke="#784719">
                    <circle cx="28" cy="19" r="1" />
                    <circle cx="20" cy="19" r="1" />
                </g>
                <path fill="#fff" d="m24 43l-5-12l5 1l5-1z" stroke-width="1" stroke="#fff" />
                <path fill="#d32f2f" d="m23 35l-.7 4.5l1.7 4l1.7-4L25 35l1-1l-2-2l-2 2z" stroke-width="1" stroke="#d32f2f" />
                <path fill="#546e7a" d="m29 31l-5 12l-5-12S8 33 8 44h32c0-11-11-13-11-13" stroke-width="1" stroke="#546e7a" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": f"{size}rem",
            "height": f"{size}rem",
        },
    )
    return businessman_svg


def building_icon(size, size_html):
    building_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 24 24">
                <path fill="currentColor" d="M17 11V3H7v4H3v14h8v-4h2v4h8V11zM7 19H5v-2h2zm0-4H5v-2h2zm0-4H5V9h2zm4 4H9v-2h2zm0-4H9V9h2zm0-4H9V5h2zm4 8h-2v-2h2zm0-4h-2V9h2zm0-4h-2V5h2zm4 12h-2v-2h2zm0-4h-2v-2h2z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": {size},  # w-10
            "height": {size},  # h-10
        },
    )
    return building_svg


def projects_icon(size, size_html):
    projects_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 1024 1024">
                <path fill="currentColor" d="M312.1 591.5c3.1 3.1 8.2 3.1 11.3 0l101.8-101.8l86.1 86.2c3.1 3.1 8.2 3.1 11.3 0l226.3-226.5c3.1-3.1 3.1-8.2 0-11.3l-36.8-36.8c-3.1-3.1-8.2-3.1-11.3 0L517 485.3l-86.1-86.2c-3.1-3.1-8.2-3.1-11.3 0L275.3 543.4c-3.1 3.1-3.1 8.2 0 11.3z" />
                <path fill="currentColor" d="M904 160H548V96c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H120c-17.7 0-32 14.3-32 32v520c0 17.7 14.3 32 32 32h356.4v32L311.6 884.1c-3.7 2.4-4.7 7.3-2.3 11l30.3 47.2v.1c2.4 3.7 7.4 4.7 11.1 2.3L512 838.9l161.3 105.8c3.7 2.4 8.7 1.4 11.1-2.3v-.1l30.3-47.2c2.4-3.7 1.3-8.6-2.3-11L548 776.3V744h356c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32m-40 512H160V232h704z" />
            </svg>""",
        style={
            "color": rx.color_mode_cond(
                light="#1A202C",
                dark="rgba(255, 255, 255, 0.92)",
            ),
            "width": {size},  # w-10
            "height": {size},  # h-10
        },
    )
    return projects_svg


def discord_icon(size, size_html):
    discord_svg = rx.html(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width={size_html} height={size_html} viewBox="0 0 24 24">
	<path fill="currentColor" d="M20.317 4.37a19.8 19.8 0 0 0-4.885-1.515a.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.3 18.3 0 0 0-5.487 0a13 13 0 0 0-.617-1.25a.08.08 0 0 0-.079-.037A19.7 19.7 0 0 0 3.677 4.37a.1.1 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.08.08 0 0 0 .031.057a19.9 19.9 0 0 0 5.993 3.03a.08.08 0 0 0 .084-.028a14 14 0 0 0 1.226-1.994a.076.076 0 0 0-.041-.106a13 13 0 0 1-1.872-.892a.077.077 0 0 1-.008-.128a10 10 0 0 0 .372-.292a.07.07 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.07.07 0 0 1 .078.01q.181.149.373.292a.077.077 0 0 1-.006.127a12.3 12.3 0 0 1-1.873.892a.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.08.08 0 0 0 .084.028a19.8 19.8 0 0 0 6.002-3.03a.08.08 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.06.06 0 0 0-.031-.03M8.02 15.33c-1.182 0-2.157-1.085-2.157-2.419c0-1.333.956-2.419 2.157-2.419c1.21 0 2.176 1.096 2.157 2.42c0 1.333-.956 2.418-2.157 2.418m7.975 0c-1.183 0-2.157-1.085-2.157-2.419c0-1.333.955-2.419 2.157-2.419c1.21 0 2.176 1.096 2.157 2.42c0 1.333-.946 2.418-2.157 2.418" stroke-width="0.5" stroke="currentColor" />
</svg>""",
        style={
            "width": {size},  # w-10
            "height": {size},  # h-10
        },
    )
    return discord_svg
