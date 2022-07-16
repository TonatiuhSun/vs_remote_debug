# vs_remote_debug
Remote debugging tutorial for Visual studio code, attach a debug to a remote running docker container

### Starting the Application
* Run using docker 
    * `docker build . -t remote_debug -f docker/Dockerfile`
    * `docker run -p 8000:8000 remote_debug bash -c "python3 -uB -m debugpy --listen 0.0.0.0:5005 -m src.web.app"`
* Run using docker-compose  
    * `docker-compose -f local_deployment/docker_compose_local.yml up`
* Local swagger URL is available at `http://{server-ip}:8081/docs#`