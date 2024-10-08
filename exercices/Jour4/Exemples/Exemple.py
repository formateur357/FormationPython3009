# Importation de la bibliothèque requests qui permet d'effectuer des requêtes HTTP
import requests

# Envoi d'une requête GET à l'URL spécifiée
response = requests.get("http://api.exemple.com/data")

# Vérification si la requête a réussi (code de statut 200)
# if response.status_code == request.codes.ok
#   traitement des donnees
# else:
#   response.raise_for_status() <= Leve une exception HTTPError

if response.status_code == 200: 
    print("requete reussi")  # Affichage d'un message de succès
else:
    # Affichage d'un message d'erreur avec le code de statut
    print(f"Erreur: {response.status_code}")

# Accès au contenu brut de la réponse
response.content

# Accès au contenu de la réponse sous forme de chaîne de caractères
response.text

# Tentative de conversion du contenu de la réponse en format JSON
response.json()

# Définition des paramètres à envoyer avec la requête
params = {"api_key": "your_key", "parma2": "valeur2"}

# Envoi d'une nouvelle requête GET avec des paramètres d'URL
response = requests.get("http://api.exemple.com/data", params=params)

# Définition des données à envoyer dans une requête POST
data = {"key": "value"}

# Envoi d'une requête POST à l'URL spécifiée avec les données
response = requests.post("http://api.exemple.com/data", data=data)

# Définition des en-têtes de la requête, spécifiant que le contenu est au format JSON
headers = {"Content-Type": "application/json", "Authorization": "Bearer your_key"}

# Envoi d'une requête GET avec des en-têtes personnalisés
response = requests.get("http://api.exemple.com/data", headers=headers)

data = response.json()

# data = {'nom': Alice, 'age': 30}
nom = data['nom']
age = data['age']

# Authentification HTTP Basic
from requests.auth import HTTPBasicAuth

response = requests.get("http://api.exemple.com", auth=HTTPBasicAuth('utilisateur', 'mot_de_passe'))

