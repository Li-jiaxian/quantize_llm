GPUS=${1}

CUDA_VISIBLE_DEVICES=${GPUS} python main_longeval.py \
--model-name-or-path /opt/data/private/hf_models/longchat-13b-16k/ --use_flash_attn \
--task lines --test_dir new_cases \