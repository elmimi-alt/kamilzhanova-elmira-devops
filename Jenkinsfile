pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
    }
    environment {
        STUDENT_NAME = 'Elmira'
        STUDENT_SURNAME = 'Kamilzhanova'
        STUDENT_GROUP = 'IT2-2304'
        STUDENT_ID = '37713'
        IMAGE_NAME = 'kamilzhanova-elmira-devops'
        CONTAINER_NAME = 'kamilzhanova-elmira-container'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/main.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 scripts/check_app.py'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    if docker container inspect "$CONTAINER_NAME" > /dev/null 2>&1; then
                        docker rm -f "$CONTAINER_NAME"
                    fi
                    docker run -d --name "$CONTAINER_NAME" -p 8000:8000 \
                        -e STUDENT_NAME -e STUDENT_SURNAME \
                        -e STUDENT_GROUP -e STUDENT_ID "$IMAGE_NAME"
                    python3 scripts/check_app.py http://127.0.0.1:8000
                    docker images "$IMAGE_NAME"
                    docker ps --filter "name=$CONTAINER_NAME"
                '''
            }
        }
    }
}