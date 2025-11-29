class Evaluator:
    def evaluate(self, insights):
        # Example re-scoring or enrichment if needed
        evaluated = []
        for it in insights:
            score = it.get('confidence', 0.5)
            # small heuristic: penalize extremely low ROAS further
            roas = it.get('avg_roas')
            if roas is not None and roas < 1.0:
                score = min(0.95, score + 0.05)
            it['confidence'] = round(score, 2)
            evaluated.append(it)
        return evaluated
