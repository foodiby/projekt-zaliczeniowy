# Wybieramy lekki obraz Pythona
FROM python:3.9-slim

# Ustawiamy folder roboczy w kontenerze
WORKDIR /app

# Kopiujemy listę bibliotek i instalujemy je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę kodu
COPY . .

# Informujemy, na jakim porcie działa aplikacja
EXPOSE 5000

# Komenda startowa
CMD ["python", "app.py"]