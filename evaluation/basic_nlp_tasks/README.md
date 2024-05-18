# Evaluation with OpenCompass

Basic instructions on evaluating quantized LLMs with [OpenCompass](https://github.com/open-compass/opencompass).


## Installation

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

## Evaluation

1. Prepare datasets. Change directory to `QLLM-Evaluation/qllm_eval/evaluation/q_opencompass/` and create a new folder:

   ```
   cd quantize-llm/evaluation
   mkdir data
   cd data
   ```

   Run the following commands to download and place the datasets in the `./qllm_eval/evaluation/q_opencompass/data` directory can complete dataset preparation.

   ```
   # Run in the OpenCompass directory
   wget https://github.com/open-compass/opencompass/releases/download/0.1.8.rc1/OpenCompassData-core-20231110.zip
   unzip OpenCompassData-core-20231110.zip
   ```

   You may also use the pre-downloaded zip file, which is located at `/share/datasets/public_datasets/`.

2. Run the following demo command to evaluate `hf-llama2-7b` with weights quantized to 8-bit on `wingrande` dataset:

   ```
   cd quantize-llm/evaluation
   CUDA_VISIBLE_DEVICES=0 python main.py --models hf_llama2_7b --datasets winogrande_ll_c5cf57 --work-dir ./outputs/debug/Llama2 --w_bit 8
   ```

3. If you want to evaluate models with different quantization settings, please modify `./qllm_eval/evaluation/q_opencompass/utils/build.py`. If you want to support new datasets and new models, please add their configs to `./qllm_eval/evaluation/q_opencompass/configs`, whose original configs may be found at opencompass repo.

   - Specially, if you want to evaluate the models with kv cache quantized, please modify the imported model class in the model configuration file. We provide class `HuggingFaceCausalLM_` for this specific need.

   ```python
   from qllm_eval.evaluation.q_opencompass.utils.models import HuggingFaceCausalLM_
   ```

