<h3 align="center">DTRGym: Reinforcement learning Environments for Dynamic Treatment Regimes </h3>


---
## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Module Description](#module_description)
- [Usage](#usage)
- [Reference](#reference)
- [Special Thanks](#special_thanks)
- [Acknowledge](#acknowledgement)

## 🧐 About <a name = "about"></a>
DTR-Gym is a benchmarking platform with four unique simulation environments aimed at improving treatments in areas including cancer chemotherapy, tumor growth, diabetes, and sepsis therapy.

The design of DTR-Gym is committed to replicate the intricacies of real clinical scenarios, thereby providing a robust framework for exploring and evaluating reinforcement learning algorithms.


## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
+ Python 3.10: The project is developed using Python 3.10. It is recommended to use the same version to avoid compatibility issues.

### Installing
1. Clone the repository
```
git clone git@github.com:GilesLuo/SimMedEnv.git
```
2. Install the required packages
```
cd SimMedEnv
pip install -r requirements.txt
```

3. Test the installation
```
python test_installation.py
```

### Initialise the Environment

You can run the example by:
```python
import gymnasium as gym
import DTRGym  # this line is necessary!

env = gym.make('AhnChemoEnv-discrete', n_act=11)
print(env.action_space.n)
print(env.observation_space.shape)
```

## 🎈 Module Description <a name="module_description"></a>

### Simulation Environments
There are four simulation environments in the DTRGym. Each environment simulates a specific disease and treatment.

| Environment                                   | Disease        | Treatment                                   | Dynamics | Action Space |
|-----------------------------------------------|----------------|---------------------------------------------|----------|--------------|
| [*AhnChemoEnv*](DTRGym/ahn_chemo_env.py)      | Cancer         | Chemotherapy                               | ODE      | Cont./Disc.  |
| [*GhaffariCancerEnv*](DTRGym/ghaffari_cancer_env.py) | Cancer         | Chemotherapy & Radiotherapy                | ODE      | Cont./Disc.  |
| [*OberstSepsisEnv*](DTRGym/OberstSepsisEnv/env.py)   | Sepsis         | Antibiotics, Mechanical Ventilation, Vasopressors | SCM      | Disc.        |
| [*SimGlucoseEnv*](DTRGym/simglucose_env.py)          | Type-1 Diabetes | Insulin Administration                    | ODE      | Cont./Disc.  |

### Environment Settings
There are five default settings for each environment. The settings are designed to simulate different scenarios in the real world. The settings include:

| Setting | Description                                                                        |
|---------|------------------------------------------------------------------------------------|
| 1       | No PK/PD variation, no observation noise, no missing values. |
| 2       | PK/PD variation, no observation noise, no missing values. |
| 3       | PK/PD variation, observation noise (medium), no missing values. |
| 4       | PK/PD variation, observation noise (large), no missing values. |
| 5       | PK/PD variation, observation noise (large), missing values. |

For different environments, the variations are defined as follows:

| Environment            | PK/PD Variation                            | Observation Noise (Medium)             | Observation Noise (Large)          | Missing Values |
|------------------------|--------------------------------------------|----------------------------------------|------------------------------------|----------------|
| *AhnChemoEnv*          | 10%                                        | 20%                                    | 50%                                | 50%            |
| *GhaffariCancerEnv*    | 10%                                        | 10%                                    | 20%                                | 50%            |
| *OberstSepsisEnv*      | 10%                                        | 20%                                    | 50%                                | 50%            |
| *SimGlucoseEnv*        | Parameters of different patients          | Use data from simulated glucose monitor.| Further randomize food intake times.| 50%           |


## 🔧 Usage <a name="usage"></a>
### Use Default Environment Configuration
DTR-Gym provides default environment configuration to simulate the real-world clinical scenarios. For example, if you want to use the setting 1, you can initialise the environment by
```python
import gymnasium as gym
import DTRGym

env = gym.make("AhnChemoEnv-continuous-setting1")
```

### Customize Maximum Timestep
You can set the maximum available timestep for the environment by passing value to `max_t`. Here's an example:

```python
import gymnasium as gym
import DTRGym

env = gym.make("AhnChemoEnv-continuous", max_t=50)
print(env.max_t)
```

### Choose Action Space
When creating the environment, you can choose from a discrete action space version or a continuous action space version. For all the environment except "TangSepsisEnv-discrete", which only has the discrete actions space version, you can choose different action space by pass id. The environment with same id prefix are only different on the type of action space. They have the same observation space, same disease dynamics, and the same reward function. So feel free to choose the environment according to your RL policy.

Here's an example:

```python
import DTRGym

continuous_env = gym.make("AhnChemoEnv-continuous")
discrete_env = gym.make("AhnChemoEnv-discrete")

print(continuous_env.env_info["action_type"])
print(discrete_env.env_info['action_type'])
print(continuous_env.observation_space.sample() in discrete_env.observation_space)

```

### Customize Action Number (for Discrete Action Space Env)
You can also set the the number of action you want the environment to have by using the `n_act`. This is only effective for the discrete version. Here is an example:

```python
import DTRGym

env = gym.make("AhnChemoEnv-discrete", n_act=5)
print(env.n_act)
```

## Reference <a name="reference"></a>

If you use the DTR-Gym in your research, please cite the following paper:

```
To be updated
```


## ✍️ Sepcial Thanks <a name = "special_thanks"></a>
Special thanks to the following contributors that make the DTR-Gym possible:
- [@Mingcheng Zhu](https://github.com/JasonZuu) - who developed DTRGym and produced extensive DTRBench experiments.
- To be continued

## 🎉 Acknowledgement <a name = "acknowledgement"></a>
  - [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)
  - [Simglucose](https://github.com/jxx123/simglucose)
  - [gumbel-max-scm](https://github.com/clinicalml/gumbel-max-scm)

