from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def logistic_regression_model_generator(df, target_variable):
    while df.shape[0] > 1_000_000:
        df = df.sample(frac=0.1, random_state=42)
    while df.shape[0] > 100_000:
        df = df.sample(frac=0.5, random_state=42)
    x = df.drop(target_variable, axis=1)
    y = df[target_variable]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    cols = x_train.columns
    num_cols = x_train.select_dtypes(include='number').columns
    cat_cols = list(set(cols) - set(num_cols))
    preprocessor = ColumnTransformer(transformers=[('categorical', OneHotEncoder(handle_unknown='ignore'), cat_cols)],
                                     remainder='passthrough')
    x_train_encoded = preprocessor.fit_transform(x_train)
    x_test_encoded = preprocessor.transform(x_test)
    model.fit(x_train_encoded, y_train)
    y_pred = model.predict(x_test_encoded)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy
