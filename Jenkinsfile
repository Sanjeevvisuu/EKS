pipeline {
    agent { label 'slave1' }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub') // Environment variable for Docker Hub credentials
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/EKS.git'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo 'Building the Django application as a Docker image...'
                    sh '''
                    # Ensure that the Jenkins user can access Docker (optional if sudo is configured)
                        docker-compose build
                    '''
                }
            }
        }

        stage('Docker Image Push') {
            steps {
                script {
                    echo 'Pushing application to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        # Log in to Docker Hub
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        # Tag and push the image to Docker Hub
                           docker tag django_travel $DOCKER_USERNAME/travel_app:latest
                           docker push $DOCKER_USERNAME/travel_app:latest
                        '''
                    }
                    echo 'Docker image pushed to Docker Hub.'
                }
            }
        }

        stage('Running the image') {
            steps {
                script {
                    echo 'Running the Docker image...'
                    sh '''
                    # Ensure that the Jenkins user can access Docker (optional if sudo is configured)
                         docker run -d -p 8000:8000 $DOCKER_USERNAME/travel_app:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...' // Cleanup after build completes, regardless of success or failure
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
