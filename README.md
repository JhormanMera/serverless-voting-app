# <b> **_Aplicación de Votación_** </b>

Esta es una aplicación sin servidor construida con Docker. Lee más en el [repositorio de example-voting-app](https://github.com/bfirsh/funker-example-voting-app).

**Nota:** Por requerimientos del presente proyecto se modifico el código fuente.

## <b> _Arquitectura_ </b>

Consiste en un servidor de entrada simple que escucha las solicitudes HTTP. Toda la otra funcionalidad de la aplicación se ejecuta bajo demanda como contenedores de Docker para cada solicitud HTTP:

- **_vote_**: La aplicación web de votación, como un contenedor CGI que sirve una única solicitud HTTP.
- **_process-vote_**: Un contenedor que procesa un voto en segundo plano, ejecutado por la aplicación de votación.
- **_result_**: La aplicación web de resultados, como un contenedor CGI.

## <b> _Arquitectura del despliegue_ </b>
![arquitectura](/resources/img/arq_image.png)

## <b> _Ejecución_ </b>

Ejecuta en este directorio:




## <b> _Tecnologías usadas en el desarrollo del proyecto_ </b> 🛠️

* Docker
* Docker compose
* Kubernetes
* Helm
* Jenkins
* Elk
* Prometheus
* Grafana

## <b> _Estrategia de Branching_ </b> 📄

* ### Github Flow: 
Se basa en un flujo de trabajo basado en branches que permite a equipos de desarrollo enfocarse principalmente en la entrega continua. A diferencia de Git Flow, no existen los branches de “releases”, ya que está pensado para que la implementación en producción ocurra con frecuencia, incluso varias veces al día si es posible. 

En esta estrategia de branching, en el repositorio tenemos dos tipos de branches: 

- main (o master): el branch de código principal, es el que contiene el código que está listo para producción. 

- features: los branches de funcionalidades que permiten el desarrollo en paralelo. 

Principios que seguir: 

- El código que está en main debe poder implementarse en producción en cualquier momento. 

- Cuando se crean nuevos feature branches, se deben crear con nombres descriptivos. Por ejemplo, feature/add-new-account-type. 

#### Para ejecutar los microservicios con docker

- Es necesario tener ````docker y docker compose```` instalado en el sistema
- Dentro de la carpeta principal, ejecutar el comando ````docker-compose up -d```` para levantar todos los servicios al mismo tiempo 

## <b> _Para ejecutar los microservicios con kubernetes_ </B>

  


## <b> _Por:_ </b>
<b> 😊😊 _**Ing. DevOps:**_ 😊😊 </b>

+ [Camilo González Velasco](https://github.com/camilogonzalez7424 "Camilo G.")
+ [Jhorman Mera](https://github.com/JhormanMera "Jhorman M.")


<br>

[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

<!--[![forthebadge](https://forthebadge.com/images/badges/docker-container.svg)](https://forthebadge.com)-->