## 🤖 AI SQL Automation using LangChain and OpenAI

This project allows you to interact with your SQL Server database using natural language.
Instead of writing SQL queries manually, you can ask questions in plain English, and the AI will generate and execute SQL queries automatically.

---

# 📌 Features

* Connect to SQL Server using Windows Authentication
* Ask questions in natural language
* Automatically generates SQL queries
* Executes queries and returns results
* Uses OpenAI GPT model for intelligent responses
* Beginner-friendly project structure

---

# 🛠️ Technologies Used

* Python
* LangChain
* OpenAI GPT-4o-mini
* SQLAlchemy
* PyODBC
* Microsoft SQL Server
* dotenv

---

# 📁 Project Structure

```
AI_SQL_AUTOMATION/
│
├── main.py
├── .env
├── requirements.txt
└── README.md


# 💬 Example Questions

You can ask questions like:

```
List all tables
```

```
Show top 5 customers by sales
```

```
Count total orders
```

```
Show total revenue
```

---

# 🧠 How it works

1. User enters a question
2. LangChain SQL Agent converts it into SQL query
3. SQL query is executed on SQL Server
4. Results are returned in natural language

---

# 🔒 Requirements

* Python 
* SQL Server installed
* ODBC Driver 17 for SQL Server
* OpenAI API Key

---

# 📸 Example Output

```
Please ask your question: list all tables

Answer:
Customers, Orders, Products

```

AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.
2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
OPENAI_API_KEY



# 👨‍💻 Author

Jayachandra

---

# ⭐ If you like this project, please star the repository!
