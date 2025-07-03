

from tkinter import *
import oracledb

conn=oracledb.connect(user="PWDMANAGER", password="pwdpassword", dsn="localhost:1521/FREEPDB1")
cursor=conn.cursor()


# function that shows new window with all passwords
def passwords(userid):
    root = Tk()
    root.title("Passwords")
    root.geometry("400x340")
    root.resizable(False, False)
    title_font = ("Bahnschrift SemiLight SemiConde", 20)
    fnt = ("Javanese Text", 13)
    error_font = ("Javanese Text", 9)
    retrieved_password = StringVar()

    # Function to clear the screen completely
    def clear_widgets():
        user_id_lbl.place_forget()
        user_id_ent.place_forget()
        password_lbl.place_forget()
        password_ent.place_forget()
        website_ent.place_forget()
        website_lbl.place_forget()
        url_ent.place_forget()
        url_lbl.place_forget()
        email_ent.place_forget()
        email_lbl.place_forget()
        password_lst.place_forget()
        error_lbl.place_forget()    
        addtodb_but.place_forget()
        select_but.place_forget()
        remove_but.place_forget()
        show_pass_lbl.place_forget()
        update_but.place_forget()
        update_password_ent.place_forget()

    # Function to show relevant widgets for adding password
    def add_passwords():
        clear_widgets()
        website_lbl.place(x=100, y=100, anchor=CENTER)
        url_lbl.place(x=100, y=140, anchor=CENTER)
        user_id_lbl.place(x=100, y=180, anchor=CENTER)
        email_lbl.place(x=100, y=220, anchor=CENTER)
        password_lbl.place(x=100, y=260, anchor=CENTER)
        
        website_ent.place(x=300, y=100, anchor=CENTER)
        url_ent.place(x=300, y=140, anchor=CENTER)
        user_id_ent.place(x=300, y=180, anchor=CENTER)
        email_ent.place(x=300, y=220, anchor=CENTER)
        password_ent.place(x=300, y=260, anchor=CENTER)
        
        addtodb_but.place(x=200, y=320, anchor=CENTER)
        
    # Function to show relevant widgets for getting passwords
    def get_passwords():
        clear_widgets()
        insert_account()
        password_lst.place(x=70, y=190, anchor=CENTER)
        show_pass_lbl.place(x=300, y=120, anchor=CENTER)
        remove_but.place(x=320, y=300, anchor=CENTER)
        select_but.place(x=200, y=300, anchor=CENTER)
        update_but.place(x=260, y=300, anchor=CENTER)
        
        website_lbl.place(x=170, y=80, anchor=CENTER)
        url_lbl.place(x=170, y=120, anchor=CENTER)
        user_id_lbl.place(x=170, y=160, anchor=CENTER)
        email_lbl.place(x=170, y=200, anchor=CENTER)
        password_lbl.place(x=170, y=240, anchor=CENTER)
        
        website_ent.place(x=300, y=80, anchor=CENTER)
        url_ent.place(x=300, y=120, anchor=CENTER)
        user_id_ent.place(x=300, y=160, anchor=CENTER)
        email_ent.place(x=300, y=200, anchor=CENTER)
        password_ent.place(x=300, y=240, anchor=CENTER)

    def insert_into_db():
        cursor.execute("select count(*) from useraccounts")
        number=cursor.fetchone()[0]+1
        username=user_id_ent.get("1.0", "end-1c")
        password=password_ent.get("1.0", "end-1c")
        website=website_ent.get("1.0", "end-1c")
        url=url_ent.get("1.0", "end-1c")
        email=email_ent.get("1.0", "end-1c")
        
        cursor.execute("select accountid from useraccounts where websitename=:1 and accountname=:2", (website, username))
        data=cursor.fetchall()
        if(data):
            error_lbl.config(text="There alread exists a password for this website and username", fg="red")
            error_lbl.place(x=200, y=290, anchor=CENTER)
            return

        
        if(website=="" or password==""):
            error_lbl.config(text="Password/Website feild should not be empty", fg="red")
            error_lbl.place(x=200, y=290, anchor=CENTER)
            return
        
        cursor.execute("insert into useraccounts values(:1,:2,:3,:4,:5,:6,:7)",(number,userid,username,url,password,website,email))
        conn.commit()
        
        error_lbl.config(text="Successfully created", fg="grey")
        error_lbl.place(x=200, y=290, anchor=CENTER)
        
    def showpassword():
        website=password_lst.get(password_lst.curselection())
        cursor.execute("select * from useraccounts where accountid=:1",(hiddendict[website],))
        W=cursor.fetchone()
        website_ent.delete(1.0, "end")
        website_ent.insert(1.0, W[5])
        url_ent.delete(1.0, "end")
        url_ent.insert(1.0, W[3])
        user_id_ent.delete(1.0, "end")
        user_id_ent.insert(1.0, W[2])
        email_ent.delete(1.0, "end")
        email_ent.insert(1.0, W[6])
        password_ent.delete(1.0, "end")
        password_ent.insert(1.0, W[4])

    def update_password():
        error_lbl.config(text="")
        error_lbl.place(x=200, y=290, anchor=CENTER)
        username=user_id_ent.get("1.0", "end-1c")
        password=password_ent.get("1.0", "end-1c")
        website=website_ent.get("1.0", "end-1c")
        url=url_ent.get("1.0", "end-1c")
        email=email_ent.get("1.0", "end-1c")
        
        if(website=="" or password==""):
            error_lbl.config(text="Password/Website feild should not be empty", fg="red")
            error_lbl.place(x=200, y=270, anchor=CENTER)
            return
        
        try:
            cursor.execute("update useraccounts set accountname=:1, accounturl=:2, accountpassword=:3, websitename=:4, email_id=:5 where accountid=:6", (username, url, password, website, email, hiddendict[website]))
            conn.commit()
        except KeyError:
            error_lbl.config(text="Website name cannot be changed", fg="red")
            error_lbl.place(x=200, y=270, anchor=CENTER)
            return
        
        error_lbl.config(text="Successfully created", fg="grey")
        error_lbl.place(x=200, y=290, anchor=CENTER)
        
            
    def remove_account():
        removing_account=password_lst.get(password_lst.curselection())
        print(removing_account)
        I=password_lst.get(0,END).index(removing_account)
        password_lst.delete(I)
        cursor.execute("delete from useraccounts where accountid=:1",(hiddendict[removing_account],))
        conn.commit()
        website_ent.delete(1.0, "end")
        url_ent.delete(1.0, "end")
        user_id_ent.delete(1.0, "end")
        email_ent.delete(1.0, "end")
        password_ent.delete(1.0, "end")
        

    hiddendict = dict()
    password_lst = Listbox(root, height=15, width=13)
    def insert_account():
        password_lst.delete(0,END)
        cursor.execute("select * from useraccounts where userid =:1 order by websitename",(userid,))
        hiddendict.clear()
        L=cursor.fetchall()
        for i in range(len(L)):
            website=str(L[i][5])
            accountid=L[i][0]       
            hiddendict[website]=accountid
            password_lst.insert(i, website)
            
    title_label = Label(root, text="PASSWORDS", font=title_font)
    
    error_lbl = Label(root, font=error_font)
    
    add_but = Button(root, text='Add Password', bd=0, command=add_passwords)  
    get_but = Button(root, text='Show Passwords', bd=0, command=get_passwords)  
    
    website_lbl = Label(root, text="Website", font=fnt)
    url_lbl = Label(root, text="Link", font=fnt)
    user_id_lbl = Label(root, text="Username", font=fnt)   
    email_lbl = Label(root, text="Email", font=fnt)
    password_lbl = Label(root, text="Password", font=fnt)
    
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break" 
    def prevent_newline(event):
        return "break"
    
    website_ent = Text(root, wrap="none", height=1, width=18)
    website_ent.bind("<Return>", prevent_newline)
    website_ent.bind("<Tab>", focus_next_widget)
    url_ent = Text(root, wrap="none", height=1, width=18)
    url_ent.bind("<Return>", prevent_newline)
    url_ent.bind("<Tab>", focus_next_widget)
    user_id_ent = Text(root, wrap="none", height=1, width=18)
    user_id_ent.bind("<Return>", prevent_newline)
    user_id_ent.bind("<Tab>", focus_next_widget)
    email_ent = Text(root, wrap="none", height=1, width=18)
    email_ent.bind("<Return>", prevent_newline)
    email_ent.bind("<Tab>", focus_next_widget)
    password_ent = Text(root, wrap="none", height=1, width=18)
    password_ent.bind("<Return>", prevent_newline)
    password_ent.bind("<Tab>", focus_next_widget)
    
    addtodb_but = Button(root, text="Add", padx=5,command=insert_into_db)

    remove_but = Button(root, text="Remove", command=remove_account)
    select_but = Button(root, text="Show", padx=10, command=showpassword)
    update_but = Button(root, text="Update", padx=8, command=update_password)
    show_pass_lbl = Label(root, textvariable=retrieved_password)
    update_password_ent=Text(root, wrap="none", height=1, width=18)
    password_ent.bind("<Return>", prevent_newline)
    password_ent.bind("<Tab>", focus_next_widget)

    title_label.place(x=200, y=15, anchor=CENTER)

    add_but.place(x=100, y=45, anchor=CENTER)
    get_but.place(x=300, y=45, anchor=CENTER)

    root.mainloop()

