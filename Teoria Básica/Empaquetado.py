def unha_funcion ():
    print("Unha función")

class UnhaClase:
    def __init__(self):
        print("Unha clase")

print("Un módulo, esto se muestra siempre") # Unidad más pequeña, siempre que se importe se llama siempre

if __name__ == "__main__": # El código que se escriba dentro de aquí no será mostrado en el resto de módulos que importen esto, ya que esto solo se ejecuta en la main de "Empaquetado"
    print("Esto no se muestras cuando se importa")