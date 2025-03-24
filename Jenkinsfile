pipeline {
    agent any
    stages { 
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yemmi17/simple_jenkins_project.git'
            }
        }

 /*     Т.к разраб клоун немного и делал все на винде, через wsl. Сначала делал, а потом думал, но убирать не хочу ))  
        пусть лежит тут и напоминает мне о былой рукожопости
        stage('Install Docker') { 
            steps {
                sh '''
                    if ! command -v docker &> /dev/null
                    then
                        echo "Docker not found! Installing..."
                        sudo apt update
                        sudo apt install -y docker.io
                        sudo systemctl start docker
                        sudo systemctl enable docker
                        sudo usermod -aG docker $USER
                        echo "Docker installed successfully!"
                    else
                        echo "Docker is already installed."
                    fi
                '''
            }
        }*/

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    export PATH=$PWD/venv/bin:$PATH
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    export PATH=$PWD/venv/bin:$PATH
                    python -m unittest test_api.py  
                '''
            }
        } 

        stage('Build Docker image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }

        stage('Run Docker container') {
            steps { 
                sh 'docker run -d -p 5000:5000 my-python-app'
            }
        }
    }
}
