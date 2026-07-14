from llm_classification.config import load_config


def test_llm_classification_config() -> None:
    config = load_config("configs/llm_classification.yaml")

    assert config["data"]["competition"] == "llm-classification-finetuning"
    assert config["data"]["target_columns"] == [
        "winner_model_a",
        "winner_model_b",
        "winner_tie",
    ]
    assert config["metric"]["name"] == "multiclass_log_loss"
