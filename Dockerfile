FROM python:3.10-slim
        RUN apt-get update && apt-get install -y ffmpeg
        WORKDIR /app
        COPY requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt
        COPY . .
        CMD ["python", "main.py"]
        ```
    *   **"Commit changes"** tugmasini bosib saqlang.

---

### Oxirgi tekshiruv:
Hammasini to'g'ri qilgan bo'lsangiz, asosiy sahifada mana bu **3 ta fayl** turishi kerak:
1. `main.py`
2. `requirements.txt`
3. `Dockerfile`


