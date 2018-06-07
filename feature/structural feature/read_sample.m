function [sample_no chr_no] = read_sample(file_name)

%read file


sample_no=[];
chr_no=[];

[data1,data2,data3,data4]=textread(file_name,'%s%d%d%s','delimiter', '	');

sample_no = data2;
chr_no = data1;

