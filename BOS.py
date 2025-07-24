import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_agents = 100
num_generations = 200
rounds_per_generation = 10
mutation_rate = 0.02

# Battle of the Sexes Payoff Matrix
# Row player's preference is Opera, Column player's is Football
a = 3  # Row player's payoff for preferred coordination
b = 1  # Row player's payoff for non-preferred coordination
c = 1  # Column player's payoff for non-preferred coordination
d = 3  # Column player's payoff for preferred coordination


payoff_matrix = np.array([
    [a, 0],     # Opera payoffs
    [0, b]      # Football payoffs
])

# Initialize population with slight bias (60% Football, 40% Opera)
population = np.random.choice([0, 1], size=num_agents, p=[0.4, 0.6])

# Track strategy frequencies over time
opera_freq = []
football_freq = []

# Run simulation
for generation in range(num_generations):
    # Calculate current frequencies
    opera_count = np.sum(population == 0)
    football_count = np.sum(population == 1)
    opera_freq.append(opera_count / num_agents)
    football_freq.append(football_count / num_agents)
    
    # Play rounds and calculate fitness
    fitness = np.zeros(num_agents)
    for _ in range(rounds_per_generation):
        # Random pairings
        np.random.shuffle(population)
        for i in range(0, num_agents, 2):
            if i+1 < num_agents:  # Ensure we have a pair
                strategy1 = population[i]
                strategy2 = population[i+1]
                # Apply payoffs only if coordination occurs
                if strategy1 == strategy2:
                    if strategy1 == 0:  # Both chose Opera
                        fitness[i] += a
                        fitness[i+1] += c
                    else:  # Both chose Football
                        fitness[i] += b
                        fitness[i+1] += d
    
    # Evolutionary update with replicator dynamics and mutation
    strategy_fitness = [np.mean(fitness[population == i]) if np.any(population == i) else 0 for i in range(2)]
    avg_fitness = np.mean(fitness)
    
    new_population = np.zeros(num_agents, dtype=int)
    for i in range(num_agents):
        if np.random.random() < mutation_rate:
            # Random mutation
            new_population[i] = np.random.randint(0, 2)
        else:
            # Probabilistic strategy selection based on relative fitness
            probs = np.array([opera_freq[-1], football_freq[-1]])
            for j in range(2):
                if avg_fitness > 0:
                    probs[j] *= (1 + (strategy_fitness[j] - avg_fitness) / avg_fitness)
            probs = np.maximum(0, probs)
            if np.sum(probs) > 0:
                probs = probs / np.sum(probs)
                new_population[i] = np.random.choice(2, p=probs)
            else:
                new_population[i] = np.random.randint(0, 2)
    
    population = new_population

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(opera_freq, 'purple', label='Opera Frequency')
plt.plot(football_freq, 'green', label='Football Frequency')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Strategy Dynamics in Battle of the Sexes')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()