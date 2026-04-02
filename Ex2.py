def find_keyword_lines(file_path, keyword):
    result=[]
    with open(file_path,'r',encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if keyword in line:
                result.append(line_number)
    return result