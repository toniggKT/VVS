import pandas as pd
import numpy as np

with open('tested.csv'): #1.a
    datta = pd.read_csv('tested.csv')
    pd.options.display.max_columns = None
    #print(datta.isnull().sum().sum()) #1.б.1/1.1 все пропуски
    #print(datta['Survived'].isna().sum()) #пропуски в Survived 0
    #Survived-0, Pclass-0, Name-0, Sex-0, Age-86, SibSp-0, Parch-0, Ticket-0, Fare-1, Cabin-327, Embarked-0

    #print(datta.head(4)) #1.в первые н строк
    #print(datta.describe()) #1.г базовая статистика по столбцам
    #print(datta.dtypes) #1.б.2 признаки
    #print(datta.shape[0]) #строки 1.д
    #print(len(datta)) #строки 1.д
    #print(datta.shape[1]) #столбцы 1.д

    #datta['Age'] = datta['Age'].fillna(30.272590) #1.1 заполнение средним значением
    #print(datta['Age'].isna().sum())
    #df_cleaned = datta.dropna() #1.1 удаление строк где есть пустые значения
    #print(df_cleaned.isnull().sum().sum())

    #II.1
    #женщинф
    women = datta[datta['Sex'] == 'female']
    women_surv = women[women['Survived'] == 1]
    women_unsurv = women[women['Survived'] == 0]

    surv_w = women['Survived'].sum() #women_surv.shape[0], кол-во выживших
    all_w = women.shape[0] #всего женщин
    #all_w = len(women)
    pr_surv_w = (surv_w/all_w)*100 #процент выживших женщин, ==100

    #print(women_surv.describe())
    mean_age_w = 30.272362 #средний возраст женщин, поскольку выжили все, он вообще средний

    #мужчины
    men = datta[datta['Sex'] == 'male']
    men_surv = men[men['Survived'] == 1]
    men_unsurv = men[men['Survived'] == 0]

    surv_m = men_surv.shape[0]
    all_m = men.shape[0]
    pr_surv_m = (surv_m/all_m)*100 #==0
    #print(men.describe())
    mean_age_m = 30.272732
    #вывод: все женщины выжили, мужчины нет, средний возраст += одинаковый

    #II.2
    df1 = datta[(datta['Age']>30) & (datta['Sex']=='male') & (datta['Pclass']==1)]
    df2 = datta[((datta['Age'] < 18) | (datta['Sex']=='female')) & (datta['Survived']==1)]

    #II.3
    mean_age = datta.groupby(['Pclass', 'Sex'])['Age'].mean()
    pr_surv = datta.groupby(['Pclass', 'Sex'])['Survived'].mean()*100
    mean_fare = datta.groupby(['Pclass', 'Sex'])['Fare'].mean()
    print(mean_age)
    print(pr_surv)
    print(mean_fare)

    df = pd.concat([mean_age, pr_surv, mean_fare], axis=1) #склееная таблица
    print(df)




