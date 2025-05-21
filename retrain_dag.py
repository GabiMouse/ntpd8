def retrain_and_validate(**kwargs):
    import os
    import joblib
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from datetime import datetime

    # pobranie dane iris
    iris = load_iris(as_frame=True)
    df = iris.frame
    X = df.drop(columns='target')
    y = df['target']

    # podział train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # trening nowego modelu
    clf_new = RandomForestClassifier(random_state=42)
    clf_new.fit(X_train, y_train)

    # walidacja nowego modelu
    y_pred_new = clf_new.predict(X_test)
    acc_new = accuracy_score(y_test, y_pred_new)
    print(f"New model accuracy: {acc_new:.4f}")

    # stary model miał acc = 1
    acc_old = 1.0
    print(f"Old model accuracy: {acc_old:.4f}")

    # porównanie wyników
    if acc_new > acc_old:
        print("New model is better!")
    elif acc_new == acc_old:
        print("New model accuracy is the same as old model.")
    else:
        print("Old model is better than the new model.")

    # zapis nowego modelu w folderze dags
    model_dir = "/opt/airflow/dags"
    os.makedirs(model_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_model_path = os.path.join(model_dir, f"rf_model_{timestamp}.pkl")
    joblib.dump(clf_new, new_model_path)
    print(f"New model saved to: {new_model_path}")

    return new_model_path
