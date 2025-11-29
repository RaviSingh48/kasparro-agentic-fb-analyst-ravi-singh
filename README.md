# Kasparro Agentic FB Analyst – Ravi Singh

## Overview
This project implements an agentic pipeline (planner → data → insight → evaluator → creative generator)
for synthetic Facebook ads dataset (undergarments). Run locally to generate `insights.json`, `creatives.json`, and `report.md`.

## Quick start
1. Place `synthetic_fb_ads_undergarments.csv` inside the `data/` folder (you already did).
2. Create and activate a venv, install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```bash
   python run.py --data data/synthetic_fb_ads_undergarments.csv --out reports/
   ```
4. Outputs:
   - `reports/insights.json`
   - `reports/creatives.json`
   - `reports/report.md`
