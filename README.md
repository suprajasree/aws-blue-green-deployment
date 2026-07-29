# 🚀 AWS Blue-Green Deployment using Docker, Nginx & GitHub Actions

<p align="center">

![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white)

</p>

---

# 📌 Project Overview

This project demonstrates a **production-ready Blue-Green Deployment** strategy using **AWS EC2**, **Docker**, **Nginx**, and **GitHub Actions**.

The CI/CD pipeline automatically deploys application updates to the inactive environment, performs health checks, and switches production traffic through Nginx with minimal downtime.

---

# 🏗️ Architecture

<p align="center">
  <img src="architecture/aws-blue-green-architecture.png" alt="AWS Blue-Green Deployment Architecture" width="100%">
</p>

---

# ✨ Key Features

- 🚀 Blue-Green Deployment Strategy
- ⚙️ Automated CI/CD with GitHub Actions
- 🐳 Dockerized Flask Application
- ☁️ AWS EC2 Deployment
- 🌐 Nginx Reverse Proxy
- ❤️ Health Check Validation
- 🔄 Automated Traffic Switching
- ⏱️ Minimal Downtime Deployment
- 🐧 Linux Server Administration

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Cloud | AWS EC2 |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Reverse Proxy | Nginx |
| Backend | Python Flask |
| Operating System | Ubuntu Linux |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
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
├── architecture/
│   └── aws-blue-green-architecture.png
│
├── screenshots/
│   ├── 01-health-check.png
│   ├── 02-blue-green-containers.png
│   ├── 03-nginx-traffic-switch.png
│   ├── 04-end-to-end-deployment.png
│   ├── 05-github-actions-pipeline.png
│   ├── 06-workflow-history.png
│   └── 07-green-environment.png
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🔄 CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions workflow starts automatically.
3. Workflow connects securely to the AWS EC2 instance.
4. Docker builds and deploys the application.
5. Health checks validate the deployment.
6. Nginx switches production traffic to the healthy environment.
7. End users access the updated application with minimal downtime.

---

# ❤️ Health Check

### Endpoint

```text
/health
```

### Sample Response

```json
{
  "status": "healthy",
  "version": "1.0",
  "environment": "GREEN"
}
```

---

# 📸 Project Screenshots

## GitHub Actions CI/CD Pipeline

![GitHub Actions Pipeline](screenshots/05-github-actions-pipeline.png)

---

## Workflow Execution History

![Workflow History](screenshots/06-workflow-history.png)

---

## Blue & Green Docker Containers

![Blue Green Containers](screenshots/02-blue-green-containers.png)

---

## Nginx Traffic Switching

![Traffic Switch](screenshots/03-nginx-traffic-switch.png)

---

## Application Health Check

![Health Check](screenshots/01-health-check.png)

---

## End-to-End Deployment

![Deployment](screenshots/04-end-to-end-deployment.png)

---

## Production Traffic Switched to Green Environment

![Green Environment](screenshots/07-green-environment.png)

---

# 💼 Skills Demonstrated

- AWS EC2
- Docker
- GitHub Actions
- CI/CD Pipeline Automation
- Nginx Reverse Proxy
- Linux Administration
- SSH Deployment
- Blue-Green Deployment
- Python Flask
- Git & GitHub

---

# 📚 Key Learning Outcomes

- Implemented Blue-Green deployment on AWS EC2.
- Automated deployments using GitHub Actions.
- Built and managed Docker containers.
- Configured Nginx as a reverse proxy.
- Implemented health checks before production traffic switching.
- Reduced deployment downtime using automated routing.

---

# 🚀 Future Enhancements

- Amazon EKS (Kubernetes)
- Terraform Infrastructure as Code
- Prometheus Monitoring
- Grafana Dashboards
- AWS Application Load Balancer
- Let's Encrypt SSL
- Amazon CloudWatch Monitoring

---

# 👩‍💻 Author

## Supraja

**DevOps Engineer**

**Skills:** AWS • Docker • GitHub Actions • Linux • Nginx • Python • Flask • CI/CD

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.