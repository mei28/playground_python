import matplotlib

# temporary work around down to virtualenv
# matplotlib issue.
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from sklearn.linear_model import LogisticRegression

# import specific projection format.
from fairml import audit_model
from fairml import plot_dependencies

import os 
import sys

get_ipython().run_line_magic("matplotlib", " inline")


INPUT_DIR = '/working/input'


df = pd.read_csv(os.path.join(INPUT_DIR,'propublica/propublica_data_for_fairml.csv'))


TARGET = 'Two_yr_Recidivism'
y = df[TARGET]
X = df.drop(TARGET, axis=1)


clf = LogisticRegression(penalty='l2', C=0.01)
clf.fit(X.values, y.values)


importancies, _ = audit_model(clf.predict, X)


plot_dependencies(
    importancies.median(), 
    reverse_values = False,
    title = 'FairML'
)



