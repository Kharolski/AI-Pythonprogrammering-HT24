import numpy as np  
import random

# Definiera miljön (4x4 Gridworld) med hinder
class Gridworld:
    def __init__(self):
        self.grid_size = 4              # Rutnätets storlek (4x4)
        self.start_state = (0, 0)       # Starttillståndet
        self.goal_state = (3, 3)        # Måltillståndet

    def reset(self):
        return self.start_state     # Återställ agenten till startpunkten
    
    def step(self, state, action):
        actions = {
            0: (-1, 0),     # Upp
            1: (1, 0),      # Ner
            2: (0, -1),     # Vänster
            3: (0, 1)       # Höger
        }

        # Nuvarande position
        row, col = state

        # Beräkna ny position
        new_row = row + actions[action][0]
        new_col = col + actions[action][1]

        # Håll agenten inom gränserna för rutnätet
        new_row = max(0, min(new_row, self.grid_size - 1))
        new_col = max(0, min(new_col, self.grid_size - 1))

        new_state = (new_row, new_col)

        # Ge belöning för att nå målet
        if new_state == self.goal_state:
            return new_state, 10, True      # Belöning +10 och målet nått
        else:
            return new_state, -1, False     # Stegkostnad -1
        

# Q-learning-agent
class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.env = env
        self.alpha = alpha      # Inlärningshastighet
        self.gamma = gamma      # Diskonteringsfaktor
        self.epsilon = epsilon  # Utforskning vs utnyttjande-faktor
        self.q_table = {}       # Q-tabellen för att lagra värden (tillstånd, handling)

    def get_q_value(self, state, action):
        # Returnerar Q-värdet för ett tillstånd och en handling (standard 0 om inte sett förut)
        return self.q_table.get((state, action), 0.0)
    
    def update_q_value(self, state, action, reward, next_state):
        # Uppdaterar Q-värdet enligt Q-learning-formeln
        max_q_next = max([self.get_q_value(next_state, a) for a in range(4)])   # Maximalt Q-värde för nästa tillstånd
        current_q = self.get_q_value(state, action)
        new_q = current_q + self.alpha * (reward + self.gamma * max_q_next - current_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, state):
       # Välj handling med epsilon-greedy metod (utforskning vs utnyttjande)
       if random.uniform(0, 1) < self.epsilon:
           # Utforska: välj en slumpmässig handling
           return random.choice([0, 1, 2, 3])               
       else:
           # Utnyttja: välj den bästa kända handlingen
           q_values = [self.get_q_value(state, a) for a in range(4)]
           return np.argmax(q_values)
       
    def train(self, episodes):
        for episode in range(episodes):
            state = self.env.reset()        # Återställ till starttillståndet
            done = False
            total_reward = 0

            while not done:
                action = self.choose_action(state)                          # Välj handling
                next_state, reward, done = self.env.step(state, action)     # Utför handling och få belöning
                self.update_q_value(state, action, reward, next_state)      # Uppdatera Q-värdet
                state = next_state                                          # Gå till nästa tillstånd
                total_reward += reward

            print(f"Episode {episode + 1}: Total reward: {total_reward}")


# Skapa miljö och agent
env = Gridworld()
agent = QLearningAgent(env)

# Träna agenten med 1000 episoder
agent.train(1000)

# Visa den tränade Q-tabellen
print("\nTrained Q-values:")
for state_action, value in agent.q_table.items():
    print(f"State {state_action[0]}, Action {state_action[1]}: {value:.2f}")