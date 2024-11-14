import random

def generate_random_list(n, seed=None):
    if seed is not None:
        random.seed(seed)  # Sets the random seed for reproducibility
    return [random.randint(0, n*10) for _ in range(n)]  



if __name__ == "__main__":
    for n in range(7, 12):
        generated_list = generate_random_list(n, seed=42)
        print(f"Generated list for n={n}: {generated_list}")