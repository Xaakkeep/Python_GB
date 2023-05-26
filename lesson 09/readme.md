# Домашняя работа

## Урок 9. Работа с табличными данными

### **Самостоятельная практика №1**

1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data

    ```python
    df = pd.read_csv('lesson 09/california_housing_test.csv')
    print(df)
    ```

    Out

    ```cmd
      longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value
    0       -122.05     37.37                27.0       3885.0           661.0      1537.0       606.0         6.6085            344700.0
    1       -118.30     34.26                43.0       1510.0           310.0       809.0       277.0         3.5990            176500.0
    2       -117.81     33.78                27.0       3589.0           507.0      1484.0       495.0         5.7934            270500.0
    3       -118.36     33.82                28.0         67.0            15.0        49.0        11.0         6.1359            330000.0
    4       -119.67     36.33                19.0       1241.0           244.0       850.0       237.0         2.9375             81700.0
    ...         ...       ...                 ...          ...             ...         ...         ...            ...                 ...
    2995    -119.86     34.42                23.0       1450.0           642.0      1258.0       607.0         1.1790            225000.0
    2996    -118.14     34.06                27.0       5257.0          1082.0      3496.0      1036.0         3.3906            237200.0
    2997    -119.70     36.30                10.0        956.0           201.0       693.0       220.0         2.2895             62000.0
    2998    -117.12     34.10                40.0         96.0            14.0        46.0        14.0         3.2708            162500.0
    2999    -119.63     34.42                42.0       1765.0           263.0       753.0       260.0         8.5608            500001.0

    [3000 rows x 9 columns]
    ```

2. Посмотреть сколько в нем строк и столбцов

    ```python
    print(df.shape)
    ```

    Out

    ```cmd
    Количество строк и столбцов: (3000, 9)
    ```

3. (Доп) Определить какой тип данных имеют столбцы

    ```python
    print(df.dtypes)
    ```

    Out

    ```cmd
    longitude             float64
    latitude              float64
    housing_median_age    float64
    total_rooms           float64
    total_bedrooms        float64
    population            float64
    households            float64
    median_income         float64
    median_house_value    float64
    dtype: object
    ```

4. (Доп) Проверить есть ли в файле пустые значения

    ```python
    print(df.isnull().sum())
    ```

    Out

    ```cmd
    longitude             0
    latitude              0
    housing_median_age    0
    total_rooms           0
    total_bedrooms        0
    population            0
    households            0
    median_income         0
    median_house_value    0
    dtype: int64
    ```

### **Самостоятельная практика №2**

1. Показать median_house_value где median_income < 2

    ```python
    print(df.loc[df['median_income'] < 2, ['median_house_value']])
    ```

    Out

    ```cmd
          median_house_value
    5                67000.0
    6                67000.0
    16              181300.0
    28              350000.0
    43               79300.0
    ...                  ...
    2943             57200.0
    2964             91300.0
    2985            109400.0
    2986             85400.0
    2995            225000.0

    [360 rows x 1 columns]
    ```

2. (Доп) Показать данные в первых 2 столбцах

    ```python
    print(df[['longitude', 'latitude']])
    ```

    Out

    ```cmd
          longitude  latitude
    0       -122.05     37.37
    1       -118.30     34.26
    2       -117.81     33.78
    3       -118.36     33.82
    4       -119.67     36.33
    ...         ...       ...
    2995    -119.86     34.42
    2996    -118.14     34.06
    2997    -119.70     36.30
    2998    -117.12     34.10
    2999    -119.63     34.42

    [3000 rows x 2 columns]
    ```

3. (Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000

    ```python
    print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])
    ```

    Out

    ```cmd
          longitude  latitude  housing_median_age  total_rooms  total_bedrooms  population  households  median_income  median_house_value
    4       -119.67     36.33                19.0       1241.0           244.0       850.0       237.0         2.9375             81700.0
    7       -120.65     35.48                19.0       2310.0           471.0      1341.0       441.0         3.2250            166900.0
    8       -122.84     38.40                15.0       3080.0           617.0      1446.0       599.0         3.6696            194400.0
    13      -117.03     32.97                16.0       3936.0           694.0      1935.0       659.0         4.5625            231200.0
    16      -120.81     37.53                15.0        570.0           123.0       189.0       107.0         1.8750            181300.0
    ...         ...       ...                 ...          ...             ...         ...         ...            ...                 ...
    2978    -121.34     38.64                17.0       2761.0           501.0      1128.0       482.0         3.7562            139700.0
    2981    -120.66     35.49                17.0       4422.0           945.0      2307.0       885.0         2.8285            171300.0
    2984    -117.59     33.88                13.0       3239.0           849.0      2751.0       813.0         2.6111            107000.0
    2985    -120.47     34.94                17.0       1368.0           308.0       642.0       303.0         1.8633            109400.0
    2991    -117.17     34.28                13.0       4867.0           718.0       780.0       250.0         7.1997            253800.0

    [792 rows x 9 columns]
    ```

### **Самостоятельная практика №3**

1. Определить какое максимальное и минимальное значение median_house_value

    ```python
    print(df['median_house_value'].max()) # Максимальное
    print(df['median_house_value'].min()) # Минимальное
    ```

    Out

    ```cmd
    Максимальное значение: 500001.0
    Минимальное значение: 22500.0
    ```

2. (Доп) Показать максимальное median_house_value, где median_income = 3.1250

    ```python
    print(df.loc[df['median_income'] == 3.1250, ['median_house_value']].max())
    ```

    Out

    ```cmd
    median_house_value    233300.0
    dtype: float64
    ```

3. (Доп) Узнать какая максимальная population в зоне минимального значения median_house_value

    ```python
    print(df.loc[df['median_house_value'] == df['median_house_value'].min(), ['population']].max())
    ```

    Out

    ```cmd
    population    1230.0
    dtype: float64
    ```
