import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pickle

input_dir = "data/data_train"
categorical = ["empty", "not_empty"]

data = []
labels = []

for category_idx, category in enumerate(categorical):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42)

parameters = [{'gamma': [0.01, 0.001, 0.0001], 'C': [1, 10, 100, 1000]}]

model = GridSearchCV(SVC(), parameters, cv=5, scoring='recall', verbose=2, n_jobs=-1)
model.fit(x_train, y_train)
y_prediction = model.predict(x_test)

print("Best Score:",model.best_score_)
print("Best Params:",model.best_params_)
print(classification_report(y_test, y_prediction))

pickle.dump(model.best_estimator_, open('model.pkl', 'wb'))


