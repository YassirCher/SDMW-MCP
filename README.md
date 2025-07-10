# SDMW-MCP

# Projet MCP - Intégration Spring Boot & Python
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

Une implémentation complète du protocole Model Context Protocol (MCP) comprenant un client Spring Boot et un serveur Python. Ce système démontre une fonctionnalité de chat basée sur l'IA avec intégration d'outils pour les informations boursières, les données d'entreprise, les opérations sur le système de fichiers et la gestion des employés.

**Auteur**: Manus AI

## Table des Matières
- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Technologies Utilisées](#technologies-utilisées)
- [Structure du Projet](#structure-du-projet)
- [Configuration de Développement](#configuration-de-développement)
- [Points d'Accès API](#points-d'accès-api)
- [Configuration](#configuration)
- [Performance & Surveillance](#performance--surveillance)
- [Dépannage](#dépannage)
- [Captures d'Écran](#captures-d'écran)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Contact](#contact)
- [FAQ](#faq)
- [Démo](#démo)
- [Feuille de Route](#feuille-de-route)




## Introduction

Ce projet implémente le Model Context Protocol (MCP) avec une architecture multi-tiers :
- **Client MCP Spring Boot**: Gère les requêtes de chat IA et l'intégration d'outils.
- **Serveur MCP Python**: Fournit divers outils et services.
- **Serveur MCP Spring Boot**: Services d'entreprise supplémentaires.

Le système démontre le raisonnement de l'IA avec l'utilisation d'outils, la gestion de la mémoire et les capacités de chat en temps réel.




## Fonctionnalités

### 🤖 Interface de Chat IA
- Chat interactif avec l'assistant IA
- Visualisation du processus de réflexion en temps réel
- Conversations conscientes de la mémoire
- Intégration d'outils pour des capacités améliorées

### 🛠️ Outils Disponibles
- **Informations Boursières**: Récupération de données boursières en temps réel
- **Données d'Entreprise**: Recherche d'informations sur les entreprises
- **Opérations sur le Système de Fichiers**: Capacités de gestion de fichiers
- **Informations sur les Employés**: Gestion des données RH

### 💻 Fonctionnalités Techniques
- Architecture API RESTful
- Requêtes cross-origin (CORS) activées
- Persistance de la mémoire entre les sessions
- Gestion des erreurs et validation




## Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Spring Boot   │    │   Python MCP    │
│   MCP Client    │◄──►│   Server        │
│   (Port 8066)   │    │                 │
└─────────────────┘    └─────────────────┘
          │
          ▼
┌─────────────────┐
│   Spring Boot   │
│   MCP Server    │
│   (Port 8899)   │
└─────────────────┘
```




## Installation

### Prérequis
- **Java 21** ou version ultérieure
- **Python 3.12** ou version ultérieure
- **Maven** (ou utiliser le wrapper inclus)
- **Ollama** (pour le service de modèle IA) - Installer depuis [ollama.ai](https://ollama.ai) avec modele llama3.1:8b le moins volumineux (4,9GB)

### Cloner le Dépôt
```bash
git clone https://github.com/YassirCher/SDMW-MCP.git
```

### Guide de Démarrage Rapide

Pour une démonstration rapide, suivez ces étapes dans l'ordre :

#### 1. Configuration d'Ollama (Modèle IA)
```bash
# Installer et démarrer Ollama
ollama serve

# Dans un nouveau terminal, télécharger le modèle requis
ollama pull llama3.1:8b
```

#### 2. Démarrer le Serveur MCP Python
```bash
cd mcp-server-python
# Activer l'environnement virtuel existant
.venv\Scripts\activate  # Sous Windows
# source .venv/bin/activate  # Sous macOS/Linux

python server.py
```

#### 3. Démarrer le Client MCP Spring Boot
```bash
cd mcp-client
./mvnw spring-boot:run
```

#### 4. Démarrer le Serveur MCP Spring Boot (Optionnel)
```bash
cd mcp-server
./mvnw spring-boot:run
```

### Vérification
Une fois tous les services en cours d'exécution, vous devriez voir :
- ✅ Serveur MCP Python : `http://localhost:8899`
- ✅ Client MCP Spring Boot : `http://localhost:8066`
- ✅ Modèle IA Ollama : `http://localhost:10000`




## Utilisation

### Accéder à l'Application
1. **API Backend**: http://localhost:8066
2. **Swagger UI**: http://localhost:8066/swagger-ui.html 

### Flux de Chat Basique
1. Utilisez des requêtes suggérées ou tapez les vôtres via l'API.
2. Observez le processus de réflexion et la réponse de l'IA.
3. Explorez les différents outils et capacités.

### Exemples de Requêtes
- `"Bonjour, comment allez-vous ?"` - Salutation basique
- `"Quelles entreprises connaissez-vous ?"` - Informations sur l'entreprise
- `"Parlez-moi de l'action Apple"` - Informations boursières
- `"Lister tous les employés"` - Données des employés
- `"Quels fichiers sont disponibles ?"` - Opérations sur le système de fichiers




## Technologies Utilisées

### Backend
- **Spring Boot 3.x** - Cadre principal
- **Spring AI** - Intégration de l'IA
- **Spring Data JPA** - Opérations de base de données
- **H2 Database** - Base de données en mémoire
- **Maven** - Outil de construction
- **Java 21** - Langage de programmation

### Serveur Python
- **Python 3.12** - Langage de programmation
- **MCP SDK** - Protocole de Contexte de Modèle




## Structure du Projet

```
mcp-project-spring-python/
├── README.md
├── mcp-client
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   └── test
│   └── target
│       ├── classes
│       ├── generated-sources
│       ├── generated-test-sources
│       └── test-classes
├── mcp-server
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   └── test
│   └── target
│       ├── classes
│       ├── generated-sources
│       ├── generated-test-sources
│       └── test-classes
├── pom.xml
├── project_structure.txt
├── python-mcp-server
│   ├── README.md
│   ├── __pycache__
│   │   └── server.cpython-312.pyc
│   ├── main.py
│   ├── pyproject.toml
│   ├── python-mcp-server.iml
│   ├── server.py
│   └── uv.lock
├── src
│   ├── main
│   │   ├── java
│   │   └── resources
│   └── test
│       └── java
└── yassir-mcp-demo-spring-python.iml

26 directories, 19 files
```




## Configuration de Développement

### Fichiers de Configuration

#### Propriétés de l'Application (Spring Boot)
- **Port**: 8066
- **URL du Serveur MCP**: http://localhost:8899
- **Base de Données**: H2 en mémoire
- **Modèle IA**: llama3.1 via Ollama

### Variables d'Environnement
```bash
# Optionnel : Définir les clés API si vous utilisez des services externes
CLAUDE_API_KEY=votre_clé_api_ici
OLLAMA_BASE_URL=http://localhost:10000
```




## Points d'Accès API

### Point d'Accès Principal du Chat
- **GET** `/chat?query={message}` - Envoyer un message de chat à l'IA

### Points d'Accès des Outils (via le Serveur MCP)
- Outils d'information boursière
- Récupération de données d'entreprise
- Opérations sur le système de fichiers
- Gestion des employés




## Configuration

### Fichiers de Configuration Clés

#### mcp-servers.json
Fichier de configuration pour les connexions au serveur MCP :
```json
{
  "servers": {
    "server1": {
      "url": "http://localhost:8899",
      "sse-endpoint": "/sse"
    }
  }
}
```

#### application.properties
Paramètres de configuration clés :
```properties
# Configuration du Serveur
server.port=8066

# Configuration du Client MCP
spring.ai.mcp.client.type=sync
spring.ai.mcp.client.sse.connections.server1.url=http://localhost:8899
spring.ai.mcp.client.sse.connections.server1.sse-endpoint=/sse

# Configuration du Modèle IA
spring.ai.ollama.base-url=http://localhost:10000
spring.ai.ollama.chat.model=llama3.1

# Configuration de la Base de Données
spring.datasource.url=jdbc:h2:mem:testdb
spring.h2.console.enabled=true
```




## Performance & Surveillance

### Exigences du Système
- **Mémoire**: 16 Go de RAM minimum, 32 Go recommandés. Notez que les modèles de langage volumineux comme Llama 3.1:8B peuvent nécessiter 16 Go de RAM supplémentaires ou plus, en fonction de la taille du modèle et de l'utilisation. Pour les systèmes avec une RAM limitée, il est conseillé d'utiliser des modèles plus petits comme `llama3.1` ou `mistral`.
- **CPU**: Processeur multi-cœur recommandé
- **Stockage**: 8 Go d'espace libre pour les modèles et les dépendances
- **Réseau**: Connexion Internet stable pour la configuration initiale

### Métriques de Performance
- **Temps de Démarrage**: ~2-3 minutes pour tous les services
- **Temps de Réponse**: <2 secondes pour les requêtes typiques
- **Utilisation de la Mémoire**: ~14 Go de RAM au total pour tous les services
- **Débit**: ~10 requêtes concurrentes prises en charge

### Vérifications de Santé
Surveiller la santé du service à :
- Spring Boot Actuator: `http://localhost:8066/actuator/health`
- Serveur MCP Python: Vérifier la sortie de la console pour "Server listening on port 8899"




## Dépannage

### Problèmes Courants

#### Conflits de Ports
```bash
# Vérifier si les ports sont utilisés
netstat -an | findstr "8066 8899 10000"

# Tuer les processus utilisant des ports spécifiques (Windows)
taskkill /F /PID <process_id>
```

#### Problèmes de Version Java
```bash
# Vérifier la version de Java
java -version

# Devrait afficher Java 21 ou version ultérieure
# Sinon, mettre à jour la variable d'environnement JAVA_HOME
```

#### Ollama ne Répond pas
```bash
# Vérifier si Ollama est en cours d'exécution
ollama list

# Redémarrer le service Ollama
ollama serve

# Télécharger le modèle requis
ollama pull llama3.1
```

#### Problèmes d'Environnement Virtuel Python
```bash
# Sous Windows
cd mcp-server-python
.venv\Scripts\activate

# Sous macOS/Linux
cd mcp-server-python
source .venv/bin/activate

# Réinstaller les dépendances
pip install -r requirements.txt
```

#### Problèmes CORS
Si vous rencontrez des erreurs CORS :
1. Assurez-vous que le client MCP Spring Boot est en cours d'exécution sur le port 8066
2. Vérifiez que `@CrossOrigin` est correctement configuré
3. Redémarrez l'application Spring Boot

### Mode Débogage
Activer la journalisation de débogage dans `application.properties`:
```properties
logging.level.ma.tajeddine.mcpclient=DEBUG
logging.level.org.springframework.ai=DEBUG
```




## FAQ

### Questions Générales

**Q: Puis-je utiliser différents modèles d'IA ?**
R: Oui, modifiez le fichier `application.properties` pour utiliser différents modèles Ollama :
```properties
spring.ai.ollama.chat.model=llama2
# ou
spring.ai.ollama.chat.model=mistral
```

**Q: Comment ajouter de nouveaux outils au serveur MCP ?**
R: Étendez le serveur MCP Python en :
1. Ajoutant de nouvelles définitions d'outils dans `server.py`
2. Implémentant la logique de l'outil dans des modules séparés
3. Enregistrant les outils auprès du serveur MCP

**Q: Puis-je déployer cela en production ?**
R: Oui, mais considérez :
- Utiliser des bases de données externes au lieu de H2
- Configurer une sécurité appropriée (authentification, autorisation)
- Mettre en place un proxy inverse (nginx, Apache)
- Utiliser des variables d'environnement pour la configuration sensible

**Q: Comment sauvegarder l'historique du chat ?**
R: Actuellement, l'historique du chat est stocké en mémoire. Pour la persistance :
- Implémentez le stockage en base de données dans le client Spring Boot
- Ajoutez des points d'accès pour l'historique des conversations
- Envisagez d'utiliser Redis pour le stockage de session

### Questions Techniques

**Q: Pourquoi la réponse de l'IA est-elle lente ?**
R: Causes possibles :
- Temps de chargement du modèle Ollama (première requête)
- Latence réseau vers le serveur MCP
- Opérations d'outils complexes
- Ressources système insuffisantes

**Q: Puis-je intégrer avec Claude ou GPT au lieu d'Ollama ?**
R: Oui, décommentez et configurez dans `application.properties`:
```properties
spring.ai.anthropic.api-key=${CLAUDE_API_KEY}
spring.ai.anthropic.chat.options.model=claude-sonnet-4-20250514
```




## Démo

### Étapes de Démonstration Rapide
1. Démarrez tous les services en suivant le Guide de Démarrage Rapide.
2. Utilisez un client API (comme Postman ou Swagger UI) pour interagir avec l'API Spring Boot sur `http://localhost:8066`.
3. Essayez ces exemples de requêtes :
   - "Bonjour, quel est votre nom ?"
   - "Lister toutes les entreprises"
   - "Parlez-moi d'Apple"
   - "À quels fichiers pouvez-vous accéder ?"
   - "Retenez que mon nom est John"




## Captures d'Écran

Cette section présente les différentes fonctionnalités et capacités du projet MCP à travers des démonstrations visuelles.

<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/1a10156e-c0e5-4450-9e7a-0f3804c7004e" />



Lien du Projet: [https://github.com/votre_utilisateur/mcp-project-spring-python](https://github.com/votre_utilisateur/mcp-project-spring-python)




## Feuille de Route

### Fonctionnalités Prévues
- [ ] Chat en temps réel avec support WebSocket
- [ ] Authentification et autorisation des utilisateurs
- [ ] Persistance de l'historique des conversations
- [ ] Intégrations d'outils supplémentaires
- [ ] Conteneurisation Docker
- [ ] Manifestes de déploiement Kubernetes
- [ ] Tests d'intégration
- [ ] Benchmarks de performance

### Idées de Contribution
- Ajouter de nouveaux outils MCP (météo, actualités, etc.)
- Améliorer la conception de l'interface utilisateur
- Ajouter des capacités de chat vocal
- Implémenter des salons/canaux de discussion
- Ajouter des fonctionnalités d'exportation/importation

---

⭐ **Mettez une étoile à ce dépôt si vous le trouvez utile !**




## Expériences avec les Modèles d'IA

Lors du développement de ce projet, plusieurs modèles de langage ont été testés pour l'intégration avec Spring AI et le support des outils. Voici un résumé des observations :

### Modèles Gratuits
- **Deepseek et Mistral (versions gratuites)**: Ces modèles ont été testés pour leur accessibilité. Cependant, ils n'ont pas démontré un support adéquat pour l'intégration des outils spécifiques de Spring AI. Cela signifie que les fonctionnalités avancées nécessitant l'appel de fonctions ou d'outils définis dans l'application Spring Boot n'étaient pas pleinement opérationnelles avec ces modèles.

### Modèles Payants ou Limités
### Limitations techniques
- **OpenAI et Grok**: Ces modèles offrent des capacités avancées et un bon support des outils, mais ils ne sont pas gratuits. Leur utilisation implique des coûts, ce qui peut être un facteur limitant pour les projets personnels ou à budget restreint.
- **Gemini (via Vertex AI)**: Bien que Gemini soit un modèle puissant et que des versions gratuites existent pour un usage général, l'accès aux modèles Gemini optimisés pour les agents et l'intégration d'outils (nécessaires pour ce type de projet) se fait souvent via des services cloud comme Google Cloud Vertex AI. Ces services ne sont pas gratuits et entraînent des coûts d'utilisation, ce qui rend l'expérimentation et le déploiement plus onéreux.
Le modèle `llama3.1:8b` est très volumineux et nécessite **au minimum 16GB de RAM** pour fonctionner correctement.
- Il requiert également un **GPU performant** (idéalement avec plus de 12GB de VRAM) pour un bon temps d'inférence.
- Lors de mes tests, un **problème de mémoire insuffisante** a été rencontré (voir capture ci-dessous).
- <img width="987" height="165" alt="image" src="https://github.com/user-attachments/assets/a2485f24-031e-491a-b225-364e1b837113" />
<img width="213" height="437" alt="image" src="https://github.com/user-attachments/assets/ebb6288c-05f0-4781-9233-11af9f89d147" />



Ces expériences soulignent l'importance de choisir un modèle d'IA non seulement en fonction de ses capacités, mais aussi de ses exigences en ressources (RAM, GPU) et de son modèle économique (gratuit, payant, freemium avec limitations).



