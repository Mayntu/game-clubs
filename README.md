# 🚀 Game Clubs

## 🛠️ Tech Stack

 - **Python (FastAPI)**
 - **PostgreSQL**
 - **Docker**

## ⚡ Первый запуск проекта

### 1️⃣ Клонировать репозиторий

```sh
git clone https://github.com/mayntu/gake-clubs.git
cd game-clubs
```

### 2️⃣ Запустить PostgreSQL контейнер

```sh
docker compose up --build
```

### 3️⃣ Создать виртуальную среду python (3.12)

```sh
python -m venv venv
```

### 4️⃣ Активировать виртуальную среду

#### Windows:

```sh
.\venv\Scripts\activate
```

#### macOS/Linux:

```sh
source venv/bin/activate
```

### 5️⃣ Установить библиотеки

```sh
python -m pip install -r requirements.txt
```

### 6️⃣ Создать .env файл с переменными окружения

#### Windows: 

_создайм .env файл и заполняем его_

#### Linux

```sh
touch .env
```

_заполняем .env_

#### Пример:

```
  DB_HOST=localhost
  DB_PORT=5432
  DB_PASSWORD=admin
  DB_USERNAME=admin
  DB_NAME=clubs
```

### 7️ Запустить приложение

```sh
python app.py
```

## ⚡ Обычный запуск проекта

### 1️⃣ Запустить PostgreSQL контейнер

```sh
docker compose up --build
```

### 2️⃣ Активировать виртуальную среду

#### Windows:

```sh
.\venv\Scripts\activate
```

#### macOS/Linux:

```sh
source venv/bin/activate
```

### 3️⃣ Запустить приложение

```sh
python app.py
```

## 📂 Структура проекта

📦 your-repo
├── 📁 src                # Главная папка проекта
├── 📁 venv               # Виртуальное окружение
├── 📄 .env               # Скрытые переменные
├── 📄 .gitignore         # gitignore
├── 📄 app.py             # Входная точка приложения
├── 📄 requirements.txt   # Нужные библиотеки
├── 📄 Dockerfile         # Docker конфигурация
├── 📄 docker-compose.yml # Файл Docker Compose
└── 📄 README.md          # Документация

📝 TODO
...
