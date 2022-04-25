#설치해야하는 것들 소개 !중요 : chromdriver , konlpy
#!pip install selenium
#!pip install beautifulsoup4
#!pip install konlpy
# chrome 버전확인후 그에 맞는 크롬드라이버를 다운받은 후 그 path 를 지정해주어야 함.]

import Login #chromdriver 설치필요
import QNA as q
import with_class as wc
import score
import pandas as pd
import time
import show
from tkinter import *
import tkinter.simpledialog
import tkinter.font
import tkinter.messagebox

qna = q.Qna() #모듈의 클래스 실행 및 시작(아래 세줄)
qna.btn.pack()
qna.root.mainloop()
prodic = qna.dic
nstudents = qna.nstudents

root = Tk()

##학생 수 입력부분은 구현의 다양성이 힘들어서 생략하였습니다.
# student_li = [None]*(nstudents)
# student_li[0]=input('이용자의 웹엑스 네임을 정확히 입력해주셔야 합니다.(예 : 고귀환,))')
# for i in range(1,nstudents):
#     student_li[i]=input('학생의 웹엑스 네임을 정확히 입력해주셔야 합니다.(예 : WUZHEN, wujin)')

student_li = ['고귀환','WUZHEN','wujin']

delay_time1 = tkinter.simpledialog.askinteger('수업이 얼마후 시작입니까?(초단위로 입력부탁드립니다.)','수업이 얼마후 시작입니까?(초단위로 입력부탁드립니다.)')
time.sleep(3)

Login.login(qna.email,qna.pwd,qna.class_name)
time.sleep(delay_time1)

# in_class = wc.In_class(qna.class_time, qna.qnumber, False)
# in_class.alert(qna.dic)

##================== 위는 수업 동안 발생하는 이벤트
##================== 아래는 수업이 끝난 후에 발생하는 이벤트
##수업이 끝난 후 txt file을 저장해준다. 그후 아래의 행동

filepath=tkinter.simpledialog.askstring('경로 입력','다운받은 txtfile의 path를 입력해주세요.\n txtfile의 경로를 여기 넣어주시면 됩니다.')
raw_data_path = tkinter.simpledialog.askstring('참고자료 경로 입력','채점에 참고할 교안의 path를 입력해주세요. 답이 정해지지 않은 문제 채점을 위한 참고용입니다.\n 형식은 .txt 입니다.')
with open(raw_data_path,'r') as raw_file :
    raw_data = raw_file.read()
score.mod(filepath) #한번만 실행해야함
data = pd.read_csv(filepath,header=None)
ansdic = score.get_answer(data,qna.dic,student_li) 
scoredict = score.scoredict(qna.dic,ansdic,student_li,raw_data)

#show module 만 만들면됨
#-----아래는 Gui
dfli = show.show(qna.dic, ansdic, student_li, scoredict)
show.showtk(dfli)
ctn = tkinter.messagebox.askyesno("Question","더 자세히 보시겠습니까?")
if ctn :
    print(student_li[1:])
    who = tkinter.simpledialog.askstring('학생 선택','누구를 보시겠습니까? 학생명단은 콘솔창에 떠있습니다.')
    show.personal_show(dfli, who)

tkinter.messagebox.showinfo('긴과제 봐주셔서 정말 감사합니다.','긴 과제 봐주셔서 정말 감사합니다.\n ok를 누르면 끝이 납니다.')
    




####---아래내용은 디버깅을 위한 참고내용
example={'1.컴퓨팅 사고력의 주요 개념은?':'자료수집, 자료분석, 자료표현, 문제분해, 추상화, 알고리즘과 절차, 자동화, 시뮬레이션, 병렬화'\
    ,'2.컴퓨팅 사고력은 문제해결을 위해 컴퓨팅 기기를 활용하여 자료를 논리적으로 분석하고 ***를 통하여 표현하며 알고리즘적 사고를 통해 해결과정의 ***를 수행할 수 있는 능력을 의미'\
    :'추상화, 자동화', '3.선형 구조인 자료구조를 말하시오':'연결리스트, 스택, 큐, 배열','4.트리에서 부모가 없는 노드의 명칭은?':'루트 노드'\
    ,'9.알고리즘의 표현방법들은 무엇이 있는가?':'플로우 차트, 순서도, 자연어, 수도코드'\
    ,'5.알고리즘의 성능을 측정하는 기준들은?':'정확성, 작업량, 수행량, 메모리 사용량, 단순성, 명확성, 최적성'\
    ,'6.자료정렬하는데 기준이 되는 값을 뭐라고 하는가?':'키, key'\
    ,'7.자료정렬알고리즘의 종류들을 말해보시오':'합병정렬, 선택정렬, 삽입정렬, 버블정렬'\
    ,'8.자료 탐색 알고리즘의 종류들을 말해보시오':'너비 우선 탐색, 깊이 우선 탐색, 선형 탐색'}