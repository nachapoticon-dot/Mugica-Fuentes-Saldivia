class Biblioteca:
    """Coordina los préstamos entre los libros y los socios."""

    def __init__(self, nombre):
        self._nombre = nombre
        # Diccionarios para encontrar rápido por ISBN y por DNI
        self._libros = {}
        self._socios = {}

    @property
    def nombre(self):
        return self._nombre

    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios:
            raise ValueError(f"Ya existe un socio con DNI {socio.dni}")
        self._socios[socio.dni] = socio

    def _buscar_libro(self, isbn):
        if isbn not in self._libros:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        return self._libros[isbn]

    def _buscar_socio(self, dni):
        if dni not in self._socios:
            raise ValueError(f"No existe un socio con DNI {dni}")
        return self._socios[dni]

    def prestar(self, isbn, dni):
        libro = self._buscar_libro(isbn)
        socio = self._buscar_socio(dni)
        # Validamos todo antes de cambiar algo, así un error no deja nada a medio hacer
        if not libro.disponible:
            raise ValueError(f"El libro '{libro.titulo}' no está disponible")
        if not socio.puede_pedir():
            raise ValueError(f"{socio.nombre} ya tiene el máximo de libros")
        libro.prestar()
        socio.agregar_libro(libro)

    def devolver(self, isbn, dni):
        libro = self._buscar_libro(isbn)
        socio = self._buscar_socio(dni)
        if libro not in socio.libros:
            raise ValueError(f"{socio.nombre} no tiene el libro '{libro.titulo}'")
        socio.quitar_libro(libro)
        libro.devolver()

    def libros_disponibles(self):
        return [libro for libro in self._libros.values() if libro.disponible]
