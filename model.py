"""
MODEL - Модель даних
Класи для роботи з даними витрат
"""

from datetime import datetime
from typing import List, Optional, Dict
import json
import os


class Expense:
    """Клас, що представляє одну витрату"""
    
    def __init__(self, expense_id: int, amount: float, description: str, category: str = "Інше"):
        """
        Ініціалізація витрати
        
        Args:
            expense_id: Унікальний ідентифікатор витрати
            amount: Сума витрати
            description: Опис витрати
            category: Категорія витрати
        """
        self.id = expense_id
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict:
        """Перетворює витрату в словник"""
        return {
            'id': self.id,
            'amount': self.amount,
            'description': self.description,
            'category': self.category,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Expense':
        """Створює витрату зі словника"""
        expense = cls(
            expense_id=data['id'],
            amount=data['amount'],
            description=data['description'],
            category=data.get('category', 'Інше')
        )
        expense.date = data.get('date', expense.date)
        return expense
    
    def __repr__(self) -> str:
        return f"Expense(id={self.id}, amount={self.amount}, description='{self.description}')"


class ExpenseModel:
    """Модель для роботи з даними витрат"""
    
    def __init__(self, storage_file: str = "expenses.json"):
        """
        Ініціалізація моделі
        
        Args:
            storage_file: Шлях до файлу для збереження даних
        """
        self.storage_file = storage_file
        self.expenses: List[Expense] = []
        self.next_id = 1
        self.load_expenses()
    
    def add_expense(self, amount: float, description: str, category: str = "Інше") -> Expense:
        """
        Додає нову витрату
        
        Args:
            amount: Сума витрати
            description: Опис витрати
            category: Категорія витрати
            
        Returns:
            Створена витрата
        """
        expense = Expense(self.next_id, amount, description, category)
        self.expenses.append(expense)
        self.next_id += 1
        self.save_expenses()
        return expense
    
    def delete_expense(self, expense_id: int) -> bool:
        """
        Видаляє витрату за id
        
        Args:
            expense_id: Ідентифікатор витрати для видалення
            
        Returns:
            True якщо витрата видалена, False якщо не знайдена
        """
        for i, expense in enumerate(self.expenses):
            if expense.id == expense_id:
                self.expenses.pop(i)
                self.save_expenses()
                return True
        return False
    
    def get_all_expenses(self) -> List[Expense]:
        """
        Отримує список всіх витрат
        
        Returns:
            Список всіх витрат
        """
        return self.expenses.copy()
    
    def get_total_amount(self) -> float:
        """
        Обчислює загальну суму всіх витрат
        
        Returns:
            Загальна сума витрат
        """
        return sum(expense.amount for expense in self.expenses)
    
    def get_expense_by_id(self, expense_id: int) -> Optional[Expense]:
        """
        Отримує витрату за id
        
        Args:
            expense_id: Ідентифікатор витрати
            
        Returns:
            Витрата або None якщо не знайдена
        """
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
    
    def save_expenses(self) -> None:
        """Зберігає витрати у файл"""
        try:
            data = [expense.to_dict() for expense in self.expenses]
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Помилка збереження: {e}")
    
    def load_expenses(self) -> None:
        """Завантажує витрати з файлу"""
        if not os.path.exists(self.storage_file):
            return
        
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(item) for item in data]
                if self.expenses:
                    self.next_id = max(exp.id for exp in self.expenses) + 1
        except Exception as e:
            print(f"Помилка завантаження: {e}")
            self.expenses = []

