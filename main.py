from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA VALIDATION STAGE"

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "MODEL TRAINER STAGE"

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "MODEL EVAlUATION STAGE"

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
