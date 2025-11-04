pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup Python') {
      steps {
        sh 'python -m venv venv || true'
        sh '. venv/bin/activate && pip install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh '. venv/bin/activate && pytest'
      }
      post {
        always {
          archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
        }
      }
    }
  }
}
