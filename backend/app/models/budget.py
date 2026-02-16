"""
============================================
ASSIGNED TO: Member 2 (Backend Lead)

Budget data models and validation.

TODO:
1. Add more robust validation with Pydantic
2. Add data type checking
3. Add custom error messages
============================================
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class BudgetInput:
    """Data class representing user budget input."""
    monthly_income: float
    expenses: Dict[str, float]
    
    @property
    def total_expenses(self) -> float:
        """Calculate total expenses."""
        return sum(self.expenses.values())
    
    @property
    def remaining(self) -> float:
        """Calculate remaining income after expenses."""
        return self.monthly_income - self.total_expenses
    
    @property
    def expense_percentages(self) -> Dict[str, float]:
        """Calculate percentage of income for each expense category."""
        if self.monthly_income == 0:
            return {k: 0 for k in self.expenses}
        return {
            category: (amount / self.monthly_income) * 100
            for category, amount in self.expenses.items()
        }


def validate_budget_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate budget input data.
    
    TODO (Member 2): Improve validation logic
    
    Args:
        data: Dictionary containing budget data
        
    Returns:
        Dictionary with 'valid' boolean and optional 'message' string
    """
    # Check for required fields
    if 'monthly_income' not in data:
        return {
            'valid': False,
            'message': 'monthly_income is required'
        }
    
    if 'expenses' not in data:
        return {
            'valid': False,
            'message': 'expenses is required'
        }
    
    # Validate monthly_income
    try:
        income = float(data['monthly_income'])
        if income < 0:
            return {
                'valid': False,
                'message': 'monthly_income cannot be negative'
            }
    except (ValueError, TypeError):
        return {
            'valid': False,
            'message': 'monthly_income must be a number'
        }
    
    # Validate expenses
    if not isinstance(data['expenses'], dict):
        return {
            'valid': False,
            'message': 'expenses must be an object with category: amount pairs'
        }
    
    for category, amount in data['expenses'].items():
        try:
            expense_amount = float(amount)
            if expense_amount < 0:
                return {
                    'valid': False,
                    'message': f'Expense for {category} cannot be negative'
                }
        except (ValueError, TypeError):
            return {
                'valid': False,
                'message': f'Expense for {category} must be a number'
            }
    
    return {'valid': True}
