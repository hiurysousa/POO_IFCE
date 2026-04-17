import rich
class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5


    def __init__(self, canal = 1, volume = 2):
        self.canalAtual:int = canal
        self.volumeAtual:int = volume
        self.power:bool = False

    def mostrar_tv(self):
        if self.power == False:
            print(f'A TV está desligada')
        else:
            print(f'CANAL e VOLUME')

    def tradeCanal(self):
            opcao = input("Canal = 1 | 2 | 3 | 4 | 5")
            match opcao:
                case '1':
                    self.canalAtual = 1
                    print("Canal 1 selecionado")
                case '2':
                    self.canalAtual = 2
                    print("Canal 2 selecionado")
                case '3':
                    self.canalAtual = 3
                    print("Canal 3 selecionado")
                case '4':
                    self.canalAtual = 4
                    print("canal 4 selecionado")
                case '5':
                    self.canalAtual = 5
                    print("Canal 5 selecionado")
                case _:
                    print("Canal inexistente.")

    def tradeVolume(self):
            user = input("< VOL > ")
            if user == "<" and self.volumeAtual > 0:
                self.volumeAtual -= 10
            elif user == ">" and self.volumeAtual < 100:
                self.volumeAtual += 10
            print(f"Volume atual: {self.volumeAtual}")

    def ligaDesliga(self):
        print(" # TV DESLIGADA # (@ para ligar ou desligar)")
        while True:
            user = input("")
            if user == "@":
                self.power = not self.power
                if self.power:
                    print(' # TV LIGADA # (@ para ligar ou desligar)')
                    self.tradeCanal()
                    self.tradeVolume()
                else:
                    print(" # TV DESLIGADA # (@ para ligar ou desligar)")

c1 = ControleRemoto()
c1.ligaDesliga()