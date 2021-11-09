try: import Tkinter as tk
except: import tkinter as tk
w = tk.Tk()
w.title('내컴퓨터에서만 가능한, 단축 링크 만들기!')
lb1 = tk.Label(w, text = '사이트 타이틀')
lb1.pack()
ip1 = tk.Entry(w)
ip1.pack()
titles = None
names = None
urls = None
def r1(i = ip1):
    global titles
    titles = i.get()
btn1 = tk.Button(w, text = '확인',command = r1)
btn1.pack()
lb2 = tk.Label(w, text = '컴퓨터에 저장할 사이트 경로(\\를 / 로 표기해 주세요, (파일탐색기에서 폴더의 상단 주소창을 복사해서그 \' 복사한 주소/파일명.html\'로 써주세요))')
lb2.pack()
ip2 = tk.Entry(w)
ip2.pack()
def r2(i = ip2):
    global names
    names = i.get()
btn2 = tk.Button(w, text = '확인',command = r2)
btn2.pack()
lb3 = tk.Label(w, text = '이동할 링크(\'htpps://\' 나 \'http://\'그리고 \'www\' 를 명확히 써주세요)')
lb3.pack()
ip3 = tk.Entry(w)
ip3.pack()
def r3(i = ip3):
    global urls
    urls = i.get()
btn3 = tk.Button(w, text = '확인',command = r3)
btn3.pack()
lb4 = tk.Label(w,text = '완성하셨으면 종료하세요, (상단 바에 X 표시를 누르시면 됩니다(창을 닫아주시라는 말입니다))')
lb4.pack()
w.mainloop()
with open(names,'w') as f:
        f.write('<!DOCTYPE html>\n<html lang="ko">\n<head>\n	<meta charset="UTF-8">\n	<title>{}</title>\n</head>\n<body>\n	<meta http-equiv=\'refresh\' content=\'0;url={}\'>	\n</body>'.format(titles, urls))
