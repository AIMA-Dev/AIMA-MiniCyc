# AIMA MiniCyc

<a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=figma,py,qt,docker,grafana"/></a>

Industrial application to control and monitor the "MiniCyc" particle accelerator (Cyclotron) designed by AIMA Developpement

## Setup Docker

To run the MiniCyc application in a Docker container, follow these steps:

1. Make sure Docker is installed on your system.
2. Clone this repository to your machine.
3. Navigate to the project directory:
   ```bash
   cd AIMA-MiniCyc/grafanaStreaming
   ```
4. Start the Docker container using Docker Compose:
    ```bash
    docker-compose up -d
    ```
6. Once the containers are up and running, you can access the application via your web browser:
  - MiniCyc Application: http://localhost:8080
  - Grafana (Monitoring): http://localhost:3000
7. Use the following credentials to log in to Grafana:
  - Username: admin
  - Password: admin

Make sure to replace admin with the appropriate username and password if you have modified the default settings in your Grafana configuration.
