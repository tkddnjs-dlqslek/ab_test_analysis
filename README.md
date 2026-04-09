# 추천 알고리즘의 인과적 효과 분석

**Counterfactual Evaluation of Recommendation Algorithms**

Kuaishou(쾌수, 중국 숏폼 영상 플랫폼)의 공개 데이터셋 2종을 활용하여,
추천 알고리즘이 유저 행동과 콘텐츠 다양성에 미치는 **인과적 효과**를 분석한 프로젝트입니다.

## 핵심 결론

> **추천 알고리즘은 CTR을 153% 올리지만, 92.4%의 유저에서 콘텐츠 다양성을 감소시킨다.**

| 분석 영역 | 핵심 결론 | 수치 근거 |
|-----------|----------|----------|
| A/B 테스트 | 모든 참여 지표 유의하게 향상 | CTR +153%, 좋아요 +269%, 댓글 +610% |
| 인과추론 | 거의 모든 유저에게 양(+)의 효과 | CATE > 0인 유저 99.3%, ATT = 0.263 |
| OPE | Direct Method 추정량이 가장 정확 | DM 오차 0.2%, IPS 92%, SNIPS 12% |
| 필터버블 | 콘텐츠 다양성 체계적 감소 | 92.4% 유저 Shannon Entropy 하락 |

## 분석 파이프라인

```
01_eda.ipynb              → 탐색적 데이터 분석 (12개 피드백 비교, 유저 특성)
    ↓
02_ab_test_basic.ipynb    → A/B 테스트 (z-test, Bootstrap CI, SRM, Power Analysis)
    ↓
03_causal_inference.ipynb → 인과추론 (PSM, T-Learner CATE, Uplift 4분면)
    ↓
04_ope.ipynb              → Off-Policy Evaluation (DM, IPS, SNIPS vs Ground Truth)
    ↓
05_filter_bubble.ipynb    → 필터버블 (Entropy, Gini, Long Tail, 시계열)
    ↓
06_final_report.ipynb     → 종합 리포트 + 비즈니스 제안
```

## 주요 분석 결과

### 1. A/B 테스트

| 지표 | Control | Treatment | Lift | p-value |
|------|---------|-----------|------|---------|
| CTR | 0.176 | 0.445 | +153% | < 1e-300 |
| 좋아요 | 0.005 | 0.018 | +269% | < 1e-300 |
| 팔로우 | 0.0003 | 0.0013 | +410% | < 1e-300 |
| 댓글 | 0.0003 | 0.0025 | +610% | < 1e-300 |
| 싫어요 | 0.0011 | 0.0008 | -32% | 7.7e-08 |

- Bonferroni 보정 후 7개 지표 모두 유의
- Cohen's d = 0.578 (중간 효과), Power = 100%

### 2. 인과추론

- **PSM**: Caliper=0.05, 매칭률 100%, 매칭 후 모든 SMD < 0.1
- **ATT(CTR)**: 0.263 (나이브 대비 +5.2%)
- **CATE**: 99.3% 유저 양의 효과, 핵심 변수 — 가입일수(34%), 팔로잉(20%), 팬수(20%)

### 3. Off-Policy Evaluation

| 정책 | Ground Truth | DM 오차 | SNIPS 오차 |
|------|-------------|---------|-----------|
| Popular | 0.662 | 0.00% | 13.3% |
| UserCF | 0.791 | 0.00% | 12.4% |
| Blend | 0.834 | 0.24% | 9.9% |

### 4. 필터버블

| 지표 | Random | Recommended | 변화 |
|------|--------|------------|------|
| Shannon Entropy | 5.147 | 4.723 | -8.2% |
| Gini Index | 0.758 | 0.809 | +6.7% |
| 80% 커버리지 | 상위 75% 영상 | 상위 23% 영상 | 극단적 편중 |

## 비즈니스 제안

1. **유저 세그먼트별 차별화**: Persuadables에 집중 추천, Sleeping Dogs에 랜덤 확대
2. **다양성 메커니즘**: 카테고리 쿼터제, Long Tail 부스팅, 탐색 비율 세그먼트별 차등
3. **OPE 활용**: 새 알고리즘 배포 전 DM으로 사전 평가, 정기 랜덤 실험 유지

## 데이터셋

| 데이터셋 | 용도 | 규모 |
|---------|------|------|
| [KuaiRand-Pure](https://zenodo.org/records/12600781) | Treatment/Control 실험 | 1,481,556 상호작용 |
| [KuaiRec 2.0](https://zenodo.org/records/12594951) | Ground Truth (완전관측) | 4,676,570 상호작용, 관측 밀도 99.6% |

> 데이터 파일은 용량 문제로 레포에 포함되어 있지 않습니다. 위 링크에서 다운로드 후 `data/` 폴더에 배치하세요.

## 기술 스택

| 구분 | 도구 |
|------|------|
| 언어 | Python 3.10+ |
| 통계 | scipy, statsmodels |
| ML | scikit-learn, surprise |
| 인과추론 | econml, causalml, scikit-uplift |
| 시각화 | matplotlib, seaborn, plotly |

## 프로젝트 구조

```
ab_test_analysis/
├── data/
│   ├── kuairec/          # KuaiRec 2.0
│   └── kuairand/         # KuaiRand-Pure
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_ab_test_basic.ipynb
│   ├── 03_causal_inference.ipynb
│   ├── 04_ope.ipynb
│   ├── 05_filter_bubble.ipynb
│   ├── 06_final_report.ipynb
│   └── figures/           # 시각화 24장
├── src/
│   ├── data_loader.py
│   └── utils.py
├── requirements.txt
└── PROJECT_EXPLANATION.md  # 상세 설명 문서
```

## 참고 논문

- Gao et al. (2022) "KuaiRec: A Fully-observed Dataset" (CIKM 2022)
- Gao et al. (2022) "KuaiRand: An Unbiased Sequential Recommendation Dataset" (CIKM 2022)
