# Traveling Salesperson

Traveling Salesperson Problem (TSP) Solver with Simulated Annealing & Chaos Theory
This project tackles the classic Traveling Salesperson Problem (TSP) using an optimization technique inspired by Simulated Annealing, enhanced by chaotic logistic map-based swapping.

What is the TSP?
The Traveling Salesperson Problem asks:
“Given N cities, what is the shortest possible route that visits each city exactly once and returns to the starting point?”

TSP is NP-Hard, meaning that brute force approaches (checking every possible route) become infeasible as N grows due to factorial time complexity. That's where heuristics like Simulated Annealing come in.

Simulated Annealing (SA): Optimization Inspired by Metal Cooling
Analogy:
Imagine dropping a hot metal ball on a jagged landscape. If the ball is hot, it can jump over hills to escape shallow dips (local minima). As it cools, it settles into deeper valleys (closer to the global minimum). We use this idea to escape bad routes and progressively find better ones.

Code Logic & Workflow
Step	What It Does
- Generate Cities	Random 2D coordinates for N cities
- Initial Route	Random ordering of cities
- SA Loop	Iteratively improve route using swaps
- Chaos Swap	Swaps chosen using the Logistic Map formula
- Acceptance	Better solutions accepted; worse ones maybe accepted with probability e^(-ΔE/T)
- Cooling	Gradually reduce temperature to fine-tune search
- Output	Plots the final best route overlaid on city positions

Chaos Theory: Logistic Map Swapping
Instead of randomly swapping two cities, this project uses a Logistic Map, a chaotic but deterministic function: x = r * x * (1 - x)
This: 
- Simulates how complex systems search for patterns.
- Deterministic yet highly sensitive to initial values (like quantum systems).
- Helps explore a broader space more strategically than pure randomness.

Final Output
At the end of the algorithm:
- Dots represent cities
- Line shows the optimized path visiting all cities once and returning to the start

Requirements
- Python 3.x
- matplotlib
- numpy

Install dependencies with:

pip install -r requirements.txt

File Structure: tsp-simulated-annealing-chaos
1. tsp_solver.py         # Main implementation
2. README.md             # You are here
3. requirements.txt      # Dependencies

Try It Yourself

You can run the script directly: python tsp_solver.py

Feel free to tweak parameters like:
- Number of cities
- Initial temperature
- Cooling rate
- Logistic map seed values

Inspiration
- Simulated Annealing: Kirkpatrick, S. et al. (1983): Chaos Theory & Optimization: Logistic Map-based approaches in AI

Author Notes
This project blends the principles of classical optimization, chaotic systems, and AI-inspired search to offer a powerful heuristic for solving hard problems. Great for educational purposes and experimentation in hybrid optimization techniques.

