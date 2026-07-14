from llm_classification.config import load_config


def test_load_baseline_config() -> None:
    config = load_config("configs/baseline.yaml")

    assert config["experiment"]["name"] == "baseline"
    assert config["experiment"]["seed"] == 42

