import financial_controller as financial
import matplotlib.pyplot as plt
import numpy as np

def lanzar():
  """
    Inicializa la aplicación y llama en orden los métodos, para dar el flujo de la aplicación.
  """  
  iniciar_calculadora()
  capital, interes, plazo_meses, valor_seguro, abono_capital = solicitar_entradas()
  
  valor_cuota = financial.obtener_valor_cuota(capital, interes, plazo_meses)
  resultado_simulacion = financial.simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital )

  mostrar_resultados( capital, valor_cuota, valor_seguro, resultado_simulacion, abono_capital )
  fin_calculadora()
  firma()
  


  capital_credito = []
  interes_credito = []
  meses_credito = []


  for i in resultado_simulacion:
    capital_credito.append(i['total_cuota'])
    interes_credito.append(i['intereses'])
    meses_credito.append(i['mes'])
  
  cuota_abono = np.array(capital_credito) - np.array(interes_credito)
  data1= cuota_abono 
  data2= interes_credito

  x = meses_credito

  #plt.figure(figsize=(9,7))
  plt.bar(x,data1,color="Blue",label="Abono a Capital")
  plt.bar(x,data2,color="Orange",bottom=np.array(data1),label="Intereses")
  
  plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
  plt.show()
  


def iniciar_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""*****************************************************************************
***********************  CALCULADORA FINANCIERA  ****************************
*****************************************************************************
  """)
  

def fin_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""
*****************************************************************************
*************************  CALCULO FINALIZADO  ******************************
*****************************************************************************""")


def mostrar_resultados(capital_inicial, valor_cuota, seguro, simulacion, abono_capital):
  print()
  print("Mes {}: Desembolso: {}".format(0, capital_inicial) )
  print("Valor de la cuota: {}".format(valor_cuota) )

  header = '|     Mes     |     Capital Base     |     Intereses     |     Seguro     |     Total Cuota     |     Abono a capital     |     Saldo después del pago     |'
  print( header )

  count = 0
  for data in simulacion:
    count += 1
    linea = '|'
    
    columan = ' {} '.format( data['mes'] )
    while len(columan) < 13:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_inicial'] )
    while len(columan) < 22:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['intereses'] )
    while len(columan) < 19:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( seguro )
    while len(columan) < 16:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['total_cuota'] )
    while len(columan) < 21:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['abono_capital'] )
    while len(columan) < 25:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_despues_pago'] )
    while len(columan) < 32:
      columan = ' ' + columan
    linea += columan + '|'

    print( linea )





def firma():
  """
    Muestra el nombre del creador de la aplicacion
  """
  firma = {
    'nombre': 'Almeiro Arango Avila', # Colocar su nombre completo
  }
  print("Este desarrollo fue creado por: {}".format(firma['nombre']))
  return firma['nombre']
  



def solicitar_entradas() -> tuple:
  # TODO: Documentar este código
  # TODO: Desarrollar este código

  capital = float(input('Ingresa el monto del credito a solicitar: '))
  interes = float(input('Ingresa tasa de interes efectiva anual: '))
  interes = float(interes / 100)
  plazo_meses = int(input('Ingresa plazo en meses: '))
  valor_seguro = int(input('Ingresa el valor del seguro: '))
  abono_capital = int(input('Ingresa el valor esperado del abono a capital: '))


  return capital, interes, plazo_meses, valor_seguro, abono_capital
  