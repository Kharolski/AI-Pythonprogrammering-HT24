import numpy as np
import random

# Definiera miljö (i detta fall en 4x4 grid)
state = 16
actions = 4     # Upp, Ner, Vänster, Höger

# Initiera Q-tabellen med nollor
Q = np.zeros((state, actions))

# Definiera hyperparametrar
alpha = 0.1         # Inlärningshastighet
gamma = 0.9         # Diskonteringsfaktor
epsilon = 0.1       # Epsilon för epsilon-greedy strategi

# Funktion för att välja en åtgärd baserat på epsilon-greedy strategi
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, actions - 1)   # Utforska
    else:
        return np.argmax(Q[state])              # Utnyttja
    
# Träningsfunktion
def train(episodes):
    for _ in range(episodes):
        state = 0           # Börja i startläget

        while state != 15:  # Tills målet nås (antar att 15 är målläget)
            action = choose_action(state)

            # Simulera nästa tillstånd och belöning (Förenklat miljö)
            next_stage = min(state + 1, 15)         # Förenklar genom att alltid gå framåt
            reward = 1 if next_stage == 15 else 0

            # Uppdatera Q-värdet
            old_q = Q[state, action]
            next_max = np.max(Q[next_stage])

            new_q = (1 - alpha) * old_q + alpha * (reward + gamma * next_max)
            Q[state, action] = new_q

            state = next_stage

# Träna agenten
train(1000)
print(Q)






