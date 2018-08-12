 n = 1; %chr number
 number_cell = 25; % the number of cells
%%%------------loading all cell datasets and filtering sample ----------
sample_all = [];
for j =1:number_cell         
    file_name = ['D:\PHD\methylation\bigdata\GSE65364_RAW\Ca_' num2str(j) '\chr' num2str(n) '.bed'];    
    [data1,data2,data3,data4]=textread(file_name,'%s%d%d%s','delimiter', '	');
    data4 = str2num(char(data4));    
    sample = [data2,data3,data4];  
    sample_all = [sample_all; sample];    
end

[I] = find(sample_all(:,2)>=4);
sample_all = sample_all(I,:);
[sample,i,j]=unique(sample_all(:,1));
sample = sample_all(i,:);
sample = sortrows(sample,1);
clear sample_all 

%%%%---------loading another cell dataset and ranking sample according position information-------------

for j =1:number_cell    
    
    file_name = ['D:\PHD\methylation\bigdata\GSE65364_RAW\Ca_' num2str(j) '\chr' num2str(n) '.bed'];
    [data1,data2,data3,data4]=textread(file_name,'%s%d%d%s','delimiter', '	');
    data4 = str2num(char(data4));
    eval( ['chr_' num2str(j)  '=[data2,data3,data4' '];']);   
    eval(['[I]=find(chr_' num2str(j) '(:,2)>= 4);']);
    eval(['chr_' num2str(j) '=chr_' num2str(j) '(I,:);']);  
    eval(['chr_' num2str(j) '=sortrows(chr_' num2str(j) ',1);']);
   
end
clear data1;clear data2;clear data3;clear data4;
%%%-------------positional feature extration -----------------------------
index_chr = ones(number_cell,1);
value_begin = [];
value_end = [];
for i = 1:number_cell
    value_begin = [value_begin , eval(['chr_' num2str(i) '(51,1)'])];
    value_end = [value_end , eval(['chr_' num2str(i) '(length(chr_' num2str(i) ')-51 , 1)'])];
end
[Imin] = find(sample(:,1)== max(value_begin));
[Imax] = find(sample(:,1)== min(value_end));

index_chr_end = ones(number_cell,1);
    for i =1:number_cell
        index_chr_end(i) = eval(['length(chr_' num2str(i) ')-50']); 
    end
%%%--------------------------extracting F positional features--------------------------
 feature=[];
for i = Imin:Imax
    sub = [];
    point_index = sample(i,1);
    for jj = 1:number_cell   
        sub_sub = [];
        eval(['chr_tmp = chr_' num2str(jj) ';']);
        for ii = index_chr(jj):index_chr_end(jj)
            if chr_tmp(ii, 1) > point_index && chr_tmp(ii-1, 1) < point_index
                index_chr(jj) = ii; 
                sub_sub = [sub_sub,[chr_tmp(ii,3), chr_tmp(ii,1)-point_index, chr_tmp(ii-1,3), point_index-chr_tmp(ii-1,1)]];                                    
                break
            end
            if chr_tmp(ii,1) == point_index                
                index_chr(jj) = ii;                
                sub_sub = [sub_sub,[chr_tmp(ii+1,3), chr_tmp(ii+1,1)-point_index, chr_tmp(ii-1,3), point_index-chr_tmp(ii-1,1)]];
                break                
            end            
        end
        sub = [sub, sub_sub];       
    end
    sub=[point_index,sub];
    feature=[feature;sub];
end
feature(:,2:end) = line_map(feature(:,2:end)); %normalize

%%%--------------------------extracting D positional features--------------------------


for jj = 1:number_cell 
    eval(['chr = chr_' num2str(jj) '(:,1);']);  
    feature_D = Dfeature(feature,chr,jj);
    eval(['feature_D_' num2str(jj) ' = feature_D;']);  
end

feature_D_all=[];
for ii=1:length(feature(:,1))    
    sub_sub=[];
    for jj = 1:number_cell
        eval(['feature_11 = feature_D_' num2str(jj) ';'])
        [I]=find(feature_11(:,1)==feature(ii,1));
        if length(I)==0     
            break
        else
            sub_sub=[sub_sub,feature_11(I,2:end)];            
        end         
    end
    if length(sub_sub) == 8*number_cell        
        feature_D_all=[feature_D_all;[feature(ii,1),sub_sub]];
    end
end

for ii = 1:number_cell
    feature_sub=[];
    eval(['chr = chr_' num2str(ii) ';']); 
    feature_D = feature_D_all;
    feature_D(:,(ii-1)*8+2:ii*8+1)=[];
    for jj=1:length(chr(:,1))
        [I]=find(feature_D(:,1) == chr(jj,1));
        [J]=find(feature(:,1) == chr(jj,1));
         if length(I)+length(J)==2
              feature_sub=[feature_sub;[chr(jj,[1,3]),feature(J,2:end),feature_D(I,2:end)]];
         end         
    end
    eval(['feature_cell' num2str(ii) '=feature_sub;']);             
end


