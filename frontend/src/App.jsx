import { useState } from 'react'
import Header from './components/Header'
import BudgetForm from './components/BudgetForm'
import BudgetResults from './components/BudgetResults'

function App() {
  const [analysisResult, setAnalysisResult] = useState(null)
  const [lastBudget, setLastBudget] = useState(null)
  const [scenarioLabel, setScenarioLabel] = useState(null)
  const [monthlyIncome, setMonthlyIncome] = useState(0)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleBudgetSubmit = async (budgetData) => {
    setIsLoading(true)
    setError(null)
    setScenarioLabel(null)
    setLastBudget(budgetData)
    setMonthlyIncome(budgetData.monthly_income || 0)
    try {
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(budgetData),
      })

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}))
        throw new Error(errData.message || 'Failed to analyze budget')
      }

      const result = await response.json()
      setAnalysisResult(result)
    } catch (err) {
      setError(err.message)
      console.error('Budget analysis error:', err)
    } finally {
      setIsLoading(false)
    }
  }

  const handleWhatIfSubmit = async (scenario) => {
    if (!lastBudget || !scenario) return
    const base = lastBudget
    const income = base.monthly_income || 0
    let updated = JSON.parse(JSON.stringify(base))
    let label = ''

    const lower = scenario.toLowerCase().trim()

    // Pattern 1: Save X% more
    if (lower.includes('save') && lower.includes('%')) {
      const match = lower.match(/(\d+(?:\.\d+)?)\s*%/)
      if (match) {
        const pct = parseFloat(match[1]) / 100
        const extra = income * pct
        updated.expenses.savings = (updated.expenses.savings || 0) + extra
        label = `What if you saved ${match[1]}% more?`
      }
    }
    // Pattern 2: Cut/Reduce/Lower/Less category by $X or ~10%
    else if (lower.match(/(cut|reduce|lower|decrease|less)/)) {
      const amountMatch = lower.match(/\$(\d+(?:\.\d+)?)/)
      let amount = amountMatch ? parseFloat(amountMatch[1]) : 0
      
      const categoryMap = {
        'rent': 'rent',
        'housing': 'rent',
        'food': 'food',
        'groceries': 'food',
        'entertainment': 'entertainment',
        'transportation': 'transportation',
        'utilities': 'utilities',
        'savings': 'savings',
        'other': 'other',
      }
      
      let category = null
      for (const [key, value] of Object.entries(categoryMap)) {
        if (lower.includes(key)) {
          category = value
          break
        }
      }
      
      if (category) {
        // If no explicit dollar amount, default to 10% of that category
        if (!amount && updated.expenses[category]) {
          amount = updated.expenses[category] * 0.1
        }
        if (amount > 0) {
          updated.expenses[category] = Math.max(
            0,
            (updated.expenses[category] || 0) - amount
          )
          const action = lower.includes('cut')
            ? 'cut'
            : lower.includes('reduce')
            ? 'reduced'
            : lower.includes('lower') || lower.includes('less')
            ? 'lowered'
            : 'decreased'
          label = `What if you ${action} ${category.replace('_', ' ')} by $${amount.toFixed(
            2
          )}?`
        }
      }
    }
    // Pattern 3: Increase/Add/More category by $X or ~10%
    else if (lower.match(/(increase|add|raise|more)/)) {
      const amountMatch = lower.match(/\$(\d+(?:\.\d+)?)/)
      let amount = amountMatch ? parseFloat(amountMatch[1]) : 0
      
      const categoryMap = {
        'rent': 'rent',
        'housing': 'rent',
        'food': 'food',
        'groceries': 'food',
        'entertainment': 'entertainment',
        'transportation': 'transportation',
        'utilities': 'utilities',
        'savings': 'savings',
        'other': 'other',
      }
      
      let category = null
      for (const [key, value] of Object.entries(categoryMap)) {
        if (lower.includes(key)) {
          category = value
          break
        }
      }
      
      if (category) {
        if (!amount && updated.expenses[category]) {
          amount = updated.expenses[category] * 0.1
        }
        if (amount > 0) {
          updated.expenses[category] =
            (updated.expenses[category] || 0) + amount
          label = `What if you increased ${category.replace(
            '_',
            ' '
          )} by $${amount.toFixed(2)}?`
        }
      }
    }

    if (!label) {
      setError(`Couldn't parse scenario: "${scenario}". Try: "Save 5% more" or "Cut entertainment by $50"`)
      return
    }

    try {
      setIsLoading(true)
      setError(null)
      setScenarioLabel(label)
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updated),
      })

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}))
        throw new Error(errData.message || 'Failed to analyze scenario')
      }

      const result = await response.json()
      setAnalysisResult(result)
      // Do NOT change lastBudget or monthlyIncome; this keeps baseline as original
    } catch (err) {
      setError(err.message)
      console.error('What-if analysis error:', err)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen">
      <Header />

      <main className="container mx-auto px-4 py-10 max-w-4xl">
        <section className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 tracking-tight drop-shadow-lg">
            Take control of your finances
          </h1>
          <p className="text-lg text-emerald-50 max-w-xl mx-auto drop-shadow-md">
            Enter your income and expenses to get a personalized budget breakdown,
            saving tips, and simple explanations—powered by free AI.
          </p>
        </section>

        <section className="mb-12" id="budget">
          <BudgetForm onSubmit={handleBudgetSubmit} isLoading={isLoading} />
        </section>

        {error && (
          <div
            className="mb-8 p-4 rounded-xl bg-red-50 border border-red-200 text-red-700 text-sm"
            role="alert"
          >
            <strong>Error:</strong> {error}
          </div>
        )}

        {analysisResult && (
          <section className="mb-12">
            <BudgetResults
              results={analysisResult}
              monthlyIncome={monthlyIncome}
              scenarioLabel={scenarioLabel}
              hasBaseline={!!lastBudget}
              onWhatIf={handleWhatIfSubmit}
            />
          </section>
        )}

        <footer className="text-center text-sm text-emerald-100 mt-16 pb-8">
          <p>
            <strong className="text-white">Disclaimer:</strong> This tool is for educational purposes only
            and does not constitute financial advice. Consult a qualified financial
            advisor for personalized guidance.
          </p>
        </footer>
      </main>
    </div>
  )
}

export default App
