from flask import Blueprint, render_template, redirect, request
from app_func import logistic_regression_model_generator
from pandas.errors import ParserError
import plotly.graph_objects as go
import pandas as pd
import urllib.error
import base64
import io

Views = Blueprint("views", __name__)


@Views.route("/")
def slash(): return redirect("/deac109:machine_learning")


@Views.route("/deac109:machine_learning", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        dataset_url = request.form.get("dataset_url")
        target_variable = request.form.get("target_column")

        try:
            df = pd.read_csv(dataset_url)
        except (urllib.error.HTTPError, ParserError, OSError):
            return render_template("wrong_url.html")

        if target_variable not in list(df.columns):
            return render_template("wrong_target.html", columns=list(df.columns))

        model, accuracy = logistic_regression_model_generator(df, target_variable)
        coefficients = model.coef_[0]
        print(coefficients)
        feature_names = list(df.columns)
        if len(coefficients) > len(feature_names):
            fig = go.Figure(data=go.Bar(x=coefficients, y=feature_names))
            fig.update_layout(title='Logistic Regression Model Coefficients',
                              xaxis_title='Coefficients',
                              yaxis_title='Features')
        else:
            fig = go.Figure(data=go.Bar(x=feature_names, y=coefficients))
            fig.update_layout(title='Logistic Regression Model Coefficients',
                              xaxis_title='Features',
                              yaxis_title='Coefficients')
        image_bytes = io.BytesIO()
        fig.write_image(image_bytes, format='png')
        image_bytes.seek(0)
        plot_base64 = base64.b64encode(image_bytes.read()).decode('utf-8')
        return render_template("result.html", sample=df, plot=plot_base64, accuracy=accuracy)
    return render_template("home.html")
