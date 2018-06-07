import time
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics
import scipy.io as scio
import lightgbm as lgb

def roc(test_label, predict, score):
    vaule = np.ones((1, 12)).astype(np.float64)
    precision = metrics.precision_score(test_label, predict)
    recall = metrics.recall_score(test_label, predict)
    tn, fp, fn, tp = metrics.confusion_matrix(test_label, predict).ravel()
    #print tn, fp, fn, tp
    ACC = metrics.accuracy_score(test_label, predict)
    AUC = roc_auc_score(test_label, score)
    AUPR = metrics.average_precision_score(test_label, score)
    F1 = 2 * (precision * recall) / (precision + recall)
    MCC = metrics.matthews_corrcoef(test_label, predict)
    special = float(tn) / (tn + fp)
    vaule[0, :] = [ACC, AUC, F1, MCC, special, recall, precision, AUPR,tn, fp, fn, tp]
    return vaule,AUC
   
data = scio.loadmat(r'number.mat')
number = np.array(data['number'])

for i in range(10,25):

    Result = np.ones((551, 12)).astype(np.float64)
    
    data = scio.loadmat(r'Ca_551_%s.mat'%(i+1))
    x_train = np.array(data['train_x'])  

    y_train = np.array(data['train_y']).T[0,:]
    x_test = np.array(data['test_x'])

    test_label = np.array(data['test_y']).T[0,:] 
    
    for j in range(9,551):
       
        Pos = number[0,0:j+1]  
        print np.shape(Pos)
        x_tra = x_train[:,Pos-1] 
   
        x_tes = x_test[:,Pos-1]    

        params = {'task': 'train',              
                  'boosting_type': 'gbdt', 
                  'objective': 'binary',  
                  'num_boost_round':570,              
                  'max_depth': 5,
                  'num_leaves': 22,
                  'learning_rate':0.04,
                  'scale_pos_weight': 2,
                  'nthread': 8, 
                  'bagging_fraction': 0.7,
                  'feature_fraction': 0.9,              
                  'metric': {'12','auc'}              
                  }
         

        dtrain = lgb.Dataset(x_tra, y_train)
        d_eval = lgb.Dataset(x_tes,test_label,reference=dtrain) 
        #start = time.time()    
        gbm = lgb.train(params, dtrain)
        #end = time.time()
        #print end-start
        score = gbm.predict(x_tes)
        #scio.savemat('ligth_score_%s_result.mat'%(i+1), {'score': score})
        y_pred = (score >= 0.5) * 1
        vaule,AUC = roc(test_label, y_pred, score)  
        Result[j,0:12] = vaule         

    scio.savemat('featue_number_%s.mat'%(i+1), {'Result': Result})







