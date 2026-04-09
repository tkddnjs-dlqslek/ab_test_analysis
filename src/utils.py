"""공통 유틸리티"""
import numpy as np
import pandas as pd
from scipy import stats


def z_test_proportions(n1, p1, n2, p2):
    """두 비율의 z-검정 (A/B 전환율 비교)"""
    p_pool = (n1 * p1 + n2 * p2) / (n1 + n2)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z = (p1 - p2) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value


def bootstrap_ci(data, stat_func=np.mean, n_bootstrap=10000, ci=0.95, seed=42):
    """Bootstrap 신뢰구간"""
    rng = np.random.RandomState(seed)
    boot_stats = []
    n = len(data)
    for _ in range(n_bootstrap):
        sample = rng.choice(data, size=n, replace=True)
        boot_stats.append(stat_func(sample))
    alpha = (1 - ci) / 2
    lower = np.percentile(boot_stats, alpha * 100)
    upper = np.percentile(boot_stats, (1 - alpha) * 100)
    return lower, upper


def srm_test(n_control, n_treatment, expected_ratio=None):
    """Sample Ratio Mismatch 검정"""
    total = n_control + n_treatment
    if expected_ratio is None:
        expected_ratio = n_control / total
    expected_control = total * expected_ratio
    expected_treatment = total * (1 - expected_ratio)
    chi2, p_value = stats.chisquare(
        [n_control, n_treatment],
        [expected_control, expected_treatment]
    )
    return chi2, p_value


def cohens_d(group1, group2):
    """Cohen's d 효과 크기"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std


def shannon_entropy(distribution):
    """Shannon Entropy (다양성 측정)"""
    p = np.array(distribution, dtype=float)
    p = p[p > 0]
    p = p / p.sum()
    return -np.sum(p * np.log2(p))


def gini_index(distribution):
    """Gini Index (불균등도 측정)"""
    arr = np.sort(np.array(distribution, dtype=float))
    n = len(arr)
    index = np.arange(1, n + 1)
    return (2 * np.sum(index * arr) - (n + 1) * np.sum(arr)) / (n * np.sum(arr))
