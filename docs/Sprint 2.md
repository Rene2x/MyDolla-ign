# Sprint 2 Plan — Venture 5: myDolla$ign

**Sprint Duration:** April 8 – April 14, 2026
**Sprint Goal:** Wire remaining UI components, clean up legacy code, and add quantitative evaluation metrics.
**Final Demo:** April 29, 2026

---

## Context

After Milestone 2, myDolla$ign has one of the strongest MVPs: working end-to-end flow with three-tier AI fallback, quiz grading, and a well-designed stepped UI. The main areas for Sprint 2 are integrating the remaining PRD features (pie chart, 50/30/20 comparison, what-if scenarios), cleaning up legacy code, and strengthening evaluation with quantitative metrics.

---

## Sprint 2 Tasks

### P0 — Wire Remaining UI Components (Days 1–4)

| Task | Owner | Description |
|---|---|---|
| Integrate ExpensePieChart | Gauge | Wire `ExpensePieChart.jsx` into `BudgetResults.jsx` to show visual breakdown of user's expense categories |
| Integrate BudgetComparison | Hugo | Wire `BudgetComparison.jsx` to display 50/30/20 rule comparison against user's actual spending |
| What-if scenario panel | Rene | Implement what-if functionality: "What if I reduced entertainment by $100?" → show updated analysis |
| Saving plan display | Allison | Display the saving plan section from AI response (3-6 month plan) in a clean, timeline-style UI |

### P1 — Code Cleanup (Days 2–4)

| Task | Owner | Description |
|---|---|---|
| Remove legacy backend/src/ | Rene | Delete `backend/src/ai_tutor.py`, `rule_engine.py`, `prompt_templates.py`, `rules/financial_rules.json` — these are M1 artifacts |
| Remove legacy Flask template | Rene | Delete `backend/templates/index.html` — no longer the active UI |
| Clean up demo.py | Gauge | Either integrate terminal demo into main app or clearly mark as a standalone utility |
| Mark demo video complete | Allison | Update Milestone 2 Deliverables checklist to check the demo video box (links exist) |

### P2 — Evaluation Strengthening (Days 3–6)

| Task | Owner | Description |
|---|---|---|
| Add quantitative metrics | Allison | Create metrics table: grounding accuracy (% of explanations referencing user's actual numbers), quiz relevance, tip-to-rule mapping accuracy |
| Real user testing | All | Have 3-5 non-team-members test the app with their own budget data. Document feedback |
| Edge case expansion | Gauge | Test: zero income, all expenses exceed income, extreme values, single category only |
| Fallback quality assessment | Rene | Compare AI output vs deterministic fallback across 5 scenarios. Document quality differences |

### P3 — Demo Polish (Days 5–7)

| Task | Owner | Description |
|---|---|---|
| Loading state animations | Hugo | Add smooth transitions between the 3 steps (quiz → grading → results) |
| Mobile responsiveness | Hugo | Ensure the UI works well on smaller screens for demo flexibility |
| Demo rehearsal | All | Full team run-through with success, fallback, and edge cases |
| Update README | Allison | Document all new features and components added in Sprint 2 |

---

## Definition of Done (Sprint 2)

- [ ] Pie chart displays user's expense breakdown
- [ ] 50/30/20 comparison shows in results
- [ ] Legacy M1 code removed from `backend/src/` and `backend/templates/`
- [ ] Quantitative evaluation metrics documented
- [ ] At least 3 non-team-members have tested the app
- [ ] Each team member has code commits this sprint

---

## Contribution Expectations

Hugo dominated Milestone 2 contributions (18 commits including the major MVP commit). For Sprint 2, **Rene**, **Gauge**, and **Allison** should each own and deliver at least one feature. Tasks are distributed to balance the workload.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 2 (this sprint) | Apr 8–14 | Wire remaining components, cleanup, evaluation |
| Sprint 3 | Apr 15–21 | What-if refinement, presentation prep, user feedback iteration |
| Sprint 4 | Apr 22–28 | Final polish, demo rehearsal, final deliverables |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |
