# @title Cell 2: Analysis Parameters (Colab Form) { display-mode: "form" }
rows_to_display = 5 # @param {type:"slider", min:1, max:20, step:1}
show_data_types = True # @param {type:"boolean"}
export_to_drive = False # @param {type:"boolean"}

print(f"📊 Displaying the first {rows_to_display} rows of your file:\n")
display(df.head(rows_to_display))

if show_data_types:
    print("\n🔍 Column names and Data Types:")
    display(df.dtypes)

if export_to_drive:
    from google.colab import drive
    print("\n🔄 Requesting access to your Google Drive to save the report...")
    drive.mount('/content/drive')
    
    drive_path = '/content/drive/MyDrive/data_analysis_summary.csv'
    df.describe().to_csv(drive_path)
    print(f"💾 Summary report successfully saved to: {drive_path}")
