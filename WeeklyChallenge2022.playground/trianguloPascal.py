import numpy as np

class TresEnLinea():
    """
    Realizar un programa que simule el juego de las tres en raya.
    Cada jugador solo debe colocar su ficha una vez por turno y no debe ser sobre una casilla ya ocupada.
    En caso de que el jugador haga trampa el ganador será el otro.
    Para ganar se debe conseguir realizar una línea recta (horizontal, vertical o diagonal) con la misma ficha.
    El tablero es de 3x3 y cualquier casilla podrá estar vacía u ocupada sólo por una ficha X o 0.
    El programa debe realizar las siguientes operaciones:

    Mostrar el tablero por pantalla.
    Poner una ficha en una cuadricula comprobando que no está ocupada.
    Comprobar si se produce tres en raya e indicar si es de X o de O, o si hay empate.
    """

    def __init__(self):
        self.ficha = ["X", "O"]
        self.juego = np.array([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]])

        self.jugadores = list()
        self.jugar = True

    def display(self):
        print(self.juego)


    def agregarJugador(self, name):
        if len(self.jugadores) == 2:
            print(f"Ya estan todos los jugadores {self.jugadores[0]}, {self.jugadores[1]}")
        else:
            self.jugadores.append(name)





    def control(self, valor):

        respuesta = lambda x, valor: True if  x ==  [valor, valor, valor] else False
        #invertir = np.fliplr(self.juego).diagonal()
        lista_control = [
            list(self.juego[0]),
            list(self.juego[1]),
            list(self.juego[2]),
            list(self.juego[:, 0]),
            list(self.juego[:, 1]),
            list(self.juego[:, 2]),
            list(self.juego.diagonal()),
            #np.fliplr(self.juego).diagonal()
        ]

        for y in lista_control:
            if y == [valor, valor, valor]:
                return True


    def inicioJuego(self):

        turno = True
        lugar = -1
        # iniciamos el juego
        while self.jugar:

            # damos el turno
            while turno:

                # visualizamos el tablero
                self.display()

                # visualizamos el nombre del jugador
                lugar += 1

                if lugar > 1:
                    lugar = 0

                print("=================================")
                print(f"Juega {self.jugadores[lugar]} ")

                # ingresa la fila
                fila = int(input("Ingrese la Fila :"))

                # ingresa la columna
                columna = int(input("Ingrese columna :"))

                # si no encuentra los
                if self.juego[fila][columna] == "0":
                    self.juego[fila][columna] = self.ficha[lugar]

                    if self.control(self.ficha[lugar]):
                        turno = False
                        self.jugar = False
                        break






jugar = TresEnLinea()
jugar.agregarJugador('alejandro')
jugar.agregarJugador('sebastian')
jugar.inicioJuego()
