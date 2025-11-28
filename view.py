"""
VIEW - Представлення (інтерфейс користувача)
Клас для відображення інформації користувачу
"""

from typing import List, Optional
from model import Expense


class ExpenseView:
    """View для відображення інформації користувачу"""
    
    @staticmethod
    def show_menu() -> None:
        """Показує головне меню"""
        print("\n" + "="*50)
        print("📊 ОБЛІК ВИТРАТ")
        print("="*50)
        print("1. Додати нову витрату")
        print("2. Видалити витрату за id")
        print("3. Показати список витрат")
        print("4. Показати загальну суму витрат")
        print("5. Вийти")
        print("="*50)
    
    @staticmethod
    def get_user_choice() -> str:
        """Отримує вибір користувача"""
        return input("\nОберіть опцію (1-5): ").strip()
    
    @staticmethod
    def get_expense_input() -> tuple:
        """
        Отримує дані про витрату від користувача
        
        Returns:
            Кортеж (amount, description, category)
        """
        try:
            amount = float(input("Введіть суму витрати: "))
            description = input("Введіть опис витрати: ").strip()
            category = input("Введіть категорію (за замовчуванням 'Інше'): ").strip()
            
            if not description:
                description = "Без опису"
            if not category:
                category = "Інше"
            
            return amount, description, category
        except ValueError:
            print("❌ Помилка: введіть коректну суму!")
            return None, None, None
    
    @staticmethod
    def get_expense_id() -> Optional[int]:
        """Отримує id витрати для видалення"""
        try:
            expense_id = int(input("Введіть id витрати для видалення: "))
            return expense_id
        except ValueError:
            print("❌ Помилка: введіть коректний id!")
            return None
    
    @staticmethod
    def show_expense_added(expense: Expense) -> None:
        """Показує повідомлення про додавання витрати"""
        print(f"\n✅ Витрата додана успішно!")
        print(f"   ID: {expense.id}")
        print(f"   Сума: {expense.amount} грн")
        print(f"   Опис: {expense.description}")
        print(f"   Категорія: {expense.category}")
        print(f"   Дата: {expense.date}")
    
    @staticmethod
    def show_expense_deleted(expense_id: int, success: bool) -> None:
        """Показує результат видалення витрати"""
        if success:
            print(f"\n✅ Витрата з id={expense_id} успішно видалена!")
        else:
            print(f"\n❌ Витрата з id={expense_id} не знайдена!")
    
    @staticmethod
    def show_expenses_list(expenses: List[Expense]) -> None:
        """Показує список всіх витрат"""
        if not expenses:
            print("\n📝 Список витрат порожній")
            return
        
        print("\n" + "="*80)
        print("📋 СПИСОК ВИТРАТ")
        print("="*80)
        print(f"{'ID':<5} {'Сума':<12} {'Категорія':<15} {'Опис':<30} {'Дата':<20}")
        print("-"*80)
        
        for expense in expenses:
            print(f"{expense.id:<5} {expense.amount:<12.2f} {expense.category:<15} "
                  f"{expense.description[:28]:<30} {expense.date:<20}")
        
        print("="*80)
        print(f"Всього витрат: {len(expenses)}")
    
    @staticmethod
    def show_total_amount(total: float) -> None:
        """Показує загальну суму витрат"""
        print("\n" + "="*50)
        print(f"💰 ЗАГАЛЬНА СУМА ВИТРАТ: {total:.2f} грн")
        print("="*50)
    
    @staticmethod
    def show_error(message: str) -> None:
        """Показує повідомлення про помилку"""
        print(f"\n❌ Помилка: {message}")
    
    @staticmethod
    def show_message(message: str) -> None:
        """Показує загальне повідомлення"""
        print(f"\n{message}")

