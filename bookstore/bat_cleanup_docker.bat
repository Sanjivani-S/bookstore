docker ps -q -a                     
docker stop $(docker ps -q)       
docker rm $(docker ps -a -q)
docker network rm $(docker network ls -q)
docker volume rm $(docker volume ls -q)