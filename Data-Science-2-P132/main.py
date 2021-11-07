import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("star_with_gravity.csv")

mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius, mass)
plt.title("Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass, gravity)
plt.title("Mass Vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()