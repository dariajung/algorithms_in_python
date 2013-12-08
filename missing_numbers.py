# Hacker Rank Missing Numbers Algorithm Question

def missing(a, b):
    a_map = {}
    b_map = {}
    missing = []
    for num in a:
        if num in a_map.keys():
            a_map[num] += 1
        else:
            a_map[num] = 1
    for num in b:
        if num in b_map.keys():
            b_map[num] += 1
        else:
            b_map[num] = 1

    for num in b:
        if a_map.get(num) == None:
            if num not in missing: 
                missing.append(num)
        elif b_map.get(num) > a_map.get(num):
            if num not in missing: 
                missing.append(num)
    
    missing.sort()
    for num in missing:
        print num,

if __name__ == '__main__':
    a_length = input()
    a = map(int, raw_input().strip().split(" "))
    b_length = input()
    b = map(int, raw_input().strip().split(" "))
    missing(a, b)

    