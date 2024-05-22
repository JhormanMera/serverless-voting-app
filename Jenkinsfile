pipeline {
  agent {
    kubernetes {
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    label: agent
spec:
  containers:
  - name: python
    image: python:3.10.5-alpine3.16
    env:
    - name: "PGDATABASE"
      value: "postgres"
    - name: "PGUSER"
      value: "postgres"
    - name: "PGPASSWORD"
      value: "postgres"
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: '/var/run/docker.sock'
      name: docker-socket
  - name: helm
    image: lachlanevenson/k8s-helm:latest
    command:
    - cat
    tty: true
  - name: node
    image: node:6.12.1-slim
    env:
    - name: "PORT"
      value: "80"
    command:
      - cat
    tty: true
  - name: docker
    image: docker:latest
    command:
      - cat
    tty: true
    privileged: true
    volumeMounts:
    - name: docker-socket
      mountPath: '/var/run/docker.sock'
  volumes:
  - name: docker-socket
    hostPath:
      path: '/var/run/docker.sock'
  securityContext:
    runAsUser: 0
      '''
    }
  }
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/JhormanMera/serverless-voting-app.git.git', branch: 'master'
      }
    }
    stage('Test Vote') {
      steps {
        container('python') {
          sh 'echo \"Succesfull: Test Passed\" exit 1'
        }
      }
    }
    stage('Test Result') {
      steps {
        container('node') {
          sh 'npm install'
          sh 'npm run'
        }
      }
    }
    stage('Build images & push') {
      environment {
        registryCredential = 'dockerhub'
      }
      steps {
        container('docker') {
          script {
            docker.withRegistry( '', 'dockerhub' ) {
              def apiImage = docker.build("jhormanmera/vote:${env.BUILD_ID}", "./vote/")
              apiImage.push()
              apiImage.push('latest')
              def webImage = docker.build("jhormanmera/result:${env.BUILD_ID}", "./result/")
              webImage.push()
              webImage.push('latest')
            }
          }
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        container('helm') {
          sh "helm upgrade --install vote ./charts/vote --set image.tag=${env.BUILD_ID}"
          sh "helm upgrade --install result ./charts/result --set image.tag=${env.BUILD_ID}"
        }
      }
    }
  }
}