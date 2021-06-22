

#import matplotlib.pyplot as plt
#import math
#import numpy as np
#import pandas as pd

def simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital ) -> dict:
  # TODO: Documentar Método
  # TODO: Desarrollar este 

  mes = 0
  saldo_capital = float(0)
  prestamo = []
  datos_credito = {}
  

  while capital > 0 :
    mes += 1
    interes_mensual = round(capital * convertir_interes_efectivo_anual_a_mensual(interes),2) 
    saldo_para_cuota = capital
    saldo_capital = round(capital,2)

    nuevo_abono_capital = round(capital - (valor_cuota - interes_mensual),2)

    if nuevo_abono_capital < abono_capital:
      abono_capital = nuevo_abono_capital

    capital = round(capital - abono_capital - (valor_cuota - interes_mensual), 2)

    if saldo_para_cuota <= valor_cuota:
      valor_cuota = saldo_para_cuota + interes_mensual 

      nuevo_abono_capital = round(saldo_para_cuota - (valor_cuota - interes_mensual),2)

      if nuevo_abono_capital != abono_capital:
        abono_capital = nuevo_abono_capital
      
 

    datos_credito = {'mes': mes, 'saldo_inicial':saldo_capital, 'intereses':interes_mensual, 'total_cuota':valor_cuota + valor_seguro, 'abono_capital':abono_capital, 'saldo_despues_pago':capital}
    prestamo.append(datos_credito)

    #print(pd.DataFrame([datos_credito]))
    
  return prestamo

    
def calcular_nuevo_valor_adeudado( capital, interes ) -> float:
  # TODO: Documentar Método
  # TODO: Desarrollar este método
  # AYUDA: usar el método "convertir_interes_efectivo_anula_a_mensual" para convertir el interes de anual a mensual

  new_capital=capital * (1 + convertir_interes_efectivo_anual_a_mensual(interes))

  return round(new_capital,2)

  
def convertir_interes_efectivo_anual_a_mensual(interes):
  """
    Convierte el interes de efectivo anula a efectivo mensual
  """
  return (1 + interes)**(1/12) - 1


def obtener_valor_cuota(monto, tasa, cuotas):
    """
    Retorna el valor actual de la cuota, para cuotas son fijas.
                
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)]. 
    Donde: 
        R = renta (cuota)
        P = principal (préstamo adquirido)
        i = tasa de interés
    """
    efectiva_mensual = convertir_interes_efectivo_anual_a_mensual(tasa)
    valor_cuota = monto * ( (efectiva_mensual * ((1 + efectiva_mensual)**cuotas)) / (((1 + efectiva_mensual)**cuotas) - 1) )
    valor_cuota = valor_cuota + 1 # método para evitar un més adicional (truco)
    return round( valor_cuota, 2)


