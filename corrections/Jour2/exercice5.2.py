#################################################################################
# Exercice 1

# test_addition.py

import ctypes

# Charger la bibliothèque
lib = ctypes.CDLL("./libaddition.so")  # Utilisez 'addition.dll' sur Windows

# Définir les types d'arguments et de retour
lib.addition.argtypes = (ctypes.c_int, ctypes.c_int)
lib.addition.restype = ctypes.c_int

# Appeler la fonction
resultat = lib.addition(10, 15)
print(f"Le résultat de l'addition est: {resultat}")

#################################################################################
# Exercice 2

# setup.py

from setuptools import setup, Extension

module = Extension("factorielle_module", sources=["factorielle_module.c"])

setup(
    name="FactorielleModule",
    version="1.0",
    description="Module d'extension pour calculer la factorielle",
    ext_modules=[module],
)

# test_factorielle.py
import factorielle_module

resultat = factorielle_module.factorielle(5)
print(f"5! = {resultat}")

#################################################################################
# Exercice 3

# fibonnacci.py

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


import time

start = time.time()
result = fibonacci(35)
end = time.time()

print(f"Fibonacci(35) = {result}")
print(f"Temps écoulé: {end - start} secondes")

# Conversion en Cython (fibonacci.pyx):

def fibonacci(int n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibonacci.pyx")
)

# test_fibonnacci.py

import time
from fibonacci import fibonacci

start = time.time()
result = fibonacci(35)
end = time.time()

print(f"Fibonacci(35) = {result}")
print(f"Temps écoulé: {end - start} secondes")


####################################################################
# Exercice 5

# test_point.py

import ctypes

# Définir la structure Point
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# Charger la bibliothèque
lib = ctypes.CDLL('./libpoint.so')

# Définir la fonction
lib.deplacer_point.argtypes = (ctypes.POINTER(Point), ctypes.c_int, ctypes.c_int)
lib.deplacer_point.restype = None

# Créer un point et le déplacer
p = Point(10, 20)
print(f"Avant déplacement: x={p.x}, y={p.y}")

lib.deplacer_point(ctypes.byref(p), 5, -3)
print(f"Après déplacement: x={p.x}, y={p.y}")