# function that shows new window to create new account
def sign_up():
    root = Tk()
    root.title("Password Manager")
    root.geometry("400x250")
    root.resizable(False, False)
    title_font = ("Bahnschrift SemiLight SemiConde", 20)
    fnt = ("Javanese Text", 13)
    error_font = ("Javanese Text", 9)
        
    def back():
        root.destroy()
        main()

    title_label = Label(root, text="CREATE ACCOUNT", font=title_font)
    username_lbl = Label(root, text="Username", font=fnt)
    password_lbl = Label(root, text="Password", font=fnt)
    rpassword_lbl = Label(root, text="Confirm Password", font=fnt)
    error_lbl = Label(root, text="Passwords do not match", font=error_font)


    username_ent = Entry(root)
    password_ent = Entry(root, show="*")
    rpassword_ent = Entry(root, show="*")

    back_but = Button(root, text='Back', command=back, padx=5)

    title_label.place(x=200, y=30, anchor=CENTER)
    username_lbl.place(x=100, y=90, anchor=CENTER)
    password_lbl.place(x=100, y=135, anchor=CENTER)
    rpassword_lbl.place(x=100, y=180, anchor=CENTER)

    username_ent.place(x=300, y=86, anchor=CENTER)
    password_ent.place(x=300, y=131, anchor=CENTER)
    rpassword_ent.place(x=300, y=176, anchor=CENTER)
    back_but.place(x=250, y=220, anchor=CENTER)
    
    def create_account():
        cursor.execute("select count(userid) from usernames")
        number=cursor.fetchone()[0]+1
        
        username=username_ent.get()
        password=password_ent.get()
        rpassword=rpassword_ent.get()
        
        error_lbl.config(text="")        
        
        if 4<len(username)<20:
            error_lbl.config(text="Username should be between 4 and 20 characters", fg="red")
            error_lbl.place(x=200, y=200, anchor=CENTER)
            return
        
        if not username or not password or not rpassword:
            error_lbl.config(text="All fields are required", fg="red")
            error_lbl.place(x=200, y=200, anchor=CENTER)
            return
        
        if(rpassword!=password):
            error_lbl.config(text="Passwords do not match", fg="red")
            error_lbl.place(x=200, y=200, anchor=CENTER)
            return
        
        cursor.execute("select username from usernames where username=:1", (username,))
        if cursor.fetchone():
            error_lbl.config(text="Username already exists", fg="red")
            error_lbl.place(x=200, y=200, anchor=CENTER)
            return
        
        cursor.execute("insert into usernames values(:1, :2)", (number, username))
        cursor.execute("insert into passwords values(:1, :2)", (number, password))
        conn.commit()

        error_lbl.config(text="Account created successfully!", fg="green")
        error_lbl.place(x=200, y=200, anchor=CENTER)
        
    create_but = Button(root, text='Create',command=create_account)
    create_but.place(x=150, y=220, anchor=CENTER)
    root.mainloop()


