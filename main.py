from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import os
from sensor.pipeline.training_pipeline import TrainingPipeline


def test_exception():
    try:
        logging.info('we are dividing 1 by 0')
        x= 1/0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == '__main__':
    # mongodb_client = MongoDBClient()
    # print('pubudu')
    # print(mongodb_client.database.list_collection_names())

    try:
        train_pipelie = TrainingPipeline()
        train_pipelie.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)

    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_config = DataIngestionConfig(training_pipeline_config = training_pipeline_config)
    # print(data_ingestion_config.__dict__)

    

    


        

