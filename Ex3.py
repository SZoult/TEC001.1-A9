def calculate_average_score(file_path):
    total_score=0
    count=0
    with open(file_path,'r',encoding='utf-8') as file:
        for line in file:
            name, score=line.strip().split(',')
            total_score+=float(score)
            count+=1
    if count==0:
        return 0
    return round(total_score/count,2)