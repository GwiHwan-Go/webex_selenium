#!pip install pandas
#!pip install numpy
import pandas as pd
import numpy as np
from collections import defaultdict
import konlpy
from konlpy.tag import Okt

def mod(path):
    src1 = ','
    tar1 = '='
    src2 = '    '
    tar2 = ','
    filepath = path #txt file의 path
    check=0
    def modify(fpath,src,tar):
        with open(fpath, 'r') as file :
            content = file.read()
        content = content.replace(src,tar)
        with open(fpath,'w') as file :
            file.write(content)

    modify(filepath,src1,tar1)
    modify(filepath,src2,tar2)

# mod('/Users/gwihwango/Desktop/python project/project/chatting copy.txt') 딱 한번만 실행해야함!

# with open('/Users/gwihwango/Desktop/python project/project/chatting copy.txt', 'r') as file :
#     content = file.read()


#학생 수 : students_num
#prodic 은 미리 설정해놓은 질문: 답 딕션
def get_answer(data,prodic,student_list):
    dic={}
    #data = dataframe of chat
    for i in student_list :
        dic[i]=[None]*len(prodic)
    for i in range(len(data.iloc[:,2])):
        find,nameflag=0,1
        question,name='',''
        for j in range(len(data.iloc[:,2][i])):
            if data.iloc[:,2][i][j]=='님':
                nameflag=0
            if nameflag==1:
                name+=data.iloc[:,2][i][j]
            if find==1:
                question+=data.iloc[:,2][i][j]
            if data.iloc[:,2][i][j]=='\t':
                if data.iloc[:,2][i][j+1].isnumeric() :
                    find=1
        print(name,question,question[0])
        print(dic)
        if len(question)>2 :
            dic[name][int(question[0])-1] = question
    return dic



def score(answer, sans):
    if sans :
        okt = Okt()
        score=0
        ans_noun = set(okt.nouns(answer))
        sans_noun = set(okt.nouns(sans))
        for i in sans_noun :
            if i in ans_noun :
                score+=1
    else :
        return -1
    return score


def nans_score(raw_data,sans): #raw_data
    if sans :
        okt = Okt()
        score=0
        ans_noun = set(okt.nouns(raw_data))
        sans_noun = set(okt.nouns(sans))
        for i in sans_noun :
            if i in ans_noun :
                score+=1
    else :
        return -1
    
    return score

def scoredict(prodic,ansdic,student_list,raw_data):#raw_data = 미리 올려놓은 교안 텍스트 파일
    dic={}
    for i in student_list :
        dic[i]=[0]*len(list(prodic))
    
    #prodic 의 value 값과 ansdic의 특정 학생의 답의 인덱스와 맞춰서 매길것임
    for i in range(len(prodic.values())):
        for student in student_list :
            if list(prodic.values())[i] == '0' or list(prodic.values())[i] == 'O' or list(prodic.values())[i] == 'o':
                #미리 올려둔 교안 받기
                sco = nans_score(raw_data,ansdic[student][i])
            else :
                sco = score(list(prodic.values())[i],ansdic[student][i])

            dic[student][i]=sco
                
    return dic

if __name__ =='__main__':
    data = pd.read_csv('/Users/gwihwango/Desktop/python project/project/chat2 copy.txt',header=None)
    student_list = ['고귀환','WUZHEN','wujin']
    prodic = {'컴퓨팅 사고력의 주요 개념은?':'자료 수집 자료 분석','컴퓨팅 사고력 문제해결':'추상화 자동화','자료정렬하는데 기준이 되는값':'탐색키','자료정렬알고리즘의 종류들을 말해보세요.':'0'}
    jebaldic = get_answer(data,prodic,student_list)

    raw_data_path = '/Users/gwihwango/Desktop/python project/project/chat_for_test.txt'
    with open(raw_data_path,'r') as raw_file :
        raw_data = raw_file.read()
    jebalsco = scoredict(prodic, jebaldic, student_list, raw_data)
    print(jebalsco)

example={'컴퓨팅 사고력의 주요 개념은?':'자료수집, 자료분석, 자료표현, 문제분해, 추상화, 알고리즘과 절차, 자동화, 시뮬레이션, 병렬화'\
    ,'컴퓨팅 사고력은 문제해결을 위해 컴퓨팅 기기를 활용하여 자료를 논리적으로 분석하고 ***를 통하여 표현하며 알고리즘적 사고를 통해 해결과정의 ***를 수행할 수 있는 능력을 의미'\
    :'추상화, 자동화', '선형 구조인 자료구조를 말하시오':'연결리스트, 스택, 큐, 배열','트리에서 부모가 없는 노드의 명칭은?':'루트 노드'\
    ,'알고리즘의 표현방법들은 무엇이 있는가?':'플로우 차트, 순서도, 자연어, 수도코드'\
    ,'알고리즘의 성능을 측정하는 기준들은?':'정확성, 작업량, 수행량, 메모리 사용량, 단순성, 명확성, 최적성'\
    ,'자료정렬하는데 기준이 되는 값을 뭐라고 하는가?':'키, key'\
    ,'자료정렬알고리즘의 종류들을 말해보시오':'합병정렬, 선택정렬, 삽입정렬, 버블정렬'\
    ,'자료 탐색 알고리즘의 종류들을 말해보시오':'너비 우선 탐색, 깊이 우선 탐색, 선형 탐색'}
