
# CogniCart – Engine-1 (Automated Attribute Extraction Engine)

**Engine-1** is the AI-powered product catalog ingestion service for **CogniCart**. It serves as the intelligent entry point for the platform, processing seller product submissions through advanced AI understanding to output highly structured and enriched product catalog data.

## 🧠 Engine Responsibilities

This engine operates as the primary transformation layer in the CogniCart ecosystem:

1. **Event Ingestion:** Receives raw product submission events from sellers.
2. **Multimodal Understanding:** Analyzes both product images and text descriptions simultaneously.
3. **Structured Generation:** Converts unstructured inputs into standardized, structured Catalog JSON.
4. **Event Publishing:** Broadcasts enriched product events for downstream consumption (Recommendation Engine, Search, etc.).

---

## 🚀 Tech Stack

* **Core:** Python 3.x
* **API Framework:** FastAPI
* **Validation:** Pydantic
* **AI/ML (Upcoming):** Florence-2 (Vision-Language Model), LLM Structuring
* **Infrastructure (Upcoming):** Kafka

---

## 📁 Project Structure

```text
engine-1/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── routes.py        # API endpoints
│   └── schemas.py       # Pydantic data models
│
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

```

---

## ⚙️ Setup & Installation

Follow these steps to set up the development environment locally.

### 1. Create Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Run the Server

Start the development server with live reloading enabled:

```bash
uvicorn app.main:app --reload

```

### 4. ✅ Health Check

Verify the service is running correctly by accessing the health endpoint:

* **URL:** `http://localhost:8000/health`
* **Expected Response:**

```json
{
  "status": "ok",
  "service": "engine-1"
}

```

---

## 📅 Development Roadmap

| Timeline | Milestone | Focus Area |
| --- | --- | --- |
| **Day 2** | **Vision Integration** | Integration of Florence-2 for image analysis. |
| **Day 3** | **Data Structuring** | Implementation of LLM-based attribute extraction. |
| **Day 4** | **Finalizer** | Logic to finalize and validate catalog entries. |
| **Day 5** | **Confidence Scoring** | Building the Confidence Engine to score AI outputs. |
| **Day 6** | **Persistence** | Database integration and schema setup. |
| **Day 7** | **Messaging** | Kafka integration for event streaming. |
| **Day 8** | **Integration** | Connecting Engine-1 APIs with the Frontend. |
| **Day 9** | **QA** | Comprehensive testing (Unit & Integration). |
| **Day 10** | **Polish** | Final demo preparation and documentation refinement. |

---
