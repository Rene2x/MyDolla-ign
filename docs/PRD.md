# Product Requirements Document (PRD)
## My Dolla $ign - Budget Education Platform

**Version:** 1.0  
**Date:** February 15, 2026  
**Authors:** Hugo, Rene, Gauge, Allison

---

## 1. Problem + Target Users

**Problem:** Many young adults and first-time earners lack access to trustworthy, easy-to-understand financial education. Without proper guidance, they struggle with basic budgeting and saving habits, leading to poor financial decisions, unnecessary stress, and debt accumulation.

**Target Users:** 
- College students managing money for the first time
- Young adults (18-30) entering the workforce
- First-time earners with limited financial education background

**Why It Matters:** Financial literacy is a critical life skill that affects long-term well-being. By providing accessible budgeting education early, we can help users build healthy financial habits and avoid common pitfalls like overspending and poor savings practices.

---

## 2. Goal / Success Metrics

| Metric | Target | How We'll Measure |
|--------|--------|-------------------|
| User Comprehension | 80%+ users understand their budget breakdown | Post-analysis survey |
| Task Completion | Users complete budget input in < 5 minutes | Time tracking |
| User Satisfaction | 4/5 average rating | In-app feedback form |
| AI Response Quality | Accurate, helpful budget explanations | Manual review of outputs |

---

## 3. MVP User Stories

1. **As a** student, **I want** to input my monthly income and expenses, **so that** I can see a clear breakdown of where my money goes.

2. **As a** first-time earner, **I want** to receive AI-generated explanations of my spending patterns, **so that** I can understand my financial habits.

3. **As a** young adult, **I want** to learn budgeting concepts in simple terms, **so that** I can make better financial decisions.

4. **As a** user, **I want** to categorize my expenses (rent, food, entertainment, etc.), **so that** I can identify areas where I might overspend.

5. **As a** user, **I want** to receive personalized budgeting tips based on my data, **so that** the advice is relevant to my situation.

6. **As a** user, **I want** to see visual representations of my budget, **so that** I can quickly understand my financial snapshot.

7. **As a** user, **I want** the platform to be simple, **so that** I don't feel overwhelmed by financial terminology.

8. **As a** user, **I want** to choose a primary financial goal (for example, emergency fund, debt payoff, big purchase), **so that** the advice and saving plan are focused on what matters most to me.

9. **As a** user, **I want** to run simple “what-if” scenarios (for example, spending less on eating out) against my existing budget, **so that** I can see the impact of changes without re-entering everything.

---

## 4. MVP Scope vs. Non-Goals

### Must-Have Features (MVP)

1. **Budget Input Form**
   - Income input field (monthly, after taxes)
   - Expense categories: Rent/Housing, Food/Groceries, Transportation, Entertainment, Utilities, Savings, Other
   - Primary goal selection (for example, general, emergency fund, debt payoff, big purchase) to focus the analysis
   - Simple, clean UI with real-time total calculation

2. **AI-Generated Budget Analysis** (via Google Gemini, free tier, with rule-based fallback)
   - **Financial advice:** One short paragraph, personalized to the user's numbers
   - **Saving tips:** 3–5 actionable bullets (for example, emergency fund, auto-transfers)
   - **Where savings could go:** Educational only—general categories (for example, high-yield savings, retirement accounts, index funds); no specific products or recommendations; always “talk to a licensed advisor”
   - **Saving plan:** Short 3–6 month plan aligned to the user's selected goal, using code-calculated numbers and AI narrative when available
   - Category-by-category breakdown and percentages (computed in code)
   - Explanation of budgeting concepts (for example, 50/30/20) in insights
   - Graceful fallback: when Gemini is unavailable (for example, due to rate limits or quota), the backend returns a deterministic rule-based response with the same structure so the UI always has content

3. **Results Display**
   - Sections: Financial advice, Saving tips, Where savings could go, Saving plan
   - Clear budget summary and visual breakdown (progress bars per category)
   - Visualizations: expense pie chart and 50/30/20 rule comparison chart
   - Simple what-if scenario panel that lets users describe a change in one category in plain language and re-runs the analysis while preserving the original baseline
   - Actionable insights list and disclaimer

### Nice-to-Have Features (Post-MVP)

- User accounts and saved budgets
- Budget tracking over time (month-to-month comparison)
- Additional advanced visualizations (for example, trends over time, multi-month comparisons)
- Mobile-responsive design improvements
- Export budget summary as PDF

