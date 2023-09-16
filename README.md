# rdms-backend

## Command For Docker
### Build Docker Image 
run below command in same directory with Dockerfile
```
docker build -t {ImageName} .
```

### Create And Run Database Container
```
docker run --name {ContainerName} -p 3306:3306 {ImageName}
```

### View All Container
```
docker ps -a
```

### Stop Running Container
```
docker stop {ContainerName}
```

### Remove Docker Image
```
docker rm {ImageName}
```