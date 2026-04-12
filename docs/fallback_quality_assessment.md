# Fallback quality — AI vs deterministic (Rene / Sprint 2)

**Code:** `backend/app/services/ai_service.py` — `analyze_budget()` uses Gemini when configured; otherwise `generate_fallback_response()` with `output_source: fallback_deterministic`.

## Five scenarios to compare

| # | Scenario | What to check |
|---|----------|----------------|
| 1 | Balanced budget, positive remaining | AI: richer prose. Fallback: same numbers, shorter text, still cites savings % / rules. |
| 2 | Expenses &gt; income | Both flag overspending; fallback is explicit about negative remaining. |
| 3 | Zero income | Fallback quiz explains need for income; AI may vary wording. |
| 4 | Housing &gt; ~30% of income | Both can cite housing guideline; fallback is formulaic. |
| 5 | One category dominates | Breakdown always from code; narrative differs by path. |

**Guarantee:** Category percentages and breakdown are always computed in Python, not invented by the model.

See `POST /api/analyze` and `output_source` in the JSON response to know which path ran.
