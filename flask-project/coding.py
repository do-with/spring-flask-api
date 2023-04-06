def solution(info, query):
    answer = []
    for q in query:
        count = 0
        q_buf = q.strip().split('and ')
        print(q_buf)
        for i in info:
            i_buf = i.split(' ')
            print(i_buf)
            if i_buf[-1] >= q_buf[-1].split(' ')[-1] and q_buf[-1].split(' ')[0] in i_buf:
                print('hello')
                for standard in q_buf:
                    if standard.strip() in '-': count+=1
                    elif standard.strip() in i_buf: count+=1
            else: pass
            if count == len(i_buf)-1:
                answer.append(count)
    print(answer)

    return answer   
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
      ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]   )