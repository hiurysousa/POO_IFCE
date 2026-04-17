import rich
class Gamer:
    def __init__(self, nome, nick, games = ()):
        self.nome = nome
        self.nick = nick
        self.games = games

    def adicionarGame(self, game) -> None:
        self.games = list(self.games)
        self.games.append(game)

    def exibirFicha(self):
        print(f"Nome Real: {self.nome} \nJogos Favoritos: ")
        for game in self.games:
            print(f"{game}")

g1 = Gamer("Hiury", "Easymoneysniper")
g1.adicionarGame("League of Legends")
g1.adicionarGame("Fifa")
rich.inspect(g1)
g1.exibirFicha()
