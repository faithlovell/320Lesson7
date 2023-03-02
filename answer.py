"""

input_info : {ID: {int num P, int lowest page, int latest page, int avg, int num S}



The students should be sorted in ascending order based the status results: 
first by their lowest page ID, than their latest page ID, and finally by their average score. Truncate any decimals to become integers

"""

def create_students(file):
    input_info = dict()
    part_of_entry = 0
    is_P = False
    is_S = False
    next(file) #skips first line (# of inputs)
    for line in file:
        for entry in line.split():
            part_of_entry += 1 #ID (1), action code (2), number based on code (3), time stamp (4) then reset to 0

            match part_of_entry: #match only works with python 3.10 +
                case 1:
                    studentID = entry
                    if studentID not in input_info.keys():
                        input_info[studentID] = {'lowP': -1, 'lateP': -1, 'avgScore': 0, 'scoreCount': 0}

                case 2:
                    if entry == 'P':
                        is_P = True

                    elif entry == "S":
                        is_S = True

                case 3:
                    if is_P:
                        input_info[studentID]['lateP'] = int(entry)

                        if input_info[studentID]['lowP'] > -1 and int(entry) < input_info[studentID]['lowP']: #if there have already been P entries 
                            input_info[studentID]['lowP'] = int(entry)
                        elif input_info[studentID]['lowP'] == -1: #when it is the first P entry
                            input_info[studentID]['lowP'] = int(entry)

                        is_P = False #reset flag

                    if is_S:
                        input_info[studentID]['avgScore'] += int(entry)
                        input_info[studentID]['scoreCount'] += 1

                        is_S = False #reset flag
                    
                case 4:
                    part_of_entry = 0
    
    return input_info

def sort_students(input_info): 
    #calculate average score, remove students without at least one P and one S, removes unneeded scorecount key
    copied_info = input_info.copy() #to prevent runtime error
    for student in copied_info:
        if input_info[student]['scoreCount'] > 0 and input_info[student]['lowP'] > -1:
            input_info[student]['avgScore'] = int(input_info[student]['avgScore'] / input_info[student]['scoreCount'])
            del input_info[student]['scoreCount']
        else:
            del input_info[student]
    
    #sorted function syntax found on https://developers.google.com/edu/python/sorting
    sorted_keys = sorted(input_info, key=lambda x: (input_info[x]['lowP'], input_info[x]['lateP'], input_info[x]['avgScore']))

    #print answer & store it in a variable for unit tests
    answer = []
    for key in sorted_keys:
        print(key, input_info[key]['lowP'], input_info[key]['lateP'], input_info[key]['avgScore'])
        answer.append(key)
        answer.append(input_info[key]['lowP'])
        answer.append(input_info[key]['lateP'])
        answer.append(input_info[key]['avgScore'])
    
    return answer
    
    

def solution(file):
    #for easy unit testing
    input_info = create_students(file)
    return sort_students(input_info)

if __name__ == '__main__':
    file_name = input()
    file = open(file_name)
    solution(file)