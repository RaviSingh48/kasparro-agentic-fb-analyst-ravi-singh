import json, os
from src.agents.planner import Planner
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator import Evaluator
from src.agents.creative_generator import CreativeGenerator

def run_pipeline(data_path: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    planner = Planner()
    tasks = planner.plan("Analyze FB ads performance and generate insights.")
    print('Planned tasks:', tasks)

    # Data load & prep
    data_agent = DataAgent(data_path)
    df = data_agent.load_data()

    # Insights
    insight_agent = InsightAgent()
    insights = insight_agent.generate_insights(df)

    # Evaluate insights
    evaluator = Evaluator()
    evaluated = evaluator.evaluate(insights)

    # Creatives
    generator = CreativeGenerator()
    creatives = generator.generate_creatives(df, top_n=8)

    # Save outputs (UTF-8 fixes)
    with open(os.path.join(out_dir, 'insights.json'), 'w', encoding='utf-8') as f:
        json.dump(evaluated, f, indent=2, ensure_ascii=False)

    with open(os.path.join(out_dir, 'creatives.json'), 'w', encoding='utf-8') as f:
        json.dump(creatives, f, indent=2, ensure_ascii=False)

    # Simple markdown report (UTF-8 safe)
    with open(os.path.join(out_dir, 'report.md'), 'w', encoding='utf-8') as f:
        f.write('# Final FB Ads Analysis Report\n\n')
        f.write('## Executive summary\n\n')
        f.write('- Total campaigns analyzed: {}\n'.format(len(evaluated)))
        f.write('\n## Top 8 Insights\n')
        for ins in evaluated[:8]:
            f.write('### {}\n'.format(ins['campaign_name']))
            f.write('- Hypotheses: {}\n'.format('; '.join(ins['hypotheses'])))
            f.write('- Confidence: {:.2f}\n'.format(ins.get('confidence', 0.0)))
            f.write('- Evidence: {}\n\n'.format(ins.get('evidence', {})))

        f.write('## Creative suggestions (sample)\n\n')
        for c in creatives[:8]:
            f.write('### {}\n'.format(c['campaign_name']))
            f.write('- Existing: {}\n'.format(', '.join(c.get('existing_messages_sample', [])[:3])))
            f.write('- Suggestions: {}\n\n'.format('; '.join(c.get('suggested_creatives', [])[:4])))

    print('Saved outputs to', out_dir)
