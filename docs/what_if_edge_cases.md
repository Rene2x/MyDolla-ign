# What-if edge cases (Sprint 3, Rene)

Behavior is implemented in `frontend/src/components/WhatIfPanel.jsx` (clamping + “decrease all”) and validated against `POST /api/analyze` with `normalizeBudgetPayload` in `frontend/src/utils/budgetPayload.js`.

| Case | Expected behavior |
|------|-------------------|
| Decrease a category by more than its current amount | Per-category amount floors at **$0**. UI notes that the decrease was limited. |
| Decrease **every** category at once | **Decrease all categories** subtracts the same dollar amount from each line, each floored at $0. |
| Increase a category above **monthly income** | Single line item is **capped at monthly income** when income &gt; 0; UI notes the cap. (Totals may still exceed income if other lines are large — that is allowed for “what-if” stress tests.) |
| Zero monthly income | No income-based cap on increases; amounts still cannot go below $0. |

## Quick manual test

1. Run backend + frontend, submit a normal budget, open **What-if**.
2. Pick a small category (e.g. entertainment $200), **Decrease** by **500** → category becomes **$0**, notice mentions limit.
3. Enter **Decrease all** with **50** → every category drops by 50, none negative.
4. **Increase** rent with an absurd delta so rent would exceed income → value caps at income, notice explains cap.
