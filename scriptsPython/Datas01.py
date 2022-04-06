from datetime import date

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%y')
    print(type(data_atual))

def trabtime():
    horario = time(hour=15, minute=18, second=30)
    print(horario)

if __name__ == '__main__':
    #trabalhando_com_date()
    trabtime()