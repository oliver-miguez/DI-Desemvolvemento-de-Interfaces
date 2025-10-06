import Empaquetado # Llama a las funcionalidades del módulo empaquetado

#from math import  pi # Importa en el script el "pi" de la libreria de math
#from math import  * # Importa lo relacionado con la libreria math (NO RECOMENDABLE, CONSUME MUCHA MEMÓRIA)



# Al importar directamente importamos el código dentro del módulo por eso siempre aparece por consola "Un módulo"
# Llama a los métodos del módulo Empaquetado
# 1º Forma de llamar métodos del módulo importado Empaquetado
#Empaquetado.unha_funcion()
Empaquetado.UnhaClase()

# 2º Forma de llamar métodos del módulo importado Empaquetado
from Empaquetado import unha_funcion # Permite utilizar la función "unha_funcion()" sin llamar directamente a la importación para usarla
unha_funcion()


if  __name__ == "__main__": # De esta forma podremos usar los métodos del import del módulo en la main de esta nueva clase
    unha_funcion()