import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_agents = 100
num_generations = 200
rounds_per_generation = 10
mutation_rate = 0.02

# Chicken Game Payoff Matrix
# [Swerve, Straight]
# Payoffs for row player
V = 4  # Value of winning
C = 10  # Cost of crash
payoff_matrix = np.array([
    [V/2, 0],      # Swerve payoffs
    [V, -C/2]      # Straight payoffs
])

# Initialize population (50% Swerve, 50% Straight)
population = np.random.randint(0, 2, num_agents)

# Track strategy frequencies over time
swerve_freq = []
straight_freq = []

# Run simulation
for generation in range(num_generations):
    # Calculate current frequencies
    swerve_count = np.sum(population == 0)
    straight_count = np.sum(population == 1)
    swerve_freq.append(swerve_count / num_agents)
    straight_freq.append(straight_count / num_agents)
    
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
    
    # Evolutionary update using imitate-the-best with mutation
    new_population = np.zeros(num_agents, dtype=int)
    for i in range(num_agents):
        if np.random.random() < mutation_rate:
            # Random mutation
            new_population[i] = np.random.randint(0, 2)
        else:
            # Select random opponent and compare fitness
            opponent = np.random.randint(0, num_agents)
            if fitness[opponent] > fitness[i]:
                new_population[i] = population[opponent]  # Imitate if better
            else:
                new_population[i] = population[i]  # Keep current strategy
    
    population = new_population

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(swerve_freq, 'blue', label='Swerve Frequency')
plt.plot(straight_freq, 'red', label='Straight Frequency')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Strategy Dynamics in Chicken Game')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Print theoretical mixed equilibrium
p_swerve = V/C
print(f"Theoretical mixed equilibrium: {p_swerve:.2f} Swerve, {1-p_swerve:.2f} Straight")
print(f"Final simulation state: {swerve_freq[-1]:.2f} Swerve, {straight_freq[-1]:.2f} Straight")