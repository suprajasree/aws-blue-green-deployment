\# 🚀 Production-Style Zero-Downtime Blue-Green Deployment Pipeline

A production-inspired DevOps project demonstrating **Zero-Downtime Blue-Green Deployment** on **AWS EC2** using **Docker**, **Nginx**, **GitHub Actions**, and **Flask**.

---

# 📖 Project Overview

This project simulates a real-world production deployment pipeline where new application versions are released without downtime using the **Blue-Green Deployment Strategy**.

The application is containerized with Docker and deployed on an AWS EC2 instance. Nginx acts as the reverse proxy that switches production traffic between Blue and Green environments after successful health checks.

The deployment process is fully automated using GitHub Actions.

---

# 🎯 Objectives

- Deploy Dockerized applications on AWS EC2
- Implement Blue-Green Deployment
- Achieve Zero Downtime deployments
- Automate deployments using GitHub Actions
- Configure Nginx Reverse Proxy
- Perform Health Checks before deployment
- Automatically switch production traffic
- Support Rollback deployment strategy

---

# 🏗️ Architecture

```
                     Developer

                         │
                         │
                    Git Push
                         │
                         ▼

                 GitHub Repository
                         │
                         ▼

               GitHub Actions Workflow
                         │
                    SSH Deployment
                         │
                         ▼

                 AWS EC2 Ubuntu Server
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼

      Blue Container         Green Container
        Port 5001              Port 5002
              │                     │
              └──────────┬──────────┘
                         │
                         ▼

                Nginx Reverse Proxy
                         │
                         ▼

                  Production Traffic
```

---

# ⚙️ Technology Stack

### Cloud

- AWS EC2

### Containerization

- Docker

### Web Server

- Nginx

### CI/CD

- GitHub Actions

### Backend

- Python
- Flask

### Operating System

- Ubuntu Linux

### Version Control

- Git
- GitHub

### Scripting

- Bash

---

# 📂 Project Structure

```
aws-blue-green-deployment/

├── app.py
├── Dockerfile
├── requirements.txt
│
├── scripts/
│   ├── deploy.sh
│   ├── switch.sh
│   ├── rollback.sh
│   └── health-check.sh
│
├── nginx/
│   ├── blue.conf
│   ├── green.conf
│   └── nginx.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── screenshots/
│
└── README.md
```

---

# 🚀 Features

- ✅ Dockerized Flask Application
- ✅ Blue-Green Deployment
- ✅ Zero Downtime Deployment
- ✅ Nginx Reverse Proxy
- ✅ Docker Container Management
- ✅ Health Check API
- ✅ GitHub Actions CI/CD
- ✅ AWS EC2 Deployment
- ✅ Automated Deployment Scripts
- ✅ Automatic Traffic Switching
- ✅ Rollback Support

---

# 🌐 Application Endpoints

## Dashboard

```
/
```

Displays

- Application Version
- Deployment Environment
- Hostname
- Deployment Status
- Deployment Time

---

## Health Check

```
/health
```

Returns

```json
{
    "environment":"GREEN",
    "hostname":"container-id",
    "status":"healthy",
    "version":"2.0"
}
```

Used by the deployment script before switching production traffic.

---

# 🐳 Docker Commands

## Build Image

```bash
docker build -t bluegreen-app .
```

## Run Blue Container

```bash
docker run -d \
--name blue \
-p 5001:5000 \
bluegreen-app
```

## Run Green Container

```bash
docker run -d \
--name green \
-p 5002:5000 \
-e ENVIRONMENT=GREEN \
-e VERSION=2.0 \
bluegreen-app
```

## List Containers

```bash
docker ps
```

## View Logs

```bash
docker logs blue
```

## Stop Container

```bash
docker stop blue
```

---

# ⚡ Deployment Workflow

```
Developer

      │

Git Push

      │

GitHub Actions

      │

SSH into EC2

      │

Git Pull

      │

Build Docker Image

      │

Deploy Green Container

      │

Health Check

      │

Switch Nginx Traffic

      │

Production
```

---

