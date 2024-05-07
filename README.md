# Aplicación de Votación de Ejemplo sin Servidor con Docker
Esta es una aplicación sin servidor construida con Docker. Lee más en el [repositorio de Serverless Docker](https://github.com/bfirsh/serverless-docker).

## Arquitectura

Consiste en un servidor de entrada simple que escucha las solicitudes HTTP. Toda la otra funcionalidad de la aplicación se ejecuta bajo demanda como contenedores de Docker para cada solicitud HTTP:

- **vote**: La aplicación web de votación, como un contenedor CGI que sirve una única solicitud HTTP.
- **record-vote-task**: Un contenedor que procesa un voto en segundo plano, ejecutado por la aplicación de votación.
- **result**: La aplicación web de resultados, como un contenedor CGI.

#### Arquitectura del despliegue
![arquitectura](/resources/img/arq_image.png)

## Ejecución

Ejecuta en este directorio:

```bash
$ make
```

### Integrantes

* [Camilo Gonzalez V.](https://github.com/camilogonzalez7424)
* [Jhorman Mera](https://github.com/JhormanMera)

### Tecnologías usadas en el desarrollo del proyecto
* Docker
* Docker compose
* Kubernetes
* Helm
* Jenkins
* Elk
* Prometheus
* Grafana

### Estrategia de Branching

* #### Github Flow: 
Se basa en un flujo de trabajo basado en branches que permite a equipos de desarrollo enfocarse principalmente en la entrega continua. A diferencia de Git Flow, no existen los branches de “releases”, ya que está pensado para que la implementación en producción ocurra con frecuencia, incluso varias veces al día si es posible. 

En esta estrategia de branching, en el repositorio tenemos dos tipos de branches: 

* main (o master): el branch de código principal, es el que contiene el código que está listo para producción. 

* features: los branches de funcionalidades que permiten el desarrollo en paralelo. 

Principios que seguir: 

* El código que está en main debe poder implementarse en producción en cualquier momento. 

* Cuando se crean nuevos feature branches, se deben crear con nombres descriptivos. Por ejemplo, feature/add-new-account-type. 

#### Para ejecutar los microservicios con docker

* Es necesario tener ````docker y docker compose```` instalado en el sistema
* Dentro de la carpeta principal, ejecutar el comando ````docker-compose up -d```` para levantar todos los servicios al mismo tiempo 

#### Para ejecutar los microservicios con kubernetes

*  






