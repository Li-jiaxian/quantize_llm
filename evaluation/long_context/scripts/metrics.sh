# evaluate
for gold_index in 0 4 9;do
    python evaluate_qa_responses.py \
        --input-path /opt/data/private/ljx/quantize_llm/evaluation/long_context/outputs/10_total_documents/nq-open-10_total_documents_gold_at_${gold_index}-longchat-13b-16k-predictions-score.jsonl.gz \
        --output-path /opt/data/private/ljx/quantize_llm/evaluation/long_context/outputs/10_total_documents/nq-open-10_total_documents_gold_at_${gold_index}-longchat-13b-16k-predictions-score.jsonl
done