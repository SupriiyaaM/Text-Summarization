from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    all_required_files: list
    
    
@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    tokenizer_name : Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    evaluation_strategy: str
    eval_steps: int
    num_train_epochs: int
    logging_steps: int
    save_steps: float
    weight_decay: float
    gradient_accumulation_steps: int
    warmup_steps: int
    per_device_train_batch_size: int
    
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path