# 🔄 Blue-Green Deployment Flow

```
Current Production

        │

      Users

        │

      Nginx

        │

 Blue Environment

-----------------------------

Deploy New Version

        │

 Green Environment

        │

Health Check

        │

Switch Traffic

        │

Zero Downtime

        │

Rollback (If Needed)
```

---

# 🔁 Deployment Process

1. Developer pushes code to GitHub.
2. GitHub Actions workflow starts.
3. Workflow connects to AWS EC2 using SSH.
4. Latest code is pulled from GitHub.
5. Docker image is built.
6. Green container is deployed.
7. Health checks validate the application.
8. Nginx switches production traffic.
9. Blue container remains available for rollback.
10. Deployment completes without downtime.

---

# 📈 DevOps Concepts Demonstrated

- Docker Containerization
- Continuous Integration
- Continuous Deployment
- Blue-Green Deployment
- Zero Downtime Deployment
- Nginx Reverse Proxy
- Health Checks
- Automated Rollback
- Infrastructure Automation
- Linux Administration
- AWS EC2
- GitHub Actions

---

# 📸 Screenshots

Add screenshots of:

- ✅ AWS EC2 Instance
- ✅ Docker Containers
- ✅ GitHub Repository
- ✅ GitHub Actions Workflow
- ✅ Successful Pipeline
- ✅ Application Dashboard
- ✅ Blue Environment
- ✅ Green Environment
- ✅ Health Check Response
- ✅ Nginx Configuration
- ✅ Zero-Downtime Traffic Switch

---

# 🚀 Future Enhancements

- Kubernetes Deployment (Amazon EKS)
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboards
- AWS CloudWatch Logs
- Docker Compose
- SSL with Let's Encrypt
- Multi-Environment Deployments
- Slack Notifications
- SonarQube Integration

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with

- AWS EC2
- Docker
- GitHub Actions
- CI/CD Pipelines
- Nginx
- Linux Administration
- Blue-Green Deployment
- Health Monitoring
- Bash Automation
- Production Deployment Strategy

---

# 👩‍💻 Author

**Supraja**

Cloud | DevOps | AWS Engineer

GitHub

https://github.com/suprajasree

LinkedIn

