# Evaluation Test Cases
## My Dolla $ign AI Budget Tutor

Version: 1.0  
Date: February 15, 2026  
Authors: Hugo, Rene, Gauge, Allison

## Overview

This document contains 20 synthetic user budget scenarios used to evaluate the AI tutor performance. Each test case includes:
- Input data
- Expected explanation themes
- Expected quiz alignment
- Expected tip grounding
- Pass or Fail evaluation

## Evaluation Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Data Reference Accuracy | Percent of outputs referencing real user values | 100% |
| Rule Citation Rate | Percent of outputs citing financial rules (when status is ok) | 100% |
| Quiz Relevance Rate | Percent of quizzes related to user specific data | 100% |
| Hallucination Rate | Percent of outputs with invented numbers or claims | 0% |

## Test Cases

### Case 1: College Student with Low Income
Input:
```json
{
  "monthly_income": 1500,
  "expenses": {"rent": 600, "food": 300, "entertainment": 200, "savings": 100},
  "goal": "emergency_fund"
}
```
Expected Themes: Housing at 40% (above guideline), low savings rate  
Expected Quiz: About housing percentage or savings target  
Expected Tip: Reference R_HOUSING_COST or R_SAVINGS_BENCHMARKS  
Result: PASS

### Case 2: High Earner with Good Savings
Input:
```json
{
  "monthly_income": 10000,
  "expenses": {"rent": 2500, "food": 800, "transportation": 500, "savings": 2000},
  "goal": "retirement"
}
```
Expected Themes: Strong savings (20%), housing within guideline (25%)  
Expected Quiz: About savings rate or retirement planning  
Expected Tip: Reference R_EMERGENCY_FUND or R_SAVINGS_BENCHMARKS  
Result: PASS

### Case 3: Overspender with High Entertainment
Input:
```json
{
  "monthly_income": 3000,
  "expenses": {"rent": 900, "food": 400, "entertainment": 1000, "savings": 100},
  "goal": "debt_payoff"
}
```
Expected Themes: Entertainment at 33% (excessive), low savings  
Expected Quiz: About 50/30/20 allocation or wants vs needs  
Expected Tip: Reference R_50_30_20 for reducing wants  
Result: PASS

### Case 4: Housing Cost Crisis
Input:
```json
{
  "monthly_income": 2500,
  "expenses": {"rent": 1500, "food": 300, "utilities": 200, "savings": 0},
  "goal": "general_savings"
}
```
Expected Themes: Housing at 60% (critical), zero savings  
Expected Quiz: About housing affordability guideline  
Expected Tip: Reference R_HOUSING_COST urgently  
Result: PASS

### Case 5: Perfect Budget
Input:
```json
{
  "monthly_income": 5000,
  "expenses": {"rent": 1500, "food": 500, "transportation": 300, "entertainment": 200, "savings": 1000},
  "goal": "emergency_fund"
}
```
Expected Themes: Housing 30% (ideal), savings 20% (ideal)  
Expected Quiz: Reinforce good habits  
Expected Tip: Reference R_EMERGENCY_FUND for next steps  
Result: PASS

### Case 6: No Savings
Input:
```json
{
  "monthly_income": 4000,
  "expenses": {"rent": 1200, "food": 600, "entertainment": 800, "transportation": 400, "savings": 0},
  "goal": "emergency_fund"
}
```
Expected Themes: Zero savings, goal mismatch  
Expected Quiz: About importance of savings  
Expected Tip: Reference R_SAVINGS_BENCHMARKS  
Result: PASS

### Case 7: Debt Heavy Scenario
Input:
```json
{
  "monthly_income": 3500,
  "expenses": {"rent": 1000, "food": 400, "debt_payment": 1200, "savings": 100},
  "goal": "debt_payoff"
}
```
Expected Themes: High debt payment (34% of income)  
Expected Quiz: About debt to income ratio  
Expected Tip: Reference R_DEBT_WARNING  
Result: PASS

### Case 8: Very Low Income
Input:
```json
{
  "monthly_income": 800,
  "expenses": {"rent": 400, "food": 200, "utilities": 100, "savings": 0},
  "goal": "emergency_fund"
}
```
Expected Themes: Housing at 50%, no room for savings  
Expected Quiz: About prioritization on low income  
Expected Tip: Reference R_HOUSING_COST  
Result: PASS

### Case 9: High Income with High Spending
Input:
```json
{
  "monthly_income": 15000,
  "expenses": {"rent": 4000, "food": 1500, "entertainment": 3000, "transportation": 1000, "savings": 500},
  "goal": "retirement"
}
```
Expected Themes: Low savings rate (3.3%), high entertainment  
Expected Quiz: About lifestyle inflation or savings rate  
Expected Tip: Reference R_SAVINGS_BENCHMARKS  
Result: PASS

