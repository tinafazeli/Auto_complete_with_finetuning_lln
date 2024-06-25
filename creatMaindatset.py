import csv 

textData=open('datafile.csv',encoding='utf-8')

dataSet=[]

with textData as csv_file:
    sentence=csv.reader(csv_file)
    for row in sentence:
        dataSet.append(','.join(row))

del dataSet[0]

#باید برای هر کلمه ی موجود در دیتاست بیایم پرفیکس هاش رو دربیاریم

NewDataSet=[]
for sentence in dataSet:
    word=sentence.split()
    for i in word:
        length=len(i)
        for j in range(1, length):
            prefix=i[:j]
            full=i
            NewDataSet.append((full,prefix))

# درست کردن فایل اصلی دیتا ست و ذخیره اش تو csv

with  open('MainDataSet.csv','w',newline='', encoding='utf-8' ) as csvFile:
    header=['Prefix','Word']
    write=csv.DictWriter(csvFile,fieldnames=header)
    write.writeheader()
    for prefix, full in NewDataSet:
        write.writerow({'Prefix': prefix, 'Word': full})
