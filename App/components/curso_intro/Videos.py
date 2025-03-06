import reflex as rx


def videos(videos_list: list, titulo: str):
    return rx.container(
        rx.grid(
            rx.heading(
                titulo,
                style={
                    "font_weight": "bold",
                    "font_size": "1.875rem",
                    "color": rx.color_mode_cond(light="#2D3748", dark="#F7FAFC"),
                },
            ),
            rx.vstack(
                *[
                    rx.aspect_ratio(
                        rx.el.iframe(
                            title=f"Video {i + 1}",
                            alt="Bitcoin Video",
                            src=video.get("link", ""),
                            allow_full_screen=True,
                            style={
                                "border": "none",
                                "width": "100%",
                                "height": "100%",
                            },
                        ),
                        ratio=16 / 9,
                        style={
                            "position": "relative",
                            "height": "300px",
                            "border_radius": "1rem",  # rounded={'2xl'}
                            "box_shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",  # boxShadow={'2xl'}
                            "width": "100%",
                            "overflow": "hidden",
                            "background": rx.color_mode_cond(
                                light="white", dark="#1A202C"
                            ),
                        },
                    )
                    for i, video in enumerate(videos_list)
                ],
                spacing="3",
                style={
                    "width": "100%",
                    "align_items": "stretch",
                    "background": rx.color_mode_cond(light="white", dark="#1A202C"),
                },
            ),
            gap="2.5rem",
            style={
                "background": rx.color_mode_cond(light="white", dark="#1A202C"),
            },
        ),
        style={
            "max_width": "80rem",  # 5xl
            "padding_y": "3rem",  # py={12} = 3rem
            "margin": "0 auto",
            "background": rx.color_mode_cond(light="white", dark="#1A202C"),
        },
    )
