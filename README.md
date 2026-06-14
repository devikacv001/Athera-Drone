# 🚁 Athera Drone

## AI-Powered Autonomous Retrieval System

Athera Drone is an intelligent autonomous retrieval platform that combines voice intelligence, mission planning, location awareness, and computer vision to help users obtain essential items with minimal effort.

The system transforms natural language requests into actionable missions by identifying required items, locating suitable nearby stores, generating optimized retrieval plans, and verifying products through AI-powered visual recognition. By integrating multiple AI agents into a unified workflow, Athera Drone demonstrates how autonomous systems can assist people in accessing everyday necessities more efficiently and reliably.

---

## 🌟 Problem Statement

Obtaining essential items is not always convenient, particularly during emergencies, for elderly individuals, people with disabilities, or when mobility and time are limited. Traditional delivery services often involve delays, inventory uncertainty, and significant human intervention.

There is a growing need for intelligent systems capable of understanding user requirements, planning retrieval missions, locating nearby resources, and verifying requested items autonomously.

---

## 💡 Proposed Solution

Athera Drone addresses this challenge through an AI-driven multi-agent system capable of:

* Understanding voice-based requests
* Extracting required items and quantities
* Identifying appropriate store categories
* Finding nearby stores using live location data
* Generating retrieval missions using AI planning
* Verifying products through computer vision

The platform serves as a proof of concept for future autonomous retrieval and assistance systems.

---

## 🎯 Key Features

### 🎤 Voice Command Processing

* Real-time voice input
* Automatic speech-to-text conversion
* Natural language understanding

### 🛒 Intelligent Item Extraction

* Detects products from spoken requests
* Extracts item quantities automatically
* Supports multiple product categories

### 📍 Location-Aware Store Discovery

* Uses user location for contextual search
* Finds nearby stores relevant to requested items
* Provides distance estimates
* Generates navigation links

### 🧠 AI Mission Planning

* Creates structured retrieval workflows
* Generates step-by-step execution plans
* Supports autonomous decision-making pipelines

### 👁️ Product Verification Agent

* Uses OpenAI CLIP for visual verification
* Supports image, video, and webcam inputs
* Confirms product presence before collection

---

## 🏗️ System Architecture

```text
User Voice Command
        │
        ▼
Speech Recognition Agent
        │
        ▼
Item Extraction Agent
        │
        ▼
Store Planning Agent
        │
        ▼
Nearby Store Discovery Agent
        │
        ▼
Mission Planner Agent
        │
        ▼
Product Verification Agent
        │
        ▼
Mission Completion
```

---

## 🔄 Workflow

### Step 1: User Request

```text
I need two packets of milk and one carrot.
```

### Step 2: Speech Recognition

```text
I need two packets of milk and one carrot
```

### Step 3: Item Extraction

```json
{
  "milk": 2,
  "carrot": 1
}
```

### Step 4: Store Selection

```text
Store Type: Supermarket
```

### Step 5: Nearby Store Discovery

```text
Royal Mart Supermarket
Distance: 1.8 km

Ratnadeep Supermarket
Distance: 3.3 km
```

### Step 6: Mission Planning

```text
Find nearby supermarket
Collect available items
Move to another store if required
Return after completion
```

### Step 7: Product Verification

```text
FOUND: carrot
Confidence Score: 23.4
```

---

## 🛠️ Technology Stack

### Backend

* FastAPI
* Python

### AI & Machine Learning

* Faster Whisper
* LangGraph
* LangChain Core
* OpenAI CLIP
* Transformers
* PyTorch

### Computer Vision

* OpenCV
* Pillow

### Location Services

* OpenStreetMap Nominatim
* Geopy

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
Athera-Drone/
│
├── backend/
│   ├── app.py
│   ├── extractor.py
│   ├── mission_planner.py
│   ├── shop_planner.py
│   ├── shop_finder.py
│   ├── product_detector.py
│   ├── requirements.txt
│   └── test_graph.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/devikacv001/Athera-Drone.git
```

Navigate to the project directory:

```bash
cd Athera-Drone
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

---

## ▶️ Running the Application

Start the backend server:

```bash
cd backend
uvicorn app:app --reload
```

Open the frontend:

```text
frontend/index.html
```

Or run a local server:

```bash
cd frontend
python -m http.server 5500
```

Visit:

```text
http://localhost:5500
```

---

## 📋 Requirements

```text
fastapi
uvicorn
faster-whisper
requests
python-multipart
langgraph
langchain-core
torch
transformers
pillow
opencv-python
geopy
```

---

## 🚀 Future Enhancements

* Autonomous drone integration
* Multi-store route optimization
* Inventory-aware mission planning
* Real-time navigation assistance
* Mobile application support
* Product barcode verification
* Multi-language voice commands
* Advanced object detection models
* Autonomous delivery confirmation

---

## 🎓 Project Vision

Athera Drone explores the intersection of AI agents, autonomous systems, location intelligence, and computer vision. The project demonstrates how multiple specialized AI components can collaborate to transform a simple voice request into a complete retrieval mission.

The long-term vision is to enable intelligent autonomous platforms capable of assisting people in obtaining essential resources safely, efficiently, and independently.

---

## 👥 Team

### Devika C V
Computer Science and Business Systems  
Dayananda Sagar College of Engineering

GitHub: https://github.com/devikacv001

### Vinay G
Computer Science and Business Systems  
Dayananda Sagar College of Engineering

Email: vinaygovindraj04@gmail.com

---

### Built with AI, Computer Vision, Voice Intelligence, and Autonomous Planning.
