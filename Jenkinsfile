pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Code is already checked out by Declarative: Checkout SCM
                echo 'Using code from package-manager Git repository'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python --version
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build and Test') {
            steps {
                bat '''
                python -m py_compile app.py
                python app.py
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'app.py', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
