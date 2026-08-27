from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):
    print("🤖 Training advanced model...")

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    return model

def predict(model, X_test):
    print("🔍 Predicting...")
    return model.predict(X_test)