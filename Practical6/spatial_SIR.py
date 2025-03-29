"""
    pseudocode
    import the necessary libraries
    define the color map
    initialize the population and other infomation
    randomly select the location of the outbreak
    let the 8 people around the infected individual has change to get infected
    let the infected people have change to recover
    allow the animation to display
    *for the vaccination version, randomly select the location of the vaccinated individuals

"""
# import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# define the color map, to ensure that the colors are white, red, and green
# white represents the uninfected individuals, red represents the infected individuals, and green represents the recovered individuals
camp = ListedColormap(["white", "red", "green"])

# initialize the population array
population = np.zeros((100,100))
# randomly select the location of the outbreak
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# open the interactive mode
plt.ion()
# create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)

# define the rate of infection and recovery
# beta represents the rate of infection, and gamma represents the rate of recovery
beta = 0.3
gamma = 0.05

# creat a loop to loop 100 times
for time_range in range(1, 101):
    # find the infected individuals
    infected_individuals = np.where(population == 1)
    # find the susceptible individuals around the infected individuals and make sure they are within the boundary
    for i, j in zip(*infected_individuals):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x != i or y != j) and (0 <= x < 100) and (0 <= y < 100):
                            # randomly infect the susceptible individuals
                            if population[x, y] == 0:
                                population[x, y] = np.random.choice([0, 1], p=[1-beta, beta])
        # randomly recover the infected individuals
        population[i, j] = np.random.choice([1, 2], p=[1-gamma, gamma])

    # clear the previous frame
    ax.clear()

    # redraw the frame
    ax.imshow(population, cmap=camp, interpolation="nearest", vmin=0, vmax=2)
    ax.set_title(f"Time = {time_range}")

    # pause for 0.02 seconds, to allow the animation to be visible
    plt.pause(0.02)

# close the interactive mode, and display the final frame
plt.ioff()
plt.title("please close the window to see the vaccination version")
plt.show()



# create the vaccination version
camp = ListedColormap(["white", "red", "green"])
# initialize the population array
population = np.zeros((100,100))

# open the interactive mode
plt.ion()
# create a figure and axis
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)

# define the rate of infection and recovery
# beta represents the rate of infection, and gamma represents the rate of recovery
beta = 0.3
gamma = 0.05
vaccinated_rate = 0.1
# the people who are vaccinated
# calculate the number of people who are vaccinated
vaccinated_total = int(100 * 100 * vaccinated_rate)
# randomly select the location of the vaccinated individuals
vaccinated_indices = np.random.choice(100 * 100, vaccinated_total, replace=False)
vaccinated_x, vaccinated_y = np.unravel_index(vaccinated_indices, (100, 100))
population[vaccinated_x, vaccinated_y] = 2

# randomly select the location of the outbreak
outbreak = np.random.choice(range(100), 2)
while population[outbreak[0], outbreak[1]] == 2:
    outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# creat a loop to loop 100 times
for time_range in range(1, 101):
    # find the infected individuals
    infected_individuals = np.where(population == 1)
    # find the susceptible individuals around the infected individuals and make sure they are within the boundary
    for i, j in zip(*infected_individuals):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x != i or y != j) and (0 <= x < 100) and (0 <= y < 100):
                            # randomly infect the susceptible individuals
                            if population[x, y] == 0:
                                population[x, y] = np.random.choice([0, 1], p=[1-beta, beta])
        # randomly recover the infected individuals
        population[i, j] = np.random.choice([1, 2], p=[1-gamma, gamma])

    # clear the previous frame
    ax.clear()

    # redraw the frame
    ax.imshow(population, cmap=camp, interpolation="nearest", vmin=0, vmax=2)
    ax.set_title(f"Time = {time_range}, Vaccinated rate = {vaccinated_rate}")

    # pause for 0.02 seconds, to allow the animation to be visible
    plt.pause(0.02)

# close the interactive mode, and display the final frame
plt.ioff()
plt.show()