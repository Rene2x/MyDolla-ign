import { useState } from 'react'
import ExpensePieChart from './ExpensePieChart'
import BudgetComparison from './BudgetComparison'

function WhatIfInput({ onWhatIf }) {
  const [input, setInput] = useState('')
  const [examples] = useState([
    'Save 5% more',
    'Cut entertainment by $50',
    'Lower housing by $200',
    'Increase savings by $100',
  ])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (input.trim()) {
      onWhatIf(input.trim())
      setInput('')
    }
  }

  return (
    <div className="bg-slate-50 rounded-xl p-4 border border-slate-200">
      <form onSubmit={handleSubmit} className="space-y-3">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="e.g., Save 5% more, Cut entertainment by $50..."
            className="flex-1 px-3 py-2 text-sm border border-slate-300 rounded-lg focus:border-emerald-500 focus:ring-1 focus:ring-emerald-200 outline-none text-slate-900 placeholder:text-slate-400"
          />
          <button
            type="submit"
            disabled={!input.trim()}
            className="px-4 py-2 bg-emerald-600 text-white text-sm font-medium rounded-lg hover:bg-emerald-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Calculate
          </button>
        </div>
        <div className="flex flex-wrap gap-2">
          <span className="text-xs text-slate-500">Quick examples:</span>
          {examples.map((ex, i) => (
            <button
              key={i}
              type="button"
              onClick={() => {
                setInput(ex)
                onWhatIf(ex)
                setInput('')
              }}
              className="px-2 py-1 text-xs bg-white border border-slate-300 rounded-md hover:bg-slate-50 text-slate-700"
            >
              {ex}
            </button>
          ))}
        </div>
      </form>
    </div>
  )
}

