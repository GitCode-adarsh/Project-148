# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:09:20 2021

@author: Adarsh
"""
from tkinter import*
import random

root = Tk()
root.title("Random Number List")
root.configure(background = "red")
root.geometry("600x400")

List1 = ["Pencil","NoteBook","Chips","Chocolates","Tickets","Hanky","IdCard","Tiffin Box","Watch","Biscuits"]
random_item_list = Label(root,bg = "blue",fg ="white")
items_in_bag = Label(root,bg ="blue", fg="white")
def picnicbag():
    randomlist = random.sample(range(1,10),1)
    random_item_list["text"] = "Listed Items : "+str(List1)

    items_in_bag["text"] = "Put Item No : "+str(randomlist)+" In Bag"
    
btn=Button(root,text="Which item to put in bag?",command=picnicbag,bg="yellow",fg="red")
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

random_item_list.place(relx=0.5,rely=0.5,anchor=CENTER)
items_in_bag.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()