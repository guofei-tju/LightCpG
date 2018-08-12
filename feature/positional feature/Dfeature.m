function [feature_D] = Dfeature(feature_all,chr,jj)
    feature_D=[];
    sub_sub=[];
    
    for i=1:length(feature_all(:,1))
        
        [I]=find(chr <= feature_all(i,1),1,'last');
        if chr(I)> feature_all(i,1)
            [S]=find(feature_all(:,1) == chr(I));
            [J]=find(feature_all(:,1) == chr(I+1));  
            if length(I)+length(J)==2
                sub_sub = [feature_all(S,(jj-1)*4+2:jj*4+1),feature_all(J,(jj-1)*4+2:jj*4+1)];   
            end
        else
            [S]=find(feature_all(:,1) == chr(I+1));
            [J]=find(feature_all(:,1) == chr(I-1));
            if length(S)+length(J)==2
                sub_sub = [feature_all(S,(jj-1)*4+2:jj*4+1),feature_all(J,(jj-1)*4+2:jj*4+1)];  
            end
        end
        if length(sub_sub) == 8
            feature_D=[feature_D;[feature_all(i,1), sub_sub]];
        end
    end
end