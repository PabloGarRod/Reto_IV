class Entregable:

    def __init__(self):
        self.entregado = None

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado


class Serie(Entregable):
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


class Videojuego(Entregable):
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
        return f"{self.titulo}, {self.horas_estimadas}, {self.entregado}, entregado: {self.entregado}, {self.genero}, {self.compañía} "
