
import pandas as pd
import streamlit as st
import plotly.express as px

def process_csv(file_path):
    try:
        df = pd.read_csv(file_path, sep=';')
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file is empty at {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse the CSV file at {file_path}")
        return None


file_path = r"C:\Users\RodrigoPintoMesquita\Documents\GitHub\DR4_TP3\app\data\classification_results.csv"
df_result = process_csv(file_path)

if df_result is not None:
    st.title("Proportion by Category")
    proportions = df_result['model_classification'].value_counts(normalize=True) * 100
    fig = px.pie(values=proportions, names=proportions.index, title='Proportion of each category')
    st.plotly_chart(fig)
