f = open(r"C:\Users\FREDDY\Desktop\Automatizar\mil.txt","r")
f.readline()
f.readline()
f.readline()
axis_x,axis_y = rf"{f.readline()}".removesuffix(r"\n").split(",")
print(axis_y,axis_x) 
#Se obtiene la medida de los ejes: x e y

