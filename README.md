# fin-en-fin-data-translation
This repo helps you to translate dataframe headers or column values from fin-to-en and en-to-fin.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This Python project provides a simple and efficient way to translate DataFrame headers and column values between Finnish and English. With two specialized classes, "column" and "headers," you can effortlessly handle translations to suit your multilingual data analysis needs. Classes support both Pandas DataFrames and are customizable with adjustable temperature and maximum text length settings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Installation

To use this Python project, you need to have Python installed on your system. Simply clone this repository and import the `translate` class into your Python project.

python
pip install git+https://github.com/aarnisi/fin-en-fin-data-translation

## Usage

In this section, we'll demonstrate how to use the `column` and `headers` classes to perform operations on a DataFrame column. Parameters to use:

| Parameter    | Description                                               | Mandatory |
|--------------|-----------------------------------------------------------|-----------|
| `df`         | The DataFrame you want to work with (Pandas)              |    Yes    |
| `column`     | The name of the column you want to perform actions on     |   *Yes    |  
| `action`     | The translation action 'en-fi' / 'fi-en'                  |    Yes    |
| `temperature`| An integer parameter (0-100)                              |    No     |
| `max_length` | An integer parameter (0-200)                              |    No     |

*`column` parameter must be empty when using `headers`

```python
# Import the necessary libraries
import pandas as pd
from translate import column, headers

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)

df_column = column(df, column='Age', action='en-fi').df          #Remember to use .df to get dataframe values from python class
df_column.show()

df_headers= column(df, action='en-fi').df                        #Remember to use .df to get dataframe values from python class
df_headers.show()

```
