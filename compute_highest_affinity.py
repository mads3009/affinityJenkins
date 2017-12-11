
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    map = dict()
    for i in range(0,len(site_list)):
        if(site_list[i] in map):
            map[site_list[i]].append(user_list[i])
        else:
            map[site_list[i]] = [user_list[i]]

    print(map)

    site1=""
    site2=""
    max_aff = 0

    for key1 in map:
        for key2 in map:
            if(key1 < key2):
                length = len(set(map[key1]).intersection(map[key2]))
                if(length>max_aff):
                    max_aff = length
                    site1=key1
                    site2=key2

    if(site1.lower()<site2.lower()):
        return (site1, site2)
    else:
        return (site2, site1)


def highest_affinity2(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    map = dict()
    for i in range(0,len(site_list)):
        if(site_list[i] in map):
            map[site_list[i]].append(user_list[i])
        else:
            map[site_list[i]] = [user_list[i]]

    print(map)

    site1=""
    site2=""
    max_aff = 0

    for key1 in map:
        for key2 in map:
            if(key1 < key2):
                length = len(set(map[key1]).intersection(map[key2]))
                if(length>max_aff):
                    max_aff = length
                    site1=key1
                    site2=key2

    if(site1.lower()<site2.lower()):
        return (site1, site2)
    else:
        return (site2, site1)

def highest_affinity3(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    map = dict()
    for i in range(0,len(site_list)):
        if(site_list[i] in map):
            map[site_list[i]].append(user_list[i])
        else:
            map[site_list[i]] = [user_list[i]]

    print(map)

    site1=""
    site2=""
    max_aff = 0

    for key1 in map:
        for key2 in map:
            if(key1 < key2):
                length = len(set(map[key1]).intersection(map[key2]))
                if(length>max_aff):
                    max_aff = length
                    site1=key1
                    site2=key2

    if(site1.lower()<site2.lower()):
        return (site1, site2)
    else:
        return (site2, site1)
