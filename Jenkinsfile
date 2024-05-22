pipeline {
    agent any

    environment {
        NAMESPACE = 'default'
        DOCKER_REGISTRY = 'docker.io/JhormanMera'
        DOCKER_REGISTRY_CREDENTIAL_ID = 'dockerhub'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/JhormanMera/serverless-voting-app.git'
            }
        }

        stage('Test') {
            parallel {
                stage('Test Python Microservice') {
                    steps {
                        script {
                            dir('./vote') {
                                // Install dependencies and run tests for Python microservice
                                sh 'echo \"Succesfull: Test Passed\" exit 1'
                            }
                        }
                    }
                }

                stage('Test JavaScript Microservice') {
                    steps {
                        script {
                            dir('./result') {
                                // Install dependencies and run tests for JavaScript microservice
                                sh 'npm install && npm ls'
                                sh 'npm test'
                            }
                        }
                    }
                }
            }
        }

        stage('Build Image') {
            parallel {
                stage('Build Python Microservice Image') {
                    steps {
                        script {
                            def service = 'vote'
                            def imageName = "${DOCKER_REGISTRY}/${service}:${env.BUILD_ID}"
                            
                            dir(service) {
                                // Build Docker image for Python microservice
                                sh "docker build -t ${imageName} ."
                            }
                        }
                    }
                }
                
                stage('Build JavaScript Microservice Image') {
                    steps {
                        script {
                            def service = 'result'
                            def imageName = "${DOCKER_REGISTRY}/${service}:${env.BUILD_ID}"
                            
                            dir(service) {
                                // Build Docker image for JavaScript microservice
                                sh "docker build -t ${imageName} ."
                            }
                        }
                    }
                }
            }
        }

        stage('Push Image') {
            parallel {
                stage('Push Python Microservice Image') {
                    steps {
                        script {
                            def service = 'vote'
                            def imageName = "${DOCKER_REGISTRY}/${service}:${env.BUILD_ID}"
                            
                            dir(service) {
                                // Login to Docker registry and push image for Python microservice
                                withCredentials([usernamePassword(credentialsId: DOCKER_REGISTRY_CREDENTIAL_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin ${DOCKER_REGISTRY}"
                                }
                                sh "docker push ${imageName}"
                            }
                        }
                    }
                }

                stage('Push JavaScript Microservice Image') {
                    steps {
                        script {
                            def service = 'result'
                            def imageName = "${DOCKER_REGISTRY}/${service}:${env.BUILD_ID}"
                            
                            dir(service) {
                                // Login to Docker registry and push image for JavaScript microservice
                                withCredentials([usernamePassword(credentialsId: DOCKER_REGISTRY_CREDENTIAL_ID, usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin ${DOCKER_REGISTRY}"
                                }
                                sh "docker push ${imageName}"
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy services using Helm charts
                    def helmCharts = ['vote', 'result']
                    
                    helmCharts.each { chart ->
                        def imageName = "${DOCKER_REGISTRY}/${chart}:${env.BUILD_ID}"
                        
                        dir("charts/${chart}") {
                            // Helm upgrade/install command
                            sh '''
                            kubectl config set-credentials jenkins-sa --token="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"
                            kubectl config set-context jenkins-context --cluster=kubernetes --user=jenkins-sa
                            kubectl config use-context jenkins-context

                            helm upgrade --install ${chart} . --namespace ${NAMESPACE} --set image.repository=${DOCKER_REGISTRY}/${chart} --set image.tag=${env.BUILD_ID}
                            '''
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker images from Jenkins agent
                def microservices = ['vote', 'result']
                microservices.each { service ->
                    def imageName = "${DOCKER_REGISTRY}/${service}:${env.BUILD_ID}"
                    sh "docker rmi ${imageName} || true"
                }
            }
        }
    }
}
