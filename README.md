# Spotify 기반 한국 대중음악 분석

Spotify 데이터를 활용해서 한국어 대중음악의 음악적 특성과
Spotify 인기도 사이에 어떤 관계가 있는지 분석해봤습니다.

음악을 전공하면서 음악 데이터에 관심이 생겼고,
데이터 분석을 공부하면서 처음으로 진행해본 개인 프로젝트입니다.

## 분석 주제

- 인기 있는 한국어 노래는 어떤 음악적 특징을 가지고 있을까?
- 음악적 특성과 Spotify 인기도 사이에는 어떤 관계가 있을까?
- 음악적 특성만으로 인기곡과 비인기곡을 구분할 수 있을까?

## 데이터

Spotify에서 `Korean`으로 분류된 음악을 대상으로 분석했습니다.

- 기간: 2005 ~ 2024년
- 분석 데이터: 6,887곡

주요 음악적 특성으로 Danceability, Energy, Acousticness,
Instrumentalness, Liveness, Loudness, Speechiness,
Tempo, Valence 등을 사용했습니다.

## 분석 과정

1. 데이터 확인
2. 결측치 확인
3. 중복 데이터 확인
4. 이상값 확인 및 처리
5. 인기곡과 비인기곡 비교
6. 음악적 특성과 인기도의 상관관계 분석
7. 연도별 및 아티스트별 분석
8. Streamlit 대시보드 제작

## 인기곡과 비인기곡 비교

Popularity의 중앙값인 26을 기준으로 나누었습니다.

| 특성 | 인기곡 평균 | 비인기곡 평균 |
|---|---:|---:|
| Danceability | 0.656 | 0.623 |
| Energy | 0.772 | 0.746 |
| Acousticness | 0.147 | 0.195 |
| Instrumentalness | 0.022 | 0.094 |
| Liveness | 0.197 | 0.309 |
| Loudness | -4.394 | -5.980 |
| Speechiness | 0.094 | 0.099 |
| Tempo | 123.18 | 121.40 |
| Valence | 0.556 | 0.510 |

## 상관관계

Spotify popularity와 음악적 특성의 상관관계를 확인했습니다.

Loudness가 가장 높은 양의 상관관계를 보였으며,
Instrumentalness와 Liveness는 음의 상관관계를 보였습니다.

다만 상관관계가 전반적으로 크지는 않았기 때문에
음악적 특성만으로 Spotify 인기도를 설명하기에는 한계가 있었습니다.

## 사용한 기술

Python  
Pandas  
Matplotlib  
Streamlit  
Jupyter Notebook  
Git / GitHub

## 파일

- `real_analysis.ipynb` : 최종 분석
- `test_analysis.ipynb` : 초기 분석 및 테스트
- `app.py` : Streamlit 대시보드
- `spotify_data.csv` : 분석 데이터
- `requirements.txt` : 필요한 라이브러리

## 회고

데이터 분석을 배우면서 처음 진행해본 프로젝트입니다.

처음에는 데이터를 불러와서 그래프를 만드는 것만 생각했는데,
직접 분석해보면서 중복이나 이상값을 확인하고
분석 결과를 어떻게 해석해야 하는지도 중요하다는 것을 알게 되었습니다.

앞으로 데이터 분석을 더 공부하면서
이번 프로젝트에서 부족했던 부분도 하나씩 보완해보고 싶습니다.
