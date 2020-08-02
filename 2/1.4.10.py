





























def get_from_namespace(parent, var):
    for i in range(len(d)):
        if parent == d[i]['name']:
            if var in d[i]['var']:
                print(d[i]['name'])
                break
            else:
                get_from_namespace(d[i]['parent'], var)
                break
    else:
        print('None')
    #print(d)

def create_namespace(name, parent): #def create_namespace(name='global', parent=''):
    '''for i in range(len(d)):
        if parent == d[i]['name']:
            break
    else:
        d.append({'parent': parent, 'name': name, 'space': [], 'var': []})'''
    for i in range(len(d)):
        if name == d[-1]['name']:
            break
    else:
        d.append({'parent': parent, 'name': name, 'space': [], 'var': []})
    #print(d)

def add_from_namespace(parent, var):
    for i in range(len(d)):
        #print (str('len(d)') + str(len(d)))
        if parent == d[i]['name']:
            if var not in d[i]['var']:
                d[i]['var'].append(var)
                #print(d)
                break


d = [{'parent': '', 'name': 'global', 'space': [], 'var': []}]
a = int(input())
for i in range(a):
    s = input().split()
    if s[0] == 'get':
        get_from_namespace(*s[1:])
        # print(d)
    elif s[0] == 'add':
        add_from_namespace(*s[1:])
        # print(d)
    elif s[0] == 'create':
        create_namespace(*s[1:])
        # print(d)