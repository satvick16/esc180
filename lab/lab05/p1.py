def list1_starts_with_list2(list1, list2):
    return (len(list1) >= len(list2) and list1[0:len(list2)] == list2)


def modified(list1, list2):
    if len(list1) >= len(list2):
        for i in range(list2):
            if list1[i] != list2[i]:
                return False
        return True
    return False
