#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro
# @Capítulo: 03 - Estadísticas para comprender los datos
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   JMPEstadísticas (copiar el archivo dentro de su proyecto al mismo nivel que este archivo)
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------


from matplotlib import pyplot as plt
import pandas as pnd
import JMPEstadisticas as jmp
import numpy as np

#--- CREACION DE UN DATAFRAME ----
observaciones = pnd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})

#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(observaciones['NOTAS'])
stats.analisisCaracteristica()

valoresOrdenados = observaciones.sort_values()
valoresOrdenados = valoresOrdenados.reset_index(drop=True)
print ("Rango de la serie ="+str(valoresOrdenados[len(valoresOrdenados)-1]-valoresOrdenados[0]))

def calculoDelosCuartiles(self,mediana,rangoMediana):
    n = self.caracteristica.count()
    sort_caracteristica = self.observaciones.sort_valores()
    sort_caracteristica = sort_caracteristica.reset_index(drop=True)
    q1 = 0
    q2 = mediana
    q3 = 0

#Calculo Q1
    restoDivision = rangoMediana%2
    if (restoDivision != 0):
        q1 = sort_caracteristica[((rangoMediana/2)+1)-1]
    else:
        valorMin = sort_caracteristica[((rangoMediana/2)-1)]
        valorMax = sort_caracteristica[(rangoMediana/2)]
        q1 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

# Calculo Q3
    nbdatos = len(sort_caracteristica)+1
    nbDatosDesdeMediana = nbdatos - rangoMediana
    restoDivision = nbDatosDesdeMediana % 2
    if (restoDivision != 0):
        q3 = sort_caracteristica[(rangoMediana+np.ceil(nbDatosDesdeMediana/2))-1]
    else:
        valorMinQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))-1]
        valorMaxQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))]
        q3 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

    return ([q1, q2, q3])


def criterioDeTukey(self, primerCuartil, tercerCuartil):

    valoresExtremosInferiores = []
    valoresExtremosSuperiores = []
    observaciones = self.observaciones.sort_valores()
    intercuartil = tercerCuartil - primerCuartil
    print("Inter-cuartil = "+str(intercuartil))
    limiteInferior = primerCuartil - (1.5 * intercuartil)
    limiteSuperior = tercerCuartil + (1.5 * intercuartil)

    for valorObservacion in observaciones:
        if valorObservacion < limiteInferior:
            valoresExtremosInferiores.append(valorObservacion)

        if valorObservacion > limiteSuperior:
            valoresExtremosSuperiores.append(valorObservacion)

    valoresExtremos = valoresExtremosInferiores + valoresExtremosSuperiores

    return (valoresExtremos)


def visualizacion(self,media,mediana,cuartil_1,cuartil_2,cuartil_3):

    plt.subplot(2, 2, 1)
    plt.hist(self.observaciones)
    plt.title("Histograma y media")
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 2)
    plt.hist(self.caracteristica)
    plt.title("Histograma y mediana")
    plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1,label = str(mediana))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 3)
    plt.hist(self.caracteristica)
    plt.title("Histograma y cuartiles")
    plt.axvline(cuartil_1, color='orange', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
    plt.axvline(cuartil_2, color='orange', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
    plt.axvline(cuartil_3, color='orange', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
    plt.legend(loc='upper right')

    plt.subplot(2, 2, 4)
    plt.boxplot(self.caracteristica)
    plt.title("Diagrama de caja y bigotes")
    plt.show()

