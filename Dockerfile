FROM python:3.11

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installe les dépendances à partir du fichier requirements.txt
RUN pip install -r requirements.txt