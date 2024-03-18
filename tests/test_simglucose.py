import gymnasium as gym
import DTRGym

env = gym.make("SimGlucoseEnv-discrete")

env.reset()
for i in range(10):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info  = env.step(action)
    print(f"action: {action}, obs: {obs}, reward: {reward}, terminated: {terminated}, truncated: {truncated}, info: {info}")
    if terminated or truncated:
        env.reset()
