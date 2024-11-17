from utils import db_connect
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


engine = db_connect()
PATH = os.getcwd()
data_path = os.path.join(PATH, '/workspaces/Data_Preprocessing_Project_TutorialDianaM/data/raw/AB_NYC_2019.csv')
df = pd.read_csv(data_path)
