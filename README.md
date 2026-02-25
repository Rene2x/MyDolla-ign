# My Dolla $ign

> An AI-powered budget education tool that teaches budgeting concepts in simple, easy-to-understand terms for young adults, students, and first-time earners.

## Problem We're Solving

Many people struggle to budget and save due to a lack of accessible, trustworthy financial guidance. Our platform provides educational budget breakdowns and personalized tips to help users build financial confidence.

## Team Members & Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| **Hugo** | Frontend Lead | UI/UX, React components, form handling |
| **Rene** | Backend Lead | API development, data processing, server setup |
| **Gauge**| AI/ML Lead | AI integration, prompt engineering, budget analysis |
| **Allison** | Documentation & QA | PRD, testing, deployment, documentation |



## MVP Features

1. **Budget Input Form** - Categorized expense breakdown (income, rent, food, etc.)
2. **AI-Generated Analysis** (Google Gemini, free tier):
   - **Financial advice** - One paragraph personalized to the user's budget
   - **Saving tips** - 3–5 actionable bullets (e.g. emergency fund, auto-transfers)
   - **Where savings could go** - Educational overview (e.g. savings accounts, retirement accounts, index funds as concepts; no specific products)
3. **Results** - Expense breakdown (computed in code), key insights, and disclaimer

## Tech Stack

- **Frontend**: React.js with Tailwind CSS (Vite)
- **Backend**: Python (Flask) with REST API
- **AI**: Google Gemini API (free tier) for narrative generation; calculations in code
- **Database**: None for MVP (no persistence)

## Project Structure

```
MyDolla-Sign/
├── README.md
├── docs/
│   ├── PRD.md              # Product Requirements Document
│   ├── SPIKE_PLAN.md       # Engineering Spike Plan
│   └── pitch-deck.pdf      # Pitch deck (add after creating slides)
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   └── App.jsx         # Main app entry
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic & AI integration
│   │   └── models/         # Data models
│   ├── requirements.txt
│   └── main.py             # Server entry point
└── CONTRIBUTING.md         # Team contribution guide
```

## How to Run

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.10+ (for backend)
- [Google Gemini API key](https://aistudio.google.com/app/apikey) (free) — copy `backend/.env.example` to `backend/.env` and set `GEMINI_API_KEY`

### Backend (port 5000)
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env   # then add your GEMINI_API_KEY
python main.py
```

### Frontend (port 3000, proxies /api to backend)
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000. If the Gemini API key is missing or the API fails, the app shows a rule-based fallback analysis.

## Documentation

- [Product Requirements Document (PRD)](docs/PRD.md)
- [Engineering Spike Plan](docs/SPIKE_PLAN.md)
- [Pitch Deck](docs/pitch-deck.pdf) *(to be added)*

## Timeline

- **Week 4**: PRD, Spike Plan, Repository Setup - *We are here*
- **Milestone 2**: Working MVP demo
- **Week 11**: Final presentation

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

*Built for AI Ventures Club - Spring 2026*
