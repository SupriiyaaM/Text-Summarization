#common functions used; import this instead of writing code again and again

import os
from ensure import ensure_annotations
from box import ConfigBox #can directly access values by keys as .
import yaml
from box.exceptions import BoxValueError
from TextSummarizer.logging import logger
from pathlib import Path



#function for reading a yaml file and return Config type
@ensure_annotations
def read_yaml( path_to_yaml : Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)      
    except BoxValueError:
        raise ValueError("yaml file error") #yaml file empty
    except Exception as e:
        raise e #empty file

#create directories
@ensure_annotations
def create_directories(path_to_directories : list, verbose = True): #verbose logs if directory created and it's True
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory created at {path}")
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"