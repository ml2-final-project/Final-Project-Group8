from torch.utils.data import DataLoader

from KaggleDataset import KaggleDataset
from testing_common_utils import predict_on_test_data, model_uzeros
from training_common_utils import image_preprocessing

kaggle_data = KaggleDataset(
    csv_file="../Data/sample_labels.csv",
    root_dir="../Data/images",
    image_transform=image_preprocessing
)

kaggle_data_loader = DataLoader(kaggle_data)

predict_on_test_data(kaggle_data_loader, model_uzeros)
