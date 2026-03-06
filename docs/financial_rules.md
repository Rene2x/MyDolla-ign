# Financial Rule Base

This document contains the financial rules used by the AI Budget Tutor to provide grounded advice.

## 1. 50/30/20 Budget Rule

### Description
A budgeting guideline that allocates:
- 50% of income to Needs
- 30% of income to Wants
- 20% of income to Savings or debt repayment

### Formula
- Needs % = (Needs / Income) x 100
- Wants % = (Wants / Income) x 100
- Savings % = (Savings / Income) x 100

### Flag Conditions
- Needs greater than 50%
- Wants greater than 30%
- Savings less than 20%

### Example Application
Income: $4,000  
Needs: $2,400 which is 60% (Above target)  
Savings: $400 which is 10% (Below recommended)

Triggered Rules:
- Needs overspending
- Savings below benchmark

## 2. Savings Benchmarks

### Description
Savings health indicators:
- Minimum: 10%
- Recommended: 15 to 20%
- Strong: 20% or more

### Formula
Savings % = (Savings / Income) x 100

### Example
Income: $5,000  
Savings: $500 which is 10% (Minimum level only)

## 3. Emergency Fund Guideline

### Description
An emergency fund should cover 3 to 6 months of essential expenses.

### Logic
- Minimum Fund = Monthly Essential Expenses x 3
- Ideal Fund = Monthly Essential Expenses x 6

### Example
Essential expenses: $2,000  
Minimum target: $6,000  
Ideal target: $12,000

## 4. Overspending Threshold Detection

### Description
Spending imbalance detection rule.

### Logic
Category % = (Category Spending / Income) x 100

### Flag If
- Housing greater than 35% of income
- Any non housing category greater than 30% of income

### Example
Rent: $2,000  
Income: $4,000  
Result: 50% which triggers overspending alert

## 5. Debt to Income Ratio (DTI)

### Description
Debt payments should not exceed 36% of income.

### Formula
DTI = (Monthly Debt Payments / Income) x 100

### Flag If
DTI greater than 36%

### Example
Debt: $1,800  
Income: $4,000  
DTI = 45% which is High risk
