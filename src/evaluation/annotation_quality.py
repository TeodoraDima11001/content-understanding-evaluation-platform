import numpy as np
import pandas as pd


class AnnotationQualityEvaluator:
    """
    Production-style evaluation of annotation quality.
    Works on dataframe-level inputs (Spotify-style).
    """

    def __init__(self, df, label_col="label", gold_col="human_label", group_col=None):
        self.df = df
        self.label_col = label_col
        self.gold_col = gold_col
        self.group_col = group_col

    def accuracy(self):
        return (self.df[self.label_col] == self.df[self.gold_col]).mean()

    def disagreement_rate(self):
        return 1 - self.accuracy()

    def group_metrics(self):
        """
        Spotify-style requirement:
        performance varies by segment (content type / language / genre)
        """
        if not self.group_col:
            return None

        return self.df.groupby(self.group_col).apply(
            lambda x: (x[self.label_col] == x[self.gold_col]).mean()
        ).to_dict()

    def confidence_proxy(self):
        """
        Simulates annotation uncertainty signal.
        """
        return {
            "low_confidence_rate": (self.df["confidence"] < 0.7).mean()
            if "confidence" in self.df.columns else None
        }
