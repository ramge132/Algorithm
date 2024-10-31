def solution(progresses, speeds):
    result = []
    
    while progresses:
        progresses = [p + s for p, s in zip(progresses, speeds)]
        print(progresses)
        
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        if count > 0:
            result.append(count)
            
    return result
    
        
    