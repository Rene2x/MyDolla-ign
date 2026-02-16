# Product Requirements Document (PRD)
## My Dolla $ign - Financial Literacy Platform

**Version:** 1.0  
**Date:** February 15, 2026  
**Authors:** Rene Sanchez, Hugo Padilla, Gauge Maltos, Allison Harvel

---

## 1. Problem + Target Users

<!-- 
==========================================
ASSIGNED TO: Member 4 (Documentation Lead)
TODO: Expand these 2-4 sentences based on your research
==========================================
-->

**Problem:** Many young adults and first-time earners lack access to trustworthy, easy-to-understand financial education. Without proper guidance, they struggle with basic budgeting, saving habits, and understanding investment concepts, leading to poor financial decisions and stress.

**Target Users:** 
- College students managing money for the first time
- Young adults (18-30) entering the workforce
- First-time earners with limited financial education background

**Why It Matters:** Financial literacy is a critical life skill that affects long-term well-being. By providing accessible education early, we can help users build healthy financial habits and avoid common pitfalls like debt accumulation and poor savings practices.

---

## 2. Goal / Success Metrics

<!-- 
==========================================
ASSIGNED TO: Member 4 (Documentation Lead)
TODO: Refine these metrics based on team discussion
==========================================
-->

| Metric | Target | How We'll Measure |
|--------|--------|-------------------|
| User Comprehension | 80%+ users understand budget breakdown | Post-analysis survey |
| Task Completion | Users complete budget input in < 5 minutes | Time tracking |
| User Satisfaction | 4/5 average rating | In-app feedback form |
| AI Response Quality | Accurate, helpful explanations | Manual review of outputs |

---

## 3. MVP User Stories

<!-- 
==========================================
ASSIGNED TO: Member 3 (AI/ML Lead) & Member 4 (Documentation Lead)
TODO: Review and add any missing user stories
==========================================
-->

1. **As a** student, **I want** to input my monthly income and expenses, **so that** I can see a clear breakdown of where my money goes.

2. **As a** first-time earner, **I want** to receive AI-generated explanations of my spending patterns, **so that** I can understand my financial habits.

3. **As a** young adult, **I want** to learn budgeting concepts in simple terms, **so that** I can make better financial decisions.

4. **As a** user, **I want** to categorize my expenses (rent, food, entertainment, etc.), **so that** I can identify areas where I might overspend.

5. **As a** beginner investor, **I want** to learn basic investment terms (stocks, ETFs, risk), **so that** I can start building financial knowledge.

6. **As a** user, **I want** to receive personalized budgeting tips based on my data, **so that** the advice is relevant to my situation.

7. **As a** user, **I want** to see visual representations of my budget, **so that** I can quickly understand my financial snapshot.

8. **As a** user, **I want** the platform to be simple and jargon-free, **so that** I don't feel overwhelmed by financial terminology.

---

## 4. MVP Scope vs. Non-Goals

### Must-Have Features (MVP)

<!-- 
==========================================
ASSIGNED TO: Member 1 (Frontend) & Member 2 (Backend)
TODO: Confirm technical feasibility of each feature
==========================================
-->

1. **Budget Input Form**
   - Income input field
   - Expense categories: Rent/Housing, Food/Groceries, Transportation, Entertainment, Utilities, Savings, Other
   - Simple, clean UI

2. **AI-Generated Budget Analysis**
   - Spending pattern explanation
   - Category-by-category breakdown
   - Simple budgeting tips

3. **Investment Literacy Section**
   - Glossary of basic terms (stocks, ETFs, bonds, risk)
   - Educational explanations (not financial advice)

4. **Results Display**
   - Clear budget summary
   - Visual breakdown (pie chart or bar graph)
   - Actionable insights

### Nice-to-Have Features (Post-MVP)

- User accounts and saved budgets
- Budget tracking over time
- Comparison with recommended budgets (50/30/20 rule)
- Mobile-responsive design improvements
- Export budget as PDF

### Non-Goals (What We Will NOT Build)

- **No actual financial advice** - We provide education only, not personalized investment recommendations
- **No stock trading features** - This is not a brokerage platform
- **No real-time market data** - We focus on concepts, not live prices
- **No user authentication for MVP** - Simplified single-session experience
- **No payment processing** - Free educational tool

---

## 5. Acceptance Criteria

<!-- 
==========================================
ASSIGNED TO: Member 4 (Documentation Lead)
TODO: Add any additional test cases
==========================================
-->

### Budget Input Form
- [ ] User can enter monthly income (positive numbers only)
- [ ] User can enter expenses in at least 5 categories
- [ ] Form validates that expenses don't exceed income (warning, not blocking)
- [ ] Form submits successfully and shows loading state

### AI Analysis
- [ ] AI generates budget explanation within 10 seconds
- [ ] AI response is in plain English (no jargon)
- [ ] AI provides at least 3 actionable insights
- [ ] AI handles edge cases (zero income, very high expenses)

### Investment Literacy
- [ ] User can access glossary of at least 10 financial terms
- [ ] Each term has a clear, simple explanation
- [ ] Explanations include real-world examples

### General
- [ ] Application loads without errors
- [ ] All text is readable and accessible
- [ ] Works on desktop browsers (Chrome, Firefox, Safari)

---

## 6. Assumptions + Constraints

<!-- 
==========================================
ASSIGNED TO: All Team Members
TODO: Review and update based on your specific situation
==========================================
-->

### Assumptions
- Users have basic computer/internet literacy
- Users will provide honest income/expense data
- OpenAI API will remain available and affordable for our use case
- Users understand this is for educational purposes only

### Constraints

| Constraint Type | Details |
|----------------|---------|
| **Time** | MVP must be complete by Milestone 2 (within 11 weeks) |
| **Budget** | Limited API costs - must optimize token usage |
| **Data** | No access to real financial data; user-provided only |
| **Ethics** | Must include disclaimers that this is NOT financial advice |
| **Platform** | Web-based only for MVP; no mobile app |
| **API Limits** | OpenAI rate limits and costs must be managed |

### Privacy & Ethics Considerations
- No personal financial data is stored permanently (MVP)
- Clear disclaimers that AI-generated content is educational, not professional advice
- No collection of personally identifiable information

---

## Appendix: Team Task Distribution

| Section | Primary Owner | Reviewer |
|---------|--------------|----------|
| Problem + Users | Member 4 | Member 3 |
| Success Metrics | Member 4 | All |
| User Stories | Member 3, Member 4 | All |
| MVP Scope | Member 1, Member 2 | All |
| Acceptance Criteria | Member 4 | Member 1, Member 2 |
| Assumptions | All | All |

---

*Last Updated: February 15, 2026*
