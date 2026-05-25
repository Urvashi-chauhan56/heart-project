pipeline {
    agent any

    environment {
        IMAGE_NAME = "urvashichauhan56/heart-project"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Urvashi-chauhan56/heart-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'

                    bat 'docker push %IMAGE_NAME%'
                }
            }
        }
    }
}