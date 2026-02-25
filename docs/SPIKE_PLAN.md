# Engineering Spike Plan
## My Dolla $ign - AI Budget Analysis Proof of Concept

**Date:** February 15, 2026  
**Timebox:** 3-5 days (Complete by February 20, 2026)  
**Authors:** Hugo, Rene, Gauge, Allison

---

## 1. Riskiest Assumption

**The AI (Google Gemini API, free tier) can generate accurate, helpful, and easy-to-understand budget explanations—including financial advice, saving tips, and educational “where savings could go” content—based on user-provided income and expense data.**

We need to prove that:
- The AI can interpret structured budget data correctly
- The AI produces educational content that is understandable to our target users (students, young adults)
- The AI response time is acceptable (< 10 seconds)
- The AI doesn't provide harmful or incorrect financial information (no specific investment recommendations)
- The AI delivers structured output: financial advice, saving tips, and general “where savings could go” (e.g. savings accounts, retirement accounts, index funds as concepts only)
- Calculations (totals, percentages) are done in code; AI provides narrative only
- When the Gemini free tier is unavailable (for example due to quota or rate limits), the system still returns safe, structured content via a rule-based fallback instead of failing

---

## 2. Spike Goal

**Success means:** We can demonstrate a working prototype where:
1. A user inputs income and expense data (via simple form or hardcoded test data)
2. The data is sent to Google Gemini API (free tier) with a well-crafted prompt
3. The backend computes all numbers (totals, percentages, breakdown); AI generates narrative only
4. The AI returns structured content:
   - **Financial advice** (1 paragraph, personalized)
   - **Saving tips** (3–5 actionable bullets)
   - **Where savings could go** (educational only: e.g. savings accounts, retirement accounts, index funds as concepts; no specific products)
   - Accurate, educational, safe (disclaimers), and fast (< 10 seconds)

---

## 3. Inputs / Outputs

### Input (User Data)
```json
{
  "monthly_income": 3000,
  "expenses": {
    "rent": 1200,
    "food": 400,
    "transportation": 150,
    "utilities": 100,
    "entertainment": 200,
    "savings": 300,
    "other": 150
  }
}
```

### Expected Output (Structured AI + Code)

- **Breakdown & insights:** Computed in code (totals, percentages, key insights).
- **AI-generated sections:**
  - **Financial advice:** One short paragraph (e.g. housing at 40%, saving 10%, one main lever or win).
  - **Saving tips:** 3–5 bullets (e.g. use unallocated $500 for savings, auto-transfers, emergency fund).
  - **Where savings could go:** One paragraph in general terms only (e.g. high-yield savings, 401(k)/IRA, index funds; “talk to a licensed advisor”).
  - **Saving plan (3–6 months):** A high-level sequence of steps aligned with the user's selected goal (e.g. emergency fund, debt payoff, big purchase), based on code-calculated numbers.
- **Disclaimer:** Included in AI output and in UI.

---

## 4. Demo Plan (2-3 minutes)

### Demo Flow:

| Time | Action | Who |
|------|--------|-----|
| 0:00 - 0:30 | Introduce the spike goal and what we're testing | Gauge |
| 0:30 - 1:30 | Live demo: Enter sample budget data, submit, show AI response | Gauge |
| 1:30 - 2:00 | Show the prompt engineering approach and explain why it works | Gauge |
| 2:00 - 2:30 | Discuss edge cases tested (zero income, overspending) | Rene |
| 2:30 - 3:00 | Q&A and next steps | All |

### What We'll Show:
1. Simple web form accepting budget input and primary goal selection
2. Real-time budget analysis via Google Gemini (free tier) when available, with a deterministic rule-based fallback when the API is unavailable (for example, due to quota)
3. Formatted response with Financial advice, Saving tips, Where savings could go, a 3–6 month saving plan, and expense breakdown (including 50/30/20 insights)
4. Visual charts: expense pie chart and 50/30/20 rule comparison
5. Simple “what-if” scenario tool that lets us adjust one expense category in plain language and re-run the analysis while preserving the original baseline
6. At least 2 different test scenarios:
   - Student budget (low income, high rent percentage)
   - Working adult budget (moderate income, balanced expenses)

---

## 5. Owner(s) + Tasks

### Gauge (AI/ML Lead) - PRIMARY OWNER
- [ ] Design and test AI prompt for budget analysis
- [ ] Experiment with different prompt structures for clarity
- [ ] Test edge cases (zero values, extreme values, negative values)
- [ ] Test with expenses exceeding income
- [ ] Document prompt engineering decisions
- [ ] Ensure AI explains the 50/30/20 rule clearly
- [ ] Lead the demo presentation

