datasets = [
    [
        dict(
            abbr='lambada_6',
            eval_cfg=dict(
                evaluator=dict(type='opencompass.datasets.LambadaEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    max_out_len=5,
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(
                            prompt=
                            'Please complete the following sentence:\n{prompt}',
                            role='HUMAN'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path=
            '/opt/data/private/ljx/quantize-llm/evaluation/basic_nlp_tasks/data/data/lambada/test.jsonl',
            reader_cfg=dict(
                input_columns=[
                    'prompt',
                ],
                output_column='label',
                test_range='[300:350]',
                test_split='test',
                train_split='test'),
            type='opencompass.datasets.lambadaDataset'),
    ],
]
models = [
    dict(
        abbr='llama-2-7b-hf',
        batch_padding=False,
        batch_size=8,
        max_out_len=100,
        max_seq_len=2048,
        model_kwargs=dict(device_map='auto'),
        path='/opt/data/private/hf_models/Llama-2-7b-hf/',
        run_cfg=dict(num_gpus=1, num_procs=1),
        tokenizer_kwargs=dict(
            padding_side='left', truncation_side='left', use_fast=False),
        tokenizer_path='/opt/data/private/hf_models/Llama-2-7b-hf/',
        type='opencompass.models.HuggingFaceCausalLM'),
]
work_dir = './outputs/debug/lm/lambada_gen_217e11/20240513_211253'
