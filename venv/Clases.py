class Persona:
    nombre = ""
    edad = 0
    pais = ""

    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def saludar(self):
        print("hola mi nombre es: {}".format(self.nombre))

    def despedir(self):
        print('hasta pronto: {}'.format(self.nombre))

    def comprar(self):
        print('puedo comprar x cosa')

    #crear una instancia dela clase

ximena = Persona("ximena Figueroa",21,'Colombia')

print(ximena.nombre)
print(ximena.edad)
print(ximena.pais)
ximena.saludar()
ximena.comprar()
ximena.despedir()

class Estudiante(Persona):
        colegio = ""

        def __init__(self,nombre, edad, pais,colegio):
            Persona.__init__(self,nombre,edad,pais)
            self.colegio = colegio
        def get_colegio(self):
            print('su colegio es: {}'.format(self.colegio))

andrea = Estudiante('Andrea',25,'chile','INEM')
andrea.saludar()
andrea.comprar()
andrea.despedir()
andrea.get_colegio()

class Universidad(Estudiante):
    programa = ""

    def __init__(self,nombre,edad,pais,colegio,programa):
        Estudiante.__init__(self,nombre,edad,pais,colegio)
        self.programa = programa

    def get_programa(self):
        print('su programa es: {}'.format(self.programa))
cesmag = Universidad('Carlos', 41, 'Italia', 'aaa','ing sistemas')

cesmag.saludar()
cesmag.comprar()
cesmag.despedir()
cesmag.get_colegio()
cesmag.get_programa()


class Cargo:
    cargo = ""
    def __init__(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        print('Su cargo es: {}'.format(self.cargo))

class Trabajador(Persona,Cargo):
    sueldo = 0

    def __init__(self, nombre, edad,pais,cargo, sueldo):
        Persona.__init__(self,nombre,edad,pais)
        Cargo.__init__(self, cargo)
        self.sueldo = sueldo

    def get_sueldo(self):
        print('su salario es de: {}'.format(self.sueldo))

diana = Trabajador('Diana', 32, 'Argentina', 'Arquitecta', 1000000)

diana.saludar()
diana.comprar()
diana.despedir()
diana.get_cargo()
diana.get_sueldo()













