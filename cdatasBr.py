from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self._momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self._mes_cadastro = self._momento_cadastro.month-1  #month devolve indice indicando mes
        return meses_do_ano[self._mes_cadastro]

    def dia_semana(self):
        dia_semana = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]
        return dia_semana[self._momento_cadastro.weekday()]   #retornou 3 que é quinta-feira, devolve indice da semana

    def format_data(self):
        return self._momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastro(self):
        tempo = datetime.today() - self._momento_cadastro #seria o correto
        #vamos adicionar 30 à data pra dar diferença de um mes no cadastro
        tempo = (datetime.today() + timedelta(days=30)) - self._momento_cadastro  # seria o correto
        return tempo