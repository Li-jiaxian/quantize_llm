GPUS=${1}
CUDA_VISIBLE_DEVICES=${GPUS}

python main.py \
    --dataset needlebench_4k \
    --models hf_longchat_7b \
    --summarizer needlebench/needlebench_4k_summarizer \
    --work-dir ./outputs/needlebench \
    --num-gpus 1 \
    --max-partition-size 5000 \
    --max-num-workers 8 \