# Health-care-ecom-service
Service to replicate the healh care ecommerce backend system.

# Install the requirements:
pip install -r requirements.txt

# Run the project

## Step1: Set up the environment variables
1. `export MONGODB_URI="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"`
2. `export DATABASE_NAME="databasename"`

## Step2: Run the binary
uvicorn main:app --reload