### Non-Goals (What We Will NOT Build)

- **No specific investment advice** - We provide budgeting education and general “where savings could go” (e.g. savings accounts, retirement accounts, index funds as concepts only). We do not recommend specific funds or products.
- **No stock trading features** - This is not a brokerage or investment platform
- **No real-time market data** - We focus on personal budgeting, not markets
- **No user authentication for MVP** - Simplified single-session experience
- **No payment processing** - Free educational tool
- **No data persistence** - Budgets are not saved between sessions (MVP)

---

## 5. Acceptance Criteria

### Budget Input Form
- [ ] User can enter monthly income (positive numbers only)
- [ ] User can enter expenses in at least 6 categories
- [ ] Form shows real-time total of expenses
- [ ] Form shows remaining balance (income minus expenses)
- [ ] Form validates that all inputs are non-negative numbers
- [ ] Form submits successfully and shows loading state

### AI Analysis (Gemini, free tier)
- [ ] AI generates financial advice, saving tips, “where savings could go,” and a short saving plan within 10 seconds (when not rate-limited)
- [ ] AI response is in plain English (no financial jargon)
- [ ] AI provides at least 3 saving tips and 1 paragraph of financial advice
- [ ] Output includes a short 3–6 month saving plan section that aligns with the user's selected primary goal
- [ ] “Where savings could go” is educational only (no specific products)
- [ ] Insights (and 50/30/20) reflected in UI; edge cases handled (zero income, overspending)
- [ ] When Gemini is unavailable (for example, quota or network issues), the backend returns deterministic rule-based content with the same structure so the UI still shows advice, tips, and saving plan
- [ ] Disclaimer present in AI output and in UI

### Results Display
- [ ] Shows Financial advice, Saving tips, Where savings could go, and Saving plan
- [ ] Shows clear breakdown and percentage of income for each category
- [ ] Displays visual progress bars for each category
- [ ] Includes an expense pie chart and 50/30/20 comparison visualization
- [ ] Supports running at least one what-if scenario and clearly indicates when a scenario view is shown versus the original baseline
- [ ] Lists key insights; includes disclaimer

### General
- [ ] Application loads without errors
- [ ] All text is readable and accessible
- [ ] Works on desktop browsers (Chrome, Firefox, Safari)
- [ ] Page is usable (not necessarily optimized) on mobile

---

## 6. Assumptions + Constraints

### Assumptions
- Users have basic computer/internet literacy
- Users will provide honest income/expense data
- Google Gemini API (free tier) will remain available for our use case
- Users understand this is for educational purposes only
- Users are inputting monthly (not weekly/yearly) figures

### Constraints

| Constraint Type | Details |
|----------------|---------|
| **Time** | MVP must be complete by Milestone 2 |
| **Budget** | Limited API costs - must optimize token usage |
| **Data** | No access to real financial data; user-provided only |
| **Ethics** | Must include disclaimers that this is NOT financial advice |
| **Platform** | Web-based only for MVP; no mobile app |
| **API Limits** | Gemini free-tier rate limits; hybrid AI + rule-based fallback when API is unavailable |

### Privacy & Ethics Considerations
- No personal financial data is stored permanently (MVP)
- Clear disclaimers that AI-generated content is educational, not professional advice
- No collection of personally identifiable information
- User data is only used for the current session analysis

---

## Appendix: Team Task Distribution

| Section | Primary Owner | Reviewer |
|---------|--------------|----------|
| Problem + Users | Allison | Gauge |
| Success Metrics | Allison | All |
| User Stories | Gauge, Allison | All |
| MVP Scope | Hugo, Rene | All |
| Acceptance Criteria | Allison | Hugo, Rene |
| Assumptions | All | All |

### Individual Responsibilities

**Hugo (Frontend Lead)**
- Budget input form UI
- Results display component
- Visual breakdown (progress bars)
- Loading states and error handling
- Responsive design

**Rene (Backend Lead)**
- Flask API setup
- Budget analysis endpoint
- Input validation
- Error handling and logging
- API documentation

**Gauge (AI/ML Lead)**
- Google Gemini API integration (free tier)
- Prompt engineering for financial advice, saving tips, where savings could go, and saving plan
- AI response quality and safety (no specific investment recommendations)
- Edge case handling; fallback responses when API fails or is rate-limited

**Allison (Documentation & QA)**
- PRD maintenance
- Testing all features
- Bug documentation
- User testing coordination
- Pitch deck preparation

---

*Last Updated: February 24, 2026*
