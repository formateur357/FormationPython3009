#########################################################################
# Exercice 1

import threading  # Module pour travailler avec les threads
import time  # Module pour utiliser sleep() et gérer le temps


def print_numbers():
    """Imprime les nombres de 1 à 5 avec une pause d'une seconde entre chaque."""
    for i in range(1, 6):
        print(f"Nombre: {i}")
        time.sleep(1)  # Pause de 1 seconde


def print_letters():
    """Imprime les lettres de 'a' à 'e' avec une pause de 1,5 seconde entre chaque."""
    for letter in ["a", "b", "c", "d", "e"]:
        print(f"Lettre: {letter}")
        time.sleep(1.5)  # Pause de 1,5 seconde


# Création des threads en spécifiant la fonction cible
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Démarrage des threads
t1.start()
t2.start()

# Attente de la fin des threads pour s'assurer que le programme ne se termine pas prématurément
t1.join()
t2.join()

print("Programme terminé.")

#########################################################################
# Exercice 2

import threading
import time


def print_numbers():
    """Imprime les nombres de 1 à 5 avec une pause d'une seconde entre chaque."""
    for i in range(1, 6):
        print(f"Nombre: {i}")
        time.sleep(1)


def print_letters():
    """Imprime les lettres de 'a' à 'e' avec une pause de 1,5 seconde entre chaque."""
    for letter in ["a", "b", "c", "d", "e"]:
        print(f"Lettre: {letter}")
        time.sleep(1.5)


# Création du thread pour les nombres (thread non-démon)
t1 = threading.Thread(target=print_numbers)

# Création du thread pour les lettres (thread démon)
t2 = threading.Thread(target=print_letters)
t2.daemon = True  # Définir le thread comme démon

# Démarrage des threads
t1.start()
t2.start()

# Attente uniquement pour t1
t1.join()

print("Programme terminé.")


#########################################################################
# Exercice 3

import threading

# Variable globale partagée
counter = 0

# Création d'un verrou
lock = threading.Lock()


def increment():
    """Incrémente la variable 'counter' 1000 fois en utilisant un verrou pour éviter les conditions de course."""
    global counter
    for _ in range(1000):
        lock.acquire()  # Acquisition du verrou
        counter += 1  # Section critique
        lock.release()  # Libération du verrou


# Création des threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

# Démarrage des threads
t1.start()
t2.start()

# Attente de la fin des threads
t1.join()
t2.join()

print(f"Valeur finale du compteur: {counter}")

# Alternative pour le context with

def increment():
    """Incrémente la variable 'counter' 1000 fois en utilisant un verrou avec 'with'."""
    global counter
    for _ in range(1000):
        with lock:  # Acquisition et libération automatique du verrou
            counter += 1  # Section critique


#########################################################################
# Exercice 4

import concurrent.futures  # Pour utiliser ThreadPoolExecutor
import requests  # Pour effectuer des requêtes HTTP

# Liste des URL à télécharger
urls = [
    "https://www.python.org",
    "https://www.google.com",
    "https://www.github.com",
    # Ajoutez plus d'URL si nécessaire
]


def fetch(url):
    """Télécharge le contenu de l'URL spécifiée."""
    try:
        response = requests.get(url)
        print(f"Succès pour {url}")
        return response.content  # Retourne le contenu de la réponse
    except Exception as e:
        print(f"Erreur pour {url}: {e}")
        return None


# Création d'un pool de threads avec un maximum de 5 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Soumettre les tâches au pool de threads
    futures = {executor.submit(fetch, url): url for url in urls}

    # Récupérer les résultats au fur et à mesure qu'ils sont disponibles
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
            # Vous pouvez traiter 'data' ici si nécessaire
        except Exception as exc:
            print(f"L'URL {url} a généré une exception: {exc}")


#########################################################################
# Exercice 5

import concurrent.futures  # Pour utiliser ProcessPoolExecutor
import requests

# Liste des URL à télécharger
urls = [
    "https://www.python.org",
    "https://www.openai.com",
    "https://www.github.com",
    # Ajoutez plus d'URL si nécessaire
]


def fetch(url):
    """Télécharge le contenu de l'URL spécifiée."""
    try:
        response = requests.get(url)
        print(f"Succès pour {url}")
        return response.content
    except Exception as e:
        print(f"Erreur pour {url}: {e}")
        return None


# Création d'un pool de processus avec un maximum de 5 processus
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    # Soumettre les tâches au pool de processus
    futures = {executor.submit(fetch, url): url for url in urls}

    # Récupérer les résultats
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
            # Traiter 'data' si nécessaire
        except Exception as exc:
            print(f"L'URL {url} a généré une exception: {exc}")

#########################################################################
# Bonus

import time

start_time = time.time()  # Temps de départ

# ... votre code ...

end_time = time.time()  # Temps de fin
print(f"Temps d'exécution: {end_time - start_time} secondes")

# Observations :

# Multithreading : Pour les tâches I/O-bound, le multithreading peut être plus rapide car le GIL est libéré lors des opérations I/O, permettant à d'autres threads de s'exécuter.
# Multiprocessing : Pour les tâches CPU-bound, le multiprocessing permet un parallélisme réel, améliorant les performances.

"""
Notes supplémentaires :

Threads démons : Utilisez-les avec précaution. Les threads démons ne sont pas idéaux pour les tâches qui nécessitent une fin propre ou une sauvegarde d'état.
Verrous : Ils sont essentiels pour éviter les conditions de course, mais peuvent entraîner des deadlocks s'ils ne sont pas utilisés correctement.
GIL (Global Interpreter Lock) : En CPython, le GIL empêche l'exécution simultanée de plusieurs threads Python natifs. Le multiprocessing contourne cette limitation.
Choix entre threading et multiprocessing : Dépend du type de tâche :
I/O-bound (liées aux entrées/sorties) : Préférez le multithreading.
CPU-bound (gourmandes en calcul) : Préférez le multiprocessing.

"""
