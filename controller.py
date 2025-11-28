"""
CONTROLLER - Контролер (логіка застосунку)
Клас, що з'єднує Model та View
"""

from model import ExpenseModel
from view import ExpenseView


class ExpenseController:
    """Контролер, що з'єднує Model та View"""
    
    def __init__(self, model: ExpenseModel, view: ExpenseView):
        """
        Ініціалізація контролера
        
        Args:
            model: Модель даних
            view: Представлення
        """
        self.model = model
        self.view = view
    
    def add_expense(self) -> None:
        """Обробляє додавання нової витрати"""
        amount, description, category = self.view.get_expense_input()
        
        if amount is None:
            return
        
        if amount <= 0:
            self.view.show_error("Сума має бути більше нуля!")
            return
        
        expense = self.model.add_expense(amount, description, category)
        self.view.show_expense_added(expense)
    
    def delete_expense(self) -> None:
        """Обробляє видалення витрати"""
        expense_id = self.view.get_expense_id()
        
        if expense_id is None:
            return
        
        success = self.model.delete_expense(expense_id)
        self.view.show_expense_deleted(expense_id, success)
    
    def show_expenses_list(self) -> None:
        """Показує список витрат"""
        expenses = self.model.get_all_expenses()
        self.view.show_expenses_list(expenses)
    
    def show_total_amount(self) -> None:
        """Показує загальну суму витрат"""
        total = self.model.get_total_amount()
        self.view.show_total_amount(total)
    
    def run(self) -> None:
        """Головний цикл застосунку"""
        while True:
            self.view.show_menu()
            choice = self.view.get_user_choice()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.delete_expense()
            elif choice == '3':
                self.show_expenses_list()
            elif choice == '4':
                self.show_total_amount()
            elif choice == '5':
                print("\n👋 До побачення!")
                break
            else:
                self.view.show_error("Невірний вибір! Оберіть опцію від 1 до 5.")
            
            input("\nНатисніть Enter для продовження...")

