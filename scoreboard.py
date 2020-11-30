from turtle import Turtle

SCOREBOARD_COLOR = "white"
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 280


class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initialise le tableau de point, charge le score le plus élevé stocké sur le disque dur et affiche
        le tableau
        """
        super().__init__()
        self.penup()
        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.display_score()

    def display_score(self):
        """
        Rafraichit l'affichage du score
        :return:
        """
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.clear()
        self.write(f"Score : {self.score} - Highest score : {self.high_score}", False, align="center")


    def reset(self):
        """
        Réinitialise le score et met-à-jour le score le plus élevé si nécessaire
        Raffraichit l'affichage
        :return:
        """
        self.update_highscore()
        self.save_high_score()
        self.score = 0
        self.display_score()

    def increment_score(self):
        """
        Incrémente le score d'une unité
        :return:
        """
        self.score += 1
        self.display_score()

    def update_highscore(self):
        """
        Vérifie si le score obtenu est supérieur au score le plus élevé et le met à jour si nécessaire
        :return:
        """
        if self.score > self.high_score:
            self.high_score = self.score

    def save_high_score(self):
        """
        Sauve le score le plus élevé sur le disque dur
        :return:
        """
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))

    def load_high_score(self):
        """
        Charge le score le plus élevé sauvegardé. Crée le fichier si nécessaire
        :return:
        """
        try:
            with open("data.txt", "r") as f:
                score = f.readline()
                self.high_score = int(score)
        except FileNotFoundError:
            # File not found then file need to be created and highest score need to be initiated to 0
            self.save_high_score()
