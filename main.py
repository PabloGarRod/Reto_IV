from RETO_IV import Serie, Videojuego


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


if __name__ == '__main__':
    serie1 = Serie("Berserk", 5, False, "Seinen", "Kintaro Miura")
    serie2 = Serie("SNK", 4, False, "Acción", "Hajime Isayama")
    serie3 = Serie("Rick y Morty", 4, True, "comedia", "Dan Harmon")
    serie4 = Serie("Dragon Ball", 6, True, "Shonen", "Akira Toriyama")
    serie5 = Serie("Juego de tronos", 8, True, "fantasía", "George R.R. Martin")

    lista_series = [serie1, serie2, serie3, serie4, serie5]

    videojuego1 = Videojuego("League of Legends", 15, True, "Moba", "Riot Games")
    videojuego2 = Videojuego("World of Warcraft", 20, False, "MMORPG", "Blizzard")
    videojuego3 = Videojuego("Call of Duty", 16, False, "Shooter", "Activision")
    videojuego4 = Videojuego("Super Mario", 68, False, "Plataformas", "Nintendo")
    videojuego5 = Videojuego("Fortnite", 26, False, "Battle Royale", "Epic Games")

    lista_videojuegos = [videojuego1, videojuego2, videojuego3, videojuego4, videojuego5]

    serie1.entregar()
    serie4.entregar()
    videojuego5.entregar()
    videojuego2.entregar()

    contar_series_entregadas(lista_series)
    contar_videojuegos_entregados(lista_videojuegos)
    print("Información sobre la serie con más temporadas: ")
    print(serie_mas_temporadas(lista_series))
    print("Información sobre el videojuego con más horas: ")
    print(videojuego_mas_horas(lista_videojuegos))
