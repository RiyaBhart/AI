def query(x):
    return int(-1 *(x-7)**2 +49)

def find_peak(N):
    current = N
    while True:
        if current>0:
            left = current - 1
        else:
            left = current
            
        if current<N:
            right = current+1
        else:
            right = current

        currentval = query(current)
        leftval = query(left)
        rightval = query(right)
        
        if currentval>=leftval and currentval>=rightval:
            return current
        if currentval<rightval:
            current+=1
        else:
            current-=1
            
N =35
peakindex = find_peak(N)
print(f"Peak found at index {peakindex} with elevation {query(peakindex)}")