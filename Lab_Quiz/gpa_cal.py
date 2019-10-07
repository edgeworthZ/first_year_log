txt = '''Subject: 01175165 credits: 1 grade: A
Subject: 01204111 credits: 3 grade: B
Subject: 01355111 credits: 3 grade: B+
Subject: 01355112 credits: 3 grade: C
Subject: 01355113 credits: 3 grade: D+
Subject: 01417167 credits: 3 grade: F
Subject: 01420111 credits: 3 grade: C+
Subject: 01420113 credits: 1 grade: C
Subject: 01999021 credits: 3 grade: D
Subject: 01999043 credits: 3 grade: A
Subject: 01999111 credits: 2 grade: A
'''
dic = {'c':0,'g':0.0}
g_val = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}
lines = txt.split('\n')
i = 0
while(i < len(lines)-1):
    ln = lines[i].split()
    s = ln[1]
    c = int(ln[3])
    g = g_val[ln[5]]
    dic['c'] += c
    dic['g'] += g*c
    i += 1
print(f"Total Credit = {dic['c']}, GPA = {dic['g']/dic['c']:.2f}")
