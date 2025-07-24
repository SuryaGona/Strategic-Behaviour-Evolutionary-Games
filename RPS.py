import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_agents = 100
num_generations = 300
rounds_per_generation = 10
mutation_rate = 0.01

# RPS Payoff Matrix
# [Rock, Paper, Scissors]
payoff_matrix = np.array([
    [0, -1, 1],   # Rock payoffs
    [1, 0, -1],   # Paper payoffs
    [-1, 1, 0]    # Scissors payoffs
])

# Initialize population (randomly distributed)
population = np.random.randint(0, 3, num_agents)

# Track strategy frequencies over time
rock_freq = []
paper_freq = []
scissors_freq = []

# Run simulation
for generation in range(num_generations):
    # Calculate current frequencies
    unique, counts = np.unique(population, return_counts=True)
    freq = np.zeros(3)
    for i, count in zip(unique, counts):
        freq[i] = count / num_agents
    
    rock_freq.append(freq[0])
    paper_freq.append(freq[1])
    scissors_freq.append(freq[2])
    
    # Calculate fitness for each strategy
    fitness = np.zeros(3)
    for i in range(3):
        for j in range(3):
            fitness[i] += freq[j] * payoff_matrix[i, j]
    
    # New population based on replicator dynamics
    new_population = []
    for _ in range(num_agents):
        # Selection proportional to fitness
        if np.random.random() < mutation_rate:
            # Random mutation
            new_population.append(np.random.randint(0, 3))
        else:
            # Select based on fitness-proportional probabilities
            selection_probs = np.maximum(0, freq * (fitness - np.mean(fitness * freq)) + freq)
            selection_probs = selection_probs / np.sum(selection_probs)
            new_population.append(np.random.choice(3, p=selection_probs))
    
    population = np.array(new_population)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(rock_freq, 'orange', label='Rock')
plt.plot(paper_freq, 'green', label='Paper')
plt.plot(scissors_freq, 'red', label='Scissors')
plt.axhline(y=1/3, color='gray', linestyle='--', label='Nash Equilibrium (1/3)')
plt.xlabel('Time')
plt.ylabel('Population Share')
plt.title('Rock-Paper-Scissors Evolutionary Dynamics')
plt.legend()
plt.ylim(0.2, 0.45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()