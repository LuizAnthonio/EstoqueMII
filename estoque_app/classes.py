from datetime import date

def dataF(dat):
     datinha = date(dat)

     dia = datinha.day
     mes = datinha.month
     ano = datinha.year

     formato = '{}/{}/{}'.format(dia,mes,ano)
     return formato
