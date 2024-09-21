# import matplotlib.pyplot as plt

# # Example data (replace these lists with your actual data)
# learning_rates = [1e-2, 2e-2, 3e-2, 4e-2, 5e-2]  # X-axis data
# # eval_avg_returns = [838.8394775390625, 3867.829345703125, 4485.10546875, 4293.05908203125, 2998.950927734375]   # Y-axis data
# eval_std_returns = [68.03560638427734, 268.25811767578125, 40.636695861816406, 50.68278503417969, 1062.394287109375]

# # Create the plot
# plt.figure(figsize=(8, 6))
# plt.plot(learning_rates, eval_std_returns, marker='o', linestyle='-', color='b')

# # Set plot labels and title
# plt.title("Learning Rate vs Eval Return for Ant v2")
# plt.xlabel("Learning Rate")
# plt.ylabel("Eval Standard Return")

# # Optionally customize grid, limits, etc.
# plt.grid(True)

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Example data (replace these lists with your actual data)
dagger_iterations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # X-axis: DAgger iterations
mean_returns = [400.37359619140625, 871.9635620117188, 2225.133544921875, 2917.455322265625, 3643.220703125, 3732.237548828125, 3740.02490234375, 3745.05322265625, 3769.485107421875, 3768.22998046875]  # Y-axis: Mean returns from policy
std_returns = [161.38623046875, 19.29828453063965, 496.3664855957031, 485.3149719238281, 33.75725173950195, 19.894121170043945, 19.874101638793945, 24.86411476135254, 5.740865707397461, 4.289105415344238]  # Standard deviation (for error bars)

# Constants for horizontal lines
expert_policy_return = 3772.67041015625  # Example expert policy performance (replace with actual value)
# bc_agent_return = 1000  # Example BC agent performance (replace with actual value)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot mean returns with error bars (standard deviation)
plt.errorbar(dagger_iterations, mean_returns, yerr=std_returns, fmt='-o', color='b', label='DAgger Policy')

# Plot horizontal line for expert policy
plt.axhline(y=expert_policy_return, color='g', linestyle='--', label='Expert Policy')

# Set plot labels and title
plt.title("DAgger Iterations vs Policy's Mean Return")
plt.xlabel("DAgger Iterations")
plt.ylabel("Policy's Mean Return")

# Optionally customize grid, limits, etc.
plt.grid(True)

# Add legend
plt.legend()

# Display the plot
plt.show()

