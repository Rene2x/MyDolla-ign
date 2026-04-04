import { useState } from 'react'
import Header from './components/Header'
import BudgetForm from './components/BudgetForm'
import BudgetResults from './components/BudgetResults'

function App() {
  const [analysisResult, setAnalysisResult] = useState(null)
  const [monthlyIncome, setMonthlyIncome] = useState(0)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleBudgetSubmit = async (budgetData) => {
    setIsLoading(true)
    setError(null)
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

  return (
    <div className="min-h-screen flex flex-col">
      <Header />

      <main className="flex-1 container mx-auto px-4 py-8 max-w-2xl w-full">
        <header className="mb-8">
          <h1 className="text-2xl md:text-3xl font-semibold text-white mb-2">
            Budget check-in
          </h1>
          <p className="text-slate-300 text-sm md:text-base leading-relaxed">
            Enter your monthly income and expenses, then click <strong>Analyze</strong>. You will
            see a short explanation tied to your numbers, one quiz question, and one tip linked to
            our documented rules.
          </p>
        </header>

        <section className="mb-6" id="budget">
          <BudgetForm onSubmit={handleBudgetSubmit} isLoading={isLoading} />
        </section>

        {isLoading && (
          <p
            className="mb-4 text-sm text-emerald-200/90 flex items-center gap-2"
            role="status"
            aria-live="polite"
          >
            <span
              className="inline-block h-4 w-4 border-2 border-emerald-300 border-t-transparent rounded-full animate-spin"
              aria-hidden
            />
            Analyzing your budget…
          </p>
        )}

        {error && (
          <div
            className="mb-6 p-4 rounded-lg bg-red-950/40 border border-red-800/60 text-red-100 text-sm"
            role="alert"
          >
            <strong className="text-red-200">Could not complete analysis:</strong> {error}
          </div>
        )}

        {analysisResult && !isLoading && (
          <section className="mb-10">
            <BudgetResults
              results={analysisResult}
              monthlyIncome={monthlyIncome}
            />
          </section>
        )}

        <footer className="text-center text-xs text-slate-400 mt-auto pt-8 pb-6">
          Educational use only — not financial advice.
        </footer>
      </main>
    </div>
  )
}

export default App
