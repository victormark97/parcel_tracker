FROM python:3.10-slim

# 2. Setăm folderul de lucru în container (ca un 'cd' automat)
WORKDIR /code

# 3. Copiem fișierul de dependențe și le instalăm
# Facem asta separat pentru caching (eficiență)
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

# 4. Copiem tot codul sursă în container
COPY ./app /code/app


# 5. Comanda care rulează serverul
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]