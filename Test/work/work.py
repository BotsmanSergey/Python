import codecs

with open('readfile.txt', encoding='utf-8') as r, open("writefile.bat", 'w') as w:
    r = r.read().split('\n')
    for line in r:
        line = line.strip().split('\t')
        w.write("Get-mailbox \""+line[0]+"\" | Set-MailboxRegionalConfiguration -LocalizeDefaultFolderName:$true -Language \"ru-RU\"\n")