class Comment:
    ide = 0
    desc = ""

    def __init__(self,ide,desc):
        self.ide = ide
        self.desc = desc
        self.fecha = fecha

    def crear(self):
        self.ident = input('Digite la identificacion: ')
        self.nombre = input('Digite el nombre: ')
        self.paswd = input('Digite la contraseña para el usuario: ')


class Post(Comment):
    iden = 0
    titulo = ""
    fecha = ""

class User(Post):
    ident = 0
    nombre = ""
    paswd = ""

    def __init__(self,iden,titulo,fecha, ident, nombre, paswd):
        Post.__init__(self,iden,titulo, fecha)
        self.ident = ident
        self.nombre = nombre
        self.paswd = paswd

    def crear(self):
        self.ident = input('Digite la identificacion: ')
        self.nombre= input('Digite el nombre: ')
        self.paswd = input('Digite la contraseña para el usuario: ')







