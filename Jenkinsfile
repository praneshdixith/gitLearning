pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
        VENV_DIR = 'venv'
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
                // Create a Python virtual environment
                sh "${PYTHON_ENV} -m venv ${VENV_DIR}"
            }
        }

        stage('Install Dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                sh """
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                // Activate virtual environment and run tests
                sh """
                source ${VENV_DIR}/bin/activate
                python -m unittest discover
                """
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
