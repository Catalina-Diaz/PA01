# Este es un comentario
'''Este es un comentario de multiple linea'''
"Este es un comentario de multiple linea"

#Variables
nombrePersona = 'Catalina' #String
edad = 22 #int
numeroDecimal = 1.61 #Float
esMayorEdad = True #False Boolean

#Debug
print(nombrePersona) #Cata

#Listas = Arreglo, Array [] 0,1,2...
diasSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves']

print(diasSemana[2]) #Imprimir Miercoles

arrayMultiple = [1, 'hola', [5,6]]
print(arrayMultiple[2])#imprimir [5,6]
print(arrayMultiple[2][1])#imprimir 6

#Diccionarios = Objetos, Json {}
persona = {
    'nombre':'Catalina',
    'apellido':'Diaz',
    'edad':'22',
    'lenguajes':['Python', 'JavaScript'],
    #--nombrePersona:"Prueba",
}
print(persona['nombre']) #Catalina
print(persona['apellido']) #Diaz
print(persona['lenguajes'][1])#JavaScript
#--print(persona)#Diccionario

#Listas de disccionarios
personas = [
    {
    'nombre':'Catalina',
    'apellido':'Diaz',
    'edad':'22',
    'lenguajes':['Python', 'JavaScript'],
    },
    {
    'nombre':'Clara',
    'apellido':'D',
    'edad':'10',
    'lenguajes':['Java', '.Net'],
    },
    {
    'nombre':'Pedro',
    'apellido':'D',
    'edad':'12',
    'lenguajes':['Go', 'Rust'],
    },
]
print(personas[1]['lenguajes'][1]),

#Condiciones
if esMayorEdad == True:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

print("Terminado")