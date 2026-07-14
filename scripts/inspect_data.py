"""Inspect the competition files before building a model."""

import argparse
from pathlib import Path

import pandas as pd

from llm_classification.config import load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect Kaggle competition data")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/llm_classification.yaml"),
    )
    return parser.parse_args()


def require_columns(frame: pd.DataFrame, columns: list[str], file_name: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        raise ValueError(f"Missing columns in {file_name}: {missing}")


def main() -> None:
    config = load_config(parse_args().config)
    data = config["data"]

    paths = {
        "train": Path(data["train_file"]),
        "test": Path(data["test_file"]),
        "submission": Path(data["sample_submission_file"]),
    }
    missing_files = [str(path) for path in paths.values() if not path.is_file()]
    if missing_files:
        files = "\n- ".join(missing_files)
        raise FileNotFoundError(f"Download or extract these files first:\n- {files}")

    train = pd.read_csv(paths["train"])
    test = pd.read_csv(paths["test"])
    submission = pd.read_csv(paths["submission"])

    id_column = data["id_column"]
    text_columns = data["text_columns"]
    target_columns = data["target_columns"]
    require_columns(train, [id_column, *text_columns, *target_columns], paths["train"].name)
    require_columns(test, [id_column, *text_columns], paths["test"].name)
    require_columns(submission, [id_column, *target_columns], paths["submission"].name)

    print(f"Train:      {train.shape}")
    print(f"Test:       {test.shape}")
    print(f"Submission: {submission.shape}")
    print(f"\nTrain duplicates: {train.duplicated().sum()}")
    print("\nMissing values in train:")
    print(train[[id_column, *text_columns, *target_columns]].isna().sum().to_string())
    print("\nTarget counts:")
    print(train[target_columns].sum().astype(int).to_string())

    invalid_targets = train[target_columns].sum(axis=1).ne(1).sum()
    print(f"\nRows without exactly one target: {invalid_targets}")

    print("\nText lengths (characters):")
    lengths = train[text_columns].fillna("").apply(lambda column: column.str.len())
    print(lengths.describe().round(1).to_string())


if __name__ == "__main__":
    main()

