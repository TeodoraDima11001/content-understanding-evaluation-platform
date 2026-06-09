import numpy as np


class DecisionIntelligenceEngine:
    """
    Converts metrics into product decisions (Spotify DS II level thinking).

    This is the missing layer between:
    - analytics
    - and real product decisions
    """

    def __init__(self, baseline_metrics, experiment_metrics):
        self.baseline = baseline_metrics
        self.experiment = experiment_metrics

    def delta(self, metric):
        return self.experiment[metric] - self.baseline[metric]

    def risk_score(self):
        """
        Measures downside risk across key sensitive metrics.
        """
        risks = [
            abs(self.delta("misclassification_rate")),
            abs(self.delta("low_confidence_rate")),
            abs(self.delta("taxonomy_inconsistency")),
        ]
        return np.mean(risks)

    def decision(self):
        """
        Final Spotify-style decision logic:
        NOT just "better model wins".
        """

        engagement_gain = self.delta("engagement_rate")
        quality_gain = self.delta("annotation_quality")

        risk = self.risk_score()

        # decision logic (this is what interviewers care about)

        if engagement_gain > 0 and quality_gain > 0 and risk < 0.02:
            return "SHIP"

        if engagement_gain > 0 and quality_gain < 0:
            return "SHIP_WITH_RISK_FLAG"

        if engagement_gain < 0 and quality_gain > 0:
            return "DO_NOT_SHIP"

        return "NEEDS_FURTHER_ANALYSIS"

    def explanation(self):
        return {
            "engagement_delta": self.delta("engagement_rate"),
            "quality_delta": self.delta("annotation_quality"),
            "risk_score": self.risk_score(),
            "decision": self.decision()
        }
