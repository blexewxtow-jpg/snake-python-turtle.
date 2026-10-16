import turtle
t =turtle.Turtle()
x=0
y=0
vx=20
vy=0
def actualizar():
    global x, y
    
    posiciones=[]
    for segmento in segmentos:
        posiciones.append((segmento.xcor(),segmento.ycor()))
    anterior_x = x
    anterior_y = y
    x = x + vx
    y = y + vy
    t.goto(x,y)
    for i, segmento in enumerate(segmentos):
        if i==0:
            segmento.goto(anterior_x, anterior_y)
        else:
            segmento.goto(posiciones[i - 1])    
    if t.distance(manzana) < 20:
        ultimo = segmentos[-1]
        cola_x = ultimo.xcor()
        cola_y = ultimo.ycor()

        nueva_x = random.randrange(-200, 201, 20)
        nueva_y = random.randrange(-200, 201, 20)
        manzana.goto(nueva_x, nueva_y)
        print("¡Me comí la manzana!")
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(cola_x, cola_y)
        segmentos.append(nuevo_cuerpo)
    ventana.ontimer(actualizar, 100)
t.shape("square")
t.color("green")
t.penup()
def izquierda():
    global vx, vy
    vx=-20
    vy=0
ventana = turtle.Screen()
ventana.listen()
ventana.onkeypress(izquierda,"Left")
def derecha():
    global vx, vy
    vx=20
    vy=0
ventana.onkeypress(derecha,"Right")
def arriba():
    global vx,vy
    vx=0
    vy=20
ventana.onkeypress(arriba,"Up")
def abajo():
    global vx,vy
    vx=0
    vy=-20
ventana.onkeypress(abajo,"Down")    
manzana=turtle.Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
import random 
manzana_x = random.randrange(-200, 201, 20)
print(manzana_x)
import random
manzana_y = random.randrange(-200, 201, 20)
print(manzana_y)
manzana.goto(manzana_x, manzana_y)
segmentos = []

cuerpo = turtle.Turtle()
cuerpo.shape("square")
cuerpo.color("green")
cuerpo.penup()
cuerpo.goto(-20, 0)

segmentos.append(cuerpo)




actualizar()

turtle.done()
