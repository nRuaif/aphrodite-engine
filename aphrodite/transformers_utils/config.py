from transformers import AutoConfig, PretrainedConfig

def get_config(model: str, trust_remote_code: bool) -> PretrainedConfig:
    try:
        config = AutoConfig.from_pretrained(
            model, trust_remote_code=trust_remote_code)
    except ValueError as e:
        if (not trust_remote_code and
                "requires you to execute the configuration file" in str(e)):
            err_msg = (
                "Failed to load the model config. If the model uses custom "
                "code not yet available in HF transformers library, consider "
                "setting `trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI.")
            raise RuntimeError(err_msg) from e
        else:
            raise e
    return config