import random
from turtle import Turtle

FOOD_SHAPE = "circle"
FOOD_COLOR = "red"


class Food(Turtle):

    def __init__(self):
        """
        Initialise l'objet nourriture et le positionne à une endroit de l'écran au hasard
        """
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Place la nourriture à un endroit aléatoire
        :return:
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

