#We are MNC company  for groceries & suppliers send stock list excel sheet on a daily basis.
#There are chances of duplication of data ,
#Create a python program using pandas to upload sheet in gui & remove duplicate data.
#Usee set also 



import pandas as pd
from tkinter import Tk, filedialog, Button, Label
from tkinter.messagebox import showinfo

# Function to upload and process Excel file
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        # Read Excel file
        try:
            df = pd.read_excel(file_path)
            original_len = len(df)
            
            # Removing duplicates using pandas and set
            df.drop_duplicates(inplace=True)  # Remove duplicates with pandas
            unique_records = set([tuple(row) for row in df.values])  # Further processing with set
            
            # Converting set back to DataFrame
            df_unique = pd.DataFrame(list(unique_records), columns=df.columns)
            
            # Show result and save the cleaned data
            df_unique.to_excel("cleaned_stock_list.xlsx", index=False)
            showinfo("Success", f"Removed {original_len - len(df_unique)} duplicates. Cleaned file saved as 'cleaned_stock_list.xlsx'.")
        except Exception as e:
            showinfo("Error", f"Error processing file: {e}")

# GUI setup
root = Tk()
root.title("Stock List Cleaner")

Label(root, text="Upload Stock List to Remove Duplicates").pack(pady=10)

Button(root, text="Upload Excel File", command=upload_file).pack(pady=20)

root.geometry("300x150")
root.mainloop()
