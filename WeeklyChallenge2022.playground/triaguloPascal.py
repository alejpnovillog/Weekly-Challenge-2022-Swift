"""
* Reto #40
 * TRIÁNGULO DE PASCAL
 * Fecha publicación enunciado: 03/10/22
 * Fecha publicación resolución: 10/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *

 desarrollo de un binomio
 (a +b)**k =

"""


# libreria para el tratamiento del binomio
from sympy import Symbol, expand

def trianguloPascal(lista):
    """
    :param lista: Es el contenido de un lado del triangulo de Pascal

    La función se basa en la formula de expansión del binomio elevado
    a una determina potencia.

    """

    # definimos las listas de trabajo
    listaFinal, recorre = list(), list()

    # obtenemos el valor elemento inicial de la lista recibida
    valorInicial = lista[0]

    # obtenemos la cantidad de elementos de la lista recibida
    cantElementos = len(lista)

    # construimos la cantidad de sub-elementos de la lista Final
    listaFinal = [list() for x in range(0, cantElementos)]

    # inicializamos los sub-elemento [0], [1]
    # comienzo del triangulo de pascal
    listaFinal[0] = [valorInicial]
    listaFinal[1] = [valorInicial, valorInicial]

    # obtenemos los sub-elementos restantes del [0], [1]
    recorre = [x for x in range(2, cantElementos)]

    # definimos los symbol del binomio
    a = Symbol("a")
    b = Symbol("b")

    # recorremos los sub-elementos restantes y finalizamos la
    # construcción del triangulo de pascal
    for k in recorre:

        # obtenemos una lista de strings con el resultado de la expansion del binomio
        valor = str(expand((a + b) ** k, deep=True)).split('+')

        # reemplazamos los Symbols por el valor inicial de la lista
        valor = [x.replace(str(a), str(valorInicial)) for x in valor]
        valor = [x.replace(str(b), str(valorInicial)) for x in valor]

        # resolvemos los sub-elementos de la lista
        valor = [eval(x) for x in valor]

        # cambiamos el contenido de los sub-elementos de la listaFinal
        listaFinal[k] = valor

    # imprimimos el triangulo de pascal
    final = [print(x) for x in listaFinal]


# ejemplo del parametro
trianguloPascal([1, 1, 1, 1, 1])







