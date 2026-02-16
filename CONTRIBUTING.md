# Contributing to My Dolla $ign

This document outlines how team members should collaborate on this project.

## Team Roles and Responsibilities

### Member 1 - Frontend Lead
**Primary Responsibilities:**
- All React components in `/frontend/src/components/`
- UI/UX design and styling with Tailwind CSS
- Form handling and validation
- State management
- Connecting frontend to backend API

**Files You Own:**
- `frontend/src/App.jsx`
- `frontend/src/components/*.jsx`
- `frontend/src/index.css`
- `frontend/tailwind.config.js`

**Your TODOs:**
- [ ] Set up the development environment (`npm install`)
- [ ] Implement form validation in `BudgetForm.jsx`
- [ ] Add chart visualization in `BudgetResults.jsx`
- [ ] Make the UI responsive for mobile
- [ ] Test all user interactions

---

### Member 2 - Backend Lead
**Primary Responsibilities:**
- Flask API setup and configuration
- API route handlers
- Data validation and error handling
- Database setup (if needed)
- Deployment configuration

**Files You Own:**
- `backend/main.py`
- `backend/app/routes/*.py`
- `backend/app/models/*.py`
- `backend/requirements.txt`

**Your TODOs:**
- [ ] Set up Python virtual environment
- [ ] Configure environment variables (copy `.env.example` to `.env`)
- [ ] Test API endpoints with Postman or curl
- [ ] Add proper error logging
- [ ] Set up rate limiting for API endpoints

---

### Member 3 - AI/ML Lead
**Primary Responsibilities:**
- OpenAI API integration
- Prompt engineering for budget analysis
- AI response quality and safety
- Testing edge cases with AI
- Financial literacy content accuracy

**Files You Own:**
- `backend/app/services/ai_service.py`
- AI prompts and configuration
- Glossary content (review)

**Your TODOs:**
- [ ] Get OpenAI API key and add to `.env`
- [ ] Design and test the budget analysis prompt
- [ ] Test with various budget scenarios
- [ ] Ensure AI doesn't give harmful financial advice
- [ ] Document prompt engineering decisions
- [ ] Lead the spike demo

---

### Member 4 - Documentation & QA Lead
**Primary Responsibilities:**
- PRD documentation
- Spike plan documentation
- Testing and quality assurance
- User documentation
- Pitch deck preparation

**Files You Own:**
- `docs/PRD.md`
- `docs/SPIKE_PLAN.md`
- `docs/pitch-deck.pdf` (to be created)
- `README.md` (updates)

**Your TODOs:**
- [ ] Fill in team member names in all docs
- [ ] Review and refine PRD sections
- [ ] Create the pitch deck
- [ ] Test the application end-to-end
- [ ] Document any bugs found
- [ ] Prepare for the demo presentation

---

## Development Workflow

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-org]/MyDolla-Sign.git
   cd MyDolla-Sign
   ```

2. **Set up frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Set up backend (in a new terminal):**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   python main.py
   ```

### Git Workflow

1. **Always pull before starting work:**
   ```bash
   git pull origin main
   ```

2. **Create a branch for your feature:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

4. **Push and create a pull request:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a PR on GitHub for team review.

### Code Style

- **Frontend:** Use consistent formatting (Prettier recommended)
- **Backend:** Follow PEP 8 Python style guidelines
- **Comments:** Leave TODO comments for incomplete features
- **Commits:** Write clear, descriptive commit messages

---

## Communication

- Create GitHub Issues for bugs and feature requests
- Use pull requests for code review
- Tag relevant team members in PRs
- Update the TODO lists in code as you complete tasks

---

## Important Deadlines

- **Repository Setup Due:** Tuesday, February 17th, 2026 at 11:59 PM
- **Spike Demo:** End of Week 4
- **MVP Complete:** Milestone 2

---

## Questions?

If you're stuck or have questions:
1. Check the code comments and TODOs
2. Review the PRD and Spike Plan
3. Ask your team members
4. Reach out to the AI Ventures Club mentors
