# Games Meet Evolution: Strategic Behavior
CSCI 165 Project  
Levi Sumbela, Surya Gona, Wyatt Miller  
April 23, 2025

## Overview

This project explores how strategies evolve over time using ideas from game theory and evolutionary dynamics. We focused on four classic games:

- Rock-Paper-Scissors  
- Chicken  
- Battle of the Sexes  
- Stag Hunt

Our main goal was to simulate how strategic behavior spreads in populations and what patterns emerge.

## Methods

We created virtual populations of 100 agents and simulated how they played the games over 200+ generations. After each round, successful strategies replicated more, while unsuccessful ones faded. We also introduced a small mutation rate to allow occasional random strategy shifts.

The simulations were based on:

- **Nash Equilibrium** – where no player benefits from changing their strategy alone  
- **Replicator Dynamics** – tracking how strategies grow or shrink over time based on performance

Each game had its own setup:
- Rock-Paper-Scissors used standard rules  
- Chicken varied the payoff for swerving vs crashing  
- Battle of the Sexes gave asymmetric preferences but required coordination  
- Stag Hunt rewarded cooperation but carried more risk

## Results

- **Rock-Paper-Scissors:** Strategies cycled endlessly — rock beats scissors, scissors beats paper, paper beats rock. No stable equilibrium, just continuous shifts.
- **Chicken:** A stable mix emerged — around 60% played "Straight" while 40% swerved. Crashes punished risk-takers, keeping the balance.
- **Battle of the Sexes:** Small early advantages determined the outcome. One preference quickly dominated based on initial majority.
- **Stag Hunt:** Cooperation only succeeded when enough players started by cooperating. If too few did, the whole group switched to the safer "hare" strategy.

## Why It Matters

These results help explain real-world social patterns like:
- How trends and behaviors spread
- Why certain strategies or technologies dominate
- Why risk-aversion can hold back cooperation
- How societies can get stuck in less-than-ideal outcomes

## Reflection

The hardest part was making the math understandable. Showing visual trends of strategy shifts over time made the results more intuitive. Comparing all four games side-by-side helped show how different game setups lead to different social outcomes.

## References

- Straub, P. G. (1995). *Risk Dominance and Coordination Failures in Static Games*. The Quarterly Review of Economics and Finance.  
- Livnat, A. & Papadimitriou, C. (2016). *Sex as an Algorithm: The Theory of Evolution Under the Lens of Computation*. Communications of the ACM.  
- Sandholm, W. H. (2010). *Population Games and Evolutionary Dynamics*. MIT Press.  
- Nowak, M. A. (2006). *Evolutionary Dynamics: Exploring the Equations of Life*. Harvard University Press.  
