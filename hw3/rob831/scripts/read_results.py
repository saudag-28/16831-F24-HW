import argparse
import glob
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def get_section_results(file):
    X, Y = [], []
    for e in tf.train.summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Train_EnvstepsSoFar':
                X.append(v.simple_value)
            elif v.tag == 'Train_AverageReturn':
                Y.append(v.simple_value)
        if len(X) > 120:
            break
    return X, Y

def load_experiment_data(logdirs):
    all_X, all_Y = [], []
    for logdir in logdirs:
        # print(f"Read_dir :{logdir}")
        # exit()
        eventfile = glob.glob(os.path.join(logdir, 'events*'))[0]
        X, Y = get_section_results(eventfile)
        all_X.append(X)
        all_Y.append(Y)
    return np.array(all_X), np.array(all_Y)

def calculate_mean_and_std(data):
    data = np.array(data)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return mean, std

def plot_results(dqn_mean, dqn_std, dqn_steps, double_dqn_mean, double_dqn_std, double_dqn_steps):
    plt.figure(figsize=(10, 6))

    # Plot DQN results
    print(f"dqn_s shape :{dqn_steps.shape} | dqn_m shape :{dqn_mean.shape} | dqn_std shape :{dqn_std.shape}")
    # plt.plot(dqn_steps[1:], dqn_mean, label='DQN', color='blue')

    plt.errorbar(dqn_steps[1:], dqn_mean, yerr=dqn_std, label='DQN', fmt='-o', capsize=5, capthick=1, elinewidth=1)

    # Plot Double DQN results
    print(f"ddqn_s shape :{double_dqn_steps.shape} | ddqn_m shape :{double_dqn_mean.shape} | ddqn_std shape :{double_dqn_std.shape}")
    
    # plt.plot(double_dqn_steps[1:], double_dqn_mean, label='Double DQN', color='orange')
    plt.errorbar(double_dqn_steps[1:], double_dqn_mean, yerr=double_dqn_std, label='Double DQN', fmt='-o', capsize=5, capthick=1, elinewidth=1)

    plt.xlabel("Training Steps")
    plt.ylabel("Average Return")
    plt.legend()
    plt.title("DQN vs Double DQN Performance")
    plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))  # Enable scientific notation for x-axis
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dqn_logdirs', nargs='+', required=True, help='List of directories for DQN event files')
    parser.add_argument('--double_dqn_logdirs', nargs='+', required=True, help='List of directories for Double DQN event files')
    args = parser.parse_args()

    # Load DQN data
    dqn_X, dqn_Y = load_experiment_data(args.dqn_logdirs)
    dqn_mean, dqn_std = calculate_mean_and_std(dqn_Y)
    dqn_steps = np.mean(dqn_X, axis=0)

    # Load Double DQN data
    double_dqn_X, double_dqn_Y = load_experiment_data(args.double_dqn_logdirs)
    double_dqn_mean, double_dqn_std = calculate_mean_and_std(double_dqn_Y)
    double_dqn_steps = np.mean(double_dqn_X, axis=0)

    # Plot the results
    plot_results(dqn_mean, dqn_std, dqn_steps, double_dqn_mean, double_dqn_std, double_dqn_steps)
