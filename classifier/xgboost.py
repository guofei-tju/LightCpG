import time
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics
import scipy.io
import scipy.io as scio
import time
start_time = time.time()
def roc(test_label, predict, score):
    vaule = np.ones((1, 12)).astype(np.float64)
    precision = metrics.precision_score(test_label, predict)
    recall = metrics.recall_score(test_label, predict)
    tn, fp, fn, tp = metrics.confusion_matrix(test_label, predict).ravel()  
    print tn, fp, fn, tp
    ACC = metrics.accuracy_score(test_label, predict)
    AUC = roc_auc_score(test_label, score)
    AUPR = metrics.average_precision_score(test_label, score)
    F1 = 2 * (precision * recall) / (precision + recall)
    #MCC = metrics.matthews_corrcoef(test_label, predict)
    MCC = (tp*tn-fp*fn)/np.sqrt((tp+fp)*(tn+fn)*(tp+fn)*(tn+fp))
    special = float(tn) / (tn + fp)
    vaule[0, :] = [ACC, AUC, F1, MCC, special, recall, precision, AUPR,tn, fp, fn, tp]
    return vaule,AUC

n = 0
Result = np.ones((25, 13)).astype(np.float64)


#for i in range(25):
i=16
    
data = scipy.io.loadmat(r'Ca_551_%s.mat'%(i+1))
x_train = np.array(data['train_x'])
y_train = np.array(data['train_y'])
x_test = np.array(data['test_x'])
test_label = np.array(data['test_y']) 

params = {'booster': 'gbtree',
          'objective': 'binary:logistic',
          'eval_metric': 'auc',
          'num_boost_round': 110,
          'max_depth': 7,
          'lambda': 10,
          'subsample': 1,
          'colsample_bytree': 0.8,
          'min_child_weight': 9,
          'scale_pos_weight': 3,
          'eta': 0.3,
          'gamma': 12.5,
          'seed': 0,
          'nthread': 8,
          'silent': 1}

dtrain = xgb.DMatrix(x_train, label=y_train)
dtest = xgb.DMatrix(x_test)
watchlist = [(dtrain, 'train')]
start = time.time()
bst = xgb.train(params, dtrain, )
end = time.time()
ypred = bst.predict(dtest)
y_pred = (ypred >= 0.5) * 1
vaule,AUC = roc(test_label, y_pred, ypred)
#scio.savemat('xgboost_score_%s_result.mat'%(i+1), {'score': y_pred})
Result[i,0:12] = vaule 
Result[i,12] = end-start
print vaule   

scio.savemat('xgboodt_570.mat', {'Result': Result})
#scio.savemat('xg_GBDT_551_result_all.mat', {'Result_all': Result_all})







