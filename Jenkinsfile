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

        stage('Ensure python3-venv Installed') {
            steps {
                // Install python3-venv if not already installed
                sh '''
                if ! python3 -m venv --help >/dev/null 2>&1; then
                    echo "Installing python3-venv..."
                    sudo apt-get update
                    sudo apt-get install -y python3-venv
                else
                    echo "python3-venv is already installed."
                fi
                '''
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
