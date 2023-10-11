import pandas as pd
from fastai.tabular.all import *
from fastbook import *

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import dtreeviz

import random
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths


def r_mse(pred,y):
    return round(math.sqrt(((pred-y)**2).mean()), 6)

def m_rmse(m, xs, y):
    return r_mse(m.predict(xs), y)


if __name__ == "__main__":
    procs = []
    cat_names = []
    cont_names = ['a', 'b', 'c', 'd', 'e', 'f']

    # Split data in train and validation
    df = pd.read_json(paths.RANDOM_TABULAR_FILE)
    to = TabularPandas(
        df,
        procs,
        cat_names,
        cont_names,
        y_names='y',
        splits=RandomSplitter()(range_of(df)),
    )
    xs, y = to.train.xs, to.train.y
    valid_xs, valid_y = to.valid.xs, to.valid.y

    # Train a decision tree and try a few predictions
    dtree = DecisionTreeRegressor(
        max_leaf_nodes=20
    ).fit(xs.values, y)
    print(dtree.predict([[100, 90, 80, 70, 60, 50]]))
    print(m_rmse(dtree, valid_xs.values, valid_y))

    # Train a random forest and try a few predictions
    rf = RandomForestRegressor(
        n_jobs=-1,
        n_estimators=40,
        max_samples=8000,
        max_features=0.5,
        min_samples_leaf=5,
        oob_score=True
    ).fit(xs.values, y)
    print(rf.predict([[100, 90, 80, 70, 60, 50]]))

    # Visualize the decision tree
    viz_rmodel = dtreeviz.model(model=dtree, 
                                X_train=df[cont_names], 
                                y_train=df['y'], 
                                feature_names=cont_names, 
                                target_name='y')
    v = viz_rmodel.view()
    v.show()
