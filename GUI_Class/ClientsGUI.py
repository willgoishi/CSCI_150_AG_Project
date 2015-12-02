gclients = clients; 
class clients_class(Frame):                                             #<clients_class> class created for <clients> page when <clients> button is pressed at the main menu
    gclients = clients;
    def sequence(self, funct):
        for child in root.winfo_children():     #This is the loop that will go through the Frames widgets and delete the children
            child.destroy()
        return funct()

    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.master.title("Clients")
            
        new_database = Button(master, text =  "NEW CLIENTS DATABASE", command =  lambda:self.gclients.create_database());       #creates new database
        new_database.place(x=120, y=30);

        delete_database_gui = Button(master, text = "DELETE CLIENTS DATABASE", command=lambda:self.sequence(self.deleting_database));   #button to go to deleting database function
        delete_database_gui.place(x=130, y=550);

        new_sales_database = Button(master, text = "NEW SALES DATABASE", command = lambda: self.gclients.create_sales_db());    #creates new sales database
        new_sales_database.place(x=520, y=30);

        delete_sales_gui = Button(master, text = "DELETE SALES DATABASE", command = lambda:self.sequence(self.deleting_sales)); #button to go to deleting sales function
        delete_sales_gui.place(x=530, y=550);


        view_clients = Button(master, text = "VIEW CLIENTS", command=lambda: self.sequence(self.viewing_clients));
        view_clients.place(x=140, y=200);

        view_sales = Button(master, text = "VIEW SALES", command= lambda: self.sequence(self.viewing_sales));
        view_sales.place(x=540, y=200);

        search_by_name = Button(master, text = "SEARCH BY NAME", command = lambda: self.sequence(self.searching_by_name));
        search_by_name.place(x=130, y=400);

        search_by_prod = Button(master, text = "SEARCH BY PRODUCT", command = lambda: self.sequence(self.searching_by_prod));
        search_by_prod.place(x=530, y=400);

    
            
    # function that deletes entire clients database       
    def deleting_database(self, master = None):
        Frame.__init__(self, master);
        self.master.title("DELETING DATABASE");
        label0=Label(master, text = "DELETING THE DATABASE WILL \n ERASE ALL DATA PERMANENTLY");  #warning label
        label0.place(x=50, y=110);
        label1=Label(master, text = "DO YOU REALLY WANT TO DELETE THE DATABASE?")     #confirmation label question
        label1.place(x=50, y=170);
        label2=Label(master, text = "ENTER yes TO CONFIRM");  #confirmation label
        label2.place(x=50, y=200);
        answer=StringVar();
        entry1=Entry(master);                     #confirmation answer
        entry1.place(x=250, y= 200);
        print("answer: ", entry1.get());
        button1=Button(master, text = "CONFIRM", command=lambda:delete_confirm(entry1.get()));    #button to confirm delete confirmation answer
        button1.place(x=430, y=200);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));   #back button to go back to clients frame
        back_button.place(x=10, y=10);
        def delete_confirm(answer):       
            print("DELETING DATABASE2");
            print("YOUR ANSWER: ", answer);
            if(answer=="yes"):
                gclients.delete_database();
                print("DATABASE DELETED");
                label_confirm=Label(master, text="DELETED CLIENTS DATABASE");
                label_confirm.place(x=100, y=250);
            else:
                label_else=Label(master, text="DELETE CANCELLED");
                label_else.place(x=100, y=250);

    
            
    # function that deletes entire sales database
    def deleting_sales(self, master = None):
        Frame.__init__(self, master);
        self.master.title("DELETING SALES DATABASE");
        labela=Label(master, text = "DELETING THE DATABASE WILL \n ERASE ALL DATA PERMANENTLY");  #warning label
        labela.place(x=50, y=110);
        labelb=Label(master, text = "DO YOU REALLY WANT TO DELETE THE DATABASE?")     #confirmation label question
        labelb.place(x=50, y=170);
        labelc=Label(master, text = "ENTER yes TO CONFIRM");  #confirmation label
        labelc.place(x=50, y=200);
        entrya=Entry(master);                     #confirmation answer
        entrya.place(x=250, y= 200);
        print("answer: ", entrya.get());
        button1=Button(master, text = "CONFIRM", command=lambda:delete_sales_confirm(entrya.get()));    #button to confirm delete confirmation answer
        button1.place(x=430, y=200);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));       #back button to go back to clients frame
        back_button.place(x=10, y=10);
        def delete_sales_confirm(answer):       
            print("DELETING DATABASE2");
            print("YOUR ANSWER: ", answer);
            if(answer=="yes"):
                gclients.delete_sales_db();
                print("SALES DATABASE DELETED");
                label_confirm=Label(master, text="DELETED SALES DATABASE");
                label_confirm.place(x=100, y=250);
            else:
                label_else=Label(master, text="DELETE CANCELLED");
                label_else.place(x=100, y=250);


        

    #confirms entries for storing client info, used with function directly below
    def client_confirm(na, gui_id, gui_name, gui_phone, gui_email):
        gclients.store_client_info(gui_id, gui_name, gui_phone, gui_email); #calls function that stores information for new client
        print("\nNEW CLIENT: ", gui_name, "ADDED");
        
    #function that adds client
    def adding_client(self, master = None):
        Frame.__init__(self, master);
        self.master.title("ADD CLIENT");
        print("ADDING CLIENT");
        label_id = Label(master, text = ("ENTER ID: "));      #creates a label and entry for ID
        label_id.place(x=50, y=110);
        entry_id = Entry(master);
        entry_id.place(x=150, y=110);
        label_name = Label(master, text = ("ENTER NAME: "));     #creates a label and entry for name
        label_name.place(x=50, y=140);
        entry_name=Entry(master);
        entry_name.place(x=150, y=140);
        label_phone = Label(master, text = ("ENTER PHONE: "));     #creates a label and entry for phone number
        label_phone.place(x=50, y=170);
        entry_phone=Entry(master);
        entry_phone.place(x=150, y=170);
        label_email= Label(master, text = ("ENTER EMAIL: "));      # creates a label and entry for email
        label_email.place(x=50, y=200);
        entry_email=Entry(master);
        entry_email.place(x=150, y=200);
        store=Button(master, text = "CONFIRM", command=lambda:self.client_confirm((entry_id.get()), (entry_name.get()), (entry_phone.get()), (entry_email.get())) & self.sequence(self.viewing_clients));
        store.place(x=150, y=260);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.viewing_clients));    #back button to go back to clients frame
        back_button.place(x=10, y=10);



 #confirms entries for storing sales info, used with function directly below
    def sales_confirm(nothing, gui_num, gui_date, gui_name, gui_product, gui_quantity):
        gclients.store_sales_info(gui_num, gui_date, gui_name, gui_product, gui_quantity); #calls function that stores information for new client
        print("\nNEW SALES: ", gui_name, gui_product, gui_quantity, "ADDDED");

    #function that adds a sales entry   
    def adding_sales(self, master = None):
        Frame.__init__(self, master);
        self.master.title("ADD SALES");
        print("ADDING SALES");
        label_num = Label(master, text = ("ENTER SALES ID: "));
        label_num.place(x=50, y=110);
        entry_num=Entry(master);
        entry_num.place(x=250, y=110);
        label_date = Label(master, text = ("ENTER DATE: "));
        label_date.place(x=50, y=140);
        entry_date=Entry(master);
        entry_date.place(x=250, y=140);
        label_name = Label(master, text = ("ENTER CLIENT'S NAME: "));
        label_name.place(x=50, y=170);
        entry_name=Entry(master);
        entry_name.place(x=250, y=170);
        label_product = Label(master, text = ("ENTER PRODUCT NAME: "));
        label_product.place(x=50, y=200);
        entry_product=Entry(master);
        entry_product.place(x=250, y=200);
        label_quantity = Label(master, text = ("ENTER NUMERIC QUANTITY: "));
        label_quantity.place(x=50, y=230);
        entry_quantity=Entry(master);
        entry_quantity.place(x=250, y=230);
        store_sales=Button(master, text = "CONFIRM", command=lambda: self.sales_confirm((entry_num.get()), (entry_date.get()), (entry_name.get()), (entry_product.get()),(entry_quantity.get())) & self.sequence(self.viewing_sales));
        store_sales.place(x=250, y=260);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.viewing_sales));      #back button to go back to clients frame
        back_button.place(x=10, y=10);


    def deleting_client(self, master=None):
        self.master.title("DELETING CLIENT");
        label1=Label(master, text="ENTER NAME OF CLIENT YOU WANT TO DELETE: ");
        label1.place(x=50, y=200);
        entry1=Entry(master);
        entry1.place(x=375, y=200);
        labela=Label(master, text = "DELETING THE CLIENT WILL ERASE ALL CLIENT DATA PERMANENTLY");  #warning label
        labela.place(x=30, y=60);
        labelb=Label(master, text = "DO YOU REALLY WANT TO DELETE THE CLIENT?")     #confirmation label question
        labelb.place(x=50, y=90);
        confirm_button=Button(master, text="CONFIRM", command=lambda:delete_client_confirm(entry1.get()));
        confirm_button.place(x=600, y=200);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.viewing_clients));    #back button to go back to clients frame
        back_button.place(x=10, y=10);
        def delete_client_confirm(choice):
            print("DELETING ", choice);
            gclients.delete_client(choice);
            label_confirm=Label(master, text=("DELETED:", choice));
            label_confirm.place(x=100, y=250);
        
    def viewing_clients(self, master = None):
        Frame.__init__(self, master);
        self.master.title("VIEWING CLIENTS");
        print("VIEWING CLIENTS");
        scrollbar=Scrollbar(master, orient=VERTICAL);                   #creates scrollbar
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE);
        result=gclients.retrieve_client_data();                         #retrieves client data
        client_list=Listbox(master, yscrollcommand=scrollbar.set);      #creates list
        for row in result:                                              #inserts client data into list
            client_list.insert(END, row, "\n");                         #to the end of list
            client_list.place(x=5, y=100, width=780, height=575);
            scrollbar.config(command=client_list.yview);                #scrollbar command
        add_client = Button(master, text = "ADD NEW CLIENT", command=lambda:self.sequence(self.adding_client));      #button to go to add client function
        add_client.place(x=130, y=30);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));       #back button to go back to clients frame
        back_button.place(x=10, y=10);
        delete_client=Button(master, text="DELETE CLIENT", command = lambda:self.sequence(self.deleting_client));   #button to delete a client
        delete_client.place(x=650, y=10);

        
        

    def viewing_sales(self, master = None):
        Frame.__init__(self, master);
        self.master.title("VIEWING SALES");
        print("VIEWING SALES");
        result=gclients.retrieve_all_sales();
        scrollbar=Scrollbar(master, orient=VERTICAL);
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE);
        sales_list=Listbox(master, yscrollcommand=scrollbar.set);
        for row in result:
            sales_list.insert(END, row, "\n");
            sales_list.place(x=5, y=100, width=780, height=575);
            scrollbar.config(command=sales_list.yview);
        add_sales = Button(master, text ="ADD NEW SALES", command=lambda: self.sequence(self.adding_sales));          #button to go to add sales function
        add_sales.place(x=130, y=30);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));       #back button to go back to clients frame
        back_button.place(x=10, y=10);
        


        #function that searches through and returns all info in the clients and sales database that matches the entered name
    def searching_by_name(self, master = None):
        Frame.__init__(self, master);
        self.master.title("SEARCHING BY NAME");
        print("SEARCHING BY NAME");
        label_searchname=Label(master, text = ("ENTER NAME: "));
        label_searchname.place(x=50, y=100);
        entry_searchname=Entry(master);
        entry_searchname.place(x=150, y=100);
        confirm=Button(master, text="CONFIRM", command=lambda: show_searchname(entry_searchname.get()));
        confirm.place(x=350, y=100);
        scrollbar=Scrollbar(master, orient=VERTICAL);
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE);
        search_list=Listbox(master, yscrollcommand=scrollbar.set);
        def table_search(result):
            for row in result:
                search_list.insert(END, row, "\n");
                search_list.place(x=5, y=150, width=780, height=525);
                scrollbar.config(command=search_list.yview);
        def show_searchname(searched_name):
            print("YOU ENTERED: ", searched_name);
            result=gclients.search(searched_name);
            table_search(result);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));   #back button to go back to clients frame      
        back_button.place(x=10, y=10);
        
        
        #function that searches through the sales database and returns all info that match the entered product
    def searching_by_prod(self, master= None):
        Frame.__init__(self, master);
        self.master.title("SEACHING BY PRODUCT");
        print("SEARCHING BY PRODUCT");
        label_searchprod=Label(master, text = ("ENTER PRODUCT NAME: "));
        label_searchprod.place(x=50, y=100);
        entry_searchprod=Entry(master);
        entry_searchprod.place(x=250, y=100);
        confirm=Button(master, text="CONFIRM", command=lambda: show_searchprod(entry_searchprod.get()));
        confirm.place(x=450, y=100);
        scrollbar=Scrollbar(master, orient=VERTICAL);
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE);
        search_listprod=Listbox(master, yscrollcommand=scrollbar.set);
        def table_searchprod(result):
            for row in result:
                search_listprod.insert(END, row, "\n");
                search_listprod.place(x=5, y=150, width=780, height=525);
                scrollbar.config(command=search_listprod.yview);
        def show_searchprod(searched_prod):
            print("YOU ENTERED: ", searched_prod);
            result=gclients.searchbyprod(searched_prod);
            table_searchprod(result);
        back_button=Button(master, text="BACK", command=lambda:self.sequence(self.__init__));       #back button to go back to clients frame
        back_button.place(x=10, y=10);
