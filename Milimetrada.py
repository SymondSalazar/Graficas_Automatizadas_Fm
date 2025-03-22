import numpy as np
import matplotlib.pyplot as plt
#Se le pide al usuario para graficar los puntos en la hoja milimetrada
print("Ten en cuenta que los numeros decimales debes escribirlos con un punto. \n Ejemplo: 23.10 \nTambien ten en cuenta que los datos seran separados por una coma")

axis_x,axis_y= input("Digame que representa el eje x e y con palabras, Formato(Ejex,Ejey): ").split(",")

numerox,factorx = input("Ingrese el numero de datos en el eje x(los cm), ademas de su factor de escala (x,f.h): ").split(",")
numeroy,factory = input("Ingrese el numero de datos en el eje y(los cm), ademas de su factor de escala (y,f.v ): ").split(",")


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
x_points.insert(0,0)
y_points.insert(0,0)
print("---------------------------------------------")
print(f"Puntos del eje x: \n {x_points}\n")
print(f"Puntos del eje y: \n {y_points}\n")
print("---------------------------------------------")

print("Incertidumbre de los ejes: ")
print(f"x: {f_x/2}")
print(f"y: {f_y/2}\n")

points_to_plot = []
for i in range(int(input("Cuantos puntos deseas graficar?: "))):
  x,y = input(f"Ingrese el punto {i+1} (x,y): ").split(",")
  points_to_plot.append((float(x),float(y)))


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
plt.plot(np.array(x_points),y_lin,"-", label="Recta",color="#fff766")

#Los puntos tomados
plt.plot(close_points_cord_x,close_points_cord_y,"o",label="Datos Tomados", color="#ff6699",markersize=3)

plt.grid(True, linestyle='--', color='gray', linewidth=0.5)





#Los datos en x, y
plt.ylabel(axis_y)
plt.xlabel(axis_x)
plt.title(f"Previsualizacion de Gráfica {axis_y} vs {axis_x}")
plt.xticks(x_points,rotation = 90)
plt.yticks(y_points)
plt.legend()
plt.show()


print("-----------------------------------------------\n")
print(f"Probable ecuacion empirica:  \n {axis_y}= {round(m,2)} * {axis_x}  +({round(b,2)})")