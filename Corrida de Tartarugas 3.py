import turtle
import random

def setup_race():
    screen = turtle.Screen()
    screen.title("Corrida de Tartarugas")
    screen.bgcolor("#09FFB1")
    screen.setup(width=800, height=650)  # Ajustando o tamanho da tela
    return screen

def create_track():
    track = turtle.Turtle()
    track.speed(0)
    track.penup()
    track.goto(-200, 100)
    track.pendown()
    track.fillcolor("chocolate")
    track.begin_fill()
    for _ in range(2):
        track.forward(400)
        track.right(90)
        track.forward(400)
        track.right(90)
    track.end_fill()

    # Desenha a linha de chegada quadriculada
    track.penup()
    track.goto(200, 100)
    track.setheading(270)
    track.pencolor("black")
    
    for _ in range(20):
        track.fillcolor("black" if _ % 2 == 0 else "white")
        track.begin_fill()
        for _ in range(4):
            track.forward(20)
            track.right(90)
        track.end_fill()
        track.penup()
        track.forward(20)

    track.hideturtle()

def create_cars():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]
    cars = []
    start_y = 80

    for color in colors:
        car = turtle.Turtle()
        car.shape("turtle")
        car.color(color)
        car.penup()
        car.goto(-200, start_y)
        start_y -= 40
        cars.append(car)

    return cars

def race(cars):
    is_race_on = True
    while is_race_on:
        for car in cars:
            car.forward(random.randint(1, 10))

            if car.xcor() >= 200:
                is_race_on = False
                winner_color = car.pencolor()
                announce_winner(winner_color)
                break

def announce_winner(color):
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(0, 0)
    winner.write(f"O vencedor é o carro {color.upper()}!", align="center", font=("Arial", 16, "bold"))

# Configuração do programa
screen = setup_race()
create_track()
cars = create_cars()
race(cars)
screen.mainloop()
