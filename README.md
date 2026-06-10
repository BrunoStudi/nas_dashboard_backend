# DashboardNAS - Backend

## Présentation

DashboardNAS est une API de supervision développée avec FastAPI permettant de surveiller une infrastructure basée sur TrueNAS SCALE.

L'API collecte et expose différentes métriques système afin d'alimenter l'interface DashboardNAS développée en React.

L'objectif du projet est de centraliser la supervision des serveurs de l'infrastructure personnelle :

- 🚀 EXODUS : serveur principal
- 🔨 HÉPHAÏSTOS : serveur de sauvegarde et réplication
- 🤖 HESTIA : future assistante IA locale

---

## Fonctionnalités

### Système

- Informations système
- Uptime
- Utilisation CPU
- Utilisation mémoire

### Disques

- Inventaire des disques
- Températures
- Capacités
- État SMART

### Pools ZFS

- Liste des pools
- État des pools
- Utilisation
- Santé ZFS

### IPMI

- Températures système
- Surveillance des ventilateurs
- Contrôle manuel des ventilateurs
- Contrôle automatique des ventilateurs

### Surveillance

- Alertes système
- Historique des métriques
- Supervision matérielle

### Fonctionnalités futures

- Surveillance GPU NVIDIA Tesla P40
- Gestion des zones GPU
- Intégration HESTIA
- Notifications intelligentes
- Gestion multi-serveurs

---

## Technologies utilisées

- FastAPI
- Python
- TrueNAS SCALE
- ZFS
- SMART
- IPMI
- Docker
- Linux

---

## Installation

### Cloner le projet

```bash
git clone https://github.com/BrunoStudi/nas_dashboard_backend
cd backend
```

### Créer l'environnement virtuel

```bash
python -m venv venv
```

### Activer l'environnement

Linux :

```bash
source venv/bin/activate
```

Windows :

```bash
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Lancement

```bash
uvicorn main:app --reload
```

API disponible sur :

```text
http://localhost:8000
```

Documentation Swagger :

```text
http://localhost:8000/docs
```

Documentation ReDoc :

```text
http://localhost:8000/redoc
```

---

## Endpoints principaux

### Système

```text
/api/system
/api/cpu
```

### Disques

```text
/api/disks
/api/smart
```

### ZFS

```text
/api/zpools
```

### IPMI

```text
/api/ipmi
/api/fans
/api/temperatures
```

---

## Services utilisés

DashboardNAS s'appuie notamment sur les outils suivants :

```text
zpool
zfs
smartctl
ipmitool
lsblk
lscpu
```

---

## Architecture

```text
backend/
├── routes/
├── services/
├── models/
├── utils/
├── scripts/
├── static/
└── main.py
```

---

## Roadmap

### Terminé

- [x] Monitoring CPU
- [x] Monitoring disques
- [x] Monitoring SMART
- [x] Monitoring pools ZFS
- [x] Monitoring IPMI
- [x] Contrôle des ventilateurs

### En cours

- [ ] Historisation des métriques
- [ ] Optimisation API

### Futur

- [ ] Monitoring GPU NVIDIA Tesla P40
- [ ] Monitoring VRAM
- [ ] Contrôle ventilation GPU
- [ ] Support multi-serveurs
- [ ] Intégration HESTIA
- [ ] Notifications intelligentes

---

## Infrastructure cible

```text
🚀 EXODUS
├── TrueNAS SCALE
├── DashboardNAS Backend
├── Ollama
├── Open WebUI
└── Tesla P40

🔨 HÉPHAÏSTOS
├── Sauvegardes
├── Réplication ZFS
└── Snapshots

🏠 Home Assistant
└── Raspberry Pi

🤖 HESTIA
└── Assistante IA locale
```

---

## Auteur

Projet personnel développé pour la supervision et l'administration d'une infrastructure TrueNAS SCALE basée sur ZFS, IPMI et technologies open source.