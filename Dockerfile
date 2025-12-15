# --- STAGE 1 : BUILD ---
FROM python:3.11-slim-buster AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --- STAGE 2 : PRODUCTION (FINAL IMAGE) ---
FROM python:3.11-slim-buster
WORKDIR /app

# Copie des dépendances installées
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copie du code de l'application (main.py)
# ----------------------------------------
COPY app/main.py .
# ----------------------------------------

EXPOSE 5000

# Commande de démarrage (main.py)
# ----------------------------------------
CMD ["python", "main.py"]
# ----------------------------------------