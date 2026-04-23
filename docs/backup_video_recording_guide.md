# Backup demo video — quick guide (~5 minutes)

Use this when you record a **screen-only backup** if the live demo fails (Sprint 3 / final demo).

## What the app does (one idea)

You type a budget → the app calls **`POST /api/analyze`** → you answer a **quiz** → **`POST /api/grade-quiz`** grades you → then you see **charts, a rule-grounded tip, and optional what‑if edits**. If Gemini is not used, the header still says **Deterministic fallback (no AI call)** so viewers see a deliberate “safe path,” not a broken app.

## Why this is easy to record

- **Leave `GEMINI_API_KEY` empty** (or comment it out in `backend/.env`) so every analyze is **predictable** and the UI **labels the path** at the top of results.
- You only need **two terminals**: backend on port **5001**, frontend dev server (proxies `/api`).

## Before you record

1. **Backend:** `cd backend` → venv → `pip install -r requirements.txt` → `python main.py`.
2. **Frontend:** `cd frontend` → `npm install` → `npm run dev`.
3. Browser: full screen or **110% zoom** if text looks small; silence notifications.

Numbers for the happy path match **`docs/final_demo_script.md`** Scenario 1 (e.g. income **4000** and the listed expenses).

## Shot list (stay under ~5 minutes)

| Time | What to show |
|------|----------------|
| ~0:15 | Say the product name and that it teaches budgeting with a **quiz before** the full explanation. |
| ~1:30 | Enter Scenario 1 numbers → **Analyze** → answer the quiz → **grade** → scroll the explanation and **financial tip**; point at **Output source** (fallback or AI). |
| ~0:45 | Scroll **pie chart**, **50/30/20**, **saving plan**; open **What‑if**, apply a small **decrease** (optional: show the amber notice if a value was **capped**). |
| ~1:00 | **Scenario 2:** income **3000**, expenses **over** income → Analyze → show overspending tone and negative remaining; use what‑if to **reduce** a category. |
| ~0:45 | **Fallback proof:** confirm **Output source** reads **Deterministic fallback** (empty key / no Studio). Say one line: “Same API, no live model call.” |

## Optional second take (with AI)

Duplicate the happy path with **`GEMINI_API_KEY` set** so **Output source** reads **AI (Google AI Studio)** — only if you want both clips; one clip with fallback is enough for the rubric’s failure path.

## See also

- `docs/final_demo_script.md` — full team demo narrative and timing  
- `README.md` — **How to Run** for exact commands  
