# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ["Eva", "David", "Frank"]
salary = [7500, 8000, 9000]
bonus = ["8%", "12%", "7%"]


def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: round(salary * (int(bonus.strip('%')) / 100), 1)
            for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}


salary_dict = generate_salary_dict(names, salary, bonus)
print(salary_dict)
