import csv, codecs, re

total_time = {}
email_name = {}

with open('LN_Time.csv', encoding='utf-8') as f:
    LN_Time = csv.reader(f)
    for row in LN_Time:
        login = re.sub(r".*\\(\w)", r'\1', row[2])
        if row[6].isdigit():
            if total_time.get(login) == None:
                total_time[login] = int(row[6])
            else: total_time[login] += int(row[6])

with open('staff_list.csv', encoding='utf-8') as s:
    readers = csv.reader(s)
    for row in readers:
        if row[5] != 'NULL' and row[5] != '':
            login = re.sub(r"(\w)\@.*", r'\1', row[5])
            if email_name.get(login) == None:
                email_name[login] = row[1]


with open('LN_Time.csv', encoding='utf-8') as f, open('Astra_VDI_Total_Time.csv', 'w', newline='', encoding='utf-8') as w:
    LN_Time = csv.reader(f)
    writer = csv.writer(w)
    for row in LN_Time:
        login = re.sub(r".*\\(\w)", r'\1', row[2])
        if total_time.get(login) != None:
            row.append(total_time[login])
        else:
            row.append("No found total time")
        if email_name.get(login) != None:
            row.append(email_name[login])
        else:
            row.append('No found name') 
        writer.writerow(row)