# Simulation Environment
DTRGym provided RL environments simulating dynamics of Cancer, Diabetes and Sepsis. All the environments are implemented via standard gymnasium and can be used simply by gymnasium.make()

## Table of Contents

- [Simulation Environment](#simulation-environment)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
    - [Customize maximum timestep](#customize-maximum-timestep)
    - [Choose action space](#choose-action-space)
    - [Customize action number (for Discrete Action Space Env)](#customize-action-number-for-discrete-action-space-env)
  - [Troubleshooting](#troubleshooting)
  - [Contributing](#contributing)
  - [License](#license)
  - [Additional Resources](#additional-resources)

## Installation
todo: Add pypi installation
1. Clone the repository: `git clone https://github.com/your-username/your-project.git](https://github.com/GilesLuo/SimMedEnv.git)`
2. Navigate to the project directory: `cd your-project`

## Usage
Instructions on how to use your project:

1. Include the library in your code: `import DTRGym`
2. Create the Environment: `Env = gym.make(id)`

Here's an example of using the library:

```python
import DTRGym

env = gym.make(DTRGym.registered_id[0])
```

## Configuration
### Customize maximum timestep
You can set the maximum available timestep for the environment by passing value to `max_t`. Here's an example:

```python
import DTRGym

env = gym.make(DTRGym.registered_id[0], max_t=50)
print(env.max_t)
```

### Choose action space
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

### Customize action number (for Discrete Action Space Env)
You can also set the the number of action you want the environment to have by using the `n_act`. This is only effective for the discrete version. Here is an example:

```python
import DTRGym

env = gym.make("AhnChemoEnv-discrete", n_act=5)
print(env.n_act)
```

## Troubleshooting

In the event that you encounter difficulties while trying to use this project, the following tips may help you diagnose and resolve the issue:

1. Issue: KeyError: 'The environment id is not recognized'
Solution: Make sure you have import sim_env, since the register code is in sim_env.__init__.py. Also make sure that the environment ID you are trying to use with gym.make() is correct and registered in gym. You can check available environment IDs using the `sim_env.registered_id` list.


## Contributing

## Contributing

We welcome contributions from the community! Priority goes to NEW ENVIRONMENTS CONTRIBUTION.

If you would like to contribute to the project, please follow these steps:

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Create a Branch**: Create a branch in your fork for your contributions. It's best to use a clear and descriptive name for your branch.

3. **Make Your Changes**: Implement your changes, additions, or fixes in your branch. Please adhere to the coding standards and guidelines of the project.

4. **Write or Update Tests**: If you are adding new functionality, please include tests that cover your changes. If you are fixing a bug, ensure that it is covered by tests and consider adding new tests if necessary.

5. **Run the Tests**: Make sure all tests pass, and your changes do not introduce any new issues or regressions.

6. **Update Documentation**: If your changes involve new features or changes that require updates to the documentation, please include those updates in your contributions.

7. **Submit a Pull Request**: Once your changes are complete, and you have tested your contributions, submit a pull request to the original repository. Please provide a clear description of the changes and any relevant issue numbers.

We will review your pull request as soon as possible. Please be patient, and feel free to update your pull request based on feedback from the project maintainers.

Thank you for considering contributing to our project! We look forward to reviewing your contributions.


## License
We use MIT License for this project. You can find the license in the root directory.