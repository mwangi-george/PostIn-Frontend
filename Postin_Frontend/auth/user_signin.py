import reflex as rx


@rx.page(route="/", title="Login")
def login_default() -> rx.Component:
    return rx.center(
        rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/logo.png",
                    width="10.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    id="user_password_signin",
                    placeholder="Enter your username",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%", on_click=rx.redirect("/home")),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="/signup", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    ),
     margin_top="auto",
    padding_top="5rem",
    padding_bottom="5rem",
    width="100%",
    ) 