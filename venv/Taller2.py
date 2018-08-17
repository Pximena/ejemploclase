list1=[]
coment = {}
post = {}
user = {}

class Comment:
    ide = 0
    desc = ""
    idp = 0

    def crear_c(self):
        self.ide = input('digite la identificacion del post: ')
        self.ide = input ('digite la identificacion del comentario: ')
        self.desc = input('Digite el comentario: ')
        coment["idp"] = self.idp
        coment["ide"] = self.ide
        coment["desc"] = self.desc
        list1.append(coment)



class Post(Comment):
    iden = 0
    titulo = ""
    idu = 0


    def crear_p(self):
        #self.idu = input('Digite la identificacion del usuario: ')
        #for z in user:
        for k, v in futbolistas.items():
            print("%s -> %s" % (k, v))

            '''if v == self.idu:
                    self.iden = input('Digite la identificacion del post: ')
                    self.titulo = input('Digite el contenido: ')
                    post["idu"] = self.idu
                    post["ident"] = self.iden
                    post["nombre"] = self.titulo
                    list1.append(post)
                else:
                    print("El usuariono se encuntra registrado:")'''


class User(Post):
    ident = 0
    nombre = ""


    def crear_u(self):
        self.ident = input('Digite la identificacion: ')
        self.nombre= input('Digite el nombre: ')
        user["ident"] = self.ident
        user["nombre"] = self.nombre
        list1.append(user)


print("Menu de opciones")
print("1. Crear Usuario")
print("2. Crear Post")
print("3. Crear Comment")
print("4. Buscar comment")
print("5. Salir")

r = input("Digite la opcion escogida: ")
cons = User()
while int(r)!= 5:


    if int(r)==1:
        cons.crear_u()
    elif int(r)==2:
        cons.crear_p()
    elif int(r)==3:
        cons.crear_c()
    elif int(r)==4:
        print("Digite el id del comentario: ")

    print("Menu de opciones")
    print("1. Crear Usuario")
    print("2. Crear Post")
    print("3. Crear Comment")
    print("4. Buscar comment")
    print("5. Salir")
    r = input("Digite la opcion escogida: ")

print("Hasta pronto!!!")




#print(list1)










