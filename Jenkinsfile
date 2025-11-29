pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-username/your-python-project.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build and Test') {
            steps {
                bat 'python -m py_compile app.py'
                bat 'python app.py'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'app.py', fingerprint: true
            }
        }
    }
}
