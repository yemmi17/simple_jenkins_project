### Simple Jenkins Pipeline Project

Этот репозиторий содержит проект с автоматизированным CI/CD пайплайном на Jenkins. Пайплайн выполняет следующие шаги:

## 🚀 Функциональность

- Автоматическая сборка и тестирование после каждого push в репозиторий

- Создание виртуального окружения и установка зависимостей

- Запуск тестов с помощью unittest

- Сборка Docker-образа и запуск контейнера

## 📜 Структура репозитория
```
📂 simple_jenkins_project
├── 📂 app/                # Исходный код приложения
├── 📂 tests/              # Тесты
├── 📄 Dockerfile          # Конфигурация Docker-образа
├── 📄 requirements.txt    # Список зависимостей
├── 📄 Jenkinsfile         # CI/CD пайплайн для Jenkins
└── 📄 README.md           # Документация
```

## 🛠 Настройка и запуск

# 1. Установка зависимостей
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# 2. Локальный запуск приложения
```
python app.py
```
# 3. Запуск тестов
```
python -m unittest discover tests
```
## 🔧 Настройка CI/CD в Jenkins

# 1. Установка Jenkins и подключение к GitHub

- Добавьте репозиторий в Jenkins, указав URL GitHub

- Включите GitHub Webhook в настройках репозитория (Settings → Webhooks)

# 2. Структура Jenkinsfile

pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *') // Автозапуск каждые 5 минут, если нужно конечно ))
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/USERNAME/simple_jenkins_project.git'
            }
        }
        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 my-python-app'
            }
        }
    }
}

## 📌 Автоматический запуск

- Используйте GitHub Webhooks для автоматического триггера пайплайна при git push

- Или настройте pollSCM для проверки изменений раз в X минут

## 📢 Контакты

Если у вас есть вопросы или предложения, пишите в Issues или создавайте Pull Requests! 😊

