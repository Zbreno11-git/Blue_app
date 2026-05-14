import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Vitality Compass",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 Vitality Compass")
st.write("Measure your lifestyle vitality score based on health and longevity habits.")

st.divider()

st.header("👤 Personal Information")

name = st.text_input("Name")

age = st.slider("Age", 10, 100, 25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

city = st.text_input("City")

st.divider()

# =========================
# SLEEP & RECOVERY (25)
# =========================

st.header("😴 Sleep & Recovery")

sleep_hours = st.slider(
    "How many hours do you sleep per night?",
    0,
    12,
    7
)

sleep_quality = st.slider(
    "How would you rate your sleep quality?",
    1,
    10,
    7
)

# =========================
# PHYSICAL ACTIVITY (25)
# =========================

st.header("🏃 Physical Activity")

exercise_days = st.slider(
    "How many days per week do you exercise?",
    0,
    7,
    3
)

daily_steps = st.slider(
    "Average daily steps",
    0,
    20000,
    7000,
    step=500
)

sitting_hours = st.slider(
    "How many hours per day do you spend sitting?",
    0,
    16,
    6
)

# =========================
# NUTRITION (20)
# =========================

st.header("🥗 Nutrition")

vegetable_intake = st.slider(
    "How many servings of fruits/vegetables do you eat daily?",
    0,
    10,
    4
)

processed_food = st.slider(
    "How often do you eat ultra-processed foods?",
    0,
    10,
    5
)

water_intake = st.slider(
    "How many liters of water do you drink daily?",
    0,
    5,
    2
)

# =========================
# MENTAL WELLBEING (15)
# =========================

st.header("🧠 Mental Wellbeing")

stress_level = st.slider(
    "Stress level",
    1,
    10,
    5
)

social_connection = st.slider(
    "How connected do you feel socially?",
    1,
    10,
    6
)

sense_of_purpose = st.slider(
    "How strong is your sense of purpose?",
    1,
    10,
    6
)

# =========================
# LIFESTYLE RISKS (15)
# =========================

st.header("⚠ Lifestyle Risks")

smoking = st.selectbox(
    "Do you smoke?",
    ["Never", "Occasionally", "Frequently"]
)

alcohol = st.slider(
    "Alcohol consumption frequency",
    0,
    10,
    3
)

sunlight = st.slider(
    "Daily sunlight exposure (minutes)",
    0,
    180,
    30,
    step=10
)

st.divider()

# =========================
# SCORE CALCULATION
# =========================

sleep_score = 0
activity_score = 0
nutrition_score = 0
mental_score = 0
risk_score = 0

# =========================
# SLEEP SCORE (25)
# =========================

# Sleep hours
if 7 <= sleep_hours <= 9:
    sleep_score += 15
elif 6 <= sleep_hours < 7:
    sleep_score += 8
elif 5 <= sleep_hours < 6:
    sleep_score += 5
else:
    sleep_score -= 2

# Sleep quality
sleep_score += sleep_quality

# =========================
# ACTIVITY SCORE (25)
# =========================

# Exercise frequency

if 4 <= exercise_days <= 6:
    activity_score += 10
elif 2 <= exercise_days < 4:
    activity_score += 7
elif exercise_days == 7:
    activity_score += 8
elif exercise_days == 1:
    activity_score += 0
else:
    activity_score -= 3

if daily_steps >= 10000:
    activity_score += 10
elif daily_steps >= 7000:
    activity_score += 7
elif daily_steps >= 4000:
    activity_score += 5
else:
    activity_score -= 2

if sitting_hours <= 4:
    activity_score += 5
elif sitting_hours <= 8:
    activity_score += 3
else:
    activity_score -= 1

# =========================
# NUTRITION SCORE (20)
# =========================

# Vegetables / Fruits

if vegetable_intake >= 8:
    nutrition_score += 10
elif vegetable_intake >= 6:
    nutrition_score += 8
elif vegetable_intake >= 4:
    nutrition_score += 6
elif vegetable_intake >= 2:
    nutrition_score += 1
else:
    nutrition_score -= 1

# Ultra-processed foods

if processed_food <= 2:
    nutrition_score += 10
elif processed_food <= 4:
    nutrition_score += 7
elif processed_food <= 5:
    nutrition_score += 4
elif processed_food <= 7:
    nutrition_score += 0
else:
    nutrition_score -= 5

# Water intake

if water_intake >= 3:
    nutrition_score += 5
elif water_intake >= 2:
    nutrition_score += 4
else:
    nutrition_score += 0

nutrition_score = max(0, min(nutrition_score, 20))

# =========================
# MENTAL SCORE (15)
# =========================

# Stress (peso maior)

if stress_level <= 3:
    mental_score += 7
elif stress_level <= 5:
    mental_score += 5
elif stress_level <= 7:
    mental_score += 3
elif stress_level <= 8:
    mental_score += 1
else:
    mental_score -= 2

# Social connection

if social_connection >= 8:
    mental_score += 5
elif social_connection >= 6:
    mental_score += 3
elif social_connection >= 4:
    mental_score += 2
else:
    mental_score += 0

# Sense of purpose

if sense_of_purpose >= 8:
    mental_score += 5
elif sense_of_purpose >= 6:
    mental_score += 3
elif sense_of_purpose >= 4:
    mental_score += 2
else:
    mental_score += 0

# =========================
# RISK SCORE (15)
# =========================

if smoking == "Never":
    risk_score += 8
elif smoking == "Occasionally":
    risk_score += 0
else:
    risk_score -= 5

if alcohol <= 2:
    risk_score += 5
elif alcohol <= 5:
    risk_score += 1
elif alcohol <= 7:
    risk_score -= 1
else:
    risk_score -= 5

if 15 <= sunlight <= 60:
    risk_score += 3
elif 60 < sunlight <= 120:
    risk_score += 2
elif sunlight > 120:
    risk_score += 0
else:
    risk_score += 1

risk_score = round(risk_score)

# =========================
# TOTAL SCORE
# =========================

sleep_score = max(0, min(sleep_score, 25))
activity_score = max(0, min(activity_score, 25))
nutrition_score = max(0, min(nutrition_score, 20))
mental_score = max(0, min(round(mental_score), 15))
risk_score = max(0, min(risk_score, 15))

total_score = (
    sleep_score +
    activity_score +
    nutrition_score +
    mental_score +
    risk_score
)

# =========================
# CATEGORY
# =========================

if total_score < 50:
    category = "Poor Vitality"
elif total_score < 65:
    category = "Moderate Vitality"
elif total_score < 80:
    category = "Healthy"
else:
    category = "Optimal Vitality"

# =========================
# RESULTS
# =========================

st.header("📊 Results")

st.metric("# Vitality Score", f"{total_score}/100")

if total_score < 50:
    st.error(category)
elif total_score < 65:
    st.warning(category)
elif total_score < 80:
    st.info(category)
else:
    st.success(category)

st.write("### Category Breakdown")

st.write(f"😴 Sleep & Recovery: {sleep_score}/25")
st.write(f"🏃 Physical Activity: {activity_score}/25")
st.write(f"🥗 Nutrition: {nutrition_score}/20")
st.write(f"🧠 Mental Wellbeing: {mental_score}/15")
st.write(f"⚠ Lifestyle Risks: {risk_score}/15")

scores = {
    "Sleep & Recovery": sleep_score / 25,
    "Physical Activity": activity_score / 25,
    "Nutrition": nutrition_score / 20,
    "Mental Wellbeing": mental_score / 15,
    "Lifestyle Risks": risk_score / 15
}

lowest_area = min(scores, key=scores.get)

st.write(f"### Your biggest opportunity for improvement is:")
st.info(lowest_area)

if "submitted" not in st.session_state:
    st.session_state.submitted = False
submit = st.button(
    "Save My Results",
    disabled=st.session_state.submitted
)

import plotly.express as px
import pandas as pd

radar_df = pd.DataFrame({
    "Category": list(scores.keys()),
    "Score": [v * 100 for v in scores.values()]
})

fig = px.line_polar(
    radar_df,
    r="Score",
    theta="Category",
    line_close=True
)

fig.update_traces(
    fill='toself',
    fillcolor='rgba(30, 58, 95, 0.35)',
    line=dict(
        color='#1e3a5f',
        width=4
    )
)

fig.update_layout(
    polar=dict(
        bgcolor='rgba(0,0,0,0)',
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='rgba(30,58,95,0.2)',
            linecolor='rgba(30,58,95,0.4)',
            tickfont=dict(
                size=10,
                color='#1e3a5f'
            )
        ),
        angularaxis=dict(
            gridcolor='rgba(30,58,95,0.15)',
            linecolor='rgba(30,58,95,0.3)',
            tickfont=dict(
                size=13,
                color='#0f172a'
            )
        )
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

if submit:

    data = {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city,
        "sleep_hours": sleep_hours,
        "sleep_quality": sleep_quality,
        "exercise_days": exercise_days,
        "daily_steps": daily_steps,
        "sitting_hours": sitting_hours,
        "vegetable_intake": vegetable_intake,
        "processed_food": processed_food,
        "water_intake": water_intake,
        "stress_level": stress_level,
        "social_connection": social_connection,
        "sense_of_purpose": sense_of_purpose,
        "smoking": smoking,
        "alcohol": alcohol,
        "sunlight": sunlight,
        "total_score": total_score,
        "category": category
    }


    supabase.table("responses").insert(data).execute()


    st.session_state.submitted = True

    st.success("Results saved successfully.")
