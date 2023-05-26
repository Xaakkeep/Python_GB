import pandas as pd


# Самостоятельная практика №1
print("Самостоятельная практика №1\n")

#     Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
df = pd.read_csv('lesson 09/california_housing_test.csv')
print(f'Чтение файлы "california_housing_test.csv" с помощью pandas:\n\n{df}\n')

#     Посмотреть сколько в нем строк и столбцов

print(f'Количество строк и столбцов: {df.shape}\n')

#     (Доп) Определить какой тип данных имеют столбцы
print(f'Типы данны столбцов:\n\n{df.dtypes}\n')

#     (Доп) Проверить есть ли в файле пустые значения
print(f'Проверка есть ли в файле пустые значения:\n\n{df.isnull().sum()}\n')


# Самостоятельная практика №2
print("Самостоятельная практика №2\n")

#     Показать median_house_value где median_income < 2
print(f"median_house_value где median_income < 2:\n\n{df.loc[df['median_income'] < 2, ['median_house_value']]}\n")

#     (Доп) Показать данные в первых 2 столбцах
print(f"Данные в первых 2 столбцах\n\n{df[['longitude', 'latitude']]}\n")

#     (Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(f"Данные где housing_median_age < 20 и median_house_value > 70000\n\n{df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]}\n")


# Самостоятельная практика №3
print("Самостоятельная практика №3\n")

#     Определить какое максимальное и минимальное значение median_house_value
print(f"Максимальное значение: {df['median_house_value'].max()}")
print(f"Минимальное значение: {df['median_house_value'].min()}\n")

#     (Доп) Показать максимальное median_house_value, где median_income = 3.1250
print(f"Максимальное median_house_value, где median_income = 3.1250:\n{df.loc[df['median_income'] == 3.1250, ['median_house_value']].max()}\n")

#     (Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
print(f"Максимальная population в зоне минимального значения median_house_value:\n{df.loc[df['median_house_value'] == df['median_house_value'].min(), ['population']].max()}")