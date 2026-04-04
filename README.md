# My Dolla $ign

An AI powered budget education tool that teaches budgeting concepts in simple, easy to understand terms for young adults, students, and first time earners.

## Problem We Are Solving

Many people struggle to budget and save due to a lack of accessible, trustworthy financial guidance. Our platform provides educational budget breakdowns and personalized tips to help users build financial confidence.

## Team Members and Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| Hugo | Frontend Lead | UI/UX, React components, form handling |
| Rene | Backend Lead | API development, data processing, server setup |
| Gauge | AI/ML Lead | AI integration, prompt engineering, budget analysis |
| Allison | Documentation and QA | PRD, testing, deployment, documentation |

## MVP Features (Milestone 2)

1. **Budget form:** Monthly income, categorized expenses, goal.
2. **Analyze:** Single API path `POST /api/analyze` (JSON).
3. **Results in the UI:** Grounded explanation (uses your numbers), **one** quiz question, **one** rule-grounded tip (see `docs/financial_rules.md`), optional category breakdown, disclaimer, and **output source** (Vertex AI vs deterministic fallback).
4. **Safe fallback:** If Vertex AI is unavailable or misconfigured, the backend returns a full structured response from deterministic logic so the demo still works.

## Tech Stack

- Frontend: React.js with Tailwind CSS (Vite)
- Backend: Python (Flask) with REST API
- AI: Google Vertex AI (Gemini) for narrative sections when configured; otherwise rule-based fallback in code
- Database: None for MVP (no persistence)

## Project Structure

```
MyDolla-Sign/
├── README.md
├── docs/
│   ├── PRD.md                    # Product Requirements Document
│   ├── SPIKE_PLAN.md             # Engineering Spike Plan
│   ├── prompt_design.md          # AI Prompt Design Documentation
│   ├── spike_results.md          # AI Integration Results
│   ├── evaluation_test_cases.md  # 20 Test Cases
│   ├── financial_rules.md        # Financial Rule Base
│   └── architecture.png          # System Architecture Diagram
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   └── App.jsx               # Main app entry
│   └── package.json
├── backend/
│   ├── src/
│   │   ├── ai_tutor.py           # AI Tutor Core
│   │   ├── rule_engine.py        # Financial Rules Engine
│   │   ├── prompt_templates.py   # Prompt Builder
│   │   └── rules/
│   │       └── financial_rules.json
│   ├── demo.py                   # Interactive Demo Script
│   ├── test_tutor.py             # Test Script
│   ├── requirements.txt
│   └── main.py                   # Server entry point
└── CONTRIBUTING.md               # Team contribution guide
```

## How to Run

### Prerequisites
- Python 3.10+ (backend)
- Node.js 18+ (frontend)
- Optional: Google Cloud project with Vertex AI enabled and application default credentials (or your environment’s auth method) for live Gemini calls

### Backend setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# For live AI (same as terminal demo): set GEMINI_API_KEY from https://aistudio.google.com/apikey
# Optional: GEMINI_MODEL=gemini-2.5-flash
# Alternative: GOOGLE_CLOUD_PROJECT + Vertex AI auth
# Without either: deterministic fallback still works for demos.
```

### Run the AI Tutor Demo (Terminal)
```bash
cd backend
source venv/bin/activate
python demo.py
```

This interactive demo will:
1. Collect your budget information
2. Analyze it using AI
3. Quiz you with 2 to 3 questions
4. Give you personalized tips
5. Let you ask the AI any questions

### Run the backend API
```bash
cd backend
source venv/bin/activate
python main.py
```

Default: `http://127.0.0.1:5001` — `POST /api/analyze` expects JSON `{ "monthly_income", "expenses", "goal" }`.

### Run the frontend
```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:3000**. The dev server proxies `/api` to the backend (see `frontend/vite.config.js`).

### Milestone 2 demo checklist
- Step-by-step: [docs/milestone2_demo.md](docs/milestone2_demo.md)
- Record or link your 4–7 minute video per that doc (`docs/milestone2_demo.mp4` or URL in the same file).

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md)
- [Engineering Spike Plan](docs/SPIKE_PLAN.md)
- [Prompt Design Documentation](docs/prompt_design.md)
- [Spike Results and AI Integration](docs/spike_results.md)
- [Evaluation Test Cases](docs/evaluation_test_cases.md)
- [Financial Rules](docs/financial_rules.md)
- [Milestone 2 demo guide](docs/milestone2_demo.md)
- [Milestone 2 team handoff (three tasks)](docs/team_tasks_milestone2.md)

## Milestone 1 Deliverables

| Deliverable | Status |
|-------------|--------|
| PRD with AI Role | Complete |
| Financial Rule Base | Complete |
| AI Tutor Backend | Complete |
| Prompt Design Documentation | Complete |
| Evaluation Test Cases (20) | Complete |
| Spike Results | Complete |
| Architecture Diagram | Complete |

## License

This project is licensed under the Apache License 2.0.

Built for AI Ventures Club Spring 2026
