from sklearn.metrics import roc_auc_score
from sklearn import metrics
from keras.models import Sequential
from keras.layers import LSTM, Dense, GRU
from keras.layers.core import Dropout
from keras.backend.tensorflow_backend import set_session
import tensorflow as tf
import scipy
import scipy.io as scio
import numpy as np
import time


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
    
    
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
set_session(tf.Session(config=config))
num_classes = 1


Result = np.ones((25, 13)).astype(np.float64)

for i in range(25):    
    data = scio.loadmat(r'Ca_551_%s.mat'%(i+1))
    x_train = np.array(data['train_x'])
    y_train = np.array(data['train_y'])
    x_test = np.array(data['test_x'])
    test_label = np.array(data['test_y']) 
    with tf.device('/gpu:1'):
        model = Sequential()
        model.add(Dense(551, input_shape=(551,)))
        model.add(Dropout(0, noise_shape=None, seed=None))
        model.add(Dense(551, ))
        model.add(Dropout(0.2, noise_shape=None, seed=None))
        model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='mean_squared_error',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    start = time.time()
    model.fit(x_train, y_train, batch_size=128, epochs=570)
    end = time.time()         
    Result[i,0] = end-start
    
    predict = model.predict(x_test, batch_size=32, verbose=0)
    score = predict
    y_pred = (score >= 0.5) * 1
    vaule,AUC = roc(test_label, y_pred, score)  
    Result[i,0:12] = vaule 
    Result[i,12] = end-start   
    
    
scio.savemat('deep_time.mat', {'Result': Result})