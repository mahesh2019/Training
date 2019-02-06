import re
import pandas as pd
listin = []
listxt = []
skills = []
final = []
file1 = open('txtresumelist/1', 'r')
file2 = open('input', 'r')
filein = file2.readlines()
filetxt = file1.readlines()
for item in filein:
    listin.append(item.strip())
for item in filetxt:
    listxt.append(item.strip())
listxt = filter(None, listxt)
for item in listin:
    for item1 in listxt:
        item1 = item1.lower()
        found = item1.find(item)
        if found >= 0:
                skills.append(item)
for item in skills:
    if item in final:
        pass
    else:
        final.append(item)
total = len(final)
df = pd.DataFrame({'name': []}, {'skills': final}, {'count': total})
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

