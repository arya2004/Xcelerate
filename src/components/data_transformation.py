import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
# column transforer creates the pipeline for data
from sklearn.impute import SimpleImputer
# for NA values
from sklearn.pipeline import Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


from src.exceptions import CustomException
from src.logger import logging

from src.utils import save_object



@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path=os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_trainformation_config=DataTransformationConfig()

    #create pkl files 
    def get_data_transformer_object(self):

        '''
        responsible for data transformation
        '''

        try:
            numerical_features = ["writing_score", "reading_score"]
            categorical_features = ["gender","race_ethnicity","parental_level_of_education"	,"lunch","test_preparation_course"]

            #create pipeline
            numerical_pipeline = Pipeline(
                steps=[
                    # handles NA values and outlairs
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )
            logging.info("numerical feature standard scaling done")
            categorical_pipeline = Pipeline(
                steps=[
                    # replace with mode value
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder()),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )

            logging.info("categorical feature encoding done")

            # combine both pipelines

            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )

            return preprocessor



        except Exception as e:
            raise CustomException(e, sys)
        
    def intiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(train_path)

            logging.info('reading completed, obtaining preprecessor')

            preprocessor_object= self.get_data_transformer_object()

            target_col="math_score"
            numerical_features = ["writing_score", "reading_score"]
            categorical_features = ["gender","race_ethnicity","parental_level_of_education"	,"lunch","test_preparation_course"]

            input_feature_train_df=train_df.drop(columns=[target_col],axis=1)
            target_feature_train_df=train_df[target_col]

            input_feature_test_df=test_df.drop(columns=[target_col],axis=1)
          
            target_feature_test_df=test_df[target_col]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessor_object.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_trainformation_config.preprocessor_object_file_path,
                obj=preprocessor_object

            )

            return (
                train_arr,
                test_arr,
                self.data_trainformation_config.preprocessor_object_file_path,
            )

        except Exception as ex:
            raise CustomException(ex, sys)



