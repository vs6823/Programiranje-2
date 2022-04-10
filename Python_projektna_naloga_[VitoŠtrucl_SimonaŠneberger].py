import pylab
import numpy as np
from scipy.interpolate import UnivariateSpline
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

start = datetime(2010, 1, 1)
end = datetime(2022, 1, 1)

#Inicializacija in dodajanje grafa na osi
fig, ax = plt.subplots(3, 2)



#Plotanje podatkov
location = Point(46.05108, 14.50513, 70)
data = Daily(location, start, end)
data = data.fetch()
ax[0, 0].set_title("Ljubljana")
ax[0, 0].plot(data['tavg'],color='purple',label='Povprečna temperatura')
ax[0, 0].plot(data['tmax'],color='red',label='Največja temperatura')
ax[0, 0].plot(data['tmin'],color='yellow',label='Najnižja temperatura')

ax[0, 1].set_title("Ljubljana")
ax[0, 1].plot(data['prcp'],color='blue',label='Padavine')


location = Point(46.05108, 15.3837, 70)
data = Daily(location, start, end)
data = data.fetch()
ax[1, 0].set_title("Maribor")
ax[1, 0].plot(data['tavg'],color='purple')
ax[1, 0].plot(data['tmax'],color='red')
ax[1, 0].plot(data['tmin'],color='yellow')

ax[1, 1].set_title("Maribor")
ax[1, 1].plot(data['prcp'],color='blue')


location = Point(45.314317, 13.34127, 70)
data = Daily(location, start, end)
data = data.fetch()
ax[2, 0].set_title("Piran")
ax[2, 0].plot(data['tavg'],color='purple')
ax[2, 0].plot(data['tmax'],color='red')
ax[2, 0].plot(data['tmin'],color='yellow')

ax[2, 1].set_title("Piran")
ax[2, 1].plot(data['prcp'],color='blue')

#interpolira
#Označbe osi
ax[0, 0].set_ylabel("Temperatura [°C]")
ax[0, 0].set_xlabel("Čas [dnevi]")

ax[1, 0].set_ylabel("Temperatura [°C]")
ax[1, 0].set_xlabel("Čas [dnevi]")

ax[2, 0].set_ylabel("Temperatura [°C]")
ax[2, 0].set_xlabel("Čas [dnevi]")

ax[0, 1].set_ylabel("Padavine [mm]")
ax[0, 1].set_xlabel("Čas [dnevi]")

ax[1, 1].set_ylabel("Padavine [mm]")
ax[1, 1].set_xlabel("Čas [dnevi]")

ax[2, 1].set_ylabel("Padavine [mm]")
ax[2, 1].set_xlabel("Čas [dnevi]")
#Legenda in shranjevanje
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.02),fancybox=True, shadow=True, ncol=5)
#fig.legend()
fig.tight_layout()

#Shranjevanje
"""
ax[0, 0].grid(which='minor', alpha=0.2)
ax[0, 0].grid(which='major', alpha=0.5)

ax[1, 0].grid(which='minor', alpha=0.2)
ax[1, 0].grid(which='major', alpha=0.5)

ax[2, 0].grid(which='minor', alpha=0.2)
ax[2, 0].grid(which='major', alpha=0.5)

ax[0, 1].grid(which='minor', alpha=0.2)
ax[0, 1].grid(which='major', alpha=0.5)

ax[1, 1].grid(which='minor', alpha=0.2)
ax[1, 1].grid(which='major', alpha=0.5)

ax[2, 1].grid(which='minor', alpha=0.2)
ax[2, 1].grid(which='major', alpha=0.5)
"""

t = ["Tema najinega projekta je: »Analiza podnebnih sprememb v zadnjih 20ih letih«. Zaradi lepšega grafičnega prikaza in dostopnost podatkov sva se omejila na zadnjih 10 let.",
"Za analizo sva izbrala 3 slovenska mesta: Ljubljano, Maribor in Piran.",
"Osredotočila sva se na temperaturo in padavine. Na začetku sva imela v planu pobrati podatke iz spleta (Arso, posamezne vremenske postaje,...).",
"Med iskanjem pa sva odkrila python knjižnico meteostat, ki preko API-ja pridobi vse željene podatke s pomočjo danih koordinat.",
"Podatki so pridobljeni tako, da glede na lokacijo poišče najbližjo vremensko postajo in prebere njene podatke."]
for line in t:
    print(line)

plt.savefig('GRAF.pdf', format='pdf', dpi=2000,bbox_inches="tight")
plt.show()