(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.# 🚀 Production-Style Zero-Downtime Blue-Green Deployment Pipeline

> A production-inspired DevOps project demonstrating zero-downtime application deployments on AWS using Docker, Nginx, GitHub Actions, and Blue-Green Deployment strategy.

---

# 📖 Project Overview

This project simulates a real-world production deployment pipeline where application releases are performed without downtime using the **Blue-Green Deployment** strategy.

The application is containerized using Docker, deployed on AWS EC2, and fronted by Nginx acting as a reverse proxy. Deployment automation is handled through GitHub Actions with health checks and rollback support.

The primary objective of this project is to demonstrate modern DevOps practices including:

- Containerization
- CI/CD Automation
- Infrastructure Deployment
- Reverse Proxy Configuration
- Zero-Downtime Deployment
- Health Monitoring
- Automated Rollback

---

# 🎯 Project Objectives

- Deploy Dockerized applications on AWS EC2
- Implement Blue-Green deployment strategy
- Eliminate deployment downtime
- Automate deployments using GitHub Actions
- Configure Nginx Reverse Proxy
- Perform application health checks
- Implement deployment rollback
- Follow production deployment practices

---

# 🏗️ Project Architecture

```
                    Developer
                        │
                  Git Push
                        │
                GitHub Repository
                        │
               GitHub Actions CI/CD
                        │
                  SSH Deployment
                        │
                 AWS EC2 Instance
                        │
                 Docker Containers
                        │
        ┌───────────────┴───────────────┐
        │                               │
   Blue Container                  Green Container
    Port 5001                       Port 5002
        │                               │
        └───────────────┬───────────────┘
                        │
                Nginx Reverse Proxy
                        │
                  Production Traffic
```

---

# ⚙️ Technology Stack

## Cloud

- AWS EC2

## Containerization

- Docker

## Web Server

- Nginx

## CI/CD

- GitHub Actions

## Programming

- Python
- Flask

## Operating System

- Ubuntu Linux

## Version Control

- Git
- GitHub

## Scripting

- Bash

---

# 📂 Repository Structure

```
aws-blue-green-deployment/

│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── nginx/
│   ├── nginx.conf
│   ├── blue.conf
│   └── green.conf
│
├── scripts/
│   ├── deploy.sh
│   ├── switch.sh
│   ├── rollback.sh
│   └── health-check.sh
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── screenshots/
│
├── architecture/
│
└── README.md
```

---

# 🚀 Features

- Dockerized Flask Application
- Blue-Green Deployment
- Zero Downtime Deployment
- Docker Container Management
- Health Check Endpoint
- GitHub Actions Automation
- Nginx Reverse Proxy
- Automated Rollback
- AWS EC2 Deployment
- Bash Deployment Scripts
- Environment Variables
- Production Dashboard

---

# 📋 Current Progress

- ✅ Flask Application
- ✅ Dockerized Application
- ✅ Health Check API
- ✅ Environment Variables
- ⏳ AWS EC2 Deployment
- ⏳ Docker Deployment
- ⏳ Nginx Reverse Proxy
- ⏳ Blue-Green Deployment
- ⏳ GitHub Actions
- ⏳ Automated Rollback

---

# 🌐 Application Endpoints

## Dashboard

```
/
```

Displays the deployment dashboard including:

- Version
- Environment
- Hostname
- Deployment Time
- Status

---

## Health Check

```
/health
```

Returns

```json
{
  "status": "healthy",
  "version": "1.0",
  "environment": "BLUE"
}
```

Used during deployment validation before switching production traffic.

---

# 🐳 Docker Commands

Build Image

```bash
docker build -t devops-dashboard:v1 .
```

Run Container

```bash
docker run -d \
--name blue-app \
-p 5000:5000 \
devops-dashboard:v1
```

View Running Containers

```bash
docker ps
```

View Logs

```bash
docker logs blue-app
```

Stop Container

```bash
docker stop blue-app
```

Remove Container

```bash
docker rm blue-app
```

---

# 🚀 Deployment Workflow

```
Developer

↓

Git Push

↓

GitHub Repository

↓

GitHub Actions

↓

Build Docker Image

↓

Deploy Green Container

↓

Run Health Check

↓

Switch Nginx Traffic

↓

Production

↓

Rollback (if required)
```

---

# 🔄 Blue-Green Deployment Workflow

```
Current Production

Users

↓

Nginx

↓

Blue Container

----------------------

New Release

↓

Green Container

↓

Health Check

↓

Switch Traffic

↓

Blue → Green

↓

Zero Downtime
```

---

# 📈 DevOps Concepts Demonstrated

- Docker Containerization
- Reverse Proxy
- Blue-Green Deployment
- Continuous Integration
- Continuous Deployment
- Infrastructure Automation
- Health Monitoring
- Rollback Strategy
- Linux Administration
- AWS EC2 Deployment

---

# 🔒 Future Enhancements

- Kubernetes Deployment (Amazon EKS)
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboard
- AWS CloudWatch Integration
- SSL with Let's Encrypt
- Docker Compose
- Multi-Environment Deployment
- Slack Notifications
- SonarQube Code Analysis

---

# 📸 Screenshots

To be added

- Application Dashboard
- Docker Containers
- GitHub Actions Pipeline
- AWS EC2 Instance
- Nginx Configuration
- Blue Deployment
- Green Deployment
- Successful Zero-Downtime Switch

---

# 🎓 Learning Outcomes

This project demonstrates practical knowledge of:

- AWS EC2
- Docker
- Linux Administration
- Nginx
- GitHub Actions
- CI/CD
- Blue-Green Deployment
- Reverse Proxy
- Bash Scripting
- Health Checks
- Production Deployment Strategy

---

# 👩‍💻 Author

**Supraja**

Cloud & DevOps Engineer

GitHub:
https://github.com/suprajasree

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
# test deployment
