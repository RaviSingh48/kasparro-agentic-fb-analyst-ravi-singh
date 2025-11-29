import numpy as np

class InsightAgent:
    def generate_insights(self, df):
        insights = []
        # ensure columns exist
        if 'campaign_name' not in df.columns:
            return insights

        median_ctr = df['ctr'].median() if 'ctr' in df.columns else 0.01

        # campaign-level aggregation
        camp_groups = df.groupby('campaign_name')
        for name, group in camp_groups:
            avg_ctr = float(group['ctr'].mean()) if 'ctr' in group.columns else None
            avg_roas = float(group['roas'].mean()) if 'roas' in group.columns else None

            # compute simple trend for impressions if date exists
            impressions_trend = 0
            if 'date' in group.columns and 'impressions' in group.columns:
                g = group.sort_values('date')
                if len(g) >= 2:
                    coeffs = np.polyfit(range(len(g)), g['impressions'].fillna(0), 1)
                    impressions_trend = float(np.sign(coeffs[0]))

            hypos = []
            confidence = 0.5
            if avg_roas is not None and avg_roas < 1.5:
                hypos.append('ROAS below target (avg_roas < 1.5) — consider audience or creative changes.')
                confidence += 0.15
            if avg_ctr is not None and avg_ctr < median_ctr:
                hypos.append('CTR below dataset median — creative may be underperforming.')
                confidence += 0.15
            if impressions_trend < 0:
                hypos.append('Impressions decreasing — possible saturation or budget reallocation.')
                confidence += 0.1
            if not hypos:
                hypos.append('No strong negative signals; performance within expected range.')

            evidence = {
                'avg_ctr': avg_ctr,
                'avg_roas': avg_roas,
                'impressions_trend': impressions_trend,
                'count_rows': int(len(group))
            }

            insights.append({
                'campaign_name': name,
                'avg_ctr': avg_ctr,
                'avg_roas': avg_roas,
                'hypotheses': hypos,
                'confidence': round(min(confidence, 0.95), 2),
                'evidence': evidence
            })
        # sort by confidence ascending (prioritize low confidence / risk)
        insights = sorted(insights, key=lambda x: x.get('confidence', 0.0))
        return insights
