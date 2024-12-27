import turtle
import random

def setup_race():
    screen = turtle.Screen()
    screen.title("Corrida de Tartarugas")
    screen.bgcolor("#09FFB1")
    screen.setup(width=800, height=680)  # Ajustando o tamanho da tela

    # Adicionando mensagem no topo da tela
    title = turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.goto(0, 300)
    title.write("Corrida de Tartarugas", align="center", font=("Arial", 20, "bold"))

    return screen

def create_track():
    track = turtle.Turtle()
    track.speed(0)
    track.penup()
    track.goto(-350, 300)  # Ajuste para o novo tamanho da pista
    track.pendown()
    track.fillcolor("chocolate")
    track.begin_fill()
    for _ in range(2):
        track.forward(700)  # Largura da pista
        track.right(90)
        track.forward(600)  # Altura da pista
        track.right(90)
    track.end_fill()

    # Desenha a linha de chegada quadriculada
    track.penup()
    track.goto(350, 300)
    track.setheading(270)
    track.pencolor("black")
    
    for _ in range(30):  # Ajustado para a altura da pista
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
    colors_pt = ["Vermelho", "Azul", "Verde", "Amarelo", "Roxo", "Laranja", "Rosa", "Marrom", "Ciano", "Magenta"]
    cars = []
    start_y = 250  # Ajustado para o novo tamanho da pista

    for color in colors:
        car = turtle.Turtle()
        car.shape("turtle")
        car.color(color)
        car.penup()
        car.goto(-350, start_y)
        start_y -= 60  # Ajustado para distribuir melhor os carros
        cars.append(car)

    return cars, colors_pt

def race(cars, colors_pt):
    is_race_on = True
    while is_race_on:
        for i, car in enumerate(cars):
            car.forward(random.randint(1, 10))

            if car.xcor() >= 350:  # Ajustado para o novo tamanho da pista
                is_race_on = False
                winner_color = colors_pt[i]
                announce_winner(winner_color)
                break

def announce_winner(color):
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(0, -320)
    winner.write(f"A tartaruga vencedora é {color}!", align="center", font=("Arial", 16, "bold"))

# Configuração do programa
screen = setup_race()
create_track()
cars, colors_pt = create_cars()
race(cars, colors_pt)
screen.mainloop()
