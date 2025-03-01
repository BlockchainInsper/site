import reflex as rx

config = rx.Config(
    app_name="App",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
