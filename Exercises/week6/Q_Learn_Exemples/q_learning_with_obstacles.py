import numpy as np
import random

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

    def train(self, episodes):
        for _ in range(episodes):
            state = 0       # Börja i startläget

            while state != self.agent.env.goal:
                action = self.agent.choose_action(state)
                next_state = self.agent.env.get_next_state(state, action)
                reward = self.agent.env.get_reward(state, next_state)

                self.agent.update_q_value(state, action, reward, next_state)

                state = next_state

    def show_path(self):
        state = 0
        path = [state]
        while state != self.agent.env.goal:
            action = np.argmax(self.agent.Q[state])
            state = self.agent.env.get_next_state(state, action)
            path.append(state)
        return path


env = Environment()
agent = Agent(env)
trainer = Trainer(agent)

trainer.train(10000)

print("Q-tabell:")
print(agent.Q)
print("\nOptimal väg:")
print(trainer.show_path())


