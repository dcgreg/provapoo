from .Conta import Conta
class HistoryContas:
    def __init__(self)->None:
        self.__contas = []
    def getMediaKw(self):
        media = 0
        for conta in self.__contas:
            media+=conta.getKwGasto()
        media = media / len(self.__contas)
        return print(f"A média do consumo de kw é de {media :.2f}" )
    def getValorMediaContas(self):
        mediac = 0
        for conta in self.__contas:
            mediac+=conta.getValorPagar()
        mediac = mediac / len(self.__contas)
        return print(f"A média do valor da conta é de {mediac :.2f}" )
    def getMesMaiorConsumo(self):
        lkw=[]
        for conta in self.__contas:
            lkw.append(conta.getKwGasto())
        maior=max(lkw)
        return print(f"O maior consumo mensal foi de {maior} Kw")
    def getMesMenorConsumo(self):
        lkw=[]
        for conta in self.__contas:
            lkw.append(conta.getKwGasto())
        menor=min(lkw)
        return print(f"O menor consumo mensal foi de {menor} Kw")
    def setConta(self,conta:Conta):
        self.__contas.append(conta)
    def getContaHistory(self)->str:
        print('-' * 100)
        print("Número Conta".center(20),"Data Leitura".center(20),"Numero Leitura".center(20),"Valor".center(20),"Kw".center(20))
        print('-' * 100)
        for conta in self.__contas:
            print(conta.getDadosConta())
            