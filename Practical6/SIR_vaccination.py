'''
    pseudocode
    import necessary libraries
    creat different vaccination rate
    create a loop that lasts for a thousand days. 
    Each cycle represents one round of the infection process.
    In each cycle, calculate the number of susceptible individuals,
    the number of infected individuals, and the number of recovered individuals.
    then, store the data in the arrays S, I, and R.
    finally, plot the data.
'''
# import nessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
colors = cm.viridis(np.linspace(0, 1, 11))
# define the variables
N = 10000
beta = 0.3
gamma = 0.05
# add the vaccination process
for idx,vaccinated_rate in enumerate(np.arange (0, 1.1, 0.1)):
    R0 = int(N * vaccinated_rate)
    I0 = 1
    S0 = max(N - I0 - R0,0)
    # creat the arrays to store the data
    S = [S0]
    I = [I0]
    R = [R0]
    # creat the loop to calculate the data
    for i in range(1,1001):
        # set the rate of infection and recovery
        Infected = beta * (I[-1]/N)
        Recovered = gamma
        # set the number of new infected and recovered people to 0
        new_infected_people = 0
        new_recovered_people = 0
        # create a random array to simulate the infection and recovery process
        # in array, 0 means not infected and 1 means infected
        new_infected_people_array = np.random.choice(range(2), S[-1], p = [1-Infected, Infected]) 
        for i in new_infected_people_array.tolist():
            new_infected_people += i
        new_recovered_people_array = np.random.choice(range(2), I[-1], p = [1-Recovered, Recovered])
        for i in new_recovered_people_array.tolist():
            new_recovered_people += i
        s_new = S[-1] - new_infected_people
        i_new = I[-1] + new_infected_people - new_recovered_people
        r_new = R[-1] + new_recovered_people
        S.append(s_new)
        I.append(i_new)
        R.append(r_new)
    
# plt.plot(range(1001), S, color = "red", label = "Susceptible")
    plt.plot(range(1001), I, color = colors[idx], label = f"{round(vaccinated_rate*100,0)}%")
# plt.plot(range(1001), R, color = "green", label = "Recovered")
plt.xlabel("time")
plt.ylabel("Number of people")
plt.title("SIR model with differnent vaccination rate")
plt.legend()
plt.show()
