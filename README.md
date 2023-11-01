# Bank Queue Notification System 

This system allows the creation of branches, tellers (employees) to those branches, customers to given branches.

It also allows customers to get a service from any branch by joining a queue at a given branch.

Then the tellers can pick a customer who is in queue, the customer gets an email notification (Currently: 
Using file based email backend for django) and once the customer is served, the teller can finish serving the customer 
and be available for the next customer. 

A teller can only take a customer in queue only if the previous customer is not in queue as `NEW`. There are three stages
for a customer in queue that is `0` for `NEW`, `1` for `IN_SERVICE` and `2` for `DONE`.

## Set up


1. Create a working folder
2. Open the folder in terminal/cmd
3. Download the zip file into the folder or run git clone `https://github.com/Rovine1999/Bank-queue-notification-system` 
4. Then run `cd Bank-queue-notification-system`
5. Create a virtual environment

    - In windows run `python -m virtualenv venv`

    - In Linux run `python3 -m virtualenv venv`

    N/B: You need to have `virtualenv` installed. To install it run `pip install virtualenv`

6. Activate your environment

    - In windows run `source ./venv/Scripts/activate`

    - In linux run `source ./venv/bin/activate`

7. Install requirements using `pip install -r requirements.txt`
8. Navigate to `bank` folder using `cd bank`
9. Make migrations and migrate if you don't have `db.sqlite3` file in your folder tree using `python manage.py makemigrations && python manage.py migrate`
10. Run the server `python manage.py runserver`
11. Open `Postman`
12. Import the `postman collection` in the working folder called `Banking system.postman_collection.json`.
13. Create an environment in postman if one is not created for you and add: 
    - `base_url`: `http://localhost:8000`
    - `token`: `<Update this after using the login endpoint under users module>`

14. You are all set, test out the entire collection **top down**

