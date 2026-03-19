# BMW Car Price Prediction Project

## Project Title
BMW Car Price Prediction Using Python and Machine Learning

## Course
Advanced Python Learning Course conducted by SLIPD

## Project Overview
This project was developed to predict the price of BMW cars using machine learning techniques in Python.  
The project uses a dataset downloaded from Kaggle (`bmw.csv`) and applies data analysis, preprocessing, model training, evaluation, and a simple graphical user interface for user input.

The aim of this project is to demonstrate practical knowledge of Python, data handling, machine learning, and GUI development as part of the Advanced Python course.

## Objectives
- Load and analyze the BMW dataset
- Select important features that affect the car price
- Train a machine learning model to predict car prices
- Evaluate model performance using error metrics
- Create a simple GUI application for price prediction
- Improve practical skills in Python programming

## Dataset
The dataset used in this project is `bmw.csv`, downloaded from Kaggle.

### Main attributes used
- `year`
- `mileage`
- `tax`
- `mpg`
- `engineSize`
- `price`

These features are used to train the model and predict the selling price of a BMW car.

## Project Files
- `bmw.csv` - dataset used for training and testing
- `DL_ML_Project.ipynb` - Jupyter Notebook for data analysis, training, and evaluation
- `main.py` - Python GUI application for car price prediction
- `README.md` - project documentation

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn
- Tkinter
- Jupyter Notebook

## Machine Learning Model
This project uses **Linear Regression** from Scikit-learn.

### Input features
- Year
- Mileage
- Tax
- MPG
- Engine Size

### Target variable
- Price

## Project Process

### 1. Data Loading
The dataset is loaded using Pandas:

```python
df = pd.read_csv("bmw.csv")
````

### 2. Feature Selection

The following columns are selected as input features:

```python
x = df[['year', 'mileage', 'tax', 'mpg', 'engineSize']]
y = df['price']
```

### 3. Data Splitting

The dataset is divided into training and testing sets using `train_test_split()`.

### 4. Model Training

A Linear Regression model is trained using the training data.

### 5. Prediction

The trained model predicts prices using test data and also predicts new values entered by the user through the GUI.

### 6. Model Evaluation

The model is evaluated using:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)

## GUI Application

The `main.py` file contains a simple Tkinter-based graphical user interface.

### GUI functions

* Accepts user input for:

  * Year
  * Mileage
  * Tax
  * MPG
  * Engine Size
* Predicts the BMW car price
* Displays the predicted value on the screen

This makes the project interactive and user-friendly.

## Correction Made

A prediction issue was corrected in the notebook and project explanation.

### Problem

The variable `y_pred` was used before being defined.

### Solution

The model was first trained, and then predictions were generated before calculating evaluation metrics.

Correct order:

1. Train model
2. Predict using test data
3. Evaluate the results

## How to Run the Project

### Run the notebook

Open the notebook file:

* `DL_ML_Project.ipynb`

Run all cells in Jupyter Notebook or JupyterLab.

### Run the GUI application

Run:

```bash
python main.py
```

Make sure the following file is in the same folder:

* `bmw.csv`

## Example Prediction Workflow

1. Enter the car year
2. Enter mileage
3. Enter tax
4. Enter MPG
5. Enter engine size
6. Click the prediction button
7. View the predicted BMW price

## Learning Outcomes

This project helped in understanding:

* Working with CSV datasets in Python
* Data preprocessing and feature selection
* Training a machine learning model
* Evaluating prediction accuracy
* Building a basic GUI using Tkinter
* Applying Python for a real-world use case

## Limitations

* The model uses only a limited number of features
* Accuracy may be improved with more preprocessing or advanced models
* The GUI is basic and can be improved further
* The dataset only represents available Kaggle data and may not reflect all market conditions

## Future Improvements

* Add more data preprocessing
* Try advanced regression models
* Improve GUI design
* Add input validation and error handling
* Save and load trained models
* Compare multiple machine learning algorithms

## Conclusion

This project is a practical application of Python and machine learning for predicting BMW car prices.
It demonstrates important concepts learned in the Advanced Python Learning Course conducted by SLIPD, including data analysis, model training, evaluation, and GUI development.

## Author

Nishan Harsha Maduranga

## Acknowledgement

This project was completed for academic learning purposes as part of the Advanced Python Learning Course conducted by SLIPD.
