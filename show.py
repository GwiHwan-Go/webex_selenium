#모듈 설명
#학생 답을 수집해서 정답과 비교해 채점하였고, 이젠 점수와 질문과 답을 GUI통해서 보여줄 차례
from tkinter import *
import numpy as np
import pandas as pd
import score

def show(prodic, ansdic, studentli,sco):
    #행 = 학생, 열= 질문 과 답, 값= 점수, 학생이 말한답
    df_sco = pd.DataFrame(columns = studentli[1:])
    df_ans = pd.DataFrame(columns = studentli[1:])
    df_answer = pd.DataFrame(prodic.items(),columns=['Question','Answer'])
    for i in studentli[1:]:
        for num in range(len(prodic)):
            df_sco.loc[num,i] = sco[i][num]
    for i in studentli[1:]:
        for num in range(len(prodic)):
            df_ans.loc[num,i] = ansdic[i][num]
    
    df_ans = pd.concat([df_answer,df_ans],axis=1)
    df_sco = pd.concat([df_answer,df_sco],axis=1)

    df_li = [df_sco,df_ans]
    return df_li

def showtk(df_li):
    root = Tk()
    arr = np.array(df_li[0])
    col0 = df_li[0].columns.tolist()
    for i in range(len(arr)) :
        label = Label(root, text=col0[i])
        label.grid(row = 0, column = i)
        for j in range(len(arr[i])):
            
            label = Label(root, text=arr[i][j])
            label.grid(row = i+1 ,column = j ,padx=20)
    root.mainloop()

def personal_show(df_li,name):
    root=Tk()

    df_new = pd.concat([df_li[0].iloc[:,:2],df_li[0].loc[:,name],df_li[1].loc[:,name]],axis=1)
    col = df_new.columns.tolist()
    col[2]+=' 의 점수'
    col[3]+=' 의 답'

    arr=np.array(df_new)
    for i in range(len(arr)) :
        label = Label(root, text=col[i])
        label.grid(row = 0, column = i)
        for j in range(len(arr[i])):
            label = Label(root, text=arr[i][j])
            label.grid(row = i+1 ,column = j ,padx=20)
    
    root.mainloop()


if __name__ =='__main__':
    data = pd.read_csv('/Users/gwihwango/Desktop/python project/project/chat_for_test.txt',header=None)
    student_list = ['고귀환','WUZHEN','wujin']
    prodic = {'컴퓨팅 사고력의 주요 개념은?':'자료 수집 자료 분석','컴퓨팅 사고력 문제해결':'추상화 자동화','자료정렬하는데 기준이 되는값':'탐색키','자료정렬알고리즘의 종류들을 말해보세요.':'0'}
    ansdic = score.get_answer(data,prodic,student_list)
    sco = {'고귀환': [0, 0, 0, 5], 'WUZHEN': [1, 1, 2, 2], 'wujin': [3, 2, -1, 3]}
    dfli = show(prodic, ansdic, student_list,sco)
    showtk(dfli)
    

