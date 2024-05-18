datasets = [
    [
        dict(
            abbr='Length2000Depth5_3needle_en_4k',
            depth=5,
            diff=10,
            eval_cfg=dict(
                dataset_postprocessor=dict(
                    type=
                    'opencompass.datasets.needlebench.origin.needlebench_dataset_postprocess'
                ),
                evaluator=dict(
                    type=
                    'opencompass.datasets.needlebench.multi.NeedleBenchMultiEvaluator'
                ),
                pred_postprocessor=dict(
                    type=
                    'opencompass.datasets.needlebench.origin.needlebench_postprocess'
                ),
                pred_role='BOT'),
            file_list=[
                'PaulGrahamEssays.jsonl',
            ],
            guide=True,
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.GenInferencer'),
                prompt_template=dict(
                    template=dict(round=[
                        dict(prompt='{prompt}', role='HUMAN'),
                        dict(prompt='{answer}\n', role='BOT'),
                    ]),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            language='English',
            length=2000,
            length_buffer=600,
            needle_file_name='multi_needle_reasoning_en.json',
            num_needles=3,
            num_repeats_per_file=10,
            path=
            '/opt/data/private/ljx/quantize-llm/evaluation/needle_in_a_haystack/needlebench',
            reader_cfg=dict(
                input_columns=[
                    'prompt',
                ], output_column='answer'),
            tokenizer_model='gpt-4',
            type=
            'opencompass.datasets.needlebench.multi.NeedleBenchMultiDataset'),
    ],
]
eval = dict(runner=dict(task=dict()))
models = [
    dict(
        abbr='longchat-7b-hf',
        batch_padding=False,
        batch_size=8,
        max_out_len=450,
        max_seq_len=2048,
        model_kwargs=dict(device_map='auto'),
        path='/opt/data/private/hf_models/longchat-7b-16k',
        run_cfg=dict(num_gpus=1, num_procs=1),
        tokenizer_kwargs=dict(
            padding_side='left', truncation_side='left', use_fast=False),
        tokenizer_path='/opt/data/private/hf_models/longchat-7b-16k',
        type='opencompass.models.HuggingFaceCausalLM'),
]
work_dir = './outputs/needlebench/20240518_004934'
