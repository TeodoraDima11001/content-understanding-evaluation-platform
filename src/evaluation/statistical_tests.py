import numpy as np

def bootstrap_ci(data, metric_fn, n_boot=1000, alpha=0.05):
    """
    Bootstrap confidence interval for any metric.
    Used for evaluation uncertainty in content systems.
    """

    stats = []

    for _ in range(n_boot):
        sample = np.random.choice(data, size=len(data), replace=True)
        stats.append(metric_fn(sample))

    lower = np.percentile(stats, 100 * alpha / 2)
    upper = np.percentile(stats, 100 * (1 - alpha / 2))

    return lower, upper


def ab_test_difference(group_a, group_b):
    """
    Simple A/B test difference in means.
    """

    return np.mean(group_b) - np.mean(group_a)
