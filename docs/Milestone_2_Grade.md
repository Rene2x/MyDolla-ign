# Milestone 2 Grade — Venture 5: myDolla$ign

**Graded:** April 8, 2026
**Deadline:** April 5, 2026 (end of day)
**Late Commits:** None — all 39 commits are on or before 4/5/2026.

---

## Overall Grade: 92/100

---

## Summary

myDolla$ign delivers one of the strongest Milestone 2 submissions. The MVP flow works end-to-end: a React frontend with income/expense input form sends data to a Flask backend, which runs AI analysis via Google Gemini (with Vertex AI and deterministic fallback tiers), returning a grounded explanation, quiz question, and financial tip — all displayed in a well-designed three-step UI (quiz → grading → explanation). The fallback system is comprehensive, input validation is solid, and the prompt engineering is sophisticated (calculated budget summary injected into prompts to prevent AI hallucination of numbers). Documentation is thorough across the board.

### Video Review Notes
The demo video is ~3 minutes — **below the required 4-7 minutes**. **Strengths:** Budget form with 7 expense categories works, real-time total/remaining calculation, AI analysis produces grounded category breakdown with real percentages, quiz question references specific budget values ($300.00, 10.0%), quiz grading works end-to-end with AI evaluation (verdict: "PARTIALLY CORRECT"), and the "Output source: AI (Google AI Studio)" label provides transparency. Edge case demonstrated: expenses exceeding income ($12,000 rent on $3,000 income) shows negative remaining in red. **Critical gaps:** The presenter **never clicks "Continue to explanation and tip" (Step 3)** — meaning the grounded explanation and financial tip (two of three core required outputs) are never shown on screen. No AI-failure/fallback demo (only input validation edge case shown, not LLM unavailability). Video is 1+ minute short of minimum. For the final demo, make sure to walk through all three steps including the explanation and financial tip.

---

## Category Breakdown

### 1. End-to-End Demo Path (25/25)
- Browser flow works: form → /api/analyze → 3-step result display (quiz → grading → explanation+tip). ✓
- Explanation references real user budget values via calculated summary injection. ✓
- Quiz question tied to submitted budget. ✓
- Financial tip grounded in documented rules from `financial_rules.md`. ✓
- Three-tier AI: Google AI Studio → Vertex AI → Deterministic fallback. ✓
- Quiz grading via `/api/grade-quiz` with AI evaluation of free-text answers — goes beyond requirements. ✓
- Output source transparency label ("AI (Google AI Studio)" / "Deterministic fallback"). ✓
- Input validation for negative values, missing fields, zero income. ✓
- Disclaimer present in prompts and UI. ✓
- **Minor issue:** Some PRD features (pie chart, 50/30/20 comparison, what-if scenarios) have components created but may not be wired into the current main flow.

### 2. Code Quality & Architecture (19/20)
- Clean separation: `ai_service.py` (704 lines, core orchestration), `budget.py` (routes), `budget.py` (models).
- Structured response parsing into sections (advice, quiz, answer key, tip, saving tips, plan, insights).
- Fallback produces identical response shape — UI works regardless of AI availability. ✓
- Input sanitization and validation on both frontend and backend. ✓
- Vite config with proxy for clean API routing. ✓
- **Issue:** Legacy Milestone 1 code in `backend/src/` (ai_tutor.py, rule_engine.py, prompt_templates.py) should be cleaned up.
- **Issue:** Legacy Flask template UI (`templates/index.html`) is no longer the active path.

### 3. Documentation & Deliverables (23/25)
- PRD.md — comprehensive with problem statement, target users, MVP scope, team roles. ✓
- `financial_rules.md` — 5 documented financial rules used for grounding. ✓
- `prompt_design.md` — prompt engineering documentation. ✓
- `milestone2_demo.md` — MVP demo guide with startup instructions, sample budget, fallback instructions. ✓
- `team_tasks_milestone2.md` — task assignments for 3 teammates. ✓
- `evaluation_test_cases.md` — 20 synthetic test cases. ✓
- Demo videos — 2 YouTube links provided. ✓
- `.env.example` present with all required variables. ✓
- README updated with Milestone 2 flow, setup for both backend and frontend. ✓
- **Minor issue:** Milestone 2 Deliverables checklist shows demo video checkbox as unchecked, though links exist.

### 4. Evaluation Evidence (14/15)
- 20 test cases covering various budget scenarios. ✓
- Tests are synthetic/generated rather than from real user testing — adequate but could be stronger.
- No explicit pass/fail metrics table (retrieval accuracy, grounding accuracy, etc.) — evaluation is more descriptive than quantitative.

### 5. Repository Hygiene (14/15)
- `.gitignore`, `.env.example`, `requirements.txt`, `LICENSE` all present. ✓
- Clean project structure with separate frontend/backend directories. ✓
- Vite + Tailwind CSS setup. ✓
- **Minor:** Legacy code in `backend/src/` and `backend/templates/` should be removed.

---

## Individual Grades

| Team Member | Commits | Contribution Area | Grade |
|---|---|---|---|
| hpadi02 (Hugo) | 18 | Frontend lead, major MVP commit (quiz grading, AI Studio, stepped UI), project setup, merges | 97/100 |
| gmalt02 (Gauge) | 6 | UI polish, README update, documentation enhancements | 90/100 |
| Rene2x (Rene) | 6 | Backend lead, AI tutor backend, merges | 90/100 |
| Allirose140 (Allison) | 5 | Financial rules documentation, Flask UI, demo video link | 88/100 |

**Note:** Hugo's contribution is dominant — particularly the massive April 4 commit (`b63ab76`) that added most Milestone 2 functionality. However, the team is small (4 people) and all members contributed in their assigned areas. The distribution is reasonable given team roles, though more balance would be ideal. Many of Hugo's commits are merges, and the core work was a concentrated effort.

---

## Key Recommendations for Sprint 2
1. Wire remaining PRD components into the UI (pie chart, 50/30/20 comparison, what-if scenarios).
2. Clean up legacy Milestone 1 code in `backend/src/` and `backend/templates/`.
3. Add quantitative evaluation metrics (grounding accuracy, citation coverage, etc.).
4. Mark demo video checkbox as complete in deliverables.
5. Consider adding real user testing beyond synthetic test cases.
6. Balance contributions more evenly for the final sprint.
