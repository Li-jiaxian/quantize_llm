# GPUS=${1}
# CUDA_VISIBLE_DEVICES=${GPUS}
# datasets=(winogrande_ll_c5cf57 FewCLUE_chid_ppl_8f2872 race_ppl_a138cd lambada_gen_217e11 siqa_ppl_ced5f6 piqa_ppl_1cf9f0)
dataset='siqa_ppl_ced5f6'

python main.py \
    --models hf_llama_7b \
    --datasets ${dataset} \
    --work-dir ./outputs/debug/lm/${dataset}_llama \
    --num-gpus 1 \
    --max-partition-size 1000 \
    --max-num-workers 8 \