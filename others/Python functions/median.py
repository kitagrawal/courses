def median(lists):
    new_list = sorted(lists)
    size = len(new_list)
    mid = size/2
    
    for item in new_list:
        if size == 1:
            medians = new_list[0]
        if size % 2 == 0:
            avg_median = new_list[mid-1] + new_list[mid]
            medians = avg_median / 2.0
        else:
            medians = new_list[mid]
    return medians
