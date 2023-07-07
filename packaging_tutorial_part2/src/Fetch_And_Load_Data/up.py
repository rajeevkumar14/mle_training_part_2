import os
import urllib
import tarfile
import pandas as pd

HOUSING_PATH = (
    "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/"
)

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Input : This function take path for the data
    """
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    """
    Input : This function take path for the data
    Output : Returns data in csv format
    """
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def income_cat_proportions(data):
    """
    Input : Takes a dataframe
    Output : Return a dataframe
    """

    return data["income_cat"].value_counts() / len(data)