Postman documentation [here](https://documenter.getpostman.com/view/14081802/2s9YXbA5tH)

Create a super user, login in to admin dashboard and create `2 groups`
## Group 1 - `employee` group

Add this permissions to this group
```text
admin | log entry | Can add log entry
admin | log entry | Can change log entry
admin | log entry | Can delete log entry
admin | log entry | Can view log entry
auth | user | Can add user
auth | user | Can change user
auth | user | Can delete user
auth | user | Can view user
authtoken | Token | Can add Token
authtoken | Token | Can change Token
authtoken | Token | Can delete Token
authtoken | Token | Can view Token
authtoken | token | Can add token
authtoken | token | Can change token
authtoken | token | Can delete token
authtoken | token | Can view token
mainapp | branch | Can add branch
mainapp | branch | Can change branch
mainapp | branch | Can delete branch
mainapp | branch | Can view branch
mainapp | customer | Can add customer
mainapp | customer | Can change customer
mainapp | customer | Can delete customer
mainapp | customer | Can view customer
mainapp | employee queue assignment | Can add employee queue assignment
mainapp | employee queue assignment | Can change employee queue assignment
mainapp | employee queue assignment | Can delete employee queue assignment
mainapp | employee queue assignment | Can view employee queue assignment
notification | Can add notification
notification | Can change notification
notification | Can delete notification
notification | Can view notification
mainapp | queue | Can add queue
mainapp | queue | Can change queue
mainapp | queue | Can delete queue
mainapp | queue | Can view queue
transaction | Can add transaction
transaction | Can change transaction
transaction | Can delete transaction
transaction | Can view transaction
sessions | session | Can add session
sessions | session | Can change session
sessions | session | Can delete session
sessions | session | Can view session
```

## Group 2 - `customer` group

Add this permissions to this group

```text
admin | log entry | Can add log entry
admin | log entry | Can change log entry
admin | log entry | Can delete log entry
admin | log entry | Can view log entry
auth | permission | Can view permission
auth | user | Can change user
auth | user | Can view user
authtoken | Token | Can add Token
authtoken | Token | Can change Token
authtoken | Token | Can view Token
authtoken | token | Can add token
authtoken | token | Can change token
authtoken | token | Can view token
mainapp | branch | Can view branch
notification | Can view notification
mainapp | queue | Can add queue
mainapp | queue | Can view queue
transaction | Can view transaction
sessions | session | Can add session
sessions | session | Can change session
sessions | session | Can delete session
sessions | session | Can view session
```

## About role based access

This allows to identify between tellers (Employees) and customers. Customers have both the common and queue related 
permissions only in which they can add and view a queue but can't update nor delete.

Tellers have the ability to manage customers and also manage queues.


### Deployment to AWS EC2 instance.

1. Launch an EC2 Instance:
    - Log in to your AWS account and navigate to the EC2 dashboard.
    - Click "Launch Instance" to create a new EC2 instance. Choose an Amazon Machine Image (AMI) that suits your needs (e.g.,    Amazon Linux, Ubuntu).
    - Configure instance details, add storage, and set up security groups to allow incoming traffic on ports 22 (SSH) and 80 (HTTP).

2. Connect to your EC2 Instance:
    - Use SSH to connect to your EC2 instance. You can find the public IP address or DNS of your instance on the EC2 dashboard.
    - Use a command like this to connect: `ssh -i your-key-pair.pem` `admin@51.20.75.48`-(using your ec2 instance public ip)

3. Update and Upgrade the Packages:
    - Install and upgrade all the installed packages.
    - `sudo yum update -y`  # For Amazon Linux
    - `sudo apt update && sudo apt upgrade -y`  # For Ubuntu

4. Install Required Software:
    - Docker and docker-compose.
    - sudo apt install apt-transport-https ca-certificates curl software-properties-common
    - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    - sudo apt install docker-ce
    - sudo service docker start.
    

5. Clone/Upload Your Django Project:
    - Use git or any method you prefer to clone your Django project onto the EC2 instance.

6. Create a compose file as follows:
    ### Deployment to AWS EC2 instance.

1. Launch an EC2 Instance:
    - Log in to your AWS account and navigate to the EC2 dashboard.
    - Click "Launch Instance" to create a new EC2 instance. Choose an Amazon Machine Image (AMI) that suits your needs (e.g.,    Amazon Linux, Ubuntu).
    - Configure instance details, add storage, and set up security groups to allow incoming traffic on ports 22 (SSH) and 80 (HTTP).

2. Connect to your EC2 Instance:
    - Use SSH-client to connect to your EC2 instance. You can find the public IP address or DNS of your instance on the EC2 dashboard.
    - Use a command like this to connect: `ssh -i your-key-pair.pem` `admin@51.20.75.48`-(using your ec2 instance public ip)

3. Update and Upgrade the Packages:
    - Install and upgrade all the installed packages.
    - `sudo yum update -y`  # For Amazon Linux
    - `sudo apt update && sudo apt upgrade -y`  # For Ubuntu
4. Install Required Software:
    - docker and docker-compose.
    - sudo apt install apt-transport-https ca-certificates curl software-properties-common
   - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
   - sudo apt install docker-ce
   - sudo service docker start.
5. Clone/Upload Your Django Project:
    - Use git or any method you prefer to clone your Django project onto the EC2 instance.

6. Create a compose file as follows:

        `version: '3.9'

        services:
        db:
        image: postgres:latest
        restart: always
        environment:
            POSTGRES_PASSWORD: 8H3S;k}E*H?m
            POSTGRES_USER: postgres
            POSTGRES_DB: db1
        ports:
            - '5432:5432'
        volumes:
            - '/opt/psql-data/pp:/var/lib/postgresql/data'
        container_name: db

        # backend
        backend:
        build: ./backend/
        ports:
            - '8000:8000'

        # env_file:
        #   - fileName

        restart: always
        depends_on:
            - db
        container_name: backend

        entrypoint:
            ['./wait-for-it.sh', 'db:5432', '--', 'python', 'manage.py', 'runserver']`



7. Create a Dockerfile for the project as shown below.

        FROM python:3.9-slim

        WORKDIR /backend

        COPY . .

        EXPOSE 8000

        RUN chmod +x ./wait-for-it.sh

        ENTRYPOINT [ "python", "manage.py", "runserver" ]


9. Run the following command to start the container.

`docker-compose up --build --force-recreate --remove-orphans --no-deps;`

10. Access the application through the IP address or the link http://ec2-51-20-75-48.eu-north-1.compute.amazonaws.com/
