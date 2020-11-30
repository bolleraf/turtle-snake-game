import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake


def end_game():
    """
    Demande au joueur s'il veut rejouer. Si oui alors on réinitialise l'écran et le score. Si non on termine le jeux.
    :return:
    """
    user_choice = screen.textinput("Fin de partie", "Veux-tu recommencer (O/N)")
    if user_choice.lower() == "o":
        # Réinitialise le serpent et repositionne-le au centre. Réinitialise le score
        snake.reset()
        scoreboard.reset()
    else:
        # Réinitialise le scoreboard. Met le variable booléenne game_is_on à False ce qui fait sortir de la loop et
        # termine le jeu
        global game_is_on
        game_is_on = False
        scoreboard.reset()
        screen.bye()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Détecte la collision avec la nourriture
    if snake.head.distance(food) < 15:
        scoreboard.increment_score()
        snake.grow_snake()
        food.refresh()

    # Détecte la collision avec le mur
    if snake.head.xcor() <= -300 or snake.head.xcor() >= 300 or snake.head.ycor() <= -300 or snake.head.ycor() >= 300:
        end_game()

    # Detect collision avec la queue du serpent
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_game()

    screen.listen()
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")


screen.exitonclick()
