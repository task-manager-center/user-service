# User service for task manager

## Requirements
- Python 3.8+
- [Docker](https://www.docker.com)

```bash
# create docker network
docker network create task-manager 
# run postgres in docker
docker run -p 5438:5432 --network=task-manager -e POSTGRES_DB=user_service -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres postgres
# add DB_URI to environment (docker path)
DB_URI=postgresql+asyncpg://postgres:postgres@172.20.0.1:5438/user_service
# build service
docker build -t user-service .
# run service in docker
docker run -it --network=task-manager -p 8123:88 user-service
```