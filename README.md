# CogniCart – Engine-1 (Product Intelligence Engine)

Engine-1 is the AI-powered product catalog ingestion service for CogniCart.

It processes seller product submissions, performs AI-based understanding, and outputs structured product catalog data.

---

## 🚀 Tech Stack

- Python
- FastAPI
- Pydantic
- Florence-2 (coming)
- LLM Structuring (coming)
- Kafka (coming)

---

## 📁 Project Structure

engine-1/
│
├── app/
│ ├── main.py
│ ├── routes.py
│ └── schemas.py
│
├── requirements.txt
└── README.md


---

## ⚙ Setup

### Create Virtual Environment

```bash
python -m venv venv

Windows:

venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run Server
uvicorn app.main:app --reload

✅ Health Check

Open:

http://localhost:8000/health


Expected response:

{
  "status": "ok",
  "service": "engine-1"
}

🧠 Engine Responsibilities

Receive product submission events

Perform multimodal understanding (image + text)

Generate structured catalog JSON

Publish enriched product events

📅 Roadmap

Day-2: Florence-2 integration

Day-3: LLM structuring

Day-4: Catalog finalizer

Day-5: Confidence engine

Day-6: Database

Day-7: Kafka

Day-8: Frontend integration

Day-9: Testing

Day-10: Demo polish

