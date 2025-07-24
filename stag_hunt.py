import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_agents = 100
num_generations = 200
rounds_per_generation = 10
mutation_rate = 0.02

# Stag Hunt Payoff Matrix
# [Stag, Hare]
payoff_matrix = np.array([
    [4, 0],     # Stag payoffs (4 if both hunt stag, 0 if other hunts hare)
    [3, 3]      # Hare payoffs (3 regardless of what other does)
])

# Initialize population with even split (50% Stag, 50% Hare)
population = np.random.randint(0, 2, num_agents)

# Track strategy frequencies over time
stag_freq = []
hare_freq = []

# Run simulation
for generation in range(num_generations):
    # Calculate current frequencies
    stag_count = np.sum(population == 0)
    hare_count = np.sum(population == 1)
    stag_freq.append(stag_count / num_agents)
    hare_freq.append(hare_count / num_agents)
    
    # Play rounds and calculate fitness
    fitness = np.zeros(num_agents)
    for _ in range(rounds_per_generation):
        # Random pairings
        np.random.shuffle(population)
        for i in range(0, num_agents, 2):
            if i+1 < num_agents:  # Ensure we have a pair
                strategy1 = population[i]
                strategy2 = population[i+1]
                # Apply payoffs
                fitness[i] += payoff_matrix[strategy1, strategy2]
                fitness[i+1] += payoff_matrix[strategy2, strategy1]
    
    # Evolutionary update using imitate-better-performing with mutation
    new_population = np.zeros(num_agents, dtype=int)
    for i in range(num_agents):
        if np.random.random() < mutation_rate:
            # Random mutation
            new_population[i] = np.random.randint(0, 2)
        else:
            # Compare with random agent and adopt their strategy if better
            compare_with = np.random.randint(0, num_agents)
            if fitness[compare_with] > fitness[i]:
                new_population[i] = population[compare_with]
            else:
                new_population[i] = population[i]
    
    population = new_population

# Calculate critical threshold
critical_threshold = (payoff_matrix[1,1] - payoff_matrix[0,1]) / ((payoff_matrix[0,0] - payoff_matrix[1,0]) + (payoff_matrix[1,1] - payoff_matrix[0,1]))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(stag_freq, 'brown', label='Stag Frequency')
plt.plot(hare_freq, 'orange', label='Hare Frequency')
plt.axhline(y=critical_threshold, color='black', linestyle='--', label=f'Critical Threshold ({critical_threshold:.2f})')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Strategy Dynamics in Stag Hunt Game')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Print theoretical analysis
print(f"Critical threshold for convergence to Stag: {critical_threshold:.2f}")
print(f"Final state: {stag_freq[-1]:.2f} Stag, {hare_freq[-1]:.2f} Hare")
print(f"Payoff-dominant equilibrium: (Stag, Stag) with payoff {payoff_matrix[0,0]}")
print(f"Risk-dominant equilibrium: (Hare, Hare) with payoff {payoff_matrix[1,1]}")