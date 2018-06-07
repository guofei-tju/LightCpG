from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn import metrics
import scipy.io
import time
from sklearn.grid_search import GridSearchCV
import scipy.io as scio
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
    MCC = metrics.matthews_corrcoef(test_label, predict)
    special = float(tn) / (tn + fp)
    vaule[0, :] = [ACC, AUC, F1, MCC, special, recall, precision, AUPR, tn, fp, fn, tp]
    return vaule
Result = np.ones((25,13)).astype(np.float64)
for i in range(25):
    data = scipy.io.loadmat(r'E:\Ca_cycle\Ca_551_%s.mat'%(i+1))
    x_train = np.array(data['train_x'])
    y_train = np.array(data['train_y'])
    x_test = np.array(data['test_x'])
    test_label = np.array(data['test_y'])
    n = 0
    model_1 = GradientBoostingClassifier(n_estimators=110, learning_rate=0.04, min_samples_split=1500, max_depth = 8,
                                         min_samples_leaf=12, max_features='sqrt', random_state=10)
    start = time.time()
    model_1.fit(x_train, y_train)
    end = time.time()

    predict_1 = model_1.predict(x_test)
    score_1 = model_1.predict_proba(x_test)[:,1]
    vaule = roc(test_label, predict_1, score_1)
    print vaule
    Result[i,0:12] = vaule
    Result[i,12] = end - start
print Result
scio.savemat(r'E:\Ca_cycle\Ca_GBDT_time_result.mat', { 'Result': Result})






