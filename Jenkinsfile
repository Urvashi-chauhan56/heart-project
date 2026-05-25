pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Urvashi-chauhan56/heart-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t heart-project .'
            }
        }
    }
}