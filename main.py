import random
import math
import matplotlib.pyplot as plt

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        return math.hypot(self.x - city.x, self.y - city.y)

def generate_cities(n, width=100, height=100):
    random.seed(42)
    return [City(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

def total_distance(route):
    return sum(route[i].distance_to(route[(i + 1) % len(route)]) for i in range(len(route)))

def chaos_function(i, total):
    # Logistic map - chaotic but deterministic
    x = 0.7
    for _ in range(i):
        x = 4 * x * (1 - x)
    return int(x * total)

def chaotic_swap(route, iteration):
    i = chaos_function(iteration, len(route))
    j = chaos_function(iteration + 5, len(route))
    new_route = route[:]
    new_route[i % len(route)], new_route[j % len(route)] = new_route[j % len(route)], new_route[i % len(route)]
    return new_route

def simulated_annealing(cities, initial_temp, cooling_rate, iterations):
    current_solution = cities[:]
    current_distance = total_distance(current_solution)
    best_solution = current_solution[:]
    best_distance = current_distance
    temperature = initial_temp

    for k in range(iterations):
        new_solution = chaotic_swap(current_solution, k)
        new_distance = total_distance(new_solution)
        delta = new_distance - current_distance

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_solution = new_solution
            current_distance = new_distance
            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance

        temperature *= cooling_rate

    return best_solution, best_distance

def plot_route(route):
    x = [city.x for city in route] + [route[0].x]
    y = [city.y for city in route] + [route[0].y]
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o-')
    plt.title("Optimized Route Using Simulated Annealing with Chaos Theory")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_cities = 20
    cities = generate_cities(num_cities)
    optimized_route, best_dist = simulated_annealing(cities, initial_temp=10000, cooling_rate=0.995, iterations=10000)
    print(f"Best Distance Found: {best_dist:.2f}")
    plot_route(optimized_route)
