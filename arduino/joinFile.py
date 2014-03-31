# -*- coding: utf-8 -*-
def joinFile(out='out.txt'):
    f=open(out,'w')
    for i in range(1,13):
      for line in open('%s.txt'%i,'r'):
        if not(line.startswith('#')) and  line.strip():
            f.write(line.split('\t')[0]+'\n')
    f.close()
    
joinFile('Arduino.txt')