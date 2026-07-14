"""Training entry point."""

import argparse
from pathlib import Path

from llm_classification.config import load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a competition model")
    parser.add_argument("--config", type=Path, default=Path("configs/baseline.yaml"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    name = config["experiment"]["name"]
    print(f"Configuration '{name}' loaded. Add the competition training pipeline next.")


if __name__ == "__main__":
    main()

