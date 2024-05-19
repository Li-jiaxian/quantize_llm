# lost in the middle
GPUS=${1}
CUDA_VISIBLE_DEVICES=${GPUS} 
for gold_index in 0 4 9; do
    log_file="log_${gold_index}.log"
    python /opt/data/private/ljx/quantize-llm/evaluation/long_context/main_litm.py \
    --model_name /opt/data/private/hf_models/longchat-13b-16k/ \
    --use_flash_attn \
    --input_path /opt/data/private/ljx/quantize-llm/evaluation/long_context/qa_data/10_total_documents/nq-open-10_total_documents_gold_at_${gold_index}.jsonl.gz \
    --max_new_tokens 100 \
    --output_path /opt/data/private/ljx/quantize-llm/evaluation/long_context/outputs/nq-open-10_total_documents_gold_at_${gold_index}-longchat-13b-16k-predictions.jsonl.gz 
    > $log_file 2>&1
done