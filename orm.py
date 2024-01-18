import tkinter as tk
import random
import math
import json
import sqlite3

#declaracion variables globales
personas = []
numeropersonas = 20

class Persona:
    def __init__(self):
        self.posx = random.randint(0,1024)
        self.posy = random.randint(0,1024)
        self.radio = 30
        self.direccion = random.randint(0,360)
        self.color = "blue"
        self.entidad = ""
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=self.color)
    def mueve(self):
        self.colisiona()
        lienzo.move(
            self.entidad,
            math.cos(self.direccion),
            math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def colisiona(self):
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy > 1024:
            self.direccion += math.pi
#guardo archivo json
def guardarPersonas():
    print("Guardo a los jugadores")
   #guardo los personajes en SQL
    conexion = sqlite3.connect("jugadores.sqlite3")
    cursor = conexion.cursor()
    for persona in personas:
        cursor.execute('''
            INSERT INTO jugadores
            VALUES (
                NULL,
                '''+str(persona.posx)+''',
                '''+str(persona.posy)+''',
                '''+str(persona.radio)+''',
                '''+str(persona.direccion)+''',
                "'''+str(persona.color)+'''",
                "'''+str(persona.entidad)+'''"
           )
           ''')
    conexion.commit()
    conexion.close()
#creo una ventana      
raiz = tk.Tk()

#en la ventana creo un lienzo
lienzo = tk.Canvas(raiz,width=900,height=900)
lienzo.pack()

#boton de guardar
boton = tk.Button(raiz,text="Guarda",command=guardarPersonas)
boton.pack()

#cargar personas desde el disco duro
try:
    carga = open("jugadores.json",'r')
    cargado = carga.read()
    cargadolista = json.loads(cargado)
    for elemento in cargadolista:
        perdona = Persona()
        persona.__dir__,update(elemento)
        personas.append(persona)
except:
    print("error")
    
#creo en lienzo en la ventana
if len(personas) == 0:
    numeropersonas == 500
for i in range(0,numeropersonas):
    personas.append(Persona())

#instancias de personas en el la coleccion
for persona in personas:
    persona.dibuja()

#bucle repetitivo
def bucle():
    for persona in personas:
        persona.mueve()
    raiz.after(10,bucle)

#ejecuto el bucle
bucle()


raiz.mainloop()



        
