#모듈 설명
#미리 입력해둔 질문들을 수업중 특정시간(random or not)마다 pop_up 받는 모듈
#교수자는 pop_up받은 내용을 실시간 강의 채팅창에 침으로써 학생들에게 질문을 던진다.

import threading
import time
import random
from tkinter import *

class In_class:
    def __init__(self, class_time, cnt, rand):
        self.class_time = class_time
        self.class_cnt = cnt
        self.rand = rand
        self.end=0
        self.cnt=1
    
    def pop_up(self,ansdic):
        #ansdic 은 질문이 들어있는 dictionary
        def finish():
            root.destroy()
        root = Tk()
        root.title('{}번째 질문'.format(self.cnt))
        root.geometry('')
        root.resizable(False, False)
        label1 = Label(root, text='미리 입력해둔 {}번째 질문입니다. 채팅에 입력해주시면 됩니다. 문제번호랑 같이 입력해주세요.\n예) {} 문제, {}) 문제 {}: 문제 등'.format(self.cnt,self.cnt,self.cnt,self.cnt))
        label2 = Label(root, text=list(ansdic)[self.cnt])
        label3 = Label(root, text='종료는 왼쪽위의 빨간 버튼을 눌러주세요.')
        btn = Button(root, text='종료', command=finish)
        label1.pack()
        label2.pack()
        label3.pack()
        # btn.pack()
        self.cnt+=1
        
        root.mainloop()
        
    ##시간은 분단위로 받는다 가정함
    def alert(self,ansdic):
        interval = (self.class_time*60/self.class_cnt)
        if self.rand :
            for i in range(self.class_cnt):
                n=random.randint(1,int(self.class_time*60/self.class_cnt))
                time.sleep(n)
                self.end+=n
                self.pop_up(ansdic)
                if self.end>self.class_time*60:
                    break
        else :
            for i in range(self.class_cnt):
                time.sleep(interval)
                self.end+=interval
                self.pop_up(ansdic)
                


if __name__ == '__main__':
    dic={'asdnvwodnvasdv':2,'xzcnvkoanwv':'ansdkvowpv','asndvjoqpwv':'zncvkoqnwv','znckvowndv':'zcxnvokwndv','zncxvoqwv':'zxncvkoqwv'}
    inclass = In_class(2,20,False)
    inclass.alert(dic)

