from tkinter import*

root = Tk()

root.title("Multi Dimensional Arrays")
root.geometry("500x500")

label = Label(root)
label1 = Label(root)
label2 = Label(root)

array_1d = ["John", "James", "Thomsan"]
#print(array_1d[2])

array_2d = [["John", "A"],["James", "B"],["Thomsan", "C"]]
#print(array_2d[2][1])
#print(array_2d[1])

array_3d = [[["John", "A+", "excellent"], ["James", "A", "very good"], ["Thomsan", "B", "good"] ]]
print(array_3d [0][0][1])

def report():
    label["text"]= array_3d[0][0][0] + " got grade " + array_3d[0][0][1] + " and he's doing " + array_3d[0][0][2]
    label1["text"]= array_3d[0][1][0] + " got grade " + array_3d[0][1][1] + " and he's doing " + array_3d[0][1][2]
    label2["text"]= array_3d[0][2][0] + " got grade " + array_3d[0][2][1] + " and he's doing "+ array_3d[0][2][2]

btn = Button(root, text="report", command=report)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)
label.place(relx=0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()