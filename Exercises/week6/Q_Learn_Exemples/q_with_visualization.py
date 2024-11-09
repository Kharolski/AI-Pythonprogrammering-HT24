import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Environment:
    def __init__(self, size=4):
        self.size = size
        self.states = size * size
        self.actions = 4                # Upp, Ner, Vänster, Höger
        self.obstacles = [5, 7, 11]     # Positioner för hinder
        self.goal = self.states - 1      # Målposition (nedre högra hörnet)

    def get_next_state(self, state, action):
        if action == 0:     # Upp
            next_state = state - self.size if state >= self.size else state
        elif action == 1:   # Ner
            next_state = state + self.size if state < self.states - self.size else state
        elif action == 2:   # Vänster
            next_state = state - 1 if state % self.size != 0 else state
        else:               # Höger
            next_state = state + 1 if (state + 1) % self.size != 0 else state

        return state if next_state in self.obstacles else next_state
    
    def get_reward(self, state, next_state):
        if next_state == self.goal:
            return 100      # Hög belöning för att nå målet
        elif next_state in self.obstacles:
            return -10      # Negativ belöning för att träffa ett hinder
        else:
            return -1       # Liten negativ belöning för varje steg
        
class Agent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = np.zeros((env.states, env.actions))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.env.actions - 1)
        else:
            return np.argmax(self.Q[state])
        
    def update_q_value(self, state, action, reward, next_state):
        old_q = self.Q[state, action]
        next_max = np.max(self.Q[next_state])
        new_q = (1 - self.alpha) * old_q + self.alpha * (reward + self.gamma * next_max)
        self.Q[state, action] = new_q

class Trainer:
    def __init__(self, agent):
        self.agent = agent
        self.episode_rewards = []
        self.q_history = []

    def train(self, episodes):
        for _ in range(episodes):
            state = 0
            total_reward = 0

            while state != self.agent.env.goal:
                action = self.agent.choose_action(state)
                next_state = self.agent.env.get_next_state(state, action)
                reward = self.agent.env.get_reward(state, next_state)
                
                self.agent.update_q_value(state, action, reward, next_state)

                state = next_state
                total_reward += reward

            self.episode_rewards.append(total_reward)
            self.q_history.append(np.copy(self.agent.Q))

    def show_path(self):
        state = 0
        path = [state]
        while state != self.agent.env.goal:
            action = np.argmax(self.agent.Q[state])
            state = self.agent.env.get_next_state(state, action)
            path.append(state)
        return path

class Visualizer:
    def __init__(self, env, trainer):
        self.env = env
        self.trainer = trainer
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15,5))
        self.fig.suptitle('Reinforcement Learning Visualization')

    def init_plot(self):
        self.ax1.clear()
        self.ax1.set_title('Environment')
        self.ax1.set_xticks(range(self.env.size))
        self.ax1.set_yticks(range(self.env.size))
        self.ax1.grid(True)

        self.ax2.clear()
        self.ax2.set_title('Total Reward per Episode')
        self.ax2.set_xlabel('Episode')
        self.ax2.set_ylabel('Total Reward')

        return self.ax1, self.ax2

    def update_plot(self, frame):
        self.ax1, self.ax2 = self.init_plot()

        # Visualize environment
        q_values = self.trainer.q_history[frame]
        for i in range(self.env.states):
            row, col = divmod(i, self.env.size)
            best_action = np.argmax(q_values[i])
            color = ['r', 'g', 'b', 'y'][best_action]
            self.ax1.add_patch(plt.Rectangle((col, self.env.size-1-row), 1, 1, fill=False, edgecolor=color))
            self.ax1.text(col+0.5, self.env.size-1-row+0.5, f"{np.max(q_values[i]):.2f}", 
                          ha='center', va='center', fontsize=8)

        # Mark obstacles and goal
        for obstacle in self.env.obstacles:
            row, col = divmod(obstacle, self.env.size)
            self.ax1.add_patch(plt.Rectangle((col, self.env.size-1-row), 1, 1, facecolor='gray'))
        
        goal_row, goal_col = divmod(self.env.goal, self.env.size)
        self.ax1.add_patch(plt.Rectangle((goal_col, self.env.size-1-goal_row), 1, 1, facecolor='green', alpha=0.5))

        # Plot rewards
        episodes = range(1, frame + 2)
        rewards = self.trainer.episode_rewards[:frame+1]
        self.ax2.plot(episodes, rewards)

        return self.ax1, self.ax2
    
    def animate(self):
        if len(self.trainer.q_history) == 0:
            print("No training data to visualize")
            return

        anim = FuncAnimation(self.fig, self.update_plot, frames=len(self.trainer.q_history),
                             init_func=self.init_plot, blit=False, repeat=False, interval=100)
        plt.tight_layout()
        plt.show()


env = Environment()
agent = Agent(env)
trainer = Trainer(agent)

trainer.train(100)  # Träna i n episoder

visualizer = Visualizer(env, trainer)
visualizer.animate()

print("\nOptimal väg:")
print(trainer.show_path())



