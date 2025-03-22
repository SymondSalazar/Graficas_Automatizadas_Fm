import numpy as np
import matplotlib.pyplot as plt
print("---------------------------------------------\n")
axis_x,axis_y = input("Ingrese que representa cada eje (Eje_x , Eje_y):  ").split(",")
print("\n---------------------------------------------\n")
prom_x = input("¿Necesitas sacar promedios de datos para el eje x? (s,n)")
prom_y = input("¿Necesitas sacar promedios de datos para el eje y? (s,n)")
print("\n---------------------------------------------\n")
x_points = []
y_points = []
x=0
y=0
for i in range(int(input("Cuantos puntos deseas graficar?: "))):
    print("\n---------------------------------------------\n")
    print(f"Datos para el Punto({i+1})")
    if prom_x == "s":
        x_prom = input(f" Ingrese todos los datos de {axis_x.lower()} separados por coma (d1,d2,d3,dn): ").split(",")
        for elem in x_prom:
            x += float(elem)
   
        x = x/len(x_prom)
    else:
        x = float(input(f" Ingrese el dato de {axis_x.lower()}:  "))
    if prom_y == "s":
        y_prom = input(f" Ingrese todos los datos de {axis_y.lower()} separados por coma (d1,d2,d3,dn): ").split(",")
        for elem in y_prom:
            y += float(elem)
        y = y/len(y_prom)
    else:
        y = float(input(f"Ingrese el dato de {axis_y.lower()}: " ))


    x_points.append(x)
    y_points.append(y)


x_points = np.array(x_points)
y_points = np.array(y_points)



# Transformamos X e Y a logaritmos
log_x = np.log(x_points)
log_y = np.log(y_points)

# Ajustamos una recta en la escala log-log
coef, cov = np.polyfit(log_x, log_y, 1, cov=True)  
pendiente_error = np.sqrt(cov[0, 0])

# Función de la recta de tendencia en la escala original
y_lin = np.exp(coef[1]) * x_points**coef[0]

# Graficamos los datos y la recta de tendencia
plt.plot(x_points, y_lin, label=f"Recta de tendencia (pendiente={coef[0]:.2f})", color='red')
plt.scatter(x_points, y_points, label="Datos originales", color='blue')

# Configurar escalas logarítmicas en ambos ejes
plt.xscale('log')
plt.yscale('log')
plt.xlabel(f"{axis_x}")
plt.ylabel(f"{axis_y}")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.title(f"Previsualizacion Grafica en Log- Log de {axis_y} vs {axis_x}")
plt.show()
print("\n---------------------------------------------\n")
