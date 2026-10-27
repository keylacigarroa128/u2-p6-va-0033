# Keyla Paola Cigarroa Palacios | Fecha 27/octubre/2026
import matplotlib.pyplot as plt
import numpy as np


cantidad_productos = [100,150,200,300,500]
precio = [4000,7000,9000,12000,18000]

plt.plot(cantidad_productos,precio)
plt.show()

# Personalizar graficas 
plt.plot(cantidad_productos,precio,color="red",marker="*",linestyle="dashed",linewidth=2,markersize=12)
plt.title("Ventas de walmart 0033")
plt.xlabel("cant prod")
plt.ylabel("precio")
plt.show()

print("Keyla Paola Cigarroa Palacios | Fecha 27/octubre/2026")