### Rene (Backend Lead) - SUPPORT
- [ ] Set up Google Gemini API integration (free tier, Python)
- [ ] Create simple `/api/analyze` endpoint to receive budget data
- [ ] Handle API errors gracefully (timeouts, rate limits); use rule-based fallback
- [ ] Measure and log response times
- [ ] Ensure response includes financial_advice, saving_tips, where_savings_could_go

### Hugo (Frontend Lead) - SUPPORT
- [ ] Create minimal budget input form (functional, not polished)
- [ ] Display AI response in readable format
- [ ] Add loading spinner while waiting for AI
- [ ] Handle and display error messages

### Allison (Documentation Lead) - SUPPORT
- [ ] Document the spike process and findings
- [ ] Record demo video as backup
- [ ] Note any issues or learnings for the PRD
- [ ] Prepare spike results summary

---

## 6. Exit Criteria (Pass/Fail)

### PASS Criteria (All must be met)

| Criteria | Target | How to Verify |
|----------|--------|---------------|
| API Integration | Successfully calls Gemini API (or fallback) | API returns 200 response |
| Response Time | < 10 seconds | Measured with timestamps |
| Accuracy | Correctly calculates percentages | Manual verification with calculator |
| Readability | Non-technical person understands output | Test with 2 non-CS people |
| Safety | Includes disclaimer, no harmful advice | Manual review of 5+ responses |
| Saving Plan | Includes a short 3–6 month saving plan section aligned with the user's selected goal | Manual review |
| Edge Cases | Handles 0 income, overspending scenarios | Test suite passes |
| 50/30/20 Explanation | AI explains the rule clearly | Manual review |

### FAIL Criteria (Any one = failure)

- API consistently times out or fails (>50% failure rate)
- AI produces incorrect calculations (wrong percentages)
- AI gives specific financial advice beyond budgeting education
- Response takes > 30 seconds consistently
- Cost per request exceeds $0.10
- AI response is confusing or uses too much jargon

---

## 7. If It Fails... (Plan B)

### Fallback Options:

**Option A: Use a different AI model**
- We use Gemini (free tier) by default; if limits are hit, try Claude API or other free tiers
- Gauge will research alternatives if needed

**Option B: Rule-based analysis with limited AI**
- Use AI only for generating tips/explanations
- Use code to calculate percentages and comparisons
- Reduces AI dependency and cost

**Option C: Template-based responses**
- Pre-write budget analysis templates
- Use AI only to fill in specific numbers
- Most reliable but least personalized

**Option D: Simplified MVP scope**
- Remove AI-generated explanations entirely
- Focus on visual budget breakdown only (charts/graphs)
- Add AI features in post-MVP phase

### Decision Process:
If the spike fails, the team will meet to:
1. Analyze what specifically failed
2. Evaluate each fallback option (pros/cons)
3. Choose the best path forward within 1 day
4. Adjust PRD and timeline accordingly

---

## Spike Timeline

| Day | Tasks | Owner |
|-----|-------|-------|
| Day 1 (Mon) | Set up Gemini API, initial prompt testing | Rene, Gauge |
| Day 2 (Tue) | Refine prompts, test edge cases | Gauge |
| Day 3 (Wed) | Build minimal UI, integrate end-to-end | Hugo, Rene |
| Day 4 (Thu) | Testing, bug fixes, documentation | All |
| Day 5 (Fri) | Demo prep, final testing, | All |

---

## Resources Needed

- **Google Gemini API key (free tier)** - Get at https://aistudio.google.com/app/apikey (Gauge to set up)
- **Estimated API cost for spike:** $0 (free tier; respect rate limits)
- **Development environment:** 
  - Node.js 18+ (Hugo)
  - Python 3.10+ (Rene, Gauge)
- **Test data:** Sample budgets (see examples above)

---

## Sample Prompts to Test

### Prompt v1 (Basic)
```
Analyze this budget and provide insights:
Income: $3000
Expenses: Rent $1200, Food $400, Transportation $150...
```

### Prompt v2 (Structured with Rules)
```
You are a friendly budget educator. Analyze the following budget data.

RULES:
1. Use simple language 
2. Calculate percentages for each category
3. Compare to the 50/30/20 rule
4. Give 3-4 specific tips
5. End with a disclaimer

BUDGET DATA:
[user data here]
```

### Prompt v3 (System + User Message) — **Current approach**
- **System:** Financial educator for young adults; no specific investment recommendations; explain options in general terms only; always include a disclaimer.
- **User:** Budget data + request for three sections: Financial advice, Saving tips, Where savings could go (educational only).

**Gauge will refine prompts and document which works best.**

---

## Notes

```
Space for team notes during the spike:

- 
- 
- 

```

---

*Last Updated: February 24, 2026*
