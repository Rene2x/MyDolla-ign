/**
 * ============================================
 * ASSIGNED TO: Member 1 (Frontend Lead)
 * 
 * Budget Input Form Component
 * 
 * TODO:
 * 1. Add form validation (no negative numbers, etc.)
 * 2. Add more expense categories if needed
 * 3. Improve the UI/UX with better styling
 * 4. Add tooltips explaining each category
 * 5. Consider adding a "reset" button
 * ============================================
 */

import { useState } from 'react'

// Expense categories for the budget form
const EXPENSE_CATEGORIES = [
  { id: 'rent', label: 'Rent / Housing', placeholder: '1200' },
  { id: 'food', label: 'Food / Groceries', placeholder: '400' },
  { id: 'transportation', label: 'Transportation', placeholder: '150' },
  { id: 'utilities', label: 'Utilities', placeholder: '100' },
  { id: 'entertainment', label: 'Entertainment', placeholder: '200' },
  { id: 'savings', label: 'Savings', placeholder: '300' },
  { id: 'other', label: 'Other Expenses', placeholder: '150' },
]

function BudgetForm({ onSubmit, isLoading }) {
  const [income, setIncome] = useState('')
  const [expenses, setExpenses] = useState(
    EXPENSE_CATEGORIES.reduce((acc, cat) => ({ ...acc, [cat.id]: '' }), {})
  )

  /**
   * Handle form submission
   * TODO (Member 1): Add validation before submitting
   */
  const handleSubmit = (e) => {
    e.preventDefault()
    
    // Convert string values to numbers
    const budgetData = {
      monthly_income: parseFloat(income) || 0,
      expenses: Object.entries(expenses).reduce((acc, [key, value]) => ({
        ...acc,
        [key]: parseFloat(value) || 0
      }), {})
    }

    onSubmit(budgetData)
  }

  /**
   * Handle expense input change
   */
  const handleExpenseChange = (categoryId, value) => {
    setExpenses(prev => ({
      ...prev,
      [categoryId]: value
    }))
  }

  /**
   * Calculate total expenses for display
   */
  const totalExpenses = Object.values(expenses)
    .reduce((sum, val) => sum + (parseFloat(val) || 0), 0)

  return (
    <form 
      onSubmit={handleSubmit}
      className="bg-white rounded-xl shadow-lg p-6 md:p-8"
      id="budget"
    >
      <h2 className="text-2xl font-bold text-gray-900 mb-6">
        Enter Your Budget
      </h2>

      {/* Income Input */}
      <div className="mb-8">
        <label 
          htmlFor="income" 
          className="block text-lg font-semibold text-gray-700 mb-2"
        >
          Monthly Income (after taxes)
        </label>
        <div className="relative">
          <span className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 text-lg">
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
            className="w-full pl-8 pr-4 py-3 text-lg border-2 border-gray-200 rounded-lg 
                       focus:border-green-500 focus:ring-2 focus:ring-green-200 
                       transition-colors outline-none"
            required
          />
        </div>
      </div>

      {/* Expense Categories */}
      <div className="mb-8">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">
          Monthly Expenses
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {EXPENSE_CATEGORIES.map((category) => (
            <div key={category.id}>
              <label 
                htmlFor={category.id}
                className="block text-sm font-medium text-gray-600 mb-1"
              >
                {category.label}
              </label>
              <div className="relative">
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
                  $
                </span>
                <input
                  type="number"
                  id={category.id}
                  value={expenses[category.id]}
                  onChange={(e) => handleExpenseChange(category.id, e.target.value)}
                  placeholder={category.placeholder}
                  min="0"
                  step="0.01"
                  className="w-full pl-7 pr-4 py-2 border border-gray-200 rounded-lg 
                             focus:border-green-500 focus:ring-1 focus:ring-green-200 
                             transition-colors outline-none"
                />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Summary */}
      <div className="bg-gray-50 rounded-lg p-4 mb-6">
        <div className="flex justify-between text-sm text-gray-600 mb-2">
          <span>Total Expenses:</span>
          <span className="font-semibold">${totalExpenses.toFixed(2)}</span>
        </div>
        <div className="flex justify-between text-sm text-gray-600">
          <span>Remaining:</span>
          <span className={`font-semibold ${
            (parseFloat(income) || 0) - totalExpenses >= 0 
              ? 'text-green-600' 
              : 'text-red-600'
          }`}>
            ${((parseFloat(income) || 0) - totalExpenses).toFixed(2)}
          </span>
        </div>
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        disabled={isLoading}
        className="w-full bg-green-600 hover:bg-green-700 disabled:bg-green-300
                   text-white font-semibold py-3 px-6 rounded-lg
                   transition-colors duration-200 flex items-center justify-center"
      >
        {isLoading ? (
          <>
            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Analyzing...
          </>
        ) : (
          'Analyze My Budget'
        )}
      </button>
    </form>
  )
}

export default BudgetForm
