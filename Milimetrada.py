import numpy as np
import matplotlib.pyplot as plt
import random as rd
#Se obtienen los datos a partir de un archivo mil.txt

f = open(r"mil.txt","r")
f.readline()
title = rf"{f.readline()}".removesuffix(r"\n")

f.readline()
axis_x,axis_y = rf"{f.readline()}".removesuffix(r"\n").split(",")
f.readline()
var_y,var_x = f.readline().strip().split(",")
f.readline()
#Se obtiene la medida de los ejes x e y
numerox,numeroy = f.readline().strip().split(",")
f.readline()
#Se obtienen el factor de escala de los ejes x e y 
factorx,factory = f.readline().strip().split(",")
f.readline(),f.readline(),f.readline()

#Se obtienen los datos de los puntos que se graficaran
points_to_plot = []

i=0
x,y= 0,0
for lines in f:
    if i % 2 == 0:
        x_raw = lines.strip().split(",")
        
        for elem in x_raw:
            x += float(elem)
        x = x/len(x_raw)
    else:
        y_raw = lines.strip().split(",")

        for elem in y_raw:
            y += float(elem)
        y = y/len(y_raw)
        points_to_plot.append((x,y))
        x,y = 0,0
    i+=1
f.close()

# Distancia de los cuadritos en la hoja milimetrada
f_x = float(factorx)/10
f_y = float(factory)/10


def find_closest_coords(x_points, y_points, target_x, target_y, f_x, f_y):
    # Buscar el punto más cercano en el eje X
    closest_x = min(x_points, key=lambda x: abs(x - target_x))
    n_x = (target_x - closest_x) / f_x

    # Si n_x es negativo, tomamos el valor anterior en el eje X
    if n_x < 0:
        closest_x = x_points[x_points.index(closest_x) - 1]
        n_x = (target_x - closest_x) / f_x

    # Buscar el punto más cercano en el eje Y
    closest_y = min(y_points, key=lambda y: abs(y - target_y))
    n_y = (target_y - closest_y) / f_y

    # Si n_y es negativo, tomamos el valor anterior en el eje Y
    if n_y < 0:
        closest_y = y_points[y_points.index(closest_y) - 1]
        n_y = (target_y - closest_y) / f_y

    return closest_x, round(n_x), closest_y, round(n_y)

# Datos de los puntos en los ejes
x_points = []
y_points = []
n = 0

#Genera los puntos en x y
for i in range(int(numerox)):
    n += float(factorx)
    x_points.append(round(n,2))

n=0
for i in range(int(numeroy)):
    n += float(factory)
    y_points.append(round(n,2))


plt.text(x, y, f'{i+1} ({x}, {y})', fontsize=8, ha='right', color='black')


print("---------------------------------------------")
print(f"Puntos del eje x: \n {x_points}\n")
print(f"Puntos del eje y: \n {y_points}\n")
print("---------------------------------------------")

print("Incertidumbre de los ejes: ")
print(f"x: {f_x/2}")
print(f"y: {f_y/2}\n")




print("""
---------------------------------------------
Los datos que dara son:
  El eje mas cercano en x e y, aparte de un parametro n
  n: Representa el numero de cuadrados partiendo desde el eje dado
  En el eje x representa el numero de cuadrados a la derecha
  En el eje y representa el numero de cuadrados hacia arriba

---------------------------------------------""")

close_points_cord_x = []
close_points_cord_y = []
# Analizar los puntos
for point in points_to_plot:
    target_x, target_y = point
    closest_x, n_x, closest_y, n_y = find_closest_coords(x_points, y_points, target_x, target_y, f_x, f_y)
    close_points_cord_x.append(round(closest_x+f_x*n_x,2))
    close_points_cord_y.append(round(closest_y+f_y*n_y,2))
    print(f"Punto ({target_x}, {target_y}):")
    print(f"  Eje X cercano: {closest_x}, n para X: {n_x}")
    print(f"  Eje Y cercano: {closest_y}, n para Y: {n_y}")
    print("---------------------------------------------")

close_points_cord_x = np.array(close_points_cord_x)
close_points_cord_y = np.array(close_points_cord_y)



#Arma automaticamente la recta
#Una recta de la forma y = mx *b
m,b = np.polyfit(close_points_cord_x,close_points_cord_y,1)
y_lin = m*np.array(x_points)+b


#Se agarra dos puntos aleatorios para calcular la pendiente
x_1 = x_points[0] + f_x * rd.randint(0, 10)
x_2 = x_points[-2] + f_x * rd.randint(0, 10)

y_1 = m*x_1 + b
y_2 = m*x_2 + b

#Calculo donde se veria en la grafica milimetrada
closest_x_1, n_x_1, closest_y_1, n_y_1 = find_closest_coords(x_points, y_points, x_1, y_1, f_x, f_y)
closest_x_2, n_x_2, closest_y_2, n_y_2 = find_closest_coords(x_points, y_points, x_2, y_2, f_x, f_y)
points_m_x = [closest_x_1+f_x*n_x_1,closest_x_2+f_x*n_x_2]
points_m_y = [closest_y_1+f_y*n_y_1,closest_y_2+f_y*n_y_2]

b = -(find_closest_coords(x_points, y_points, 0, -b, f_x, f_y)[2] + f_y*find_closest_coords(x_points, y_points, 0, -b, f_x, f_y)[3])



for i, (x, y) in enumerate(zip(points_m_x, points_m_y)):
    plt.text(x+6*f_x, y-6*f_y, f'P{i+1} ({x:.2f}, {y:.2f})', fontsize=8, ha='right', color='red',weight="bold")

###Calculo de la pendiente
pendiente = (points_m_y[1]-points_m_y[0])/(points_m_x[1]-points_m_x[0])

plt.plot(np.array(x_points),y_lin,"-", label=rf"$\text{{Ecuacion empirica: }} {var_y} = {pendiente:.2f}*{var_x} + ({b:.2f})$",color="#fff766")

#Los puntos tomados
plt.plot(close_points_cord_x,close_points_cord_y,"o",label="Datos Tomados", color="#ff6699",markersize=3)
#Puntos aleatorios de le recta
plt.plot(points_m_x,points_m_y,"o",label = "Puntos para el calculo de la pendiente", color="red",markersize=12)
plt.grid(True, linestyle='--', color='gray', linewidth=0.5)

for i, (x, y) in enumerate(points_to_plot):
    plt.text(x, y, f'P{i+1} ({x}, {y})', fontsize=8, ha='right', color='#ff6699',weight="bold")




#Los datos en x, y
plt.ylabel(axis_y)
plt.xlabel(axis_x)
plt.title(rf"{title}")
plt.xticks(x_points,rotation = 90)
plt.yticks(y_points)
plt.legend()
plt.show()