### Case 10: Student with Scholarships
Input:
```json
{
  "monthly_income": 1200,
  "expenses": {"rent": 0, "food": 300, "entertainment": 200, "savings": 400},
  "goal": "general_savings"
}
```
Expected Themes: No housing cost, good savings rate (33%)  
Expected Quiz: About building habits early  
Expected Tip: Reference R_EMERGENCY_FUND  
Result: PASS

### Case 11: Single Parent
Input:
```json
{
  "monthly_income": 4500,
  "expenses": {"rent": 1400, "food": 800, "childcare": 1000, "transportation": 300, "savings": 200},
  "goal": "emergency_fund"
}
```
Expected Themes: Housing 31% (slightly above), low savings  
Expected Quiz: About emergency fund importance  
Expected Tip: Reference R_EMERGENCY_FUND  
Result: PASS

### Case 12: Retiree Fixed Income
Input:
```json
{
  "monthly_income": 3000,
  "expenses": {"rent": 800, "food": 400, "healthcare": 500, "utilities": 200, "savings": 100},
  "goal": "general_savings"
}
```
Expected Themes: Healthcare as significant expense, good housing ratio  
Expected Quiz: About budget priorities  
Expected Tip: Reference R_50_30_20  
Result: PASS

### Case 13: Freelancer Variable Income
Input:
```json
{
  "monthly_income": 6000,
  "expenses": {"rent": 1500, "food": 500, "business": 1000, "savings": 1500},
  "goal": "emergency_fund"
}
```
Expected Themes: Good savings (25%), should build larger buffer  
Expected Quiz: About emergency fund for variable income  
Expected Tip: Reference R_EMERGENCY_FUND (aim for 6 months)  
Result: PASS

### Case 14: New Graduate
Input:
```json
{
  "monthly_income": 3800,
  "expenses": {"rent": 1200, "food": 400, "student_loans": 500, "entertainment": 300, "savings": 300},
  "goal": "debt_payoff"
}
```
Expected Themes: Housing 32% (slightly high), has debt  
Expected Quiz: About debt repayment strategy  
Expected Tip: Reference R_50_30_20 or R_DEBT_WARNING  
Result: PASS

### Case 15: Minimum Data (Edge Case)
Input:
```json
{
  "monthly_income": 2000,
  "expenses": {"rent": 600},
  "goal": "general_savings"
}
```
Expected Themes: Only rent provided, limited analysis  
Expected Quiz: About complete budget tracking  
Expected Tip: Reference available rules  
Result: PASS

### Case 16: Missing Income (Refusal Case)
Input:
```json
{
  "monthly_income": null,
  "expenses": {"rent": 1000, "food": 400},
  "goal": "emergency_fund"
}
```
Expected Themes: REFUSAL because of insufficient data  
Expected Quiz: Generic educational question  
Expected Tip: Generic safe advice  
Result: PASS (status = "Insufficient data")

### Case 17: Empty Expenses (Refusal Case)
Input:
```json
{
  "monthly_income": 5000,
  "expenses": {},
  "goal": "retirement"
}
```
Expected Themes: REFUSAL because no expense data  
Expected Quiz: Generic educational question  
Expected Tip: Generic safe advice  
Result: PASS (status = "Insufficient data")

### Case 18: Zero Income (Edge Case)
Input:
```json
{
  "monthly_income": 0,
  "expenses": {"food": 200, "transportation": 100},
  "goal": "general_savings"
}
```
Expected Themes: REFUSAL or warning about no income  
Expected Quiz: About income sources  
Expected Tip: Safe generic advice  
Result: PASS

### Case 19: Negative Remaining (Overspending)
Input:
```json
{
  "monthly_income": 3000,
  "expenses": {"rent": 1500, "food": 800, "entertainment": 500, "transportation": 400},
  "goal": "debt_payoff"
}
```
Expected Themes: Spending exceeds income by $200  
Expected Quiz: About expense reduction  
Expected Tip: Reference R_50_30_20 urgently  
Result: PASS

### Case 20: Balanced Mid Income
Input:
```json
{
  "monthly_income": 5500,
  "expenses": {"rent": 1400, "food": 550, "transportation": 300, "utilities": 150, "entertainment": 400, "savings": 800},
  "goal": "emergency_fund"
}
```
Expected Themes: Housing 25% (good), savings 15% (decent)  
Expected Quiz: About increasing savings toward 20%  
Expected Tip: Reference R_SAVINGS_BENCHMARKS  
Result: PASS

## Summary Results

| Metric | Result |
|--------|--------|
| Data Reference Accuracy | 20/20 (100%) |
| Rule Citation Rate | 18/18 (100%) excluding refusal cases |
| Quiz Relevance Rate | 20/20 (100%) |
| Hallucination Rate | 0/20 (0%) |
| Refusal Accuracy | 2/2 (100%) |

## Running Test Cases

To run these test cases:

```bash
cd /Users/kitten/Documents/GitHub/MyDolla-Sign/backend
source venv/bin/activate
python test_tutor.py
```

Or create custom tests by modifying the user_data dictionary in test_tutor.py.
