
import colorama
from colorama import Fore, Back, Style, init

init()
def valor_hora(salario, carga):
    return salario/carga

def hora_extra(valor_hora):
    return valor_hora * 1.5

def qua_hora_extra(hora_extra,quantidade):
    return hora_extra * quantidade

def salario_total(salario, qua_hora_extra):
    return salario +  qua_hora_extra

def sistema_rh():
    while True:    
        print('')
        print(Style.BRIGHT+Back.BLACK + Fore.GREEN+'***SISTEMA RH***')
        salario = float(input(Style.BRIGHT+Back.BLACK + Fore.GREEN+'Salario: '))
        carga = float(input(Style.BRIGHT+Back.BLACK + Fore.GREEN+'Carga: '))
        hora_trab = valor_hora(salario, carga)
        print(Style.BRIGHT+Back.BLACK + Fore.GREEN + 'HORA DO TRABALHADOR R$', round(hora_trab,2) )
        print('-------------------------------')
        extra_50 =  hora_extra(hora_trab)
        print(Style.BRIGHT+Back.BLACK + Fore.GREEN+ 'HORA EXTRA VALOR R$', round(extra_50,2))
        print('-------------------------------')
        quantidade_extra =  float(input('Quantidade extra: '))
        qua_hr_extra = qua_hora_extra(extra_50,quantidade_extra)   
        print(Style.BRIGHT+Back.BLACK + Fore.GREEN + 'QUANTIDADE DE EXTRA HORA:', round(quantidade_extra,2)) 
        print(Style.BRIGHT+Back.BLACK + Fore.GREEN + 'QUANTIDADE DE EXTRA HORA:', round(qua_hr_extra,2)) 
        print('-------------------------------')
        salario_t = salario_total(salario,qua_hr_extra)
        print(Style.BRIGHT+ Fore.YELLOW + Back.BLACK + 'SALARIO: R$', round(salario_t, 2))


sistema_rh()

input('digiter para sair: ')

