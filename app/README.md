# Health-care-ecom-service
Service to replicate the healh care ecommerce backend system.

# Install the requirements:

```bash
pip install -r requirements.txt
```

# Run the project

## Step1: Set up the environment variables
1. 

```bash
export MONGODB_URI="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

```
2. 
```bash
export DATABASE_NAME="databasename"
```

## Step2: Run the binary
uvicorn main:app --reload

# Run the project using docker

## Create a .env file 

Put below in the env file.
1. MONGODB_URI=value
2. DATABASE_NAME=value

Note: Don't use \"\" in the value.

## Important commands
1. See Images: ```docker image ls```
2. Build Image: ```docker build -t health-care-service```    
3. Remove Image: ```docker rmi -f dd22e8a4640d``` 
4. Inspect container: ```docker container inspect health-care-container```  
5. Run Docker container: ```docker run   --name health-care-container  --env-file ./{.env file path} -p 80:80 -t health-care-service```
6. Delete container: ```docker rm health-care-container```