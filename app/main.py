import time
import os
import redis

# --- Configuration Redis ---
# L'hostname 'redis' correspond au nom du service dans docker-compose.yaml
try:
    # Tente de se connecter au service 'redis' sur le port par défaut
    cache = redis.Redis(host='redis', port=6379)
except Exception as e:
    print(f"Échec de la connexion à Redis: {e}")
    cache = None
    
COUNTER_KEY = 'global_counter'

app = Flask(__name__)

def get_hit_count():
    """Tente de se connecter à Redis et d'obtenir le compteur avec résilience."""
    retries = 5
    while True:
        try:
            if cache:
                count = cache.get(COUNTER_KEY)
                # Retourne "0" si la clé n'existe pas
                return count.decode() if count is not None else "0" 
            else:
                return "Erreur: Redis non connecté" 
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def show_counter():
    """Route principale qui affiche la valeur actuelle et les boutons."""
    try:
        count = get_hit_count()
        # Utilisation d'un formulaire pour garantir que les requêtes sont bien des POST
        return f"""
        <h1>Le compteur actuel est : {count}</h1>
        <form method="POST" action="/increment"><button type="submit">Incrémenter (+)</button></form>
        <form method="POST" action="/decrement"><button type="submit">Décrémenter (-)</button></form>
        """
    except Exception as e:
        return f"<h1>Erreur de connexion au compteur: {e}</h1>"

@app.route('/increment', methods=['POST'])
def increment():
    """Incrémente le compteur."""
    if cache:
        cache.incr(COUNTER_KEY)
        count = cache.get(COUNTER_KEY).decode()
        return f'<h1>Compteur Incrémenté. Nouvelle valeur : {count}</h1><p><a href="/">Retour</a></p>'
    return "Erreur: Redis non connecté"

@app.route('/decrement', methods=['POST'])
def decrement():
    """Décrémente le compteur."""
    if cache:
        cache.decr(COUNTER_KEY)
        count = cache.get(COUNTER_KEY).decode()
        return f'<h1>Compteur Décrémenté. Nouvelle valeur : {count}</h1><p><a href="/">Retour</a></p>'
    return "Erreur: Redis non connecté"

if __name__ == "__main__":
    # Initialisation du compteur à 0 lors du premier lancement
    if cache and cache.get(COUNTER_KEY) is None:
        cache.set(COUNTER_KEY, 0)
        print("Compteur initialisé à 0.")
    app.run(host='0.0.0.0', port=5000)