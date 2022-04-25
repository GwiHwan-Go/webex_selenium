#모듈 설명
#tkinter 의 GUI를 이용해서 사용자에게 질문과 답을 받는 과정
#GUI가 처음이라 이정도도 매우 힘들었기에 구체적인 외관은 다듬지 못했습니다.
#최종 결괏값 : 질문과 답이 담긴 딕셔너리, self.dic

from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.font
import time

class Qna :
    def __init__(self):
        self.root = Tk()
        self.root.title('수업참여 확인을 위한 문제와 질문 받는 중')
        self.root.geometry('')
        self.root.resizable(False, False)
        self.qnumber = 0
        self.my_entries=[]
        self.qlist,alist=[],[]
        self.dic = {}
        self.nstudents=0
        self.class_time = 0
        self.btn = Button(self.root, text='프로그램을 시작하겠습니다. 이 버튼을 눌러주세요.',width=50,height=5, anchor=tkinter.CENTER,command=self.click)
        self.email = ''
        self.pwd = ''
        self.class_name = ''
    def click(self):
        self.qnumber = tkinter.simpledialog.askinteger('질문 갯수 입력','수업 시에 학생들의 참여도를 파악할 질문들을 입력해주셔야 합니다.\n총 몇가지의 질문을 하시겠습니까? 숫자로 입력해주세요.')
        self.class_time = tkinter.simpledialog.askinteger('수업시간 입력(분단위)','수업시간을 분단위로 적어주세요\n(예 : 4분, 50분, 90분, 75분 등)')
        self.nstudents = tkinter.simpledialog.askinteger('총학생수','총 학생 수를 숫자로 입력해주세요.')
        self.email = tkinter.simpledialog.askstring('Webex email id 입력','웹엑스 프로그램을 실행합니다.\n Id를 이메일형태로 입력해주세요.')
        self.pwd = tkinter.simpledialog.askstring('Webex password 입력','웹엑스 프로그램을 실행합니다.\n password를 정확히 입력해주세요.')
        self.class_name = tkinter.simpledialog.askstring('Webex 클래스 명 입력','웹엑스 프로그램을 실행합니다.\n 클래스명을 정확히 입력해주세요.')
        self.btn.destroy()
        self.get_question()

    def get_question(self):
        self.qlist,self.alist=[None]*self.qnumber,[None]*self.qnumber
        for i in range(len(self.qlist)) :
            self.qlist[i] = tkinter.simpledialog.askstring('{}번째 질문'.format(i+1),'{}번째 질문을 입력해주세요.'.format(i+1))
            self.alist[i] = tkinter.simpledialog.askstring('{}번째 질문의 답'.format(i+1),'{}번째 질문의 답을 입력해주세요.\n 없다면 0 을 입력해주세요.'.format(i+1))
            
        
        self.show()

    def show(self):
        def next_to():
            btn1.destroy()
            btn2.destroy()
            newlabel = Label(self.root, text='입력하신 내용을 저장중입니다.\n 다음단계로 넘어갑니다.',font=titlefont,anchor=tkinter.S)
            newlabel.grid()
            time.sleep(2)
            self.next_to()
        titlefont = tkinter.font.Font(size=20)
        bodyfont = tkinter.font.Font(size=15)
        title = Label(self.root, text='질문과 답은 다음과 같습니다.',font=titlefont,anchor=tkinter.N)
        title.grid(row=0,column=0)
        for i in range(self.qnumber):
            if self.alist[i]==0 or self.alist[i] == 'O' or self.alist[i]=='o':
                self.alist[i] = 'None'
            mylabel1=Label(self.root,text=self.qlist[i],font=bodyfont)
            mylabel2=Label(self.root,text=self.alist[i],font=bodyfont)
            mylabel1.grid(row=i+15,column=0)
            mylabel2.grid(row=i+15,column=1)
        
        btn1 = Button(self.root, text='다음으로 넘어가시겠습니까?',width=20,height=3, command=next_to)
        btn2 = Button(self.root, text='수정할 내용이 있습니까?',width=20,height=3, command=self.click)
        btn1.grid(row=self.qnumber+20,column=0)
        btn2.grid(row=self.qnumber+20,column=1)
        
    def next_to(self) :

        self.dic = {}
        for i in range(len(self.qlist)):
            self.dic[self.qlist[i]]=self.alist[i]
        
        self.root.destroy()
        
if __name__ == '__main__':
    tk = Qna()
    tk.btn.pack()
    tk.root.mainloop()
