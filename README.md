# 🚀 Production-Style Zero-Downtime Blue-Green Deployment Pipeline

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
