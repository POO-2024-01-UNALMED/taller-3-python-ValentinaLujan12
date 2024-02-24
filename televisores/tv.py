from televisores.marca import Marca
from televisores.control import Control

class TV:
    _canal: int = 1
    _volumen: int = 1
    _precio: int = 500
    _control: Control
    _numTV: int = 0    #Atributo de clase

    def __init__(self, marca: Marca, estado: bool) -> None:
        self._marca: Marca = marca
        self._estado: bool = estado
        TV._numTV += 1

    #Para marca
    def setMarca(self, marca: str) -> None:
        self._marca = marca
    
    def getMarca(self) -> Marca:
        return self._marca
    
    #Para canal 
    def setCanal(self, canal: str) -> None:
        if (self._estado == True and (self._canal >= 1 and self._canal <= 120)):
            self._canal = canal
    
    def getCanal(self) -> int:
        return self._canal
     
    #Para precio 
    def setPrecio(self, precio: str) -> None:
        self._precio = precio
    
    def getPrecio(self) -> int:
        return self._precio
     
    #Para volumen 
    def setVolumen(self, volumen: str) -> None:
        if (self._estado == True and (self._volumen >= 0 and self._volumen <= 7)):
            self._volumen = volumen
    
    def getVolumen(self) -> int:
        return self._volumen
      
    #Para control
    def setControl(self, control: str) -> None:
        if isinstance(control, Control):
            self._control = control
    
    def getControl(self):
        return self._control

    #numTV
    @classmethod
    def setNumTV(cls, num: int) -> None:
        cls._numTV = num

    @classmethod
    def getNumTV(cls) -> int:
        return cls._numTV
    
    #Metodos de estado 
    def turnOn(self) -> None:
        self._estado: bool = True

    def turnOff(self) -> None:
        self._estado: bool = False
    
    def getEstado(self) -> bool:
        return self._estado

    #Metodos de canal 
    def canalUp(self) -> None:
        if (self._estado and (self._canal >= 1 and self._canal < 120)):
            self._canal += 1
    
    def canalDown(self) -> None:
        if (self._estado and (self._canal > 1 and self._canal <= 120)):
            self._canal -= 1

    #Metodos de volumen 
    def volumenUp(self) -> None:
        if (self._estado and (self._volumen >= 0 and self._volumen < 7)):
            self._volumen += 1
    
    def volumenDown(self) -> None:
        if (self._estado and (self._volumen > 0 and self._volumen <= 7)):
            self._volumen -= 1
    
