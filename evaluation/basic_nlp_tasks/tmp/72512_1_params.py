datasets = [
    [
        dict(
            abbr='race-high_1',
            eval_cfg=dict(
                evaluator=dict(
                    type='opencompass.openicl.icl_evaluator.AccEvaluator')),
            infer_cfg=dict(
                inferencer=dict(
                    type='opencompass.openicl.icl_inferencer.PPLInferencer'),
                prompt_template=dict(
                    template=dict(
                        A=dict(round=[
                            dict(
                                prompt=
                                'Read the article, and answer the question by replying A, B, C or D.\n\nArticle:\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                role='HUMAN'),
                            dict(prompt='A: A', role='BOT'),
                        ]),
                        B=dict(round=[
                            dict(
                                prompt=
                                'Read the article, and answer the question by replying A, B, C or D.\n\nArticle:\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                role='HUMAN'),
                            dict(prompt='A: B', role='BOT'),
                        ]),
                        C=dict(round=[
                            dict(
                                prompt=
                                'Read the article, and answer the question by replying A, B, C or D.\n\nArticle:\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                role='HUMAN'),
                            dict(prompt='A: C', role='BOT'),
                        ]),
                        D=dict(round=[
                            dict(
                                prompt=
                                'Read the article, and answer the question by replying A, B, C or D.\n\nArticle:\n{article}\n\nQ: {question}\n\nA. {A}\nB. {B}\nC. {C}\nD. {D}',
                                role='HUMAN'),
                            dict(prompt='A: D', role='BOT'),
                        ])),
                    type=
                    'opencompass.openicl.icl_prompt_template.PromptTemplate'),
                retriever=dict(
                    type='opencompass.openicl.icl_retriever.ZeroRetriever')),
            name='high',
            path=
            '/opt/data/private/ljx/quantize-llm/evaluation/basic_nlp_tasks/data/data/race',
            reader_cfg=dict(
                input_columns=[
                    'article',
                    'question',
                    'A',
                    'B',
                    'C',
                    'D',
                ],
                output_column='answer',
                test_range='[250:500]',
                test_split='test',
                train_split='validation'),
            type='opencompass.datasets.RaceDataset'),
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
work_dir = './outputs/debug/lm/race_ppl_a138cd_test/20240513_172610'
