class Carro:
    
    def __init__(self, motor, direcao, eletrico):
        self.motor = motor
        self.direcao = direcao
        self.eletrico = eletrico

    def partida(self):
        print('Dando partida no veículo...')

    def acelera(self):
        print('Carro acelerado em movimento...')

    def parar(self):
        print('Carro parado!')
