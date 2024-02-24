class Control:
    def __init__(self) -> None:
        self._tv = None
    
    def setTv(self, tv: str) -> None:
        self._tv = tv
    
    def getTv(self) -> str:
        return self._tv
    
    #Metodos de estado 
    def turnOn(self) -> None:
        self._tv.turnOn()

    def turnOff(self) -> None:
        self._tv.turnOff()

    #Metodos de canal 
    def canalUp(self) -> None:
        self._tv.canalUp()
    
    def canalDown(self) -> None:
        self._tv.canalDown()

    #Metodos de volumen 
    def volumenUp(self) -> None:
        self._tv.volumenUp()
    
    def volumenDown(self) -> None:
        self._tv.volumenDown()

    #Para canal 
    def setCanal(self, canal: int) -> None:
        self._tv.setCanal(canal)

    #Para volumen 
    def setVolumen(self, volumen: str) -> None:
        self._tv.setVolumen(volumen)

    def enlazar(self, tv) -> None:
        self._tv = tv
        self._tv.setControl(self)
    