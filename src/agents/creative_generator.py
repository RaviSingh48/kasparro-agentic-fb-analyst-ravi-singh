import re

class CreativeGenerator:
    def _seed_from_message(self, msg):
        if not msg or not isinstance(msg, str):
            return 'Comfort'
        # pick a 1-2 word seed (first meaningful noun-like token)
        tokens = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'-]+", msg)
        return tokens[0] if tokens else 'Comfort'

    def generate_creatives(self, df, top_n=8):
        creatives = []
        if 'campaign_name' not in df.columns:
            return creatives

        groups = df.groupby('campaign_name')
        # choose campaigns with lowest CTR first to prioritize
        ctrs = df.groupby('campaign_name')['ctr'].mean().sort_values()
        campaigns = ctrs.index.tolist()

        for camp in campaigns[:top_n]:
            group = groups.get_group(camp)
            msgs = group['creative_message'].dropna().astype(str).unique().tolist() if 'creative_message' in group.columns else []
            seed = self._seed_from_message(msgs[0]) if msgs else 'Comfort'
            templates = [
                f'Limited time — {{benefit}}. Shop now and save!',
                f'{{benefit}} for all sizes — feel confident. Buy today.',
                f'Customers love {{benefit}}. Tap to see styles.',
                f'Free shipping on orders over ₹999. Get {{benefit}} now.'
            ]
            suggestions = [t.format(benefit=seed) for t in templates]
            creatives.append({
                'campaign_name': camp,
                'existing_messages_sample': msgs[:3],
                'suggested_creatives': suggestions
            })
        return creatives
