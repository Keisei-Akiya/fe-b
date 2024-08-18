def floor(tNum, sNum):
    work = 0
    
    while (work <= tNum):
        work = work + sNum
    
    # ア
    # work = work * sNum
    
    # イ
    # work = work + sNum
     
    # ウ
    # work = sNum - work

    # エ
    work = work - sNum
    
    return work

work = floor(13, 6)
print(work)