from src.agents.evaluator import Evaluator

def test_eval_basic():
    ev = Evaluator()
    sample = [{'campaign_name': 'A', 'avg_roas': 0.8, 'confidence': 0.5}]
    out = ev.evaluate(sample)
    assert isinstance(out, list)
    assert out[0]['confidence'] >= 0.5
