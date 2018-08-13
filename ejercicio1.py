import turtle


dato = input('Digite el valor :')
window = turtle.Screen()

def cuadrado(n):

    square = turtle.Turtle()

    for a in range(1,5):
        square.forward(n)
        square.left(90)

    turtle.mainloop()



cuadrado(int(dato))


