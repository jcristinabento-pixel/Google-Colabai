# @title Cell 1: Environment Setup and File Upload { display-mode: "form" }

from google.colab import files
import pandas as pd
import io
import os

print("Please upload a CSV or Excel file:")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

if file_name.endswith('.csv'):
    df = pd.read_csv(io.BytesIO(uploaded[file_name]))
elif file_name.endswith(('.xls', '.xlsx')):
    df = pd.read_excel(io.BytesIO(uploaded[file_name]))
else:
    print("❌ Unsupported file format. Please upload a CSV or Excel file.")

print(f"\n✅ File '{file_name}' successfully loaded!")
