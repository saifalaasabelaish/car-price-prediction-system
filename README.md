# carGo

carGo is a project that aims to predict car prices based on real-world data from the Palestinian market. Using machine learning techniques, the project analyzes various factors influencing car prices and builds a predictive model to estimate the price of a car given its features.

## Table of Contents

- [Introduction](#introduction)
- [Description](#description)
- [Goal](#goal)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Introduction

Accurate car price prediction can benefit buyers, sellers, and market analysts by providing insights into market trends and helping in making informed decisions. This project leverages machine learning to develop a model that predicts the price of a car based on its attributes.

## Description

carGo project is designed to assist individuals in estimating the value of a car based on various features such as make, model, year of manufacture, mileage, engine size, fuel type, and transmission type. By leveraging machine learning algorithms, our application aims to provide accurate and reliable price predictions, helping users make informed decisions when buying or selling cars.

## Goal

The primary aim of this project is to build a robust and efficient car price prediction model tailored to the Palestinian market. This involves collecting and preprocessing relevant data, training machine learning models, and evaluating their performance to ensure high accuracy in predictions. Ultimately, the project seeks to enhance transparency and trust in the car market by providing valuable insights into car pricing.

## Features

- Data preprocessing and cleaning
- Feature engineering
- Model training and validation
- Model evaluation
- Price prediction for new data

## Installation

To run this project, ensure you have Python 3.7+ and the necessary libraries installed. Follow the steps below to set up the environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/saifalaasabelaish/carGo.git
    ```

2. Navigate to the car-price-prediction-system directory:
  ```bash
cd carGo

```
3. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Jupyter Notebook:
   ```bash
   jupyter-notebook
   ```  

## Dataset

The dataset used in this project includes various features such as:

- Car make and model
- Year of manufacture
- Mileage
- Engine size
- Fuel type

The dataset is collected from the most visited Palestinian car market website [oppensooq](https://www.shobiddak.com/ar) and has been cleaned and preprocessed for training.

## Model Training

The model is trained using various machine learning algorithms including:

- Linear Regression
- Decision Tree
- Polynomial Regression


## Evaluation

The model is evaluated using the R squared Score. Additional evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) can also be included for better assessment.


## Technologies

Technologies & Tools used in this project:

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.2.4-yellow)
![NumPy](https://img.shields.io/badge/NumPy-1.20-lightblue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4-green)

## Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
  

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

We would like to thank everyone who contributed to the project, including data providers and community members.

## Contact

For any questions or suggestions, please contact us at [Saifsabelaish@outlook.com](mailto:Saifsabelaish@outlook.com).
