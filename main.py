import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from sklearn.model_selection import train_test_split

# Window

root = tk.Tk()
root.title("BMW Car Price Prediction")
root.geometry("530x400")
root.configure(background="#1C1C1C")


title = tk.Label(root, text="BMW Car Price Predictor", font=("Times New Roman", 24), fg="#0066B1")
title.grid(row=0, column=0, columnspan=2, pady=10)


# Read data from file

df = pd.read_csv('bmw.csv')

x = df[['year', 'mileage', 'tax', 'mpg', 'engineSize']]
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Model training
bmw_price = LinearRegression()
bmw_price.fit(x_train, y_train)

y_pred = bmw_price.predict(x_test)


# Obtaining information from users

year =tk.Label(text="Year of Manufactured", background="#EAEAEA", fg="black", font=("Times New Roman", 14))
txt_box_year =tk.Entry(width=30, fg="#0066B1", font=("Times New Roman", 12))
mileage =tk.Label(text="Mileage", background="#EAEAEA", fg="black", font=("Times New Roman", 14))
txt_box_mileage =tk.Entry(width=30, fg="#0066B1", font=("Times New Roman", 12))
tax =tk.Label(text="Tax Rate", background="#EAEAEA", fg="black", font=("Times New Roman", 14))
txt_box_tax =tk.Entry(width=30, fg="#0066B1", font=("Times New Roman", 12))
mpg =tk.Label(text="Fuel Consumption(Miles per gallon)", background="#EAEAEA", fg="black", font=("Times New Roman", 14))
txt_box_mpg =tk.Entry(width=30, fg="#0066B1", font=("Times New Roman", 12))
engine_capacity =tk.Label(text="Engine Capacity(Ex: 3.5)", background="#EAEAEA", fg="black", font=("Times New Roman", 14))
txt_box_engine_capacity =tk.Entry(width=30, fg="#0066B1", font=("Times New Roman", 12))


year.grid(row=1, column=0, sticky='w', pady=10, padx=10)
txt_box_year.grid(row=1, column=1, pady=10, padx=10)
mileage.grid(row=2, column=0, sticky='w', pady=10, padx=10)
txt_box_mileage.grid(row=2, column=1, pady=10, padx=10)
tax.grid(row=3, column=0, sticky='w', pady=10, padx=10)
txt_box_tax.grid(row=3, column=1, pady=10, padx=10)
mpg.grid(row=4, column=0, sticky='w', pady=10, padx=10)
txt_box_mpg.grid(row=4, column=1, pady=10, padx=10)
engine_capacity.grid(row=5, column=0, sticky='w', pady=10, padx=10)
txt_box_engine_capacity.grid(row=5, column=1, pady=10, padx=10)

# Prediction function

def predict_price():
    try:
        year = int(txt_box_year.get())
        mileage = int(txt_box_mileage.get())
        tax = int(txt_box_tax.get())
        mpg = float(txt_box_mpg.get())
        engineSize = float(txt_box_engine_capacity.get())

        prediction = bmw_price.predict(pd.DataFrame([[year, mileage, tax, mpg, engineSize]],
                                                    columns=['year', 'mileage', 'tax', 'mpg', 'engineSize']))

        result_label.config(text=f"Predicted Vehicle Price is: ${round(prediction[0],2)}")
    except ValueError:
        result_label.config(text="Please enter a valid value")


# Button
btn = tk.Button(text="Calculate Price", font=("Times New Roman", 16), fg="#FFFFFF", background="#0066B1",  command=predict_price)
btn.grid(row = 6, column=1, pady=10, padx=10)

# Display results
result_label = tk.Label(text="", font=("Times New Roman", 16), fg="#00C853", bg="#1C1C1C")
result_label.grid( row=7, column=1, pady=10)

root.mainloop()