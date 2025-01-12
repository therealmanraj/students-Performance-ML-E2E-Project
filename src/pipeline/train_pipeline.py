from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException
import sys


class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def train(self):
        try:
            print("Starting Data Ingestion Step")
            train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()
            logging.info("Data Ingestion Completed")

            print("Starting Data Transformation Step")
            train_array, test_array, _ = self.data_transformation.intitate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info("Data Transformation Completed")

            print("Starting Model Training Step")
            r2_square, mae, rmse, model_name = self.model_trainer.initiate_model_trainer(train_array, test_array)
            logging.info(f"Model Training Completed with performance R2: {r2_square} MAE: {mae} and RMSE: {rmse}")

            return r2_square, mae, rmse, model_name
        except Exception as e:
            raise CustomException(e, sys)