# DevOps Monitoring App 🖥️🐳☁️

![CI](https://github.com/Jencike05/devops-monitoring/actions/workflows/main.yml/badge.svg)

Ez egy egyszerű Flask alapú monitoring app, amely megjeleníti a CPU és memóriahasználatot egy webes felületen.

A projekt célja egy teljes CI/CD pipeline gyakorlása volt:

- Automatikus tesztelés `pytest`-tel
- Docker image build és push DockerHubra
- Automatikus deploy Azure Container Instances-be GitHub Actions segítségével

---

## 🌐 Live demo

> Legutóbbi deploy (elérhetőség változhat az Azure DNS alapján):

http://devops-monitoring-8.westeurope.azurecontainer.io

---

## 🛠️ Technológiák

- Python 3.10
- Flask
- psutil
- Docker
- GitHub Actions
- Azure Container Instances

---

## ▶️ Helyi futtatás

```bash
git clone https://github.com/Jencike05/devops-monitoring.git
cd devops-monitoring
pip install -r requirements.txt
python monitor.py
