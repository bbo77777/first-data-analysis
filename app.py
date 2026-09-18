import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.family"] = "Malgun Gothic"
mpl.rcParams["axes.unicode_minus"] = False

st.set_page_config(
    page_title="한국 대중음악 분석",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

GREEN = "#1ED760"
MINT = "#4DFF91"
BRIGHT = "#7CFFB2"
DARK_GREEN = "#00A957"
LIGHT_GREEN = "#9AFFC1"
BG = "#07110D"
CARD = "#0D1B15"
CARD2 = "#10251B"
TEXT = "#F3FFF7"
MUTED = "#B8D8C4"

st.markdown(
    f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        background: {BG} !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background:
            radial-gradient(circle at 10% 5%, rgba(30,215,96,0.12), transparent 22%),
            radial-gradient(circle at 90% 10%, rgba(77,255,145,0.08), transparent 22%),
            {BG};
    }}

    header[data-testid="stHeader"] {{
        background: transparent !important;
        height: 0 !important;
    }}

    [data-testid="stDecoration"] {{
        display: none !important;
    }}

    [data-testid="stToolbar"] {{
        background: transparent !important;
    }}

    [data-testid="stAppViewBlockContainer"] {{
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }}

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #06100C 0%, #0A1811 100%);
        border-right: 1px solid rgba(30,215,96,0.25);
        min-width: 270px;
    }}

    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 2rem;
    }}

    [data-testid="stSidebar"] * {{
        color: {TEXT};
    }}

    [data-testid="stSidebarCollapseButton"] {{
        position: absolute !important;
        top: 14px !important;
        right: 12px !important;
    }}

    [data-testid="stSidebarCollapseButton"] button {{
        width: 36px !important;
        height: 36px !important;
        border-radius: 12px !important;
        background: rgba(30,215,96,0.12) !important;
        border: 1px solid rgba(77,255,145,0.55) !important;
        color: {BRIGHT} !important;
        box-shadow: 0 0 18px rgba(30,215,96,0.18) !important;
        transition: all 0.25s ease !important;
    }}

    [data-testid="stSidebarCollapseButton"] button:hover {{
        background: rgba(30,215,96,0.28) !important;
        border-color: {GREEN} !important;
        box-shadow: 0 0 25px rgba(30,215,96,0.40) !important;
        transform: scale(1.05);
    }}

    [data-testid="stSidebarCollapseButton"] svg {{
        color: {BRIGHT} !important;
        fill: {BRIGHT} !important;
        stroke: {BRIGHT} !important;
    }}

    [data-testid="stMetric"] {{
        background: linear-gradient(145deg, {CARD2}, {CARD});
        border: 1px solid rgba(30,215,96,0.25);
        border-radius: 22px;
        padding: 17px 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.20);
        transition: all 0.25s ease;
    }}

    [data-testid="stMetric"]:hover {{
        transform: translateY(-3px);
        border-color: rgba(77,255,145,0.65);
        box-shadow: 0 10px 30px rgba(30,215,96,0.15);
    }}

    [data-testid="stMetricLabel"] {{
        color: {MUTED} !important;
    }}

    [data-testid="stMetricValue"] {{
        color: {BRIGHT} !important;
        font-size: 25px !important;
        text-shadow: 0 0 12px rgba(30,215,96,0.25);
    }}

    .title {{
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin-bottom: 3px;
        background: linear-gradient(90deg, #FFFFFF, {GREEN}, {LIGHT_GREEN});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .subtitle {{
        color: {MUTED};
        font-size: 14px;
        margin-bottom: 20px;
    }}

    .section-title {{
        font-size: 24px;
        font-weight: 750;
        margin-top: 20px;
        margin-bottom: 13px;
        color: #FFFFFF !important;
        text-shadow: 0 0 12px rgba(30,215,96,0.12);
    }}

    .info-card {{
        background: linear-gradient(
            145deg,
            rgba(16,37,27,0.98),
            rgba(9,24,16,0.98)
        );
        border: 1px solid rgba(77,255,145,0.25);
        border-radius: 22px;
        padding: 20px 22px;
        margin: 12px 0 18px 0;
        box-shadow:
            0 10px 28px rgba(0,0,0,0.18),
            0 0 18px rgba(30,215,96,0.04);
        color: #F3FFF7 !important;
    }}

    .info-card b {{
        color: {BRIGHT} !important;
    }}

    .glow {{
        color: {BRIGHT} !important;
        font-weight: 800;
        text-shadow: 0 0 12px rgba(30,215,96,0.25);
    }}

    [data-testid="stSidebar"] .stSelectbox > div > div {{
        background: {CARD};
        border: 1px solid rgba(30,215,96,0.35);
        border-radius: 16px;
        transition: all 0.25s ease;
        box-shadow: 0 0 18px rgba(30,215,96,0.05);
    }}

    [data-testid="stSidebar"] .stSelectbox > div > div:hover {{
        border-color: {GREEN};
        box-shadow: 0 0 22px rgba(30,215,96,0.22);
    }}

    .stSelectbox > div > div {{
        border-radius: 16px;
        background: {CARD};
        border: 1px solid rgba(30,215,96,0.30);
    }}

    .stSelectbox > div > div:hover {{
        border-color: {GREEN};
        box-shadow: 0 0 18px rgba(30,215,96,0.16);
    }}

    [data-testid="stDataFrame"] {{
        border-radius: 20px !important;
        overflow: hidden !important;
        border: 1px solid rgba(30,215,96,0.25) !important;
        box-shadow: 0 10px 28px rgba(0,0,0,0.18) !important;
    }}

    .custom-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        overflow: hidden;
        border-radius: 18px;
        border: 1px solid rgba(77,255,145,0.28);
        background: linear-gradient(145deg, #10251B, #0B1912);
        box-shadow: 0 10px 28px rgba(0,0,0,0.20);
        color: #F3FFF7;
        font-size: 14px;
    }}

    .custom-table th {{
        background: linear-gradient(135deg, #0B8F47, #0E6E3A);
        color: #FFFFFF !important;
        font-weight: 800;
        padding: 13px 15px;
        text-align: center;
        border-bottom: 1px solid rgba(154,255,193,0.35);
    }}

    .custom-table td {{
        padding: 12px 15px;
        text-align: center;
        color: #E8FFF0 !important;
        border-bottom: 1px solid rgba(77,255,145,0.10);
    }}

    .custom-table tr:last-child td {{
        border-bottom: none;
    }}

    .custom-table tr:hover td {{
        background: rgba(30,215,96,0.10);
        color: #FFFFFF !important;
    }}

    .custom-table td:first-child {{
        color: {BRIGHT} !important;
        font-weight: 700;
    }}

    .chart-box {{
        background: linear-gradient(
            145deg,
            rgba(13,27,21,0.98),
            rgba(8,20,14,0.98)
        );
        border: 1px solid rgba(77,255,145,0.18);
        border-radius: 24px;
        padding: 10px 15px 5px 15px;
        box-shadow:
            0 12px 30px rgba(0,0,0,0.20),
            0 0 20px rgba(30,215,96,0.03);
    }}

    h1, h2, h3 {{
        color: #FFFFFF !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def show_table(data):
    table_data = data.copy()

    html = '<table class="custom-table"><thead><tr>'

    for col in table_data.columns:
        html += f"<th>{col}</th>"

    html += "</tr></thead><tbody>"

    for _, row in table_data.iterrows():
        html += "<tr>"

        for value in row:
            if isinstance(value, float):
                value = f"{value:.3f}"
            html += f"<td>{value}</td>"

        html += "</tr>"

    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)


df = pd.read_csv("spotify_tracks.csv")

analysis_df = df[
    (df["language"] == "Korean") &
    (df["danceability"] != -1) &
    (df["energy"] != -1) &
    (df["tempo"] != -1) &
    (df["valence"] != -1)
].copy()

popularity_median = analysis_df["popularity"].median()

analysis_df["popularity_group"] = analysis_df["popularity"].apply(
    lambda x: "인기곡" if x >= popularity_median else "비인기곡"
)

with st.sidebar:
    st.markdown(
        f"""
        <div style="
            padding:4px 5px 24px 5px;
            border-bottom:1px solid rgba(77,255,145,0.15);
            margin-bottom:22px;
        ">
            <div style="
                font-size:28px;
                font-weight:800;
                color:{BRIGHT};
                letter-spacing:-1px;
                text-shadow:0 0 15px rgba(30,215,96,0.25);
            ">
                🎧 BBO Music
            </div>
            <div style="
                font-size:13px;
                color:{MUTED};
                margin-top:5px;
            ">
                First Data Analysis Project
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            font-size:12px;
            color:{BRIGHT};
            font-weight:800;
            margin-bottom:8px;
        ">
            MENU
        </div>
        """,
        unsafe_allow_html=True
    )

    menu = st.selectbox(
        "메뉴",
        [
            "🏠 Overview",
            "인기곡 분석",
            "상관관계 분석",
            "음악적 특성",
            "🏆 인기곡 TOP 5",
            "연도별 분석"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        "<div style='height:22px'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            font-size:12px;
            color:{BRIGHT};
            font-weight:800;
            margin-bottom:8px;
        ">
            FILTER
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_year = st.selectbox(
        "연도",
        ["전체"] + sorted(
            analysis_df["year"].unique().tolist(),
            reverse=True
        ),
        label_visibility="collapsed"
    )

    selected_group = st.selectbox(
        "인기도",
        ["전체", "인기곡", "비인기곡"],
        label_visibility="collapsed"
    )

    st.markdown(
        f"""
        <div style="
            margin-top:30px;
            padding:16px;
            border-radius:18px;
            background:rgba(30,215,96,0.06);
            border:1px solid rgba(77,255,145,0.16);
            box-shadow:0 0 20px rgba(30,215,96,0.04);
        ">
            <div style="
                font-size:11px;
                color:{MUTED};
            ">
                DATASET
            </div>
            <div style="
                font-size:22px;
                font-weight:800;
                color:{BRIGHT};
                margin-top:4px;
            ">
                6,887
            </div>
            <div style="
                font-size:11px;
                color:{MUTED};
            ">
                Korean tracks
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

filtered_df = analysis_df.copy()

if selected_year != "전체":
    filtered_df = filtered_df[
        filtered_df["year"] == selected_year
    ]

if selected_group != "전체":
    filtered_df = filtered_df[
        filtered_df["popularity_group"] == selected_group
    ]

st.markdown(
    '<div class="title">Spotify 기반 한국 대중음악 분석</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">한국어 대중음악의 음악적 특성과 Spotify 인기도의 관계 분석</div>',
    unsafe_allow_html=True
)

if menu == "🏠 Overview":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("분석 곡 수", f"{len(filtered_df):,}")
    col2.metric("평균 인기도", f"{filtered_df['popularity'].mean():.1f}")
    col3.metric("Danceability", f"{filtered_df['danceability'].mean():.3f}")
    col4.metric("Energy", f"{filtered_df['energy'].mean():.3f}")

    st.markdown(
        '<div class="section-title">인기곡과 비인기곡</div>',
        unsafe_allow_html=True
    )

    group_mean = filtered_df.groupby("popularity_group")[
        [
            "danceability",
            "energy",
            "acousticness",
            "instrumentalness",
            "liveness",
            "speechiness",
            "valence"
        ]
    ].mean()

    group_mean = group_mean.rename(
        columns={
            "danceability": "Danceability",
            "energy": "Energy",
            "acousticness": "Acousticness",
            "instrumentalness": "Instrumentalness",
            "liveness": "Liveness",
            "speechiness": "Speechiness",
            "valence": "Valence"
        }
    )

    chart_col = st.columns([0.18, 0.64, 0.18])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(7.2, 3.4))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        group_mean.T.plot(
            kind="bar",
            ax=ax,
            color=[DARK_GREEN, GREEN],
            width=0.62
        )

        ax.set_ylim(0, 1)

        ax.tick_params(
            colors=MUTED,
            labelsize=8
        )

        ax.set_xlabel("")

        ax.set_ylabel(
            "평균값",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            axis="y",
            alpha=0.09,
            color="white"
        )

        ax.legend(
            facecolor=CARD,
            edgecolor="none",
            labelcolor=TEXT,
            frameon=False,
            fontsize=8
        )

        plt.xticks(rotation=25)

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="info-card">
            <span class="glow">분석 요약</span><br><br>
            인기곡은 비인기곡에 비해 평균적으로
            <b>Danceability, Energy, Valence</b>가 높게 나타났습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

elif menu == "인기곡 분석":

    st.markdown(
        '<div class="section-title">인기곡 분석</div>',
        unsafe_allow_html=True
    )

    popularity_stats = filtered_df.groupby(
        "popularity_group"
    ).agg(
        곡수=("track_id", "count"),
        평균인기도=("popularity", "mean"),
        평균Danceability=("danceability", "mean"),
        평균Energy=("energy", "mean"),
        평균Valence=("valence", "mean")
    ).round(3)

    show_table(popularity_stats)

    feature = st.selectbox(
        "비교할 음악 특성",
        [
            "danceability",
            "energy",
            "acousticness",
            "instrumentalness",
            "liveness",
            "loudness",
            "speechiness",
            "tempo",
            "valence"
        ]
    )

    feature_mean = filtered_df.groupby(
        "popularity_group"
    )[feature].mean()

    chart_col = st.columns([0.22, 0.56, 0.22])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(6.2, 3.3))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        bars = ax.bar(
            feature_mean.index,
            feature_mean.values,
            width=0.42,
            color=[DARK_GREEN, GREEN]
        )

        ax.set_ylabel(
            "평균값",
            color=MUTED,
            fontsize=8
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            axis="y",
            alpha=0.09,
            color="white"
        )

        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f"{bar.get_height():.3f}",
                ha="center",
                va="bottom",
                color=TEXT,
                fontsize=9
            )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

elif menu == "상관관계 분석":

    st.markdown(
        '<div class="section-title">음악적 특성과 인기도</div>',
        unsafe_allow_html=True
    )

    corr_data = analysis_df[
        [
            "popularity",
            "danceability",
            "energy",
            "acousticness",
            "instrumentalness",
            "liveness",
            "loudness",
            "speechiness",
            "tempo",
            "valence"
        ]
    ].corr()

    popularity_corr = corr_data[
        "popularity"
    ].drop("popularity").sort_values()

    chart_col = st.columns([0.18, 0.64, 0.18])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(7.2, 4.2))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        bars = ax.barh(
            popularity_corr.index,
            popularity_corr.values,
            color=[
                DARK_GREEN if x < 0 else GREEN
                for x in popularity_corr.values
            ],
            height=0.48
        )

        ax.axvline(
            0,
            color="white",
            linewidth=0.7,
            alpha=0.25
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=7
        )

        ax.set_xlabel(
            "상관계수",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            axis="x",
            alpha=0.09,
            color="white"
        )

        for bar, value in zip(
            bars,
            popularity_corr.values
        ):
            ax.text(
                value + (0.008 if value >= 0 else -0.008),
                bar.get_y() + bar.get_height() / 2,
                f"{value:.3f}",
                va="center",
                ha="left" if value >= 0 else "right",
                color=TEXT,
                fontsize=8
            )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="info-card">
            <span class="glow">분석 요약</span><br><br>
            Loudness와 Spotify 인기도의 상관계수는 약
            <b>0.347</b>로 가장 높은 양의 상관관계를 보였습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

elif menu == "음악적 특성":

    st.markdown(
        '<div class="section-title">🎧 음악적 특성 분포</div>',
        unsafe_allow_html=True
    )

    feature = st.selectbox(
        "음악 특성 선택",
        [
            "danceability",
            "energy",
            "acousticness",
            "instrumentalness",
            "liveness",
            "loudness",
            "speechiness",
            "tempo",
            "valence"
        ]
    )

    chart_col = st.columns([0.18, 0.64, 0.18])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(7.2, 3.5))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        ax.hist(
            filtered_df[feature],
            bins=30,
            color=GREEN,
            alpha=0.78,
            edgecolor="none"
        )

        ax.axvline(
            filtered_df[feature].mean(),
            color=LIGHT_GREEN,
            linestyle="--",
            linewidth=1.7
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=7
        )

        ax.set_xlabel(
            feature,
            color=MUTED,
            fontsize=8
        )

        ax.set_ylabel(
            "곡 수",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            axis="y",
            alpha=0.09,
            color="white"
        )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

elif menu == "🏆 인기곡 TOP 5":

    st.markdown(
        '<div class="section-title">🏆 인기 아티스트 TOP 5</div>',
        unsafe_allow_html=True
    )

    artist_count = filtered_df.groupby(
        "artist_name"
    ).size()

    artist_5plus = artist_count[
        artist_count >= 5
    ].index

    artist_df = filtered_df[
        filtered_df["artist_name"].isin(
            artist_5plus
        )
    ].copy()

    artist_popularity = (
        artist_df.groupby("artist_name")["popularity"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    chart_col = st.columns([0.18, 0.64, 0.18])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(7.2, 3.5))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        bars = ax.barh(
            artist_popularity.index[::-1],
            artist_popularity.values[::-1],
            color=GREEN,
            height=0.42
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=8
        )

        ax.set_xlabel(
            "평균 Spotify 인기도",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            axis="x",
            alpha=0.09,
            color="white"
        )

        for bar, value in zip(
            bars,
            artist_popularity.values[::-1]
        ):
            ax.text(
                value + 0.7,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}",
                va="center",
                color=TEXT,
                fontsize=8
            )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    artist_table = artist_popularity.rename(
        "평균 Spotify 인기도"
    ).reset_index()

    show_table(artist_table)

elif menu == "연도별 분석":

    st.markdown(
        '<div class="section-title">📈 연도별 Spotify 인기도</div>',
        unsafe_allow_html=True
    )

    year_popularity = (
        analysis_df.groupby("year")["popularity"]
        .mean()
    )

    chart_col = st.columns([0.15, 0.70, 0.15])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(8, 3.5))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        ax.plot(
            year_popularity.index,
            year_popularity.values,
            marker="o",
            linewidth=2.1,
            markersize=3.5,
            color=GREEN
        )

        ax.fill_between(
            year_popularity.index,
            year_popularity.values,
            alpha=0.09,
            color=GREEN
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=7
        )

        ax.set_xlabel(
            "연도",
            color=MUTED,
            fontsize=8
        )

        ax.set_ylabel(
            "평균 Spotify 인기도",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            alpha=0.09,
            color="white"
        )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    year_group = (
        analysis_df.groupby(
            ["year", "popularity_group"]
        )
        .size()
        .unstack(fill_value=0)
    )

    chart_col = st.columns([0.15, 0.70, 0.15])[1]

    with chart_col:
        st.markdown(
            '<div class="chart-box">',
            unsafe_allow_html=True
        )

        fig, ax = plt.subplots(figsize=(8, 3.5))

        fig.patch.set_facecolor(CARD)
        ax.set_facecolor(CARD)

        year_group.plot(
            kind="area",
            stacked=True,
            ax=ax,
            color=[DARK_GREEN, GREEN],
            alpha=0.70
        )

        ax.tick_params(
            colors=MUTED,
            labelsize=7
        )

        ax.set_xlabel(
            "연도",
            color=MUTED,
            fontsize=8
        )

        ax.set_ylabel(
            "곡 수",
            color=MUTED,
            fontsize=8
        )

        ax.spines[
            ["top", "right", "left", "bottom"]
        ].set_visible(False)

        ax.grid(
            alpha=0.09,
            color="white"
        )

        ax.legend(
            facecolor=CARD,
            edgecolor="none",
            labelcolor=TEXT,
            frameon=False,
            fontsize=8
        )

        plt.tight_layout(pad=1)

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

st.markdown(
    f"""
    <div style="
        text-align:center;
        margin-top:25px;
        padding:16px;
        color:{MUTED};
        font-size:11px;
    ">
        🎧 Korean Music Analytics · Spotify Music Data
    </div>
    """,
    unsafe_allow_html=True
)