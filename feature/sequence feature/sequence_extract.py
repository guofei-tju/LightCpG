import numpy as np
def cuting(x, y_sit, z):
    c = x
    sit = y_sit
    door = z
    seq_1 = []
    seq_1 = ''.join(sit[(c / 50) - 1:(c / 50) + 4]).replace('\n', '')[(100 + c % 50) - 1 - door:(100 + c % 50) + door]
    return seq_1
n = 0

sit_main = []
for i in range(12):
    sit_main = []
    f = open('D:\\PHD\\methylation\\heart\\hg19\\chr%s.fa' % (i+1), 'r')
    for line in f:
        sit_main.append(line.upper())
    f.close()
    for s in range(6):
        seq = []
        sub_f = open(r'C:\Users\JiangLimin\Desktop\HEP\HepG_%s\chr%s.bed' %(s+1,i+1), 'r')
        for sub_line in sub_f:
            chr_num = sub_line.split()[0]
            position = sub_line.split()[1]
            sequence_methy = cuting(int(position), sit_main, 50)
            n += 1
            seq.append('>seq__%d'%n + '\n' + sequence_methy)
        np.savetxt(r'E:\HEP\HepG_%s\chr%s.fasta'%(s+1,i+1), seq, '%s')
