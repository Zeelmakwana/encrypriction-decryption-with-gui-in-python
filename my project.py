from tkinter import *
k=Tk()
def enc():
	tk=Tk()
	tk.geometry("800x800")
	Label(tk,text='ENTER YOUR PASSWORD').pack()
	z=Entry(tk)
	z.pack()
	
	def en():
		
		p=z.get()
		tp1=[]
		for i in range  (0,3,1):
		    tp1.append(p[i:i+1])
		tp2=[]
		for i in range  (3,6,1):
		    tp2.append(p[i:i+1])
		tp3=[]
		for i in range  (6,9,1):
		    tp3.append(p[i:i+1])
	
	
		t1=[]
		for i in tp1:
			t1.append((int(i)*5))
		t2=[]
		for i in tp2:
			t2.append((int(i)*5))
		t3=[]
		for i in tp3:
			t3.append((int(i)*5))
		k=t1+t2+t3
	
		Label(tk,text='#').pack()
		
		v=''	
		for l in k:
			v+=str(l)
		with open("mn.txt","a") as f:
			f.write(v)
			f.write(' = ')
			f.write(p)
			f.write('\n')
		Label(tk,text=v).pack()
		
	Button(tk,text="click",command=en).pack()
	
	tk.mainloop()


def dec():
	tk2=Tk()
	tk2.geometry("900x900")
	def dec1():
		with open('mn.txt','r') as r:
			g=e.get()
			while 1:
				m=r.readline().split()
				if m!=[]:
					if m[0]==g:
						Label(tk2,text=m[2]).pack()
						break
					else: Label(tk2,text='Not Value Found').pack()
					break
	
	Label(tk2,text='enter your secret code = ').pack()
	e=Entry(tk2)
	e.pack()
	Button(tk2,text='Click',command=dec1).pack()
	tk2.mainloop()

f1=Frame(k,bg='red')
f1.pack()
B1=Button(f1,text='enc',command=enc)
B1.pack()

f2=Frame(k,bg='blue')
f2.pack()
Button(text='dec',command=dec).pack()





k.mainloop()
	