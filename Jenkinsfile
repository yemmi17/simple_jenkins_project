pipeline {
    agent any // любой доступный агент
    stages { 
        stage('Checkout') {
            steps{
                git 'https://github.com/yemmi17/simple_jenkins_project.git'
            }
        }
        stage('Install dependecies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }  
        stage('Run tests'){
            steps{
                sh 'python -m unittest test_api.py'
            }
        } 
        stage('Build Docker image'){
            steps{
                sh 'docker build -t my-python-app .'
            }
        }
        stage('Run Dockercontainer'){
            steps{ 
                sh 'docker run -d -p 5000:50 my-python-app'
            }
        }
    }
}