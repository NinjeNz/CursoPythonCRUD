import turtle

# Crear una instancia de Turtle
t = turtle.Turtle()

# Configurar el color y grosor de la pluma
t.color("orange")
t.pensize(5)

# Dibujar la estrella de cinco puntas
for _ in range(5):
    t.forward(100)
    t.right(144)

# Ocultar la Turtle
t.hideturtle()

# Mantener la ventana abierta
turtle.done()
