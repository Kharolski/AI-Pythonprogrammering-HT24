import numpy as np
import matplotlib.pyplot as plt
import random

class Gridworld:
    def __init__(self):
        self.grid_size = 4
        self.start_state = (3, 3)  # Startpunkten för agenten
        self.goal_state = (0, 0)   # Målpunkten för agenten
        self.hindrances = []       # Lista för att lagra hinder
    
    def reset(self):
        return self.start_state  # Återställ agenten till startpunkten

    def is_hindrance(self, state):
        return state in self.hindrances

    def step(self, state, action):
        actions = {
            0: (-1, 0),  # Upp
            1: (1, 0),   # Ner
            2: (0, -1),  # Vänster
            3: (0, 1)    # Höger
        }
        row, col = state
        new_row = row + actions[action][0]
        new_col = col + actions[action][1]
        new_row = max(0, min(new_row, self.grid_size - 1))
        new_col = max(0, min(new_col, self.grid_size - 1))

        new_state = (new_row, new_col)
        if self.is_hindrance(new_state):
            return state, -10, False  # Straff för hinder
        if new_state == self.goal_state:
            return new_state, 10, True  # Belöning för målet
        else:
            return new_state, -1, False  # Kostnad för varje steg

    def add_hindrance(self, row, col):
        if (row, col) != self.goal_state and (row, col) != self.start_state:
            self.hindrances.append((row, col))

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def set_q_value(self, state, action, value):
        self.q_table[(state, action)] = value

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(range(4))
        else:
            q_values = [self.get_q_value(state, a) for a in range(4)]
            return np.argmax(q_values)

    def update(self, state, action, reward, next_state):
        best_next_action = np.argmax([self.get_q_value(next_state, a) for a in range(4)])
        max_q_next = self.get_q_value(next_state, best_next_action)
        current_q = self.get_q_value(state, action)
        new_q_value = current_q + self.alpha * (reward + self.gamma * max_q_next - current_q)
        self.set_q_value(state, action, new_q_value)

# Visualisera miljön och agentens rörelse
def plot_grid(env, agent, path, episode):
    grid = np.zeros((env.grid_size, env.grid_size))
    for hindrance in env.hindrances:
        grid[hindrance] = -1
    grid[env.start_state] = 0.5
    grid[env.goal_state] = 1

    plt.clf()  # Rensa plotten istället för att stänga den
    plt.imshow(grid, cmap='cool', origin='upper', extent=[0, 4, 0, 4])
    path = np.array(path)
    plt.plot(path[:, 1] + 0.5, 3.5 - path[:, 0], marker='o', color='red', markersize=5, linestyle='-')
    plt.title(f"Agentens väg - Episod {episode}")
    plt.grid(True)
    plt.pause(0.5)  # Vänta 0.5 sekunder innan nästa uppdatering

def get_user_input(env):
    user_input = input("Vill du lägga till ett hinder? Ange 'y' för ja, tryck Enter för att fortsätta, eller 'q' för att avsluta: ")
    if user_input.lower() == 'y':
        try:
            row = int(input(f"Ange rad (0 till {env.grid_size - 1}): "))
            col = int(input(f"Ange kolumn (0 till {env.grid_size - 1}): "))
            env.add_hindrance(row, col)
            print(f"Hinder placerat på ({row}, {col}).")
        except ValueError:
            print("Ogiltig inmatning, försök igen.")
    elif user_input.lower() == 'q':
        print("Avslutar inlärningsprocessen...")
        return False
    return True

# Körning och visualisering av inlärningsprocessen med användarinteraktion
env = Gridworld()
agent = QLearningAgent(env)
n_episodes = 10
exit_requested = False

plt.ion()  # Sätt matplotlib till interaktivt läge

for episode in range(n_episodes):
    state = env.reset()
    path = [state]
    done = False

    while not done and not exit_requested:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(state, action)
        agent.update(state, action, reward, next_state)
        state = next_state
        path.append(state)

        plot_grid(env, agent, path, episode)
        if not get_user_input(env):
            exit_requested = True
            break

    if exit_requested:
        break

    print(f"Episod {episode} färdig.")

plt.ioff()  # Avsluta interaktivt läge
plt.show()  # Visa sista plotten tills användaren stänger den
