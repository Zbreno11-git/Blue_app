# 🧭 Vitality Compass

A health and longevity scoring platform inspired by Blue Zones research and evidence-based lifestyle factors.

Live App:  
[Vitality Compass Demo](https://vitality-compass-demo.streamlit.app)

---

## Overview

Vitality Compass is an interactive health analytics application designed to evaluate lifestyle habits and generate a personalized vitality score based on:

- Sleep & recovery
- Physical activity
- Nutrition quality
- Mental wellbeing
- Longevity risk factors

The goal of the project is not only to create a user-facing health scoring experience, but also to build a structured dataset for future analytics and machine learning applications using Supabase.

---

# Features

- Interactive health questionnaire
- Weighted vitality scoring system
- Nonlinear health/risk logic
- Dynamic vitality categories
- Radar chart visualization using Plotly
- Cloud database persistence with Supabase
- Responsive Streamlit interface
- Evidence-inspired scoring logic based on longevity research

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Frontend / Web app |
| Plotly | Interactive radar charts |
| Supabase | Cloud PostgreSQL database |
| Pandas | Data handling & analytics |
| GitHub | Version control |
| Streamlit Cloud | Deployment |

---

# Scoring Model

The scoring system was intentionally designed with weighted categories and nonlinear penalties/rewards to better reflect real-world health outcomes.

Example concepts used:
- Ultra-processed food penalties
- Sleep optimization ranges
- Stress weighting
- Lifestyle risk scaling
- Balanced vitality dimensions

Final scores are categorized into:
- Poor Vitality
- Moderate Vitality
- Healthy
- Optimal Vitality

---

# Future Analytics Vision

One of the main objectives of this project is long-term health data analysis.

All responses are stored in Supabase and can later be used for:
- Population-level health insights
- Behavioral clustering
- Correlation analysis
- Predictive health modeling
- ML classification/regression experiments
- Public dashboard analytics

Potential future features:
- Personalized recommendations
- Historical user tracking
- Community vitality benchmarks
- ML-powered vitality prediction
- Health trend visualization

---

# Screenshots

## Homepage / Questionnaire

[ INSERT SCREENSHOT HERE ]

---

## Radar Chart & Results

[ INSERT SCREENSHOT HERE ]

---

# Architecture

```text
Streamlit UI
     ↓
Scoring Engine (Python)
     ↓
Radar Visualization (Plotly)
     ↓
Supabase PostgreSQL Database
     ↓
Future Analytics / ML Pipeline
