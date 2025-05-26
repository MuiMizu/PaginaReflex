import reflex as rx

def barra():
    return rx.hstack(
        rx.hstack(
            rx.text("A.N.E.M.O", font_size="1.5rem", font_weight="bold", color="white", spacing="1",
            align="center",),
        ),
        rx.hstack(

            rx.text("Products", variant="ghost", color="white", cursor="pointer"),

            rx.text("Company", variant="ghost", color="white", cursor="pointer"),

            rx.text("Pricing", color="white", cursor="pointer"),

            rx.text("For Accountants", color="white", cursor="pointer"),
            spacing="8", margin="5", align="center",
        ),

        rx.hstack(
            rx.button("Log in", background_color="transparent", border_color="white", cursor="pointer",
                      _hover={"background" : "rgba(255,255,255,0.1)"},),

            rx.button("Lets Go", background="grey", color="white", border_radius="0.5rem",
                      padding="0.75rem 1.5rem", font_weight="500",
                      _hover={"background": "rgba(255,255,255,0.9)"}),

            spacing="5",
            align="center",
        ),

        justify="between",
        align="center",
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding="1rem 2rem",
        background="rgba(0,0,0,1)",
        box_shadow="0 4px 12px rgba(0, 0, 0, 0.8)",
        border_radius="0.5rem",
    )

def principal():
    return rx.box( 
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "Every Step",
                    rx.text("Worth Gold.", margin_top="1rem"),
                    spacing="4",
                    font_size="4rem",
                    font_weight="bold",
                    color="white",
                    line_height="1.1",
                    margin_bottom="1.5rem",
                ),

                rx.text(
                    "Work with the best tools to make your work easier and more efficient.",
                    font_size="1.3rem",
                    font_weight="bold",
                    color="white",
                    line_height="1.6",
                    margin_bottom="1rem",
                    max_width="430px",
                ),

                rx.hstack(
                    rx.button("Go To Work", background="#FF5722", color="white", border_radius="0.5rem",
                              padding="1rem 2rem", font_size="1rem", font_weight="500",
                              _hover={"background": "#E64A19"}, cursor="pointer"),

                    rx.button("Contact Us", variant="outline", color="white",
                              border_color="rgba(255,255,255,0.3)", border_radius="0.5rem",
                              padding="1rem 2rem", font_size="1rem", background="transparent",
                              _hover={"background": "rgba(255,255,255,0.1)"}),

                    spacing="3",

                ),
                spacing="0",
            ),

            rx.box(), 
            align="center",
            justify="start",
            width="100%",
            padding="4rem 2rem",
            margin_left="2rem",
            margin_bottom="8rem",
        ),
        width="100%",
        margin_top="6rem",
    )


def index():
    return rx.box(
        rx.box(
            rx.html("""
                <video autoplay muted loop id="backgroundVideo" style="
                    position: fixed;
                    right: 0;
                    bottom: 0;
                    min-width: 100%;
                    min-height: 100%;
                    z-index: -1;
                    object-fit: cover;
                ">
                    <source src="/videos/fondo.mp4" type="video/mp4">
                </video>
            """),
        ),
        
        rx.vstack(
            barra(),
            principal(),
            width="100%",
        ),
        
        min_height="100vh",
        width="100%",
        position="relative",
    )

app = rx.App()
app.add_page(index, route="/")
