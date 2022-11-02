from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series: ")
label2 = Label(root, text="Fibonacci Sum: ")
enter_num = Entry(root)
enter_num.place(relx=0.5,rely=0.2,anchor=CENTER)


def Fibonacci():
    num = int(enter_num.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label2["text"] = "Fibonacci sum: " + str(sum2) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum


btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)

btn.pack()
label_series.pack()
label2.pack()

root.mainloop()