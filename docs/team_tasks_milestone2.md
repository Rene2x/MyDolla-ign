# Milestone 2 team tasks

 Pick one each and check in when it is done.

## 1. UI polish

Focus on the budget form and the analysis flow after Analyze returns: quiz step, grader verdict, answer key, then explanation and tip. Tighten spacing and typography, make sure the layout reads well on a phone width, and keep focus states and labels clear for the textarea and buttons. The main components live in `frontend/src/components/BudgetResults.jsx` and `frontend/src/components/BudgetForm.jsx`. There is a short note at the top of `BudgetResults.jsx` pointing at this task.

## 2. Documentation

The app now has two API actions the grader cares about: `POST /api/analyze` for the budget payload and `POST /api/grade-quiz` for submitting the quiz answer. Walk through `README.md`, `docs/milestone2_demo.md`, and the MVP section at the top of `docs/prompt_design.md` and make sure they describe the three-step user flow accurately (quiz, then AI verdict, then explanation and tip). There is a note in `backend/app/routes/budget.py` pointing at this task.

## 3. Demo video

Record the walkthrough the rubric asks for: browser MVP, one full success path including submitting the quiz and showing the verdict, where the explanation and tip appear, and one safe failure or fallback (for example validation error or deterministic fallback). Use the sample numbers in `docs/milestone2_demo.md` if you want a script. Either add `docs/milestone2_demo.mp4` to the repo or paste a link into that file. There is a note at the top of `docs/demo_video.md` pointing at this task.
