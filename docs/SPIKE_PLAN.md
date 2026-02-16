# Engineering Spike Plan
## My Dolla $ign - AI Budget Analysis Proof of Concept

**Date:** February 15, 2026  
**Timebox:** 3-5 days (Complete by February 20, 2026)  
**Authors:** Rene Sanchez, Hugo Padilla, Gauge Maltos, Allison Harvel

---

## 1. Riskiest Assumption

<!-- 
==========================================
ASSIGNED TO: Member 3 (AI/ML Lead)
This is your primary responsibility
==========================================
-->

**The AI (OpenAI API) can generate accurate, helpful, and easy-to-understand budget explanations and financial literacy content based on user-provided income and expense data.**

We need to prove that:
- The AI can interpret structured budget data correctly
- The AI produces educational content that is understandable to our target users
- The AI response time is acceptable (< 10 seconds)
- The AI doesn't provide harmful or incorrect financial advice

---

## 2. Spike Goal

**Success means:** We can demonstrate a working prototype where:
1. A user inputs income and expense data (via simple form or hardcoded test data)
2. The data is sent to OpenAI API with a well-crafted prompt
3. The AI returns a budget analysis that is:
   - Accurate (correctly interprets the numbers)
   - Educational (explains concepts simply)
   - Safe (includes appropriate disclaimers)
   - Fast (responds within 10 seconds)

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

### Expected Output (AI Response)
```
Budget Analysis for Your Monthly Finances

Income: $3,000/month

Expense Breakdown:
- Housing (Rent): $1,200 (40% of income) 
  - This is within the recommended 30-35% range, though slightly high.
  
- Food: $400 (13% of income)
  - Good! This is reasonable for a monthly food budget.

[... additional categories ...]

Key Insights:
1. You're saving 10% of your income - great start! Financial experts often recommend 20%.
2. Your housing costs are your biggest expense at 40%.
3. Consider the 50/30/20 rule: 50% needs, 30% wants, 20% savings.

What is the 50/30/20 Rule?
This budgeting guideline suggests dividing your after-tax income into three categories...

Disclaimer: This analysis is for educational purposes only and does not constitute financial advice.
```

---

## 4. Demo Plan (2-3 minutes)

<!-- 
==========================================
ASSIGNED TO: Member 3 (AI/ML Lead) - Primary Demo
SUPPORT FROM: Member 2 (Backend Lead) - API Setup
==========================================
-->

### Demo Flow:

| Time | Action | Who |
|------|--------|-----|
| 0:00 - 0:30 | Introduce the spike goal and what we're testing | Member 3 |
| 0:30 - 1:30 | Live demo: Enter sample budget data, submit, show AI response | Member 3 |
| 1:30 - 2:00 | Show the prompt engineering approach and explain why it works | Member 3 |
| 2:00 - 2:30 | Discuss edge cases tested (zero income, extreme values) | Member 2 |
| 2:30 - 3:00 | Q&A and next steps | All |

### What We'll Show:
1. Simple web form OR command-line script accepting budget input
2. Real-time API call to OpenAI
3. Formatted response displayed to user
4. At least 2 different test scenarios (student budget, working adult budget)

---

## 5. Owner(s) + Tasks

<!-- 
==========================================
TASK ASSIGNMENTS - Each member has specific responsibilities
==========================================
-->

### Member 3 (AI/ML Lead) - PRIMARY OWNER
- [ ] Design and test AI prompt for budget analysis
- [ ] Experiment with different prompt structures
- [ ] Test edge cases (zero values, extreme values, negative values)
- [ ] Document prompt engineering decisions
- [ ] Lead the demo presentation

### Member 2 (Backend Lead) - SUPPORT
- [ ] Set up OpenAI API integration (Python script)
- [ ] Create simple endpoint to receive budget data
- [ ] Handle API errors and rate limiting
- [ ] Measure and log response times

### Member 1 (Frontend Lead) - SUPPORT
- [ ] Create minimal budget input form (can be very basic)
- [ ] Display AI response in readable format
- [ ] Add loading state while waiting for AI

### Member 4 (Documentation Lead) - SUPPORT
- [ ] Document the spike process and findings
- [ ] Record demo video (backup)
- [ ] Update PRD based on spike learnings

---

## 6. Exit Criteria (Pass/Fail)

### PASS Criteria (All must be met)

| Criteria | Target | How to Verify |
|----------|--------|---------------|
| API Integration | Successfully calls OpenAI API | API returns 200 response |
| Response Time | < 10 seconds | Measured with timestamps |
| Accuracy | Correctly calculates percentages | Manual verification |
| Readability | Non-technical person understands output | Test with 2 non-CS people |
| Safety | Includes disclaimer, no harmful advice | Manual review |
| Edge Cases | Handles 0 income, missing categories | Test suite |

### FAIL Criteria (Any one = failure)

- API consistently times out or fails
- AI produces incorrect calculations
- AI gives specific investment advice (liability risk)
- Response takes > 30 seconds consistently
- Cost per request exceeds $0.10

---

## 7. If It Fails... (Plan B)

<!-- 
==========================================
ASSIGNED TO: All Team Members
Discuss and agree on fallback approaches
==========================================
-->

### Fallback Options:

**Option A: Use a different AI model**
- Try Claude API, Gemini, or open-source models
- May have different pricing/performance tradeoffs

**Option B: Pre-built templates with limited AI**
- Use AI only for specific parts (tips generation)
- Use rule-based logic for budget calculations
- Reduces AI dependency

**Option C: Simplified scope**
- Remove AI-generated explanations from MVP
- Focus on visual budget breakdown only
- Add AI features post-MVP

**Option D: Local LLM**
- Use a smaller, locally-running model
- Slower but no API costs
- More control over output

### Decision Process:
If the spike fails, the team will meet to:
1. Analyze what specifically failed
2. Evaluate each fallback option
3. Choose the best path forward within 1 day
4. Adjust PRD and timeline accordingly

---

## Spike Timeline

| Day | Tasks | Owner |
|-----|-------|-------|
| Day 1 | Set up OpenAI API, initial prompt testing | Member 2, Member 3 |
| Day 2 | Refine prompts, test edge cases | Member 3 |
| Day 3 | Build minimal UI, integrate end-to-end | Member 1, Member 2 |
| Day 4 | Testing, bug fixes, documentation | All |
| Day 5 | Demo prep, final testing | All |

---

## Resources Needed

- OpenAI API key (sign up at platform.openai.com)
- Estimated API cost for spike: $5-10
- Development environment (Node.js, Python)
- Test data (sample budgets)

---

## Notes

<!-- Space for team notes during the spike -->

```
Add your notes here as you work through the spike...
```

---

*Last Updated: February 15, 2026*
