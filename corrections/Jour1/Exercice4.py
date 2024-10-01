# Exercice 1

# def generate_even_numbers(max_n):
#     """Générateur qui produit les nombres pairs de 0 à max_n inclus."""
#     for n in range(0, max_n + 1):
#         if n % 2 == 0:
#             yield n


# # Test du générateur
# for num in generate_even_numbers(10):
#     print(num)

# # ou avec comprehension de generateur :

# def generate_even_numbers2(max_n):
#     """Générateur qui produit les nombres pairs de 0 à max_n inclus."""
#     for n in range(0, max_n + 1, 2):
#         yield n


# # Test du générateur
# for num in generate_even_numbers2(10):
#     print(num)


# Exercice 2

# def fibonacci():
#     """Générateur infini des nombres de Fibonacci."""
#     a, b = 0, 1
#     while True:
#         yield a
#         # Mise à jour des valeurs pour la prochaine itération
#         a, b = b, a + b


# Création du générateur
# fib_gen = fibonacci()

# Affichage des 10 premiers nombres de Fibonacci
# for _ in range(10):
#     print(next(fib_gen))


# Exercice 3

import time


def timer(func):
    """Décorateur qui mesure le temps d'exécution d'une fonction."""

    def wrapper(*args, **kwargs):
        start_time = time.time()  # Temps au début de l'exécution
        result = func(*args, **kwargs)  # Exécution de la fonction originale
        end_time = time.time()  # Temps à la fin de l'exécution
        elapsed_time = end_time - start_time  # Calcul du temps écoulé
        print(
            f"La fonction '{func.__name__}' a mis {elapsed_time:.5f} secondes pour s'exécuter."
        )
        return result  # Retourne le résultat de la fonction originale

    return wrapper


@timer
def compute_sum(n):
    """Calcule la somme des nombres de 1 à n."""
    return sum(range(1, n + 1))


compute_sum(1000000)
compute_sum(5000000)
compute_sum(10000000)

# Exercice 4

def repeat(n):
    """Décorateur qui exécute la fonction décorée n fois."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Bonjour!")


say_hello()

print()

@repeat(5)
def say_hello():
    print("Bonjour!")


say_hello()
