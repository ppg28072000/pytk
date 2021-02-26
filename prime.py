from tkinter import *
def main():
    result = "NULL";
    def closest_prime(num):
        #checking above
        numU = num;
        numL = num;
        go =1;
        while(go):#proceed if prime not find
            numU = numU+1;
            go = prime_true(numU);
        go =1;
        while(go):
            numL = numL -1;
            go = prime_true(numL);
        return numL,numU;
    def prime_true(num):# sends 1 if prime not found
        flag = 1;
        i=2;
        while(flag==1 and i<num):
            a = num%i;
            i = i+1;
            if(a==0):
                flag =0;
                return 1;
        return 0;
    def show_form():
        timevar = IntVar();
        entry = Frame(slots,borderwidth = "6",width = "300",height = "300");
        entry.pack(side=LEFT,padx = 6);
        title = Label(entry,text = "Title",bg ="gray71",font="Helvatica 8 bold");
        title.pack(side = TOP,pady = 6,anchor = "n",fill = "y");
        time =Label(entry,text = "Time",bg ="gray71",font="Helvatica 8 bold");
        time.pack(side = LEFT,pady = 6);
        timEnt = Entry(entry,textvariable = timevar);
        timEnt.pack(side = LEFT);
        #sub = Button(entry,text = "submit",fg = "red",command = )
        
    def check_prime(event=0):		
        global result
        num = number.get();
        flag = 1;
        i = 2;
        result = "UTTAMAM tava etat ankah abhaajya asti"
        while(flag==1 and i<num):
            a = num%i;
            i= i+1;
            if(a==0):
                flag = 0;
                A = closest_prime(num);
                result = "NAA etat ankah abhaajya naasti |\n kripayaa anya anken punahah prayasa karatu | Etat anke sameepau dvi ankah : "+str(A[0])+" and "+str(A[1]);
        output.config(text = result);

    
    
    root = Tk()
    root.geometry("744x344");
    f=IntVar(root,value = 0);
    number = IntVar();
    out = StringVar(value = "nULL");
    inpFrame = Frame(root,bg = "bisque",borderwidth = "6", relief = SUNKEN,width="400");
    inpFrame.pack(side = TOP,fill="x")
    head = Label(inpFrame,text = "kripaya dhanatmak anka enter karatu gyaataaya tata abhaajya asti kim ",font="Helvatica 12 bold");
    head.pack(fill = "x");
    num = Label(inpFrame, text = "Your Number:",bg = "#b22222",font="Helvatica 12 bold");
    num.pack(side = LEFT);
    numEntry = Entry(inpFrame, textvariable = number);
    numEntry.pack(side = LEFT);
    go = Button(inpFrame, text = "GO",command=check_prime,font="Helvatica 12 bold");
    go.pack(side= LEFT);
    outFrame = Frame(root,bg = "#b20022",borderwidth = "6", relief = SUNKEN,width="300",height="400");
    outFrame.pack(side = TOP,fill="x")
    output = Label(outFrame,text = result,font="Helvatica 12 bold",fg="blue");
    output.pack();
    # tic tac toe
    schdFrame = Frame(root,bg = "yellow",borderwidth = "6", relief = SUNKEN, width = "300",height = "400");
    schdFrame.pack(side = TOP, fill = "x");
    ttinfo = Label(schdFrame,text = "tava samayasaarini atra likhatu", font = "Helvatica 10 bold");
    ttinfo.pack();
    add = Button(schdFrame,text = "Add an entry",command = show_form,borderwidth = "6", relief = SUNKEN,font = "Helvatica 8 bold");
    add.pack(side = LEFT);
    slots = Frame(schdFrame,bg = "tomato",borderwidth = "7",relief = SUNKEN, width = "100",height = "400");
    slots.pack(side = LEFT);
    root.bind("<Return>",check_prime);
    #root.bind("<Button-1>",check_prime);
    root.mainloop()
main();
