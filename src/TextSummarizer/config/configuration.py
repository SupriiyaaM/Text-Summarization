from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import (DataIngestionConfig, DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        #create folder
        create_directories([self.config.artifacts_root])
        
        
    #above entity will be the return type of following function
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion #retrieves the data_ingestion part of the configuration from self.config
        
        create_directories([config.root_dir])
        
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            status_file= config.status_file,
            all_required_files= config.all_required_files,
        )  
    
        return data_validation_config