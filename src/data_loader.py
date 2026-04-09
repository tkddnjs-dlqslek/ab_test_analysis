"""KuaiRec & KuaiRand 데이터 로더"""
import os
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def load_kuairec_small_matrix():
    """KuaiRec 소규모 완전관측 행렬 (1,411 users x 3,327 videos)"""
    path = DATA_DIR / "kuairec" / "KuaiRec 2.0" / "data" / "small_matrix.csv"
    df = pd.read_csv(path)
    return df


def load_kuairec_big_matrix():
    """KuaiRec 대규모 행렬 (일반 추천 로그)"""
    path = DATA_DIR / "kuairec" / "KuaiRec 2.0" / "data" / "big_matrix.csv"
    df = pd.read_csv(path)
    return df


def load_kuairec_user_features():
    """KuaiRec 유저 특성"""
    path = DATA_DIR / "kuairec" / "KuaiRec 2.0" / "data" / "user_features.csv"
    df = pd.read_csv(path)
    return df


def load_kuairec_item_categories():
    """KuaiRec 아이템 카테고리"""
    path = DATA_DIR / "kuairec" / "KuaiRec 2.0" / "data" / "item_categories.csv"
    df = pd.read_csv(path)
    return df


def load_kuairec_item_daily_features():
    """KuaiRec 아이템 일별 특성"""
    path = DATA_DIR / "kuairec" / "KuaiRec 2.0" / "data" / "item_daily_features.csv"
    df = pd.read_csv(path)
    return df


def load_kuairand_log_random():
    """KuaiRand 랜덤 노출 로그 (Control group)"""
    path = DATA_DIR / "kuairand" / "KuaiRand-Pure" / "data" / "log_random_4_22_to_5_08_pure.csv"
    df = pd.read_csv(path)
    return df


def load_kuairand_log_standard():
    """KuaiRand 표준 추천 로그 (Treatment group)"""
    path = DATA_DIR / "kuairand" / "KuaiRand-Pure" / "data" / "log_standard_4_08_to_4_21_pure.csv"
    df = pd.read_csv(path)
    return df


def load_kuairand_user_features():
    """KuaiRand 유저 특성"""
    path = DATA_DIR / "kuairand" / "KuaiRand-Pure" / "data" / "user_features_pure.csv"
    df = pd.read_csv(path)
    return df


def load_kuairand_video_features_basic():
    """KuaiRand 비디오 기본 특성"""
    path = DATA_DIR / "kuairand" / "KuaiRand-Pure" / "data" / "video_features_basic_pure.csv"
    df = pd.read_csv(path)
    return df


def load_kuairand_video_features_statistic():
    """KuaiRand 비디오 통계 특성"""
    path = DATA_DIR / "kuairand" / "KuaiRand-Pure" / "data" / "video_features_statistic_pure.csv"
    df = pd.read_csv(path)
    return df


def discover_files(dataset="kuairec"):
    """데이터셋 내 모든 CSV 파일 탐색"""
    dataset_dir = DATA_DIR / dataset
    files = list(dataset_dir.rglob("*.csv"))
    for f in sorted(files):
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"  {f.relative_to(dataset_dir)} ({size_mb:.1f} MB)")
    return files
