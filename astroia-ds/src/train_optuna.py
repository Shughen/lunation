import argparse, os, time, json, joblib
import pandas as pd
import optuna
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

def objective(trial, Xtr, ytr, Xval, yval, seed):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 400, 4000),
        "max_depth": trial.suggest_int("max_depth", 3, 10),
        "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.2, log=True),
        "subsample": trial.suggest_float("subsample", 0.6, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
        "min_child_weight": trial.suggest_float("min_child_weight", 1.0, 20.0),
        "gamma": trial.suggest_float("gamma", 0.0, 5.0),
        "reg_lambda": trial.suggest_float("reg_lambda", 1e-3, 10.0, log=True),
        "reg_alpha": trial.suggest_float("reg_alpha", 1e-3, 10.0, log=True),
        "eval_metric": "logloss",
        "tree_method": "hist",
        "random_state": seed,
        "n_jobs": -1
    }
    model = XGBClassifier(**params)
    model.fit(Xtr, ytr)
    proba = model.predict_proba(Xval)[:, 1]
    return roc_auc_score(yval, proba)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="../data_external/dataset.csv")
    p.add_argument("--target", default="target")
    p.add_argument("--trials", type=int, default=200)  # augmente à 300–500 pour la nuit
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--outdir", default="../outputs")
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "models"), exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "logs"), exist_ok=True)
    os.makedirs(os.path.join(args.outdir, "reports"), exist_ok=True)

    df = pd.read_csv(args.data)
    y = df[args.target]
    X = df.drop(columns=[args.target])

    Xtr, Xval, ytr, yval = train_test_split(
        X, y, test_size=0.2, random_state=args.seed, stratify=y
    )

    study = optuna.create_study(direction="maximize")
    t0 = time.time()
    study.optimize(lambda t: objective(t, Xtr, ytr, Xval, yval, args.seed),
                   n_trials=args.trials, show_progress_bar=False)
    elapsed = time.time() - t0

    best_params = study.best_params
    best_score = study.best_value

    # Entraîne un modèle final avec les meilleurs params
    final = XGBClassifier(**best_params, eval_metric="logloss", tree_method="hist",
                          random_state=args.seed)
    final.fit(Xtr, ytr)

    import matplotlib.pyplot as plt
    fig = optuna.visualization.matplotlib.plot_optimization_history(study).figure
    fig.savefig(os.path.join(args.outdir, "reports", "optuna_history.png"), dpi=150)

    joblib.dump(final, os.path.join(args.outdir, "models", "xgb_best.pkl"))
    with open(os.path.join(args.outdir, "best_params.json"), "w") as f:
        json.dump({"best_params": best_params, "best_roc_auc": best_score, "time_s": elapsed}, f, indent=2)

    print("Best ROC_AUC:", round(best_score, 4))
    print("Saved model and reports in outputs/")

if __name__ == "__main__":
    main()

