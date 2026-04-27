import { useState, useEffect } from 'react'
import { normalizeBudgetPayload } from '../utils/budgetPayload'

const LABELS = {
  rent: 'Rent / Housing',
  food: 'Food / Groceries',
  transportation: 'Transportation',
  utilities: 'Utilities',
  entertainment: 'Entertainment',
  savings: 'Savings',
  other: 'Other',
}

export default function WhatIfPanel({ budgetPayload, onReanalyze, isLoading }) {
  const [category, setCategory] = useState('entertainment')
  const [direction, setDirection] = useState('decrease')
  const [amount, setAmount] = useState('')
  const [notice, setNotice] = useState('')

  const keys = budgetPayload?.expenses ? Object.keys(budgetPayload.expenses) : []

  useEffect(() => {
    const ks = budgetPayload?.expenses ? Object.keys(budgetPayload.expenses) : []
    if (ks.length && !ks.includes(category)) setCategory(ks[0])
    // eslint-disable-next-line react-hooks/exhaustive-deps -- only reset when payload shape changes
  }, [budgetPayload])

  if (!keys.length) return null

  const cat = keys.includes(category) ? category : keys[0]
  const base = normalizeBudgetPayload(budgetPayload)
  const currentAmount = Number(base.expenses[cat]) || 0

  const amountNum = parseFloat(String(amount).trim())
  const canApply = amount !== '' && Number.isFinite(amountNum) && amountNum > 0

  const monthlyIncome = Number(base.monthly_income) || 0

  const apply = () => {
    if (!canApply) return
    const delta = direction === 'increase' ? amountNum : -amountNum
    const cur = Number(base.expenses[cat]) || 0
    const hints = []

    let raw = cur + delta
    if (delta < 0 && cur + delta < 0) {
      hints.push('Decrease limited so this category does not go below $0.')
    }
    raw = Math.max(0, raw)

    if (delta > 0 && monthlyIncome > 0 && cur + delta > monthlyIncome) {
      hints.push(
        `Increase capped at your monthly income ($${monthlyIncome.toFixed(2)}) for this line item.`
      )
      raw = Math.min(cur + delta, monthlyIncome)
    }

    setNotice(hints.join(' '))
    onReanalyze({
      ...base,
      expenses: {
        ...base.expenses,
        [cat]: raw,
      },
    })
    setAmount('')
  }

  const applyDecreaseAll = () => {
    if (!canApply || direction !== 'decrease') return
    const x = amountNum
    const expenses = { ...base.expenses }
    let anyFloored = false
    for (const k of Object.keys(expenses)) {
      const v = Number(expenses[k]) || 0
      const nv = Math.max(0, v - x)
      if (nv !== v - x) anyFloored = true
      expenses[k] = nv
    }
    setNotice(
      anyFloored
        ? `Subtracted $${x.toFixed(2)} from every category; at least one line floored at $0.`
        : `Subtracted $${x.toFixed(2)} from every category.`
    )
    onReanalyze({ ...base, expenses })
    setAmount('')
  }

  return (
    <section
      className="rounded-lg border border-sky-200 bg-sky-50/80 p-4 text-slate-900"
      aria-labelledby="whatif-h"
    >
      <h3 id="whatif-h" className="text-xs font-semibold uppercase text-sky-900 mb-2">
        What-if
      </h3>
      <p className="text-sm text-slate-700 mb-3">
        Pick a category, choose <strong>increase</strong> or <strong>decrease</strong>, enter a dollar amount, then
        re-run Analyze. The budget form above will update to match.
      </p>

      {notice ? (
        <p
          className="text-xs text-amber-900 bg-amber-50 border border-amber-200 rounded-md px-2 py-2 mb-3"
          role="status"
        >
          {notice}
        </p>
      ) : null}

      <p className="text-xs text-slate-600 mb-3 tabular-nums">
        Current {LABELS[cat] || cat}: <strong className="text-slate-800">${currentAmount.toFixed(2)}</strong>
      </p>

      <div className="flex flex-col gap-3">
        <div>
          <label htmlFor="whatif-category" className="block text-xs font-medium text-slate-600 mb-1">
            Category
          </label>
          <select
            id="whatif-category"
            value={cat}
            onChange={(e) => {
              setCategory(e.target.value)
              setNotice('')
            }}
            disabled={isLoading}
            className="w-full max-w-xs border rounded-md px-2 py-2 text-sm text-slate-900 bg-white"
          >
            {keys.map((k) => (
              <option key={k} value={k}>
                {LABELS[k] || k}
              </option>
            ))}
          </select>
        </div>

        <fieldset className="border-0 p-0 m-0">
          <legend className="block text-xs font-medium text-slate-600 mb-2">Direction</legend>
          <div className="flex flex-wrap gap-2" role="radiogroup" aria-label="Increase or decrease category">
            <button
              type="button"
              disabled={isLoading}
              onClick={() => {
                setDirection('increase')
                setNotice('')
              }}
              className={`rounded-md px-3 py-2 text-sm font-medium border transition-colors ${
                direction === 'increase'
                  ? 'border-emerald-600 bg-emerald-600 text-white'
                  : 'border-slate-300 bg-white text-slate-700 hover:border-emerald-400'
              }`}
            >
              Increase
            </button>
            <button
              type="button"
              disabled={isLoading}
              onClick={() => {
                setDirection('decrease')
                setNotice('')
              }}
              className={`rounded-md px-3 py-2 text-sm font-medium border transition-colors ${
                direction === 'decrease'
                  ? 'border-amber-600 bg-amber-600 text-white'
                  : 'border-slate-300 bg-white text-slate-700 hover:border-amber-400'
              }`}
            >
              Decrease
            </button>
          </div>
        </fieldset>

        <div>
          <label htmlFor="whatif-amount" className="block text-xs font-medium text-slate-600 mb-1">
            Amount ($)
          </label>
          <div className="flex flex-wrap items-center gap-2">
            <span className="text-sm font-semibold text-slate-700 w-4" aria-hidden>
              {direction === 'increase' ? '+' : '−'}
            </span>
            <input
              id="whatif-amount"
              type="number"
              min="0.01"
              step="0.01"
              placeholder="100"
              value={amount}
              onChange={(e) => {
                setAmount(e.target.value)
                setNotice('')
              }}
              disabled={isLoading}
              className="w-32 rounded-md border border-slate-300 bg-white px-2 py-2 text-sm tabular-nums text-slate-900 placeholder:text-slate-400 outline-none focus:border-sky-600 focus:ring-1 focus:ring-sky-500/30 disabled:bg-slate-100 disabled:text-slate-500"
            />
            <span className="text-xs text-slate-500">Enter a positive number only</span>
          </div>
        </div>

        <div className="flex flex-col sm:flex-row flex-wrap gap-2">
          <button
            type="button"
            disabled={isLoading || !canApply}
            onClick={apply}
            className="w-full sm:w-auto bg-sky-700 text-white text-sm font-medium px-4 py-2 rounded-md disabled:bg-slate-400"
          >
            {isLoading ? '…' : 'Apply & re-analyze'}
          </button>
          <button
            type="button"
            disabled={isLoading || !canApply || direction !== 'decrease'}
            onClick={applyDecreaseAll}
            title="Subtract this amount from every expense category (each floored at $0)"
            className="w-full sm:w-auto bg-white border border-sky-700 text-sky-900 text-sm font-medium px-4 py-2 rounded-md disabled:bg-slate-100 disabled:text-slate-400 disabled:border-slate-300"
          >
            {isLoading ? '…' : 'Decrease all categories'}
          </button>
        </div>
      </div>
    </section>
  )
}
