# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    # matplotlib.use('TkAgg')


    # # Create a NumPy array
    # arr = np.array([1, 2, 3, 4, 5])
    # # Perform operations on the array
    # result = arr * 2
    # print(result)

    # marks = {'A': 9,'B': 723, 'C': 78}
    # grades = {'A': 9,'B': 0, 'C': 78, 'P': 123456}
    # result = pd.DataFrame({'Marks': marks, 'grades': grades})
    # # x = np.linspace(0, 120, 5)
    # # y = np.sin(x)
    # #
    # # plt.plot(x,y)
    # # plt.show()
    #
    # # x2 = np.linspace(0, 10, 10)
    # # y2 = np.multiply(x2, 2)
    # #
    # # plt.scatter(x2, y2)
    # # plt.show()

def plot_covid_new_cases_per_days():
    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')

    csv = pd.read_csv('~/Downloads/covid.csv')
    csv.drop([ 'Country_code'], axis=1, inplace=True)
    csv = csv.fillna('NA')
    countries = csv['Country'].unique()
    print(len(countries))
    for i in range(0, len(countries)):
        C = csv[csv['Country'] == countries[i]].reset_index()
        plt.scatter(np.arange(0, len(C)), C['New_cases'], color='orange', label='New_ cases')
        plt.scatter(np.arange(0, len(C)), C['New_deaths'], color='red', label='New_deaths')
        plt.legend()
        plt.show()


def plot_covid_per_country():
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')

    csv = pd.read_csv('~/Downloads/covid.csv')
    csv.drop([ 'Country_code'], axis=1, inplace=True)
    csv = csv.fillna('NA')
    csv2 = csv.groupby('Country')[['New_cases']].sum().reset_index().head(50)
    print(csv2.head(1000))
    plt.scatter(csv2['Country'], csv2['New_cases'], color='orange', label='New_ cases')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('test')
    # plot_covid_new_cases_per_days()
    plot_covid_per_country()

