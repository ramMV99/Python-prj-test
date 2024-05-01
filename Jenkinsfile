pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Python application'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests'
                sh 'python -m unittest discover'
            }
        }
        stage('Run Task Manager') {
            steps {
                echo 'Running Task Manager'
                sh 'python task_manager.py'
            }
        }
    }
}

