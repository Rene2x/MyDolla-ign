/**
 * ============================================
 * ASSIGNED TO: Member 1 (Frontend Lead)
 * 
 * This is the main App component. Your tasks:
 * 1. Add routing if needed (react-router-dom)
 * 2. Manage global state for budget data
 * 3. Connect components together
 * 4. Add error boundaries
 * ============================================
 */

import { useState } from 'react'
import Header from './components/Header'
import BudgetForm from './components/BudgetForm'
import BudgetResults from './components/BudgetResults'
import InvestmentGlossary from './components/InvestmentGlossary'

function App() {
  // State to hold the budget analysis results from AI
  const [analysisResult, setAnalysisResult] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  /**
   * TODO (Member 1): Implement the budget submission handler
   * This function should:
   * 1. Set loading state to true
   * 2. Call the backend API with budget data
   * 3. Update analysisResult with the response
   * 4. Handle errors appropriately
   */
  const handleBudgetSubmit = async (budgetData) => {
    setIsLoading(true)
    setError(null)
    
    try {
      // TODO: Replace with actual API call
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(budgetData),
      })

      if (!response.ok) {
        throw new Error('Failed to analyze budget')
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
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        {/* Hero Section */}
        <section className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Take Control of Your Finances
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Enter your income and expenses below to get a personalized budget 
            breakdown and learn financial concepts in simple terms.
          </p>
        </section>

        {/* Budget Input Form */}
        <section className="mb-12">
          <BudgetForm 
            onSubmit={handleBudgetSubmit} 
            isLoading={isLoading} 
          />
        </section>

        {/* Error Display */}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-8">
            <strong>Error:</strong> {error}
          </div>
        )}

        {/* Budget Analysis Results */}
        {analysisResult && (
          <section className="mb-12">
            <BudgetResults results={analysisResult} />
          </section>
        )}

        {/* Investment Glossary */}
        <section className="mb-12">
          <InvestmentGlossary />
        </section>

        {/* Disclaimer */}
        <footer className="text-center text-sm text-gray-500 mt-16 pb-8">
          <p>
            <strong>Disclaimer:</strong> This tool is for educational purposes only 
            and does not constitute financial advice. Please consult a qualified 
            financial advisor for personalized guidance.
          </p>
        </footer>
      </main>
    </div>
  )
}

export default App