function BudgetResults({ results, monthlyIncome, scenarioLabel, hasBaseline, onWhatIf }) {
  if (!results) return null

  const [activeTab, setActiveTab] = useState('overview')

  const {
    financial_advice,
    saving_tips,
    saving_plan,
    where_savings_could_go,
    breakdown,
    insights,
    analysis,
    goal,
  } = results

  // Use provided monthlyIncome or calculate from breakdown
  const income = monthlyIncome || (breakdown && breakdown.length > 0 && breakdown[0].percentage > 0
    ? (breakdown[0].amount / breakdown[0].percentage) * 100
    : 0)

  const goalLabels = {
    general: 'General financial wellness',
    emergency_fund: 'Build emergency fund',
    debt_payoff: 'Pay down debt',
    big_purchase: 'Save for big purchase',
  }

  return (
    <div className="bg-white rounded-2xl shadow-xl border border-slate-100 overflow-hidden">
      <div className="bg-gradient-to-r from-emerald-600 to-teal-600 px-6 py-5">
        <h2 className="text-2xl font-bold text-white">
          Your Budget Analysis
        </h2>
        <p className="text-emerald-100 text-sm mt-1">
          Personalized for your numbers · Education only, not advice
        </p>
        {goal && (
          <div className="mt-3 inline-block px-3 py-1 bg-white/20 backdrop-blur-sm rounded-full">
            <span className="text-white text-xs font-medium">
              Goal: {goalLabels[goal] || goal}
            </span>
          </div>
        )}
        {scenarioLabel && (
          <div className="mt-2">
            <span className="inline-flex items-center px-3 py-1 rounded-full bg-emerald-900/60 text-emerald-100 text-xs">
              {scenarioLabel}
            </span>
          </div>
        )}
      </div>

      <div className="p-6 md:p-8 space-y-8">
        {/* What-if calculator */}
        {hasBaseline && onWhatIf && (
          <section className="mb-4">
            <h3 className="text-xs font-semibold uppercase tracking-wider text-emerald-500 mb-2">
              What-if calculator
            </h3>
            <WhatIfInput onWhatIf={onWhatIf} />
          </section>
        )}

        {/* Visualizations Tabs */}
        {breakdown && breakdown.length > 0 && (
          <section>
            <div className="flex gap-2 mb-4 border-b border-slate-200">
              <button
                onClick={() => setActiveTab('overview')}
                className={`px-4 py-2 text-sm font-medium transition-colors ${
                  activeTab === 'overview'
                    ? 'text-emerald-600 border-b-2 border-emerald-600'
                    : 'text-slate-500 hover:text-slate-700'
                }`}
              >
                Overview
              </button>
              <button
                onClick={() => setActiveTab('chart')}
                className={`px-4 py-2 text-sm font-medium transition-colors ${
                  activeTab === 'chart'
                    ? 'text-emerald-600 border-b-2 border-emerald-600'
                    : 'text-slate-500 hover:text-slate-700'
                }`}
              >
                Pie Chart
              </button>
              <button
                onClick={() => setActiveTab('comparison')}
                className={`px-4 py-2 text-sm font-medium transition-colors ${
                  activeTab === 'comparison'
                    ? 'text-emerald-600 border-b-2 border-emerald-600'
                    : 'text-slate-500 hover:text-slate-700'
                }`}
              >
                50/30/20 Rule
              </button>
            </div>

            {activeTab === 'overview' && (
              <div className="grid md:grid-cols-2 gap-6">
                <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-xl p-6 border border-emerald-100">
                  <ExpensePieChart breakdown={breakdown} monthlyIncome={income} />
                </div>
                <div className="bg-white rounded-xl p-6 border border-slate-200">
                  <BudgetComparison breakdown={breakdown} monthlyIncome={income} />
                </div>
              </div>
            )}

            {activeTab === 'chart' && (
              <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-xl p-8 border border-emerald-100">
                <ExpensePieChart breakdown={breakdown} monthlyIncome={income} />
              </div>
            )}

            {activeTab === 'comparison' && (
              <div className="bg-white rounded-xl p-6 border border-slate-200">
                <BudgetComparison breakdown={breakdown} monthlyIncome={income} />
              </div>
            )}
          </section>
        )}

        {/* Financial Advice */}
        {(financial_advice || analysis) && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-emerald-600 mb-2">
              Financial advice
            </h3>
            <div className="bg-emerald-50/80 border border-emerald-100 rounded-xl p-4 text-slate-700 leading-relaxed">
              {financial_advice || analysis}
            </div>
          </section>
        )}

        {/* Saving Tips */}
        {saving_tips && saving_tips.length > 0 && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-emerald-600 mb-2">
              Saving tips
            </h3>
            <ul className="space-y-2">
              {saving_tips.map((tip, i) => (
                <li
                  key={i}
                  className="flex items-start gap-3 text-slate-700"
                >
                  <span className="flex-shrink-0 w-6 h-6 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs font-semibold">
                    {i + 1}
                  </span>
                  <span>{tip}</span>
                </li>
              ))}
            </ul>
          </section>
        )}

        {/* Saving Plan */}
        {saving_plan && (saving_plan.months_1_3 || saving_plan.months_4_6) && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-emerald-600 mb-3">
              Your saving plan (3-6 months)
            </h3>
            <div className="space-y-4">
              {saving_plan.months_1_3 && saving_plan.months_1_3.length > 0 && (
                <div className="bg-emerald-50/50 border border-emerald-200 rounded-xl p-4">
                  <h4 className="text-sm font-semibold text-emerald-700 mb-2">
                    Months 1-3
                  </h4>
                  <ul className="space-y-1.5">
                    {saving_plan.months_1_3.map((item, i) => (
                      <li
                        key={i}
                        className="flex items-start gap-2 text-slate-700 text-sm"
                      >
                        <span className="text-emerald-600 mt-0.5">•</span>
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
              {saving_plan.months_4_6 && saving_plan.months_4_6.length > 0 && (
                <div className="bg-teal-50/50 border border-teal-200 rounded-xl p-4">
                  <h4 className="text-sm font-semibold text-teal-700 mb-2">
                    Months 4-6
                  </h4>
                  <ul className="space-y-1.5">
                    {saving_plan.months_4_6.map((item, i) => (
                      <li
                        key={i}
                        className="flex items-start gap-2 text-slate-700 text-sm"
                      >
                        <span className="text-teal-600 mt-0.5">•</span>
                        <span>{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </section>
        )}

        {/* Where savings could go */}
        {where_savings_could_go && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-emerald-600 mb-2">
              Where savings could go
            </h3>
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 text-slate-600 text-sm leading-relaxed">
              {where_savings_could_go}
            </div>
          </section>
        )}

        {/* Expense Breakdown */}
        {breakdown && breakdown.length > 0 && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-3">
              Expense breakdown
            </h3>
            <div className="space-y-4">
              {breakdown.map((item, i) => (
                <div key={i}>
                  <div className="flex justify-between text-sm mb-1">
                    <span className="font-medium text-slate-700">
                      {item.category}
                    </span>
                    <span className="text-slate-600 tabular-nums">
                      ${item.amount.toFixed(2)} ({item.percentage.toFixed(1)}%)
                    </span>
                  </div>
                  <div className="h-2 bg-slate-100 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-emerald-400 to-teal-500 rounded-full transition-all duration-500"
                      style={{ width: `${Math.min(item.percentage, 100)}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Key Insights */}
        {insights && insights.length > 0 && (
          <section>
            <h3 className="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-2">
              Key insights
            </h3>
            <ul className="flex flex-wrap gap-2">
              {insights.map((insight, i) => (
                <li
                  key={i}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 text-slate-700 text-sm"
                >
                  <span className="text-emerald-500">•</span>
                  {insight}
                </li>
              ))}
            </ul>
          </section>
        )}

        {/* Disclaimer */}
        <p className="text-xs text-slate-400 italic border-t border-slate-100 pt-4">
          This analysis is generated by AI for educational purposes only and does
          not constitute financial advice. Consult a qualified advisor for your
          situation.
        </p>
      </div>
    </div>
  )
}

export default BudgetResults
