import pandas as pd
from transformers import pipeline, logging
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StringType
import warnings

warnings.filterwarnings("ignore")
logging.set_verbosity(logging.WARNING)
# Create a Spark session
spark = SparkSession.builder.appName("PandasConversion").getOrCreate()


class column():
    def __init__(self, df, column: str, action: str, temperature: int = 0, max_length: int = 64):
        self.df = df
        self.column = column
        self.action = action
        self.temperature = temperature
        self.max_length = max_length


        self.ValidateInputs()
        self.model = self.CreateModel()

        if self.type == 'pandas':
            self.df = self.PandasDF()
        elif self.type == 'pyspark':
            self.df = self.PySparkDF()
        else:
            raise ValueError(f"Wrong input data format. It can be Pandas or PySpark dataframe only.")

    
    def ValidateInputs(self):
        # Check if the variable is an integer
        if isinstance(self.temperature, int):
            # Check if the variable is within the range [0, 100]
            if 0 <= self.temperature <= 100:
                pass
            else:
                raise ValueError(f"Temperature is not in the range [0, 100]. Your temperature value was {self.temperature}")
        else:
            raise ValueError("Temperature is not an integer.")
    
            # Check if the variable is an integer
        if isinstance(self.max_length, int):
            # Check if the variable is within the range [0, 200]
            if 0 <= self.max_length <= 200:
                pass
            else:
                raise ValueError(f"Max_length is not in the range [0, 200]. Your max_length value was {self.max_length}")
        else:
            raise ValueError("Max_length is not an integer.")

    
        # Check if the DataFrame is a Pandas DataFrame
        if isinstance(self.df, pd.DataFrame):
            self.type = 'pandas'
            print('Pandas dataframe input detected')
        elif isinstance(self.df, DataFrame):
            self.type = 'pyspark'
            print('PySpark dataframe input detected')
        else:
            raise ValueError(f"Wrong input data format. It can be Pandas or PySpark dataframe only.")



        if self.action.lower() == 'fi-en':
            self.model = "Helsinki-NLP/opus-mt-fi-en"
            self.langval = 'en'
        elif self.action.lower() == 'en-fi':
            self.model = "Helsinki-NLP/opus-mt-en-fi"
            self.langval = 'fi'
        else:
            raise ValueError(f"Wrong action parameter. It can be 'fi-en' or 'en-fi' and you used {self.action}")


    def CreateModel(self):
        return  pipeline(
                            task = "translation",
                            model = self.model,
                            model_kwargs={"temperature": self.temperature, "max_length": self.max_length})
    
    def PandasDF(self):
        self.df[f'{self.column}_{self.langval}'] = self.df[self.column].apply(lambda x: self.model.predict(x)[0]['translation_text'])
        return self.df
    

    def PySparkDF(self):
        self.df = self.df.toPandas()
        self.df[f'{self.column}_{self.langval}'] = self.df[self.column].apply(lambda x: self.model.predict(x)[0]['translation_text'])
        self.df = spark.createDataFrame(self.df)
        return self.df
    




class headers():
    def __init__(self, df, action: str, temperature: int = 0, max_length: int = 64):
        self.df = df
        self.action = action
        self.temperature = temperature
        self.max_length = max_length


        self.ValidateInputs()
        self.model = self.CreateModel()

        if self.type == 'pandas':
            self.df = self.PandasDF()
        elif self.type == 'pyspark':
            self.df = self.PySparkDF()
        else:
            raise ValueError(f"Wrong input data format. It can be Pandas or PySpark dataframe only.")

    
    def ValidateInputs(self):
        # Check if the variable is an integer
        if isinstance(self.temperature, int):
            # Check if the variable is within the range [0, 100]
            if 0 <= self.temperature <= 100:
                pass
            else:
                raise ValueError(f"Temperature is not in the range [0, 100]. Your temperature value was {self.temperature}")
        else:
            raise ValueError("Temperature is not an integer.")
    
            # Check if the variable is an integer
        if isinstance(self.max_length, int):
            # Check if the variable is within the range [0, 200]
            if 0 <= self.max_length <= 200:
                pass
            else:
                raise ValueError(f"Max_length is not in the range [0, 200]. Your max_length value was {self.max_length}")
        else:
            raise ValueError("Max_length is not an integer.")

    
        # Check if the DataFrame is a Pandas DataFrame
        if isinstance(self.df, pd.DataFrame):
            self.type = 'pandas'
            print('Pandas dataframe input detected')
        elif isinstance(self.df, DataFrame):
            self.type = 'pyspark'
            print('PySpark dataframe input detected')
        else:
            raise ValueError(f"Wrong input data format. It can be Pandas or PySpark dataframe only.")



        if self.action.lower() == 'fi-en':
            self.model = "Helsinki-NLP/opus-mt-fi-en"
            self.langval = 'en'
        elif self.action.lower() == 'en-fi':
            self.model = "Helsinki-NLP/opus-mt-en-fi"
            self.langval = 'fi'
        else:
            raise ValueError(f"Wrong action parameter. It can be 'fi-en' or 'en-fi' and you used {self.action}")


    def CreateModel(self):
        return  pipeline(
                            task = "translation",
                            model = self.model,
                            model_kwargs={"temperature": self.temperature, "max_length": self.max_length})
    
    def PandasDF(self):
        for col in self.df.columns:
            self.df = self.df.rename(columns={col: self.model.predict(col)[0]['translation_text']})
        return self.df
    

    def PySparkDF(self):
        self.df = self.df.toPandas()
        for col in self.df.columns:
            self.df = self.df.rename(columns={col: self.model.predict(col)[0]['translation_text']})
        self.df = spark.createDataFrame(self.df)
        return self.df
