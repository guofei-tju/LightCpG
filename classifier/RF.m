result_all = [];
figure
hold on
for i = 1:25
    eval(['load(''Ca_551_' num2str(i) '.mat'')'])
    train_x = train_x;
    test_x = test_x;

    nTree = 500;
    Factor_f1 = TreeBagger(nTree, train_x, train_y);
    [Predict_label_f1,Scores_f1] = predict(Factor_f1, test_x);
    Predict_label_f1 = str2double(Predict_label_f1);
    [Y1,X1,THRE,AUC,OPTROCPT,SUBY,SUBYNAMES] = perfcurve(test_y,Scores_f1(:,2),'1');
    plot(Y1,X1,'Color',[rand(1,3)], 'LineWidth',1);    
    [Y1,X1,TPR,AUPR] = perfcurve(test_y,(Scores_f1(:,2)),1,'xCrit','reca','yCrit','prec');
    [ACC,SN,SP,PRECISION,over_NPV,F1,MCC] = roc(Predict_label_f1,test_y);    
    result_all(i,:) = [i, ACC, AUC, AUPR, F1, MCC, PRECISION, SP, SN];
    LL=i
end
grid on;
xlabel('1-Specificity');ylabel('Sensitivity'); 