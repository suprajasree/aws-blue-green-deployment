# 🚀 AWS Blue-Green Deployment using Docker, Nginx & GitHub Actions

<p align="center">
  <img src="https://img.shields.io/badge/AWS-EC2-orange?logo=amazonaws">
  <img src="https://img.shields.io/badge/Docker-Container-blue?logo=docker">
  <img src="https://img.shields.io/badge/GitHub-Actions-black?logo=githubactions">
  <img src="https://img.shields.io/badge/Nginx-Reverse%20Proxy-green?logo=nginx">
  <img src="https://img.shields.io/badge/Python-Flask-blue?logo=python">
  <img src="https://img.shields.io/badge/Linux-Ubuntu-E95420?logo=ubuntu">
</p>

---

## 📌 Overview

This project demonstrates a **production-style Blue-Green Deployment** on **AWS EC2** using **Docker**, **Nginx**, and **GitHub Actions**.

Whenever new code is pushed to GitHub, the CI/CD pipeline automatically deploys the application to the inactive environment, verifies its health, and switches live traffic using Nginx. This approach minimizes downtime and provides a safer deployment process.

---

# 🏗 Architecture

> *(We'll replace this section with a professional architecture diagram in the next step.)*

---

## ✨ Features

- Blue-Green Deployment
- Dockerized Flask Application
- GitHub Actions CI/CD Pipeline
- AWS EC2 Deployment
- Nginx Reverse Proxy
- Automated Deployment
- Health Check Endpoint
- Zero / Minimal Downtime
- Linux Server Administration

---

## 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Cloud | AWS EC2 |
| CI/CD | GitHub Actions |
| Containers | Docker |
| Reverse Proxy | Nginx |
| Backend | Flask (Python) |
| OS | Ubuntu Linux |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
aws-blue-green-deployment/
│
├── app/
├── nginx/
├── .github/
│   └── workflows/
├── docker-compose.yml
├── README.md
├── LICENSE
└── screenshots/
```

---

## ⚙ Deployment Workflow

```text
Developer
     │
git push
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
SSH
     ▼
AWS EC2
     │
Docker Deploy
     ▼
Blue / Green Containers
     │
Health Check
     ▼
Nginx Traffic Switch
     │
     ▼
Users
```

---

## ❤️ Health Check

Endpoint

```
/health
```

Example Response

```json
{
  "status":"healthy",
  "version":"1.0",
  "environment":"GREEN"
}
```

---

## 📸 Project Screenshots

### GitHub Actions CI/CD Pipeline

![Pipeline](SCREENSHOT/GitHub%20Actions%20CICD%20Pipeline%20-%20Successful%20Deployment.png)

---

### Workflow Execution History

![Workflow](SCREENSHOT/GitHub%20Actions%20Workflow%20Execution%20History.png)

---

### Blue & Green Containers

![Containers](SCREENSHOT/Blue%20and%20Green%20Docker%20Containers%20Running%20Simultaneously.png)

---

### Nginx Traffic Switch

![Nginx](SCREENSHOT/Blue-Green%20Traffic%20Switch%20Using%20Nginx.png)

---

### Health Check

![Health](SCREENSHOT/Application%20Health%20Check%20Verification.png)

---

### Final Deployment

![Deployment](SCREENSHOT/Traffic%20Switched%20to%20Green%20Environment.png)

---

## 💼 Skills Demonstrated

- AWS EC2
- Docker
- GitHub Actions
- CI/CD Automation
- Nginx
- Linux Administration
- SSH
- Blue-Green Deployment
- Flask
- Git

---

## 🚀 Future Enhancements

- Kubernetes (Amazon EKS)
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboards
- SSL using Let's Encrypt
- AWS Load Balancer
- Amazon CloudWatch

---

## 👩‍💻 Author

**Supraja**

DevOps | AWS | Docker | GitHub Actions | Linux | Python

---

⭐ If you found this project useful, consider giving it a star.
