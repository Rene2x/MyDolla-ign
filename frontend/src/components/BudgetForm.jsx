import { useState } from 'react'

const EXPENSE_CATEGORIES = [
  { id: 'rent', label: 'Rent / Housing', placeholder: '1200' },
  { id: 'food', label: 'Food / Groceries', placeholder: '400' },
  { id: 'transportation', label: 'Transportation', placeholder: '150' },
  { id: 'utilities', label: 'Utilities', placeholder: '100' },
  { id: 'entertainment', label: 'Entertainment', placeholder: '200' },
  { id: 'savings', label: 'Savings', placeholder: '300' },
  { id: 'other', label: 'Other', placeholder: '150' },
]

const GOAL_OPTIONS = [
  { value: 'general', label: 'General financial wellness' },
  { value: 'emergency_fund', label: 'Build emergency fund' },
  { value: 'debt_payoff', label: 'Pay down debt' },
  { value: 'big_purchase', label: 'Save for big purchase' },
]

function BudgetForm({ onSubmit, isLoading }) {
  const [income, setIncome] = useState('')
  const [goal, setGoal] = useState('general')
  const [expenses, setExpenses] = useState(
    EXPENSE_CATEGORIES.reduce((acc, cat) => ({ ...acc, [cat.id]: '' }), {})
  )

  const handleSubmit = (e) => {
    e.preventDefault()
    const budgetData = {
      monthly_income: parseFloat(income) || 0,
      expenses: Object.entries(expenses).reduce(
        (acc, [key, value]) => ({ ...acc, [key]: parseFloat(value) || 0 }),
        {}
      ),
      goal: goal,
    }
    onSubmit(budgetData)
  }

  const handleExpenseChange = (categoryId, value) => {
    setExpenses((prev) => ({ ...prev, [categoryId]: value }))
  }

  const totalExpenses = Object.values(expenses).reduce(
    (sum, val) => sum + (parseFloat(val) || 0),
    0
  )
  const incomeNum = parseFloat(income) || 0
  const remaining = incomeNum - totalExpenses

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white rounded-2xl shadow-xl border border-slate-100 overflow-hidden"
      id="budget"
    >
      <div className="bg-gradient-to-r from-emerald-600 to-teal-600 px-6 py-4">
        <h2 className="text-xl font-bold text-white">Enter your budget</h2>
        <p className="text-emerald-100 text-sm">Monthly, after taxes</p>
      </div>

      <div className="p-6 md:p-8">
        <div className="mb-8">
          <label
            htmlFor="income"
            className="block text-sm font-semibold text-slate-700 mb-2"
          >
            Monthly income
          </label>
          <div className="relative">
            <span className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 font-medium">
              $
            </span>
            <input
              type="number"
              id="income"
              value={income}
              onChange={(e) => setIncome(e.target.value)}
              placeholder="3000"
              min="0"
              step="0.01"
              className="w-full pl-9 pr-4 py-3 text-lg border-2 border-slate-200 rounded-xl
                         focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200
                         transition-colors outline-none text-slate-900 placeholder:text-slate-400"
              required
            />
          </div>
        </div>

        <div className="mb-8">
          <label
            htmlFor="goal"
            className="block text-sm font-semibold text-slate-700 mb-2"
          >
            Your primary goal
          </label>
          <select
            id="goal"
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            className="w-full px-4 py-3 text-lg border-2 border-slate-200 rounded-xl
                       focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200
                       transition-colors outline-none bg-white text-slate-900"
          >
            {GOAL_OPTIONS.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>

        <div className="mb-8">
          <h3 className="text-sm font-semibold text-slate-700 mb-4">
            Monthly expenses
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {EXPENSE_CATEGORIES.map((category) => (
              <div key={category.id}>
                <label
                  htmlFor={category.id}
                  className="block text-sm font-medium text-slate-600 mb-1"
                >
                  {category.label}
                </label>
                <div className="relative">
                  <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm">
                    $
                  </span>
                  <input
                    type="number"
                    id={category.id}
                    value={expenses[category.id]}
                    onChange={(e) =>
                      handleExpenseChange(category.id, e.target.value)
                    }
                    placeholder={category.placeholder}
                    min="0"
                    step="0.01"
                    className="w-full pl-7 pr-4 py-2.5 border border-slate-200 rounded-lg
                               focus:border-emerald-500 focus:ring-1 focus:ring-emerald-200
                               transition-colors outline-none text-slate-900 placeholder:text-slate-400"
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-slate-50 rounded-xl p-4 mb-6 border border-slate-100">
          <div className="flex justify-between text-sm text-slate-600 mb-2">
            <span>Total expenses</span>
            <span className="font-semibold tabular-nums">
              ${totalExpenses.toFixed(2)}
            </span>
          </div>
          <div className="flex justify-between text-sm text-slate-600">
            <span>Remaining</span>
            <span
              className={`font-semibold tabular-nums ${
                remaining >= 0 ? 'text-emerald-600' : 'text-red-600'
              }`}
            >
              ${remaining.toFixed(2)}
            </span>
          </div>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full bg-gradient-to-r from-emerald-600 to-teal-600
                     hover:from-emerald-700 hover:to-teal-700
                     disabled:from-slate-300 disabled:to-slate-400
                     text-white font-semibold py-3.5 px-6 rounded-xl
                     transition-all duration-200 flex items-center justify-center gap-2
                     shadow-lg shadow-emerald-500/25 hover:shadow-emerald-500/30
                     disabled:shadow-none"
        >
          {isLoading ? (
            <>
              <svg
                className="animate-spin h-5 w-5 text-white"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                />
              </svg>
              Analyzing…
            </>
          ) : (
            'Analyze my budget'
          )}
        </button>
      </div>
    </form>
  )
}

export default BudgetForm
