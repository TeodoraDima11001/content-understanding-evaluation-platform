import numpy as np
import pandas as pd


class LLMEvaluator:
    """
    Evaluates LLM-generated annotations vs human labels.
    """

    def __init__(self, df, llm_col="llm_label", human_col="human_label"):
        self.df = df
        self.llm_col = llm_col
        self.human_col = human_col

    def accuracy(self):
        return (self.df[self.llm_col] == self.df[self.human_col]).mean()

    def false_positive_rate(self):
        fp = (self.df[self.llm_col] == 1) & (self.df[self.human_col] == 0)
        return fp.mean()

    def false_negative_rate(self):
        fn = (self.df[self.llm_col] == 0) & (self.df[self.human_col] == 1)
        return fn.mean()

    def confusion_summary(self):
        return {
            "accuracy": self.accuracy(),
            "fp_rate": self.false_positive_rate(),
            "fn_rate": self.false_negative_rate()
        }

    def calibration_gap(self):
        """
        Difference between LLM confidence and actual correctness.
        """
        if "llm_confidence" not in self.df.columns:
            return None

        correctness = (self.df[self.llm_col] == self.df[self.human_col]).astype(int)
        return self.df["llm_confidence"].mean() - correctness.mean()
