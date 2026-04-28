# Sprint 3 Grade, Venture 5: myDolla$ign

**Graded:** April 28, 2026
**Sprint Window:** April 15 – April 24, 2026 (extended from April 21)
**Final Demo:** April 29, 2026
**Final Deliverables Due:** May 3, 2026

---

## Overall Grade: 94/100

**Note on individual grades:** This is the venture-level grade. Members who severely under-contributed during Sprint 3 may receive a reduced individual grade applied separately.

**Note on grading scope:** Final-presentation prep items (rehearsal logs, slide deck drafts, pitch deck refreshes, backup recordings) are not counted against the Sprint 3 grade. They appear in the "Items to Complete by May 3" section instead.

---

## Summary

Sprint 3 produced the evaluation evidence the team had been missing and the codebase polish that takes the app from "M2 demo" to "final-demo ready." The quantitative metrics document (`evaluation_metrics.md`) gives grounding accuracy, quiz relevance, and tip-to-rule mapping numbers across at least 10 of the 20 scenarios. The fallback side-by-side document is now backed by real captured outputs of both AI mode and deterministic mode (Rene's Apr 22-23 capture script and JSON evidence). User testing notes from non-team-member testers landed in `user_testing.md`. The final demo script, README features section, and demo-rehearsal notes all shipped.

On the code side, `BudgetResults.jsx` was split into four focused subcomponents (`BudgetComparison.jsx`, `ExpensePieChart.jsx`, `QuizFlow.jsx`, `SavingPlan.jsx`, `WhatIfPanel.jsx`), the pie-chart label alignment is fixed, what-if edge cases now clamp safely (negative values, decrease-all, increase-beyond-income), the AI token-limit increase has a regression test in `backend/test_tutor.py`, and a `Toast.jsx` component replaces raw error text in the UI. An accessibility pass was completed on the form, chart, and keyboard navigation.

Contribution is balanced across all four members in the extended window: Hugo 8, Rene 6, Allison 6, Gauge 3. Rene's six commits all landed Apr 22-23 (within the extended deadline) and delivered both Rene-owned tasks (P0 fallback side-by-side, P2 what-if edge cases). The pattern repeats from prior sprints (Rene ships in concentrated bursts) but the work is real and on time.

The grade sits at 94 rather than higher because the M2 deliverables checkbox for the demo video was not flipped (small but explicit P1 task).

---

## Category Breakdown

### 1. Task Completion (38/40)

**P0 (3 of 3 complete):**
- Quantitative metrics table: shipped (`docs/evaluation_metrics.md`).
- Fallback side-by-side with captured outputs: shipped (`fallback_quality_assessment.md` + capture script + JSON outputs from Rene's Apr 22-23 work).
- Real user testing: shipped (`docs/user_testing.md` with feedback from multiple testers).

**P1 (3 of 4 complete):**
- Final demo script: shipped (`docs/final_demo_script.md`).
- README refresh with Sprint 2 features: shipped.
- Demo rehearsal round 1: shipped (`demo_rehearsal.md` notes from the team walk-through).
- Check M2 deliverables checkbox: not done. `Milestone 2 Deliverables.md` line 194 still shows the demo-video item unchecked.

**P2 (4 of 4 complete):**
- BudgetResults refactor: shipped. Component split into BudgetComparison, ExpensePieChart, QuizFlow, SavingPlan, WhatIfPanel.
- Pie chart label alignment: shipped.
- What-if edge cases: shipped with input clamping.
- Token limit regression check: shipped (`backend/test_tutor.py` smoke + parsing + token-config tests).

**P3 (2 of 2 graded; backup demo video deferred to final-prep):**
- Toast component: shipped (`Toast.jsx`).
- Accessibility pass: shipped (form, chart, keyboard navigation).
- Backup demo video recording: deferred to final-prep (May 3 deliverables).

### 2. Code Quality (18/20)

- BudgetResults split into focused subcomponents is a clean refactor and makes the demo code review readable.
- WhatIfPanel input clamping handles negative values, decrease-all, and increase-beyond-income.
- `Toast.jsx` is a small, reusable component.
- Pie chart fix is a small change but the kind of polish that matters on stage.

### 3. Documentation (14/15)

- `evaluation_metrics.md` is concrete with quantitative scoring.
- `fallback_quality_assessment.md` now has captured AI vs deterministic outputs.
- `user_testing.md` is real feedback, not a template.
- `final_demo_script.md` is ready for Apr 29.

### 4. Testing / Evaluation (14/15)

- 10+ scenarios scored quantitatively for grounding, quiz relevance, tip-to-rule mapping.
- Side-by-side AI vs deterministic captures.
- Real user-tester feedback (3 to 5 testers).
- `backend/test_tutor.py` regression tests.

### 5. Team Contribution (10/10)

| Member | In-window Commits | Sprint 3 Work | Signal |
|---|---|---|---|
| Hugo / hpadi02 | 8 | Demo script, user testing, toast component, regression tests | Strong |
| Rene / Rene2x | 6 | Fallback side-by-side captures with deterministic JSON, what-if edge-case clamping, backup video guide | Strong (concentrated Apr 22-23) |
| Allison / Allirose140 | 6 | Evaluation metrics doc, README refresh, accessibility pass | Strong |
| Gauge / gmalt02 | 3 | BudgetResults refactor (significant), pie chart fix, additional tester insights | Strong |

All four members shipped meaningful work. Gauge's three commits include the BudgetResults refactor, which is the largest code change of the sprint. Rene's late-window concentration is a recurring pattern but every assigned task landed within the extended deadline.

---

## Per-Task Completion Status

| Priority | Task | Owner | Status |
|---|---|---|---|
| P0 | Quantitative metrics table | Allison | Done |
| P0 | Fallback side-by-side results | Rene | Done |
| P0 | Real user testing | Gauge + Hugo | Done |
| P1 | Final demo script | Hugo | Done |
| P1 | README refresh | Allison | Done |
| P1 | Check M2 deliverables box | Allison | Not done |
| P1 | Demo rehearsal round 1 | All | Done |
| P2 | BudgetResults refactor | Gauge | Done |
| P2 | Pie chart label alignment | Gauge | Done |
| P2 | What-if edge cases | Rene | Done |
| P2 | Token limit regression check | Hugo | Done |
| P3 | Error toast component | Hugo | Done |
| P3 | Accessibility pass | Allison | Done |
| P3 | Record backup demo video | Rene | Deferred to final-prep |

---

## Definition of Done (Sprint 3) Check

- [x] `docs/evaluation_metrics.md` exists with at least 3 quantitative metrics scored against 10+ scenarios
- [x] `docs/fallback_quality_assessment.md` contains real AI and deterministic outputs side by side
- [x] `docs/user_testing.md` documents feedback from 3+ non-team testers
- [x] `docs/final_demo_script.md` exists with scenario walkthroughs and target timing
- [x] README has a Sprint 2 features section
- [ ] Demo video checkbox in `Milestone 2 Deliverables.md` is checked
- [x] At least one full team rehearsal completed
- [x] Each team member has code or documentation commits this sprint

---

## Items to Complete by May 3 (Final Deliverables)

The May 3 package is required to be under `docs/Final_Demo/` in the repo. Save the following items there:

1. **Final demo slides** (PDF or PPTX) under `docs/Final_Demo/`. Cover: problem (financial education for younger users), 3-step flow (input → grounded explanation → quiz), 50/30/20 + what-if + saving plan visualizations, evaluation numbers from `evaluation_metrics.md`, live-demo plan.
2. **Runbook** at `docs/Final_Demo/Runbook.md`. Cover: prerequisites (Node, Python), env setup, how to start backend (`python backend/app.py`) and frontend, how to walk through the 3 steps, how to switch to deterministic mode (unsetting API key for fallback demo), known edge cases (negative what-if, decrease-all).
3. **Final demo video** at `docs/Final_Demo/Final_Demo_Video.mp4`. This is the same artifact as the Sprint 3 P3 backup recording: capture a polished 5-minute screen capture that you can fall back to on Apr 29 if the live demo hits a snag.
4. **Final code on `main`**. Confirm `main` reflects the demo state after Apr 29.

Sprint 3 carryovers worth closing in the same window:

5. **Flip the M2 demo video checkbox** in `docs/Milestone 2 Deliverables.md` line 194. One-line change.
6. **Second timed rehearsal**. The plan called for round 1; for the final-deliverables narrative, doing one more dry-run after Apr 29 with all final tweaks and noting it in `docs/Final_Demo/post_demo_notes.md` is good evidence of polish.
