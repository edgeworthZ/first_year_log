def load_file():
    lines = open('/tmp/sent.log').read().splitlines()
    data = []
    for i,line in enumerate(lines):
        if i > 0: #skip header
            data.append(line)
    return data

lines = load_file()
stds,quiz,lab,q10,morningTest,augTest = set(),set(),set(),set(),set(),set()
subDic,labDic = {},{}
st_lb = list()
q12,q13 = list(),list()
q15 = 0
for line in lines:
    # Data's pivot
    dat = line.split(',')
    qz,std,lb = dat[0],dat[1],dat[2]
    datt = dat[3].split()
    date,time = datt[0],datt[1]
    # Analyze data
    stds.add(std)
    quiz.add(qz)
    lab.add(lb)
    subDic[qz] = subDic[qz]+1 if qz in subDic else 1
    labDic[lb] = labDic[lb]+1 if lb in labDic else 1
    st_lb.append(dat[1]+dat[2])
    if std == 'std01': q10.add(lb)
    if int(time[:2]) < 12:morningTest.add(qz)
    if lb == 'jumping2':
        q12.append(std)
    if lb == 'container':
        q13.append(std)
    if date[5:8] == 'Aug':
        augTest.add(qz)
    h,m,s = time.split(':')
    if int(h)%11 == 0 or int(m)%11 == 0 or int(s)%11 == 0:
        q15 += 1
    
print(f'No. of quiz_send: {len(lines)}')
print(f'No. of student(s): {len(stds)}')
print(f'No. of quiz(s): {len(quiz)}')
print(f'Average Submission/Quiz: {float(sum(subDic.values())) / len(subDic)}')
print(f'Average Submission/Item: {float(sum(labDic.values())) / len(labDic)}')
print(f'Max Submission: {max(labDic,key=labDic.get)}')
print(f"There're {len(labDic)} item(s): {' ,'.join([key for key in labDic.keys()])}")
print(f"There're {len({x[:5] for x in st_lb if st_lb.count(x) > 1})} student(s) resummited an item")
maxPair = max(set(st_lb),key=st_lb.count)
maxCount = st_lb.count(maxPair)
res = {x for x in st_lb if st_lb.count(x) == maxCount}
print(f"Max Resubmission student ({maxCount} times): {','.join(key[:8] for key in res)}")
print(f'Did student std01 send all items? : {q10 == lab}')
print(f'Morning Quiz(s): {len(morningTest)}')
print(f'First/Last sender of jumping2 is {q12[0]}/{q12[len(q12)-1]}')
print(f'First/Last sender of container is {q13[0]}/{q13[len(q13)-1]}')
print(f"There're {len(augTest)} test(s) in August")
print(f'Lucky submission: {q15}')
