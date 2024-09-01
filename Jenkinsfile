pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your GitHub repository
                git branch: 'main', url: 'https://github.com/praneshdixith/gitLearning.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Install Python and pip
                sh "${PYTHON_ENV} -m pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh "${PYTHON_ENV} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                // Run the unit tests
                sh "${PYTHON_ENV} -m unittest discover"
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
