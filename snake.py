from turtle import Turtle

DISTANCE_MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SNAKE_COLOR = "white"


class Snake(Turtle):

    def __init__(self):
        """
        Initialise le serpent
        """
        super().__init__()
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Crée les segments du serpent et les stocke dans une liste. Définit également l'élément de tête (head).
        :return:
        """

        for i in range(0, 3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color(SNAKE_COLOR)
            segment.setx(0 - (i * 20))
            self.segments.append(segment)
        self.head = self.segments[0]

    def grow_snake(self):
        """
        Ajoute un segment additional au serpent
        :return:
        """
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(self.segments[len(self.segments) - 1].position())
        self.segments.append(new_segment)

    def move(self):
        """
        Déplace le segment d'une distance de DISTANCE_MOVE
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())

        self.head.fd(DISTANCE_MOVE)

    def left(self):
        """
        Déplace à gauche
        :return:
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Déplace à droite
        :return:
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """
        Déplace vers le haut
        :return:
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Déplace vers le bas
        :return:
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        """
        Effectue un reset du serpent et le repositionne au centre pour commencer une nouvelle partie
        :return:
        """
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
