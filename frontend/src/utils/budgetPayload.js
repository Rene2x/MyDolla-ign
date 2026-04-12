/**
 * Normalize budget payload for POST /api/analyze (numeric expenses, valid goal).
 */
export function normalizeBudgetPayload(raw) {
  if (!raw || typeof raw !== 'object') {
    return { monthly_income: 0, goal: 'general', expenses: {} }
  }
  const goals = ['general', 'emergency_fund', 'debt_payoff', 'big_purchase']
  const goal = goals.includes(raw.goal) ? raw.goal : 'general'
  const income = Number(raw.monthly_income)
  const expenses = {}
  for (const [k, v] of Object.entries(raw.expenses || {})) {
    const n = Number(v)
    expenses[k] = Number.isFinite(n) ? n : 0
  }
  return {
    monthly_income: Number.isFinite(income) && income >= 0 ? income : 0,
    goal,
    expenses,
  }
}

/** Stable string for sync effects (sorted keys, numeric values). */
export function stableExpensesSignature(expenses) {
  if (!expenses || typeof expenses !== 'object') return ''
  const sorted = {}
  for (const k of Object.keys(expenses).sort()) {
    const n = Number(expenses[k])
    sorted[k] = Number.isFinite(n) ? n : 0
  }
  return JSON.stringify(sorted)
}
