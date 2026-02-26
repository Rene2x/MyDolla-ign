# Milestone 1 Deliverables  
## Team: MyDolla-ign  
### Focus: AI-Powered Personalized Budget Tutoring System  

---

## Context

During the Spike demo, the team successfully demonstrated:

- A working budgeting dashboard  
- User financial data input  
- Pie charts and calculated financial breakdowns  

However:

- There is currently **no AI presence** in the system  
- The system performs calculations only  
- No personalized tutoring or financial guidance exists  

You have been directed to pivot toward:

> Building an AI-powered budgeting tutoring system grounded in user financial data and verified financial rules.

Milestone 1 must demonstrate real AI integration and grounded tutoring logic.

---

# Milestone 1 Objective

By Milestone 1, your team must demonstrate:

- A personalized AI tutoring backend  
- Financial rule grounding (not generic advice)  
- Structured prompt design  
- Measurable evaluation of AI outputs  
- Clean GitHub documentation and engineering structure  
- Technical walkthrough video (no UI required)

---

# 1. Updated PRD-Lite (1–2 pages)

Your PRD must clearly define the product as:

> A personalized AI budgeting tutor that explains financial data, generates quizzes, and provides grounded improvement suggestions.

## The PRD must include:

### A. Clear AI Role
The AI must:
- Explain the user’s financial breakdown
- Identify potential issues (overspending, savings imbalance)
- Reference known financial heuristics
- Generate one quiz question based on user data
- Generate one actionable tip grounded in financial rules

### B. Financial Grounding Requirement (Non-Negotiable)

AI outputs must:
- Reference actual user budget values
- Reference defined financial rules
- Avoid generic advice
- Refuse to provide unsupported financial claims

### C. MVP Scope (April 5 Preview)

Must include:
- Input: user income + categorized expenses
- AI explanation referencing user data
- One quiz question tied to that data
- One grounded financial recommendation

### D. Acceptance Criteria (Testable)

Examples:

- 100% of explanations reference user values
- All tips reference at least one financial rule
- Quiz questions directly reflect the user’s budget distribution
- No hallucinated financial projections

---

# 2. Financial Rule Base (Required)

Create:

/docs/financial_rules.md

Must include documented financial principles such as:

- 50/30/20 rule
- Savings benchmarks
- Emergency fund guidelines
- Overspending detection thresholds
- Debt-to-income considerations

For each rule, document:
- Description
- Formula or logic
- Example application

---

# 3. AI Tutor Backend (Required)

Implement:

/src/ai_tutor.py

The tutor must:

- Load user financial data
- Load financial rules
- Construct a structured prompt
- Call an LLM API
- Generate:
  - Explanation
  - Quiz question
  - Tip

The prompt must explicitly constrain the model to:

- Use only user data and financial rules
- Avoid unsupported assumptions
- Refuse if insufficient data

---

# 4. Grounding & Prompt Template Documentation

Create:

/docs/prompt_design.md

Must include:

- Prompt template used
- Explanation of grounding mechanism
- How financial rules are injected
- Refusal strategy
- Example input → output

---

# 5. Evaluation Starter Kit (Minimum 20 Cases)

Create:

/docs/evaluation_test_cases.md

Include:

- 20 synthetic user budget scenarios
- Expected explanation themes
- Expected quiz alignment
- Expected tip grounding
- Pass/Fail evaluation notes

Required metrics:

- Data reference accuracy (% outputs referencing real values)
- Rule citation rate (% outputs referencing financial rules)
- Quiz relevance rate
- Hallucination rate (should be near zero)

---

# 6. Spike Update / AI Integration Document

Create:

/docs/spike_results.md

Must include:

- Original dashboard summary
- Identified lack of AI
- AI pivot rationale
- Implementation plan
- Current AI examples

---

# 7. Architecture Diagram (1 page)

Create:

/docs/architecture.png

Must clearly show:

User Data Input  
→ Budget Logic Engine  
→ Financial Rule Base  
→ LLM Tutor  
→ Structured Output  

Label deterministic components vs generative components.

---

# 8. Required Technical Walkthrough Video (No UI Required)

Submit a 5–8 minute technical walkthrough video showing:

- How user data is parsed
- How financial rules are loaded
- How prompts are constructed
- How the LLM is called
- How grounding is enforced

UI polish is NOT required. Console demonstration is acceptable.

Store as:

/docs/demo_video.mp4

or link externally in README.

---

# 9. GitHub Repository Requirements

Your repository must include:

- /docs/PRD.md  
- /docs/financial_rules.md  
- /docs/prompt_design.md  
- /docs/spike_results.md  
- /docs/evaluation_test_cases.md  
- /docs/architecture.png  
- /src/ai_tutor.py  
- /src/rule_engine.py  
- /src/prompt_templates.py  

Additionally:

- Updated README with setup and run instructions
- requirements.txt
- .env.example
- At least one meaningful commit per team member
- Sprint 1 issue board with assigned owners

---

# Required Live Demo for Milestone 1

You must demonstrate:

1. User financial data input  
2. AI explanation referencing that data  
3. A quiz question derived from that data  
4. A grounded financial tip  
5. A refusal case if data insufficient  

If AI output is generic or ungrounded, Milestone 1 is incomplete.

---

# Milestone 1 Standard

Your project must evolve from:

“We calculate and display financial data.”

To:

“We provide personalized AI tutoring grounded in verified financial rules and user-specific data.”

This is the expected senior-level outcome.
