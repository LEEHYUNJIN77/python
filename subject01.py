from tkinter import *
def insertData():
    pass

root = Tk()
root.title("컴퓨터과 3학년 1반 19번 이현진")
edtFrame = Frame(root)
edtFrame.pack()
lstFrame = Frame(root)
lstFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1= Entry(edtFrame, width=10)
edt2= Entry(edtFrame, width=10)
edt3= Entry(edtFrame, width=10)
edt4= Entry(edtFrame, width=10)

edt1.pack(side =LEFT, padx=10, pady=10)
edt2.pack(side =LEFT, padx=10, pady=10)
edt3.pack(side =LEFT, padx=10, pady=10)
edt4.pack(side =LEFT, padx=10, pady=10)

btnSelect= Button(edtFrame,text="입력", command=insertData)
btnlnsert.pack(side = LEFT, padx=10, pady=10)

btnlnsert = Button(edtFrame,text="조회", command=insertData)
btnlnsert.pack(side = LEFT, padx=10, pady=10)

lstData1= Listbox(istFrame, bg = "green")
lstData1.pack(side=LEFT, fill=BOTH, expand=1)

lstData2= Listbox(istFrame, bg = "green")
lstData2.pack(side=LEFT, fill=BOTH, expand=1)

lstData3= Listbox(istFrame, bg = "green")
lstData3.pack(side=LEFT, fill=BOTH, expand=1)

lstData4= Listbox(istFrame, bg = "green")
lstData4.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
