from tkinter import *
def main():
    result = "NULL";
    num_entries = 0;
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
    
    def add_form():
        def add_entry():
            #global num_entries
            #num_entries = num_entries +1;
            file = open("time_table.txt","a+");
            file.write(str(1)+"\n");
            file.write(str(timevar1.get())+"\n");
            file.write(str(timevar2.get())+"\n");
            file.write(str(titlevar.get())+"\n");
            #file.write(str(cmntEnt.get())+"\n");
            file.close();
            add.pack();
            entry.forget();
            show_tt();
        timevar1 = IntVar();
        timevar2 = IntVar();
        titlevar = StringVar();
        add.forget();
        entry = Frame(slots,borderwidth = "6",width = "100",height = "400");
        entry.pack();
        sn = Label(slots,text = str(num_entries),font="Helvatica 6 italic");
        sn.pack();
        
        time1 =Label(entry,text = "StartTime",fg ="black",font="Helvatica 8 bold");
        time1.pack();
        timEnt1 = Entry(entry,textvariable = timevar1);
        timEnt1.pack();
        time2 = Label(entry,text="EndTime",fg ="red",font="Helvatica 8 bold");
        time2.pack();
        timEnt2 = Entry(entry,textvariable = timevar2);
        timEnt2.pack();

        title = Label(entry,text = "Title",fg ="blue",font="Helvatica 8 bold");
        title.pack();
        titleEnt = Entry(entry,textvariable = titlevar);
        titleEnt.pack();

        cmnt = Label(entry,text = "Description",bg ="gray71",font="Helvatica 8 bold");
        cmnt.pack();
        cmntEnt = Text(entry,height = "2");
        cmntEnt.pack();
        sub = Button(entry,text = "submit",fg = "red",command =add_entry,borderwidth = "6", relief = SUNKEN);
        sub.pack();
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
    def show_tt():
        
        file = open("time_table.txt","r");
        while(1):
            sn = file.readline();
            if not sn:
                
                break;
            else:
                title = file.readline();
                time1 = file.readline();
                time2 = file.readline();
                cmnt = file.readline();
                show_entry(sn,title,time1,time2,cmnt);
                global num_entries;
                num_entries = int(sn); 
    def show_entry(sn,title,time1,time2,cmnt):
        entry = Frame(slots,borderwidth = "6",width = "40",height = "400",relief = SUNKEN,bg = "lawn green");
        entry.grid(column = sn,row = 1);
        SN = Label(entry,text = sn,fg = "black",font = "helvatica 10 bold",relief = SUNKEN);
        SN.pack();
        TITLE = Label(entry,text = title,fg = "black",font = "helvatica 10 bold");
        TITLE.pack(fill="x");
        TIME = Label(entry,text = str(time1)+ " to" + str(time2),fg = "orange",font = "helvatica 10 bold");
        TIME.pack(fill ="x");
        CMNT = Label(entry,text = cmnt,fg = "orange",font = "helvatica 10 bold");
        CMNT.pack();
    
    
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
    # timetable
    schdFrame = Frame(root,bg = "yellow",borderwidth = "6", relief = SUNKEN, width = "300",height = "400");
    schdFrame.pack(side = TOP, fill = "x");
    ttinfo = Label(schdFrame,text = "tava samayasaarini atra likhatu", font = "Helvatica 10 bold");
    ttinfo.pack();
    add = Button(schdFrame,text = "Add an entry",command = add_form,borderwidth = "6", relief = SUNKEN,font = "Helvatica 8 bold");
    add.pack(side = RIGHT);
    slots = Frame(schdFrame,bg = "tomato",borderwidth = "7",relief = SUNKEN, width = "100",height = "400");
    slots.pack(side = LEFT);
    show_tt();
    root.bind("<Return>",check_prime);
    #root.bind("<Button-1>",check_prime);
    root.mainloop()
main();
