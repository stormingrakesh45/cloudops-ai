pipeline{
    agent any 

    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage("Build Docker Images"){
            steps{
                sh 'docker build -t cloudops-ai:${BUILD_NUMBER} .'
            }
        }
    }
}
