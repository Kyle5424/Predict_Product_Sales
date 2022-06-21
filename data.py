from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt
from tqdm import tqdm
import os
import pickle

dir_path = os.path.dirname(os.path.realpath(os.getcwd()))
print(dir_path)
dir_path = os.path.join(dir_path, 'Python')

def get_data(folder_path):
    X = []
    y = []
    dirs = os.listdir(folder_path)
    for path in tqdm(dirs):
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in tqdm(file_paths):
            with open(os.path.join(folder_path, path, file_path), 'r', encoding="utf-16") as f:
                lines = f.readlines()
                lines = ' '.join(lines)
                import textLib
                lines=textLib.Text(lines).str
                X.append(lines)
                y.append(path)

    return X, y

train_path = os.path.join(dir_path, 'VNTC-master/Data/10Topics/Ver1.1/Train_Full')
X_data, y_data = get_data(train_path)

pickle.dump(X_data, open('X_test1.pkl', 'wb'))
pickle.dump(y_data, open('y_test1.pkl', 'wb'))