from TextSummarizer.components.data_ingestion import DataIngestion
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager() #initialize class CM
        data_ingestion_config = config.get_data_ingestion_config() #get it's function
        data_ingestion = DataIngestion(config= data_ingestion_config) #call DI components and pass config
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        