import zipfile
pre=r'C:\users\team2\desktop\channel'
comments = ''

f=zipfile.ZipFile(r'C:\Users\Team2\Downloads\channel.zip')
current = '90052'
filelist = {i.filename:i.comment for i in f.filelist}
while 1:
    d=f.open('{}.txt'.format(current)).read()
    comments+=filelist['{}.txt'.format(current)]
    print d
    current=d.split(' ')[3]

#print comments

#oxygen
