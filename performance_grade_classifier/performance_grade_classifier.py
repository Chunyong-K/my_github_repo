# Load libraries
import sklearn
from sklearn.utils import shuffle
from sklearn import datasets
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from sklearn import svm
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
from matplotlib import pyplot as plt
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score

# Data file import
df = pd.read_csv("performance_grade_new_DATA_SET.csv")
#print(df.head())
#pre-processing
from sklearn.exceptions import DataDimensionalityWarning
#encode object columns to integers
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder

for col in df:
  if df[col].dtype =='object':
    df[col]=OrdinalEncoder().fit_transform(df[col].values.reshape(-1,1))

#print(df.head())

#normalize
class_label =df['grade']
df = df.drop(['grade'], axis =1)
df = (df-df.min())/(df.max()-df.min())
df['grade']=class_label
#print(df.head())

#pre-processing
grade_data = df.copy()
le = preprocessing.LabelEncoder()
age = le.fit_transform(list(grade_data["age"])) # age in years
sex = le.fit_transform(list(grade_data["sex"])) # gender (1 = male; 0 = female)
graduated_h_school_type = le.fit_transform(list(grade_data["graduated_h_school_type"])) # chest-pain and chest-pain type
scholarship_type = le.fit_transform(list(grade_data["scholarship_type"])) # resting blood pressure (mm/Hg)
additional_work = le.fit_transform(list(grade_data["additional_work"])) # serum cholestrol (mg/dl)
activity = le.fit_transform(list(grade_data["activity"])) # fasting blood sugar
partner = le.fit_transform(list(grade_data["partner"])) # resting elctrocardiographic results
total_salary = le.fit_transform(list(grade_data["total_salary"]))
transport = le.fit_transform(list(grade_data["transport"]))
accomodation = le.fit_transform(list(grade_data["accomodation"]))
mother_ed = le.fit_transform(list(grade_data["mother_ed"]))
farther_ed = le.fit_transform(list(grade_data["farther_ed"]))
siblings = le.fit_transform(list(grade_data["siblings"]))
parental_status = le.fit_transform(list(grade_data["parental_status"])) # heart-disease 0-not present 1-present
mother_occup = le.fit_transform(list(grade_data["mother_occup"]))
father_occup = le.fit_transform(list(grade_data["father_occup"]))
weekly_study_hours = le.fit_transform(list(grade_data["weekly_study_hours"]))
reading_non_scientific = le.fit_transform(list(grade_data["reading_non_scientific"]))
reading_scientific = le.fit_transform(list(grade_data["reading_scientific"]))
attendance_seminars_dep = le.fit_transform(list(grade_data["attendance_seminars_dep"]))
impact_of_projects = le.fit_transform(list(grade_data["impact_of_projects"]))
attendances_classes = le.fit_transform(list(grade_data["attendances_classes"]))
preparation_midterm_company = le.fit_transform(list(grade_data["preparation_midterm_company"]))
preparation_midterm_time = le.fit_transform(list(grade_data["preparation_midterm_time"]))
taking_notes = le.fit_transform(list(grade_data["taking_notes"]))
listenning = le.fit_transform(list(grade_data["listenning"]))
discussion_improves_interest = le.fit_transform(list(grade_data["discussion_improves_interest"]))
flip_classrom = le.fit_transform(list(grade_data["flip_classrom"]))
grade_previous = le.fit_transform(list(grade_data["grade_previous"]))
grade_expected = le.fit_transform(list(grade_data["grade_expected"]))
course_id = le.fit_transform(list(grade_data["course_id"]))
grade = le.fit_transform(list(grade_data["grade"]))

#Predictive model development
x = list(zip(age, sex, graduated_h_school_type, scholarship_type, additional_work, activity, partner, total_salary,
             transport, accomodation, mother_ed, farther_ed, siblings, parental_status, mother_occup, father_occup,
             weekly_study_hours, reading_non_scientific, reading_scientific, attendance_seminars_dep, impact_of_projects
             , attendances_classes, preparation_midterm_company, preparation_midterm_time, taking_notes, listenning,
             discussion_improves_interest, flip_classrom, grade_previous, grade_expected, course_id))
y = list(grade)
# Test options and evaluation metric
num_folds = 5
seed = 7
scoring = 'accuracy'

# Model Test/Train
# Splitting what we are trying to predict into 4 different arrays -
# X train is a section of the x array(attributes) and vise versa for Y(features)
# The test data will test the accuracy of the model created
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.20, random_state=seed)
#splitting 20% of our data into test samples. If we train the model with higher data it already has seen that information and knows

#size of train and test subsets after splitting
print(np.shape(x_train)), print(np.shape(x_test))

# load the model from disk

#Fit with trainining subset
best_model = pickle.load(open('best_class_model_new.h5', 'rb'))
y_pred = best_model.predict(x_test)
model_accuracy = accuracy_score(y_test, y_pred)
print("Best Model Accuracy Score on Test Set:", model_accuracy)

