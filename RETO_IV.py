class Serie:
    titulo = ""
    numero_de_temporadas = 3
    entregado = False
    genero = ""
    creador = ""

    def __init__(self, titulo, numero_temp, entregado, genero, creador):
        self.titulo = titulo
        self.numero_de_temporadas = numero_temp
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def get_titulo(self):
        return self.titulo

    def get_numero_temporadas(self):
        return self.numero_de_temporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_numero_temporadas(self, numero):
        self.numero_de_temporadas = numero

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    def __str__(self):
        return f"{self.titulo}, {self.numero_de_temporadas}, entregado: {self.entregado}, {self.genero}, {self.creador}"


class Videojuego:
    titulo = ""
    horas_estimadas = 10
    entregado = False
    genero = ""
    compañía = ""

    def __init__(self, titulo, horas, entregado, genero, compañia):
        self.titulo = titulo
        self.horas_estimadas = horas
        self.entregado = entregado
        self.genero = genero
        self.compañía = compañia

    def get_titulo(self):
        return self.titulo

    def get_horas_estimadas(self):
        return self.horas_estimadas

    def get_genero(self):
        return self.genero

    def get_compañia(self):
        return self.compañía

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_horas_estimadas(self, horas):
        self.horas_estimadas = horas

    def set_genero(self, genero):
        self.genero = genero

    def set_compañia(self, compañia):
        self.compañía = compañia

    def __str__(self):
        return f"{self.titulo}, {self.horas_estimadas}, {self.entregado}, entregado: {self.entregado}, {self.genero}, {self.compañía}"


class Entregable(Serie, Videojuego):

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado


serie1 = Entregable("Berserk", 5, False, "Seinen", "Kintaro Miura")
serie2 = Entregable("SNK", 4, False, "Acción", "Hajime Isayama")
serie3 = Entregable("Rick y Morty", 4, True, "comedia", "Dan Harmon")
serie4 = Entregable("Dragon Ball", 6, True, "Shonen", "Akira Toriyama")
serie5 = Entregable("Juego de tronos", 8, True, "fantasía", "George R.R. Martin")

lista_series = [serie1, serie2, serie3, serie4, serie5]

videojuego1 = Entregable("League of Legends", 15, True, "Moba", "Riot Games")
videojuego2 = Entregable("World of Warcraft", 20, False, "MMORPG", "Blizzard")
videojuego3 = Entregable("Call of Duty", 16, False, "Shooter", "Activision")
videojuego4 = Entregable("Super Mario", 68, False, "Plataformas", "Nintendo")
videojuego5 = Entregable("Fortnite", 26, False, "Battle Royale", "Epic Games")

lista_videojuegos = [videojuego1, videojuego2, videojuego3, videojuego4, videojuego5]


def contar_series_entregadas(series):
    num_series = 0
    print("Las series entregadas son: ")
    for serie in series:
        if serie.entregado:
            num_series += 1
            print(serie.titulo)
    print(f"En total se han entregado: {num_series} series")


def contar_videojuegos_entregados(videojuegos):
    num_videojuegos = 0
    print("Los videojuegos entregados son: ")
    for juego in videojuegos:
        if juego.entregado:
            num_videojuegos += 1
            print(juego.titulo)
    print(f"En total se han entregado: {num_videojuegos} videojuegos")


def serie_mas_temporadas(series):
    temporadas = 0
    serie_mas = None
    for serie in series:
        if serie.numero_de_temporadas > temporadas:
            temporadas = serie.numero_de_temporadas
            serie_mas = serie
    return serie_mas

def videojuego_mas_horas(videojuegos):
    horas = 0
    videojuego_mas = None
    for videojuego in videojuegos:
        if videojuego.horas_estimadas > horas:
            horas = videojuego.horas_estimadas
            videojuego_mas = videojuego
    return videojuego_mas




serie1.entregar()
serie4.entregar()
videojuego5.entregar()
videojuego2.entregar()

contar_series_entregadas(lista_series)
contar_videojuegos_entregados(lista_videojuegos)
print(serie_mas_temporadas(lista_series))
print(videojuego_mas_horas(lista_videojuegos))