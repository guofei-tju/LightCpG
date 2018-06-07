function feature_bin = Extract_feature(Dir_f_feature,blood_sample,chr_sample)

dir_path = [Dir_f_feature '\'];
fileFolder=fullfile(dir_path);
dirOutput=dir(fullfile(fileFolder,'*.bed'));
	
	
n_features = size(dirOutput,1);n_features
n_sample = size(blood_sample,1);n_sample
feature_bin = zeros(n_sample,n_features);

for i=1:n_features
	%read
	file_name = [dir_path dirOutput(i).name];
	feature_v=[];
	chr_v=[];
	[feature_v chr_v] = read_features(file_name);
	'search'
	%search
	for j = 1:n_sample
		CHR_cell = chr_sample(j);
		CHR_str = cell2mat(CHR_cell);
		[x,y] = find(strcmp(chr_v,CHR_str));
		Candidate_feature_v = feature_v(x,:);
		idx = blood_sample(j);
		kk=find(Candidate_feature_v(:,1)<=idx&Candidate_feature_v(:,2)>=idx);
		if isempty(kk)==0
			feature_bin(j,i)=1;
		end
		k = mod(j,10000);
		if k==0
			j
		end
	
	end
	str = ['feature' num2str(i)];
	str
	
	


end