# main function that gets called where you can sign in
def main():
    global p
    root = Tk()
    root.title("Password Manager")
    root.geometry("420x250")
    root.resizable(False, False)
    title_font = ("Bahnschrift SemiLight SemiConde", 20)
    fnt = ("Javanese Text", 13)
    error_font = ("Javanese Text", 9)
    pwd_block = "*"
    p = True

    # Create main menu with sign in and sign up options
    title_label = Label(root, text="PASSWORD MANAGER", font=title_font)
    username_lbl = Label(root, text="Username", font=fnt)
    password_lbl = Label(root, text="Password", font=fnt)
    error_lbl = Label(root, text="Invalid username/password", font=error_font, fg="red")

    username_ent = Entry(root)
    password_ent = Entry(root, show=pwd_block)

    # Close window
    def destroy():
        root.destroy()

    # close current window and open sign up window
    def signup_inter():
        destroy()
        sign_up()

    # close current window and open passwords window
    def passwords_inter():
        username=username_ent.get()
        password=password_ent.get()
        cursor.execute("select u.userid, u.username, p.userpass from usernames u, passwords p")
        data=cursor.fetchall()
        for i in data:
            if username in i and password in i:
                userid=i[0]
                destroy()
                passwords(userid)
                break
        error_lbl.place(x=210, y=170, anchor=CENTER)    

    # show password when button is pressed
    def show_pwd():
        global p
        if p:
            password_ent.configure(show="")
            p = False
        else:
            password_ent.configure(show="*")
            p = True

    pwd_unlock_but = Button(root, text="Show", bd=0, command=show_pwd)
    signin_but = Button(root, text="Sign In", command=passwords_inter)
    exit_but = Button(root, text="Exit", padx=10, command=destroy)
    signup_but = Button(root, text="Click here to Sign Up", bd=0, command=signup_inter)

    # Place main menu objects onto screen
    title_label.place(x=210, y=30, anchor=CENTER)
    username_lbl.place(x=105, y=90, anchor=CENTER)
    password_lbl.place(x=105, y=140, anchor=CENTER)

    username_ent.place(x=310, y=86, anchor=CENTER)
    password_ent.place(x=310, y=136, anchor=CENTER)

    pwd_unlock_but.place(x=385, y=136, anchor=CENTER)
    signin_but.place(x=160, y=200, anchor=CENTER)
    exit_but.place(x=260, y=200, anchor=CENTER)
    signup_but.place(x=210, y=235, anchor=CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()