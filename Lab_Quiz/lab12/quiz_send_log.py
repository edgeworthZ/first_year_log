def load_file():
    lines = open('/tmp/sent.log').read().splitlines()
    data = []
    for i,line in enumerate(lines):
        if i > 0: #skip header
            data.append(line)
    return data

lines = load_file()
stds = set()
quiz = set()
lab = set()
subDic = {}
labDic = {}
st_lb = list()
q10 = set()
morningTest = set()
firstSubmission = list()
q12,q13 = '',''
augTest = set()
q15 = 0
for line in lines:
    # Data's pivot
    dat = line.split(',')
    qz = dat[0]
    std = dat[1]
    lb = dat[2]
    datt = dat[3].split()
    date = datt[0]
    time = datt[1]
    # Analyze data
    stds.add(std)
    quiz.add(qz)
    lab.add(lb)
    subDic[qz] = subDic[qz]+1 if qz in subDic else 1
    labDic[lb] = labDic[lb]+1 if lb in labDic else 1
    st_lb.append(dat[1]+dat[2])
    if std == '09006593': q10.add(lb)
    if int(time[:2]) < 12:morningTest.add(qz)
    if lb == 'jumping2' and lb not in firstSubmission:
        q12 = std
        firstSubmission.append(lb)
    if lb == 'container' and lb not in firstSubmission:
        q13 = std
        firstSubmission.append(lb)
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
print(f"Following student(s) resummited an item: {','.join({x[:8] for x in st_lb if st_lb.count(x) > 1})}")
maxPair = max(set(st_lb),key=st_lb.count)
maxCount = st_lb.count(maxPair)
res = {x for x in st_lb if st_lb.count(x) == maxCount}
print(f"Max Resubmission student ({maxCount} times): {','.join(key[:8] for key in res)}")
print(f'Did student No.09006593 send all items? : {q10 == lab}')
print(f'Morning Test(s): {len(morningTest)}')
print(f'First sender of jumping2 is {q12}')
print(f'First sender of container is {q13}')
print(f"There're {len(augTest)} test(s) in August")
print(f'Lucky submission: {q15}')
