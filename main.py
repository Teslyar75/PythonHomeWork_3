"""
ГОЛОВНИЙ ФАЙЛ ЗАСТОСУНКУ
Точка входу для запуску застосунку обліку витрат
"""

from model import ExpenseModel
from view import ExpenseView
from controller import ExpenseController


def main():
    """Головна функція застосунку"""
    # Створюємо компоненти MVC
    model = ExpenseModel()
    view = ExpenseView()
    controller = ExpenseController(model, view)
    
    # Запускаємо застосунок
    controller.run()


if __name__ == '__main__':
    main()

