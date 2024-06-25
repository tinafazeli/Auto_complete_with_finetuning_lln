import json
import csv
import re
 
with open('MehrNewsTextDara.json', errors="ignore", encoding='utf-8' ) as json_file:
    jsondata = json.load(json_file)
 
data_file = open('datafile.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

def replace(txt):

    #replace num with "یک "

    txt=re.sub(r'\d+', 'یک', txt)

    # حروف انگلیسی بیرون پرانتز حذف 
    txt=re.sub(r'\b[a-zA-Z]+\b', '',txt,flags=re.IGNORECASE)

    # حذف کلمات داخل پرانتز
    txt = re.sub(r'\([^\(\)]*\)', '', txt)

    #حذف کاراکتر های غیر ضروری
    txt = re.sub(r'[\u200b\xa0]', ' ', txt)

    #اصلاح نیم فاصله ها
    txt=re.sub(r'\u200c', ' ', txt)
    
    return txt

csv_data=[]
with open('datafile.csv', encoding='utf-8') as csv_file:
    read=csv.reader(csv_file)
    header=next(read)
    csv_data.append(header)

    for row in read:
        new_row=[replace(text) for text in row]
        csv_data.append(new_row)

with open('datafile.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)


