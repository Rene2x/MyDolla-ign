# What-if edge cases (Sprint 3, Rene)

Implemented in `frontend/src/components/WhatIfPanel.jsx` with `normalizeBudgetPayload` from `frontend/src/utils/budgetPayload.js`.

| Case | Behavior |
|------|----------|
| Decrease past zero for one category | Amount **floors at $0**; optional amber notice. |
| Decrease **all** categories at once | **Decrease all categories** subtracts the same dollar amount from each line (decrease mode only); each line floored at $0. |
| Increase one line above **monthly income** | When income > 0, that category is **capped at monthly income**; notice explains the cap. |

## Quick manual check

1. Analyze a budget, open **What-if**.
2. Large **decrease** on a small category → $0 + notice if limited.
3. **Decrease all categories** with a dollar amount → every category drops, none negative.
4. **Increase** a category by an amount that would exceed income → capped + notice.
