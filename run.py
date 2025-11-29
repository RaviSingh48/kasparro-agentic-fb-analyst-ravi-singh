from src.pipeline import run_pipeline
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/synthetic_fb_ads_undergarments.csv')
    parser.add_argument('--out', default='reports/')
    args = parser.parse_args()
    run_pipeline(data_path=args.data, out_dir=args.out)
