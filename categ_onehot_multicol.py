import pandas as pd
import numpy as np

def cat_onehot(FeaturesToConvert, final_trd):

    trd_backup = final_trd
    i = 0
    for feature in FeaturesToConvert:

        trd1 = pd.get_dummies(final_trd[feature], drop_first = True)

        final_trd.drop([feature], axis = 1, inplace = True)

        if i ==0:
            trd_backup = trd1.copy()
        else:
            trd_backup = pd.concat([trd_backup, trd1], axis = 1)
        i = i+1

    trd_backup = pd.concat([trd_backup, final_trd], axis = 1)

    return trd_backup
