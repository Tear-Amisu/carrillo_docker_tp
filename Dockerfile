# --- STAGE 1 ---
FROM python:3.11-slim-buster
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application (main.py)
# ----------------------------------------
COPY app/main.py .
# ----------------------------------------

EXPOSE 5000

# Commande de démarrage (main.py)
# ----------------------------------------
CMD ["python", "main.py"]
# ----------------------------------------