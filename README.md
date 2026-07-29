# 🚀 AWS Blue-Green Deployment with GitHub Actions CI/CD

![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-green)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow)
![Python](https://img.shields.io/badge/Python-Flask-blue)

## 📌 Project Overview

This project demonstrates a production-style **Blue-Green Deployment** strategy on **AWS EC2** using **Docker**, **Nginx**, and **GitHub Actions** for automated CI/CD.

The application is containerized using Docker and deployed to an Ubuntu EC2 instance. GitHub Actions automatically builds and deploys the latest version whenever changes are pushed to the repository, enabling near zero-downtime deployments through Blue-Green deployment.

---

# 🏗️ Architecture

```
                 Developer
                     │
                     ▼
            GitHub Repository
                     │
          Push to main branch
                     │
                     ▼
            GitHub Actions CI/CD
                     │
             SSH Deployment
                     │
                     ▼
              AWS EC2 (Ubuntu)
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
 Blue Docker Container       Green Docker Container
      │                             │
      └──────────────┬──────────────┘
                     ▼
              Nginx Reverse Proxy
                     │
                     ▼
                  End Users
```

---

# ✨ Features

* Blue-Green Deployment Strategy
* Dockerized Flask Application
* GitHub Actions CI/CD Pipeline
* AWS EC2 Deployment
* Nginx Reverse Proxy
* Zero/Minimal Downtime Deployment
* Automated Container Deployment
* Health Check Endpoint
* Linux Server Management
* Secure SSH-based Deployment

---

# 🛠️ Tech Stack

### Cloud

* AWS EC2

### DevOps

* Docker
* GitHub Actions
* CI/CD
* Nginx

### Backend

* Python
* Flask

### Operating System

* Ubuntu Linux

### Version Control

* Git
* GitHub

---

# 📁 Project Structure

```
aws-blue-green-deployment
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   ├── nginx.conf
│   ├── blue.conf
│   └── green.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── screenshots/
│
├── docker-compose.yml
│
└── README.md
```

---

# ⚙️ Deployment Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions workflow starts automatically.
3. Workflow connects securely to the AWS EC2 instance using SSH.
4. Docker image is built and deployed.
5. Blue or Green container is updated.
6. Nginx switches traffic to the healthy environment.
7. Users access the latest version with minimal downtime.

---

# ❤️ Health Check

Health Endpoint

```
/health
```

Example Response

```json
{
  "status": "healthy",
  "version": "1.0",
  "environment": "BLUE"
}
```

---

# 📷 Project Screenshots

Add your screenshots inside the `screenshots` folder and reference them here.

Example:

## AWS EC2 Instance

```
![EC2](screenshots/01-aws-ec2-instance-running.png)
```

## GitHub Actions Pipeline

```
![Pipeline](screenshots/02-github-actions-success.png)
```

## Docker Containers

```
![Docker](screenshots/03-running-containers.png)
```

## Application

```
![Application](screenshots/04-application-homepage.png)
```

---

# 🚀 Future Improvements

* Kubernetes Deployment (Amazon EKS)
* Terraform Infrastructure as Code
* Prometheus Monitoring
* Grafana Dashboards
* AWS Application Load Balancer
* SSL using Let's Encrypt
* Auto Scaling
* Amazon CloudWatch Integration

---

# 👩‍💻 Author

**Supraja**

DevOps Engineer

Skills:

* AWS
* Docker
* GitHub Actions
* Linux
* CI/CD
* Nginx
* Python
* Flask

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

