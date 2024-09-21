Q1.1 - Change the name from Ant to any other name to run for any other environment

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
	--video_log_freq -1

Q1.2 - Change the env name to Hopper to generate Hopper's data

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \ 
    --eval_batch_size 5000 \
    --num_agent_train_steps_per_iter 2000 \
	--video_log_freq -1

Q1.3

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --learning_rate 1e-2 \
	--video_log_freq -1

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --learning_rate 2e-2 \
	--video_log_freq -1

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --learning_rate 3e-2 \
	--video_log_freq -1

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --learning_rate 4e-2 \
	--video_log_freq -1

python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --learning_rate 5e-2 \
	--video_log_freq -1

Q2.1 - Change the env name to Hopper to generate Hopper's data

python rob831/scripts/run_hw1.py \
    --expert_policy_file rob831/policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name dagger_ant --n_iter 10 \
    --do_dagger --expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
	--video_log_freq -1