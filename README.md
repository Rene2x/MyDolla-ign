# My Dolla $ign

> An AI-powered financial literacy platform that teaches budgeting and investing concepts in simple, easy-to-understand terms for young adults, students, and first-time earners.

## Problem We're Solving

Many people struggle to budget, save, and understand investing basics due to a lack of accessible, trustworthy financial guidance. Our platform provides educational budget breakdowns and learning guidance to help users build financial confidence.

## Team Members & Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| **Hugo** | Frontend Lead | UI/UX, React components, form handling |
| **Rene** | Backend Lead | API development, data processing, server setup |
| **Gauge**| AI/ML Lead | AI integration, prompt engineering, budget analysis |
| **Allison** | Documentation & QA | PRD, testing, deployment, documentation |



## MVP Features

1. **Budget Input Form** - Categorized expense breakdown (income, rent, food, etc.)
2. **AI-Generated Analysis** - Explanation of spending patterns and budgeting concepts
3. **Investment Literacy Module** - Introduction to terms like stocks, ETFs, and risk evaluation

## Tech Stack

- **Frontend**: React.js with Tailwind CSS
- **Backend**: Python (Flask) with REST API
- **AI**: OpenAI API for content generation
- **Database**: SQLite (for MVP) / PostgreSQL (future)

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
- OpenAI API key

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```

> **Note**: Detailed setup instructions will be added as development progresses.

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
