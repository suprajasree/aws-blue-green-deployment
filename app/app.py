from flask import Flask
import socket
import os
from datetime import datetime

app = Flask(__name__)

# Environment Variables
VERSION = os.getenv("VERSION", "1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "BLUE")
HOSTNAME = socket.gethostname()
DEPLOYMENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>

<head>

<title>Production DevOps Dashboard</title>

<style>

body{{
    font-family:Arial,Helvetica,sans-serif;
    background:#f4f7fb;
    margin:0;
    padding:40px;
}}

.container{{
    width:850px;
    margin:auto;
    background:white;
    border-radius:12px;
    padding:35px;
    box-shadow:0px 5px 20px rgba(0,0,0,.15);
}}

h1{{
    text-align:center;
    color:#1565C0;
}}

.subtitle{{
    text-align:center;
    color:#666;
    margin-bottom:30px;
}}

table{{
    width:100%;
    border-collapse:collapse;
}}

th{{
    background:#1976D2;
    color:white;
    padding:14px;
}}

td{{
    padding:14px;
    border:1px solid #ddd;
}}

.status{{
    color:green;
    font-weight:bold;
}}

.footer{{
    margin-top:30px;
    text-align:center;
    color:#777;
}}

</style>

</head>

<body>

<div class="container">

<h1>🚀 Production DevOps Dashboard</h1>

<p class="subtitle">

Blue-Green Deployment Demo using AWS • Docker • Nginx • GitHub Actions

</p>

<table>

<tr>
<th>Parameter</th>
<th>Value</th>
</tr>

<tr>
<td>Application</td>
<td>Blue-Green Deployment v2</td>
</tr>

<tr>
<td>Version</td>
<td>{VERSION}</td>
</tr>

<tr>
<td>Environment</td>
<td>{ENVIRONMENT}</td>
</tr>

<tr>
<td>Container Hostname</td>
<td>{HOSTNAME}</td>
</tr>

<tr>
<td>Deployment Time</td>
<td>{DEPLOYMENT_TIME}</td>
</tr>

<tr>
<td>Application Status</td>
<td class="status">Healthy ✅</td>
</tr>

<tr>
<td>Deployment Strategy</td>
<td>Blue-Green Deployment</td>
</tr>

<tr>
<td>CI/CD</td>
<td>GitHub Actions</td>
</tr>

<tr>
<td>Container Platform</td>
<td>Docker</td>
</tr>

<tr>
<td>Reverse Proxy</td>
<td>Nginx</td>
</tr>

<tr>
<td>Cloud Platform</td>
<td>AWS EC2</td>
</tr>

</table>

<div class="footer">

Production-style Zero-Downtime Deployment Project

</div>

</div>

</body>

</html>
"""


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "version": VERSION,
        "environment": ENVIRONMENT,
        "hostname": HOSTNAME
    }, 200


@app.route("/version")
def version():
    return {
        "version": VERSION,
        "environment": ENVIRONMENT
    }


@app.route("/hostname")
def hostname():
    return {
        "hostname": HOSTNAME
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
