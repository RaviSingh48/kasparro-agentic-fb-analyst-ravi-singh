# 🚀 Kasparro Agentic FB Analyst — Ravi Singh

This repository contains my submission for the **Kasparro Applied AI Engineer Assignment**.  
It implements a complete **agentic AI pipeline** to analyze Facebook Ads performance using structured insights, hypothesis evaluation, and creative generation.  
The project follows the LLM-first workflow recommended in the assignment:


Planner → DataAgent → InsightAgent → Evaluator → CreativeGenerator → Reporter



All outputs are saved in the `reports/` folder as required.
# 📌 Overview

The agentic pipeline processes the provided synthetic Meta ads dataset and produces:

- **insights.json** → structured insights (CTR, ROAS, trends, hypotheses, confidence)  
- **creatives.json** → AI-generated creative suggestions  
- **report.md** → human-readable summary of key insights  
- **logs/** → reserved for runtime logs / Langfuse traces  

This project demonstrates:

- LLM-ready agent design  
- Modular execution  
- Real-world FB Ads analytics logic  
- Production-grade clarity
- 

# 🧠 Agentic Architecture

### **1. Planner Agent**
Defines the overall workflow:



Load dataset → Aggregate metrics → Generate insights → Evaluate hypotheses → Generate creatives → Export report



### **2. Data Agent**
Loads and prepares:
data/synthetic_fb_ads_undergarments.csv


Handles date parsing and campaign grouping.

### **3. Insight Agent**
Calculates:
- CTR  
- ROAS  
- Impressions trend  
- Performance anomalies  

Generates hypotheses for each campaign.

### **4. Evaluator Agent**
Assigns confidence scores & validates insights.

### **5. Creative Generator Agent**
Extracts keywords from creative messages and generates new suggestions using template-based logic.

### **6. Reporter**
Exports:
- insights.json  
- creatives.json  
- report.md  



# ⚙️ Setup Instructions

### **1. Clone the repository**
```bash
git clone https://github.com/RaviSingh48/kasparro-agentic-fb-analyst-ravi-singh
cd kasparro-agentic-fb-analyst-ravi-singh


Create and activate a virtual environment for:-

Windows:
python -m venv .venv
.venv\Scripts\Activate.ps1

macOS/Linux:
python3 -m venv .venv
source .venv/bin/activate


Install dependencies:-

pip install --upgrade pip
pip install -r requirements.txt


Run the pipeline:-

python run.py --data data/synthetic_fb_ads_undergarments.csv --out reports/


Generated files will appear in:-
reports/insights.json
reports/creatives.json
reports/report.md


File Structure:-

kasparro-agentic-fb-analyst-ravi-singh/
│
├── data/
│   └── synthetic_fb_ads_undergarments.csv
│
├── prompts/
│   ├── planner_prompt.txt
│   ├── insight_prompt.txt
│   ├── evaluator_prompt.txt
│   └── creative_prompt.txt
│
├── reports/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator.py
│   │   └── creative_generator.py
│   ├── utils/
│   │   └── io_utils.py
│   └── pipeline.py
│
├── logs/
├── tests/
│   └── test_evaluator.py
│
├── run.py
├── requirements.txt
└── README.md



Sample Output:-

Sample — insights.json:


{
  "campaign_name": "Men ComfortMax Launch",
  "avg_ctr": 0.0183,
  "avg_roas": 2.37,
  "hypotheses": [
    "CTR below dataset median — creative may be underperforming.",
    "Impressions decreasing — possible saturation or budget reallocation."
  ],
  "confidence": 0.75,
  "evidence": {
    "avg_ctr": 0.0183,
    "avg_roas": 2.37,
    "impressions_trend": -1
  }
}


Sample — creatives.json:


{
  "campaign_name": "Women Seamless Everyday",
  "existing_messages_sample": [
    "Breathable organic cotton that moves with you…"
  ],
  "suggested_creatives": [
    "Limited time — Breathable. Shop now and save!",
    "Breathable for all sizes — feel confident. Buy today.",
    "Customers love Breathable. Tap to see styles.",
    "Free shipping on orders over ₹999. Get Breathable now."
  ]
}



Sample — report.md:

# Final FB Ads Analysis Report

## Executive Summary
- Total campaigns analyzed: 12

## Top Insights
### Men ComfortMax Launch
- Hypotheses: CTR below median; Impression decline
- Confidence: 0.75

## Creative Suggestions (sample)
### Women Seamless Everyday
- Existing: Breathable organic cotton that moves with you…
- Suggestions: Limited time — Breathable…; Breathable for all sizes…



Running Tests:-

pytest -q





