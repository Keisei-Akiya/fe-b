def remainder(val, quo):
    ret = 0
    while (ret <= val):
        ret = ret + quo
    
    # ア
    # ret = val + ret - quo
    
    # イ
    # ret = ret - val + quo
    
    # ウ
    ret = quo - ret + val
    
    # エ
    # ret = quo - val - ret
        
    return ret

options = ["a", "i", "u", "e"]

for option in options:
    

ret = remainder(5, 3)
print(ret)