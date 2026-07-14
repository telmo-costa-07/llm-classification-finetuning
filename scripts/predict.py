"""Inference and submission entry point."""

import argparse
from pathlib import Path

from llm_classification.config import load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate competition predictions")
    parser.add_argument("--config", type=Path, default=Path("configs/baseline.yaml"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    destination = config["paths"]["submission_file"]
    print(f"Configuration loaded. Submission will be written to '{destination}'.")


if __name__ == "__main__":
    main()

