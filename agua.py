#- su peso en kg
#- su nivel de actividad: bajo, medio o alto
#- la cantidad de agua consumida hoy en ml

#Luego el programa debe llamar a las funciones y mostrar:
#- el objetivo diario recomendado en ml
#- el mensaje de estado de hidratación


def calcular_objetivo_ml(peso_kg, actividad):
    objetivo = peso_kg * 35
    if actividad == "bajo":
        objetivo *= 1.2
    elif actividad == "medio":
        objetivo *= 1.55
    elif actividad == "alto":
        objetivo *= 1.725
    return objetivo

def determinar_estado_hidratacion(agua_consumida, objetivo):
    if agua_consumida < objetivo:
        diferencia = objetivo - agua_consumida
        porcentaje = (diferencia / objetivo) * 100
        return f"Te falta un {porcentaje:.2f}% para llegar (faltan {diferencia:.0f} ml)."
    elif agua_consumida == objetivo:
        return "¡Excelente! Has alcanzado tu objetivo exacto."
    else:
        excedente = agua_consumida - objetivo
        return f"¡Felicidades! Has superado tu objetivo por {excedente:.0f} ml."


while True:
    try:
        peso = float(input("Ingrese su peso en kg: "))
        actividad = input("Ingrese su nivel de actividad (bajo, medio o alto): ").lower()
        if actividad not in ["bajo", "medio", "alto"]:
            print("Error: Nivel de actividad no reconocido.")
            continue
            
        agua_consumida = float(input("Ingrese la cantidad de agua consumida hoy en ml: "))

        objetivo_diario = calcular_objetivo_ml(peso, actividad)
        estado = determinar_estado_hidratacion(agua_consumida, objetivo_diario)

        print(f"\n--- Resultados ---")
        print(f"Objetivo diario recomendado: {objetivo_diario:.0f} ml")
        print(f"Estado de hidratación: {estado}\n")

        salir = input("¿Desea realizar otro cálculo? (s/n): ").lower()
        if salir != 's':
            print("¡Hasta luego!")
            break

    except ValueError: 
        print("Error. Debes ingresar números válidos.")
