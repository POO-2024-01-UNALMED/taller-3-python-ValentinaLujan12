class Marca: 
    def __init__(self, nombre: str) -> None:
        self._nombre: str = nombre
    
    def setNombre(self, nombre: str) -> None:
        self._nombre: str = nombre

    def getNombre(self) -> str:
        return self._nombre
    