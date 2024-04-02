import matplotlib.pyplot as plt
import numpy as np

# functions
def f1(x): #function1
    return x**2 + 7*x + 2
def f2(x): #function2
    return 3*x + 2
def f3(x): #function3
    return x**2
def f4(x): #function4
    return x**3
def f5(x): #function5
    return x**5
def f6(x): #function6
    return x**3 + 2*x**2 + x + 10
def f7(x): #function7
    return x**4 - 3*x**3 + 2*x**2 - x + 11
def f8(x): #function8
    return np.sin(x)
def f9(x):#function9
    return np.cos(x)
def f10(x): #function10
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 1

x = np.linspace(1, 50, 50)

# colors to represent all output values in the graph
colors = ['red', 'green', 'blue', 'orange', 'silver', 'yellow', 'pink', 'black', 'gray', 'brown']

# loads>x>outputFile
while True:
    with open('mathProb.txt') as f:
        x_values= [int(line.strip()) for line in f]
    problems = [
        'x²+7x+2',
        '3x+2',
        'x²',
        'x³',
        'x⁵',
        'x³+2x²+x+10',
        'x⁴-3x³+2x²-x+11',
        'Sin(x)',
        'Cos(x)',
        'x⁵+4x⁴+x³-2x²+100',
        'Show all funtions',
        'Exit'
    ]
    
    while True:
        # displaying variable 'problems' 
        print("Choose a problem to solve:")
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem}")
            funcCnvrt = problem
        # user's choice
        choice = int(input("Enter your choice: "))
        
        if choice == 12:
            break
        if  1 <= choice <= 10:
                    # plot the chosen function
                    if choice == 1:
                        y = [f1(i) for i in x]
                        plt.title(f'x² + 7x + 2', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 2:
                        y = [f2(i) for i in x]
                        plt.title(f'3x + 2', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 3:
                        y = [f3(i) for i in x]
                        plt.title(f'x²', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 4:
                        y = [f4(i) for i in x]
                        plt.title(f'x³', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 5:
                        y = [f5(i) for i in x]
                        plt.title(f'x⁵', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 6:
                        y = [f6(i) for i in x]
                        plt.title(f'x³ + 2x² + x + 10', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 7:
                        y = [f7(i) for i in x]
                        plt.title(f'x⁴ - 3x³ + 2x² - x + 11', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 8:
                        y = [f8(i) for i in x]
                        plt.title(f'Sin(x)', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 9:
                        y = [f9(i) for i in x]
                        plt.title(f'Cos(x)', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    elif choice == 10:
                        y = [f10(i) for i in x]
                        plt.title(f'x⁵ + 4x⁴ + x³ - 2x² + 100', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                        # assign x and y axis
                    plt.plot(x, y)
                    # plot costumize appearance
                    plt.xlabel('x axis',fontsize = 8, fontdict = {'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    plt.xticks(fontsize = 8, fontstyle = 'italic', color = 'gray')
                    plt.ylabel('y axis', fontsize = 8, fontdict = {'family':  'serif'}, fontstyle = 'italic', color = 'gray')
                    plt.yticks(fontsize = 8, fontstyle = 'italic', color = 'gray')
                    plt.grid(True, linestyle = '--', color = 'gray')
                    plt.show()
                    break                        
        if choice == 11:
            # plot all functions
            for i, func in enumerate([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]):
                plt.plot(x, func(x), label=f'Problem {i+1}', color=colors[i])
            # plot costumize appearance
            plt.title('All Functions', loc = 'left', fontdict ={'family':  'serif'}, fontstyle = 'italic', color = 'gray')
            plt.xlabel('x axis',fontsize = 8, fontdict = {'family':  'serif'}, fontstyle = 'italic', color = 'gray')
            plt.xticks(fontsize = 8, fontstyle = 'italic', color = 'gray')
            plt.ylabel('y axis', fontsize = 8, fontdict = {'family':  'serif'}, fontstyle = 'italic', color = 'gray')
            plt.yticks(fontsize = 8, fontstyle = 'italic', color = 'gray')
            plt.grid(True, linestyle = '--', color = 'gray')
            plt.show()
        else:
            print("Invalid function number")
            continue
