# Installation

1. Git clone [OpenCompass](https://github.com/open-compass/opencompass) and install it locally in the qllm_eval conda environment. See [requirements of OpenCompass](https://github.com/open-compass/opencompass/blob/main/requirements.txt).

   ```
    conda activate qllm
    git clone git@github.com:open-compass/opencompass.git
    cd <opencompass_path>
   ```

2. Install the required packages from the source.

   ```
   pip install -e .
   ```

# Evaluation

1. Prepare datasets. Change directory to `quantize-llm/evaluation/needle_in_a_haystack` and create a new folder:

   ```
   cd quantize-llm/evaluation/needle_in_a_haystack
   mkdir needlebench
   cd needlebench
   ```

   Download the datasets [here](https://github.com/open-compass/opencompass/files/14741330/needlebench.zip) and place in the `quantize-llm/evaluation/needle_in_a_haystack/needlebench` directory can complete dataset preparation.The expected file structure in the needlebench directory is shown below
   ```
   └── needlebench
      ├── multi_needle_reasoning_en.json
      ├── multi_needle_reasoning_zh.json
      ├── names.json
      ├── needles.jsonl
      ├── PaulGrahamEssays.jsonl
      ├── zh_finance.jsonl
      ├── zh_game.jsonl
      ├── zh_government.jsonl
      ├── zh_movie.jsonl
      ├── zh_tech.jsonl
      ├── zh_general.jsonl
   ```
   Change dataset path in `opencompass/configs/datasets/needlbench`

2. Run following command for evaluation

   ```
   python main.py \
      --dataset needlebench_4k \
      --models hf_llama2_7b \
      --work-dir ./outputs/needlebench \
      --num-gpus 1 \
      --max-partition-size 1000 \
      --max-num-workers 8 \
   ```
   Set dataset argument `needlebench_4k` or run `inference.sh` directly if you want to test the original needle in a haystack mission setup.  
   See opencompass docs for more details of different NeedleBench tasks. 