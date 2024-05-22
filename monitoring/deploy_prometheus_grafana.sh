#!/bin/bash

# Añadir el repositorio de Helm para Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Actualizar los repositorios de Helm
helm repo update

# Instalar Prometheus desde el repositorio prometheus-community
helm install prometheus prometheus-community/prometheus

# Exponer el servicio de Prometheus
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext

# Acceder al servicio de Prometheus mediante minikube
minikube service prometheus-server-ext

# Añadir el repositorio de Helm para Grafana
helm repo add grafana https://grafana.github.io/helm-charts

# Instalar Grafana desde el repositorio grafana
helm install grafana grafana/grafana

# Exponer el servicio de Grafana
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext

# Acceder al servicio de Grafana mediante minikube
minikube service grafana-ext

# Obtener la contraseña del administrador de Grafana
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
