import gymnasium as gym
import DTRGym
import time

print(DTRGym.registered_ids)
for id in DTRGym.registered_ids:
    env = gym.make(id)
    print(f"env: {id} is created.")
    print(f"obs space: ", env.observation_space)
    print(f"action space: ", env.action_space)
    print("=====================================")
    time.sleep(1)