import numpy as np
import matplotlib.pyplot as plt

# DigiPot Values
x = np.array([
28,
30,
32,
34,
35,
40,
41,
44,
45,
50,
51,
56,
57,
62,
65,
70,
71,
75,
80])

# Outdoor Temperature HeatPump
y = np.array([
-21.5,
-17.5,
-14,
-10.5,
-8.8,
-1.4,
-0.1,
3.7,
5.1,
10.5,
11.5,
16.1,
17,
20.9,
23.1,
26.4,
27,
29.4,
32.1])

# Anpassa ett tredjegradspolynom
coeffs = np.polyfit(x, y, 3)   # Koefficienter [a, b, c, d] för ax^3 + bx^2 + cx + d
poly = np.poly1d(coeffs)

# Skapa en jämn x-vektor för att rita kurvan
x_fit = np.linspace(min(x), max(x), 200)
y_fit = poly(x_fit)

# Skriv ut resultatet
print("Anpassat polynom:")
print(poly)

# Plotta data och den anpassade kurvan
plt.scatter(x, y, color='red', label="Mätdata")
plt.plot(x_fit, y_fit, color='blue', label="Tredjegradspolynom")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Kurvanpassning med tredjegradspolynom")
plt.show()
