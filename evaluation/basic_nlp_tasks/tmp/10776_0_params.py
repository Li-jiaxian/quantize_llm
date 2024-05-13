datasets = [
    [
        dict(
            abbr='chid-test',
            data_files=
            '/opt/data/private/ljx/quantize-llm/evaluation/basic_nlp_tasks/data/data/FewCLUE/chid/test_public.json',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                prompt_template=dict(
                    template=dict({
                        0:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content0}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        1:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content1}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        2:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content2}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        3:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content3}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        4:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content4}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        5:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content5}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        6:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content6}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ])
                    }),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='json',
            reader_cfg=dict(
                input_columns=[
                    'content0',
                    'content1',
                    'content2',
                    'content3',
                    'content4',
                    'content5',
                    'content6',
                ],
                output_column='answer'),
            split='train',
            type='opencompass.datasets.CHIDDataset'),
        dict(
            abbr='chid-dev',
            data_files=
            '/opt/data/private/ljx/quantize-llm/evaluation/basic_nlp_tasks/data/data/FewCLUE/chid/dev_few_all.json',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                prompt_template=dict(
                    template=dict({
                        0:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content0}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        1:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content1}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        2:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content2}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        3:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content3}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        4:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content4}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        5:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content5}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ]),
                        6:
                        dict(round=[
                            dict(prompt='以下句子是否通顺？\n{content6}', role='HUMAN'),
                            dict(prompt='这个句子是通顺的。', role='BOT'),
                        ])
                    }),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            path='json',
            reader_cfg=dict(
                input_columns=[
                    'content0',
                    'content1',
                    'content2',
                    'content3',
                    'content4',
                    'content5',
                    'content6',
                ],
                output_column='answer'),
            split='train',
            type='opencompass.datasets.CHIDDataset'),
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
        run_cfg=dict(num_gpus=4, num_procs=1),
        tokenizer_kwargs=dict(
            padding_side='left', truncation_side='left', use_fast=False),
        tokenizer_path='/opt/data/private/hf_models/Llama-2-7b-hf/',
        type='opencompass.models.HuggingFaceCausalLM'),
]
work_dir = './outputs/debug/lm/FewCLUE_chid_ppl_8f2872/20240513_145255'
