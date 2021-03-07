def solution(new_id):
    
    new_id = new_id.lower()
    check_lis = ['-','_','.']
    
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in check_lis:
            continue
        new_id = new_id.replace(i,'')
        
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..','.')
        if '..' not in new_id:
            break
    try:        
        if new_id[-1] == '.':
            new_id = new_id[0:len(new_id)-1]
    except:
        pass
    try:
        if new_id[0] == '.':
            new_id = new_id[1:len(new_id)]
    except:
        pass
        
    if not new_id:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[0:len(new_id)-1]
            
    a = new_id[-1]    
    while len(new_id) <= 2:
        new_id += a
        
    return new_id