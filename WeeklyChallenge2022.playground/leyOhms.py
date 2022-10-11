"""
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
"""

def calcularLeyOhms(voltios=None, ohmios=None, amperios=None):
    """
    :param voltios:
    :param ohmios:
    :param amperios:
    :return: imprime el resultado

    La formula de la ley de Ohms es V = R*I
        voltios = ohmios * amperios

        ohmios = voltios/amperios
        amperios = voltios/ohmios
    """
    parametros = [voltios, ohmios, amperios]

    # determinamos si hay mas parametros con None
    if parametros.count(None) > 1:
        return print("Invalid values")

    # si el indice es 0 retornamos el valor de la diferencia de potencial
    if parametros.index(None) == 0:
        return print(f"Voltios = {round((ohmios*amperios), 2)}")

    # si el indice es 1 retornamos el valor de los amperios
    if parametros.index(None) == 1:
        return print(f"Ohmios = {round((voltios/amperios), 2)}")

    # si el indice es 2 retornamos el valor de los ohmios
    if parametros.index(None) == 2:
        return print(f"Amperios = {round((voltios/ohmios), 2)}")


# Ejemplo con mas de un parámetro en None
calcularLeyOhms(None, None, 100)

# Ejemplo para averiguar los voltios
calcularLeyOhms(None, 25.234, 100.254)

# Ejemplo para averiguar los ohmios
calcularLeyOhms(25.234, None, 100.254)

# Ejemplo para averiguar los amperios
calcularLeyOhms(25.234, 100.254, None)