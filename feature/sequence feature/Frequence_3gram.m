function F3 = Frequence_3gram(seq,abc,ab)

seq = cell2mat(seq);

LL = length(seq);

%%%%%%%%%%%%%%%%%%%%%%%%%%3 gram%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n_ThreeContinueUnit = size(abc,1);
n_abc = zeros(n_ThreeContinueUnit,1);


for i = 1:n_ThreeContinueUnit
	t_abc_str = abc(i);
	ss = cell2mat(t_abc_str);
	idx=strfind(seq,ss);
	n_abc(i) = length(idx);
end

feature_3 = (n_abc)/(LL-2);

%%%%%%%%%%%%%%%%%%%%%%2 gram%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n_TwoContinueUnit = size(ab,1);
n_ab = zeros(n_TwoContinueUnit,1);


for i = 1:n_TwoContinueUnit
	t_ab_str = ab(i);
	ss = cell2mat(t_ab_str);
	idx=strfind(seq,ss);
	n_ab(i) = length(idx);
end

feature_2 = (n_ab)/(LL-1);

%%%%%%%%%%%%%%%%%%%%%%%%1 gram%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
idx_A=strfind(seq,'A');
idx_C=strfind(seq,'C');
idx_G=strfind(seq,'G');
idx_T=strfind(seq,'T');
feature_1 = [length(idx_A)/LL;length(idx_C)/LL;length(idx_G)/LL;length(idx_T)/LL];

F3=[feature_3;feature_2;feature_1];

F3=F3';