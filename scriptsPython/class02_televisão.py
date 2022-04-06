class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
televisão = Televisão()
print(f'A televisão esta ligada? {televisão.ligada}')
televisão.power()
print(f'A televisão esta ligada? {televisão.ligada}')

print(f'O canal é {televisão.canal}')
televisão.aumenta_canal()
televisão.aumenta_canal()
print(f'O canal é {televisão.canal}')