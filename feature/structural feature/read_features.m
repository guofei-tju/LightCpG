function [feature_v chr_v]= read_features(file_name)

%read file


feature_v=[];
chr_v=[];


[data1,data2,data3]=textread(file_name,'%s%d%d','delimiter', '	');

chr_v = data1;
feature_v=[data2,data3];