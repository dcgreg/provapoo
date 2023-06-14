from Classes import Conta,HistoryContas
from datetime import datetime as dt
   
if __name__ == "__main__":
    history = HistoryContas()
    

    history.setConta(Conta("125254",dt.strptime("01/06/2023","%d/%m/%Y"),"001",200.00,100))
    history.setConta(Conta("125254",dt.strptime("01/07/2023","%d/%m/%Y"),"002",250.00,150))
    history.setConta(Conta("125254",dt.strptime("01/08/2023","%d/%m/%Y"),"003",50.00,50))

    history.getMediaKw()
    history.getValorMediaContas()
    history.getMesMaiorConsumo()
    history.getMesMenorConsumo()
    history.getContaHistory()
   
