pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-api:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your GitHub repository
                git branch: 'main', url: 'https://github.com/praneshdixith/gitLearning.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image using the Dockerfile
                script {
                    dockerImage = docker.build(DOCKER_IMAGE, '-f Dockerfile .')
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run the unit tests inside the Docker container
                script {
                    dockerImage.inside {
                        sh 'python -m unittest discover'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace after build
            cleanWs()
        }
    }
}
