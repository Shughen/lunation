import argparse, os, time, json, joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="../data_external/dataset.csv")
    p.add_argument("--target", default="target")   # 0/1
    p.add_argument("--rounds", type=int, default=2000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", default="../outputs")
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "models"), exist_ok=True)

    df = pd.read_csv(args.data)
    y = df[args.target]
    X = df.drop(columns=[args.target])

    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.2, random_state=args.seed, stratify=y
    )

    model = XGBClassifier(
        n_estimators=args.rounds,
        max_depth=6,
        learning_rate=0.03,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        tree_method="hist",
        random_state=args.seed
    )

    t0 = time.time()
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)
    proba = model.predict_proba(Xte)[:, 1]

    metrics = {
        "roc_auc": float(roc_auc_score(yte, proba)),
        "report": classification_report(yte, pred, output_dict=True),
        "n_features": X.shape[1],
        "n_rows": len(df)
    }

    model_path = os.path.join(args.outdir, "models", "xgb_model.pkl")
    joblib.dump(model, model_path)

    with open(os.path.join(args.outdir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Saved: {model_path}")
    print(f"ROC_AUC: {metrics['roc_auc']:.4f}")
    print(f"Time_s: {time.time()-t0:.1f}")

if __name__ == "__main__":
    main()

