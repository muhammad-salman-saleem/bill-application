from tkinter import*
import math,random,os
from tkinter import messagebox




class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+100+50")
        self.root.title("Bolling Software")
        root.resizable(False, False)
        # bg_color="#074463"
        bg_color="#36454F"
        p_color="#D3D3D3"
        btn_color="#993333"
        # icon
        image_icon = PhotoImage(file="bill icon.png")
        root.iconphoto(False, image_icon)
        # Title
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #===================Variable========================
        #=============Cosmatic===============
        self.Bath_Soap=IntVar()
        self.Face_Cream=IntVar()
        self.Face_Wash=IntVar()
        self.Hair_Spray=IntVar()
        self.Hair_Gell=IntVar()
        self.Loshan=IntVar()

        #=============Grocery===============
        self.Rice=IntVar()
        self.Food_Oil=IntVar()
        self.Daal=IntVar()
        self.Wheat=IntVar()
        self.Sugar=IntVar()
        self.Tea=IntVar()

        #=============Cold Drink===============
        self.Mirinda=IntVar()
        self.Coca_Cola=IntVar()
        self.Fanta=IntVar()
        self.Dew=IntVar()
        self.Sprite=IntVar()
        self.pepsi=IntVar()

        #=============Total Product Price & Tex================
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.drinks_price=StringVar()

        self.cosmetics_tex=StringVar()
        self.grocery_tex=StringVar()
        self.drinks_tex=StringVar()

        #==============Customer================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #========================= Customer Detail Frame ===============================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",18,"bold"),).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,font=("arial",15),textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphone_lbl = Label(F1, text="Phone No.", fg="white", bg=bg_color,font=("times new roman", 18, "bold"), ).grid(row=0, column=2, padx=20, pady=5)
        cphone_text = Entry(F1, width=15, font=("arial", 15),textvariable=self.c_phone, bd=7, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=10)

        c_bill_lbl = Label(F1, text="Bill Number", fg="white", bg=bg_color,font=("times new roman", 18, "bold"), ).grid(row=0, column=4, padx=20, pady=5)
        c_bill_text = Entry(F1, width=15, font=("arial", 15),textvariable=self.search_bill, bd=7, relief=SUNKEN).grid(row=0, column=5, padx=5, pady=10)

        bill_btn=Button(F1,text="Search",command=self.Find_Bill, width=10,bg="white",fg="black", font=("arial", 15,"bold"),).grid(row=0, column=6, padx=10, pady=10)
        #========================= Cosmetics Frame=========================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),)
        F2.place(x=5,y=180,width=325,height=395)

        bath_lbl=Label(F2,text="Bath Soap",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_text=Entry(F2,width=10,textvariable=self.Bath_Soap,font=("arial",16),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=1,pady=10)

        Face_Cream_lbl=Label(F2,text="Face Cream",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_Cream_text=Entry(F2,width=10,textvariable=self.Face_Cream,font=("arial",16),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=1,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_text=Entry(F2,width=10,textvariable=self.Face_Wash,font=("arial",16),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=1,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_text=Entry(F2,width=10,textvariable=self.Hair_Spray,font=("arial",16),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=1,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gell",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_text=Entry(F2,width=10,textvariable=self.Hair_Gell,font=("arial",16),bd=7,relief=SUNKEN).grid(row=4,column=1,padx=1,pady=10)

        Body_l_lbl=Label(F2,text="Loshan",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_l_text=Entry(F2,width=10,textvariable=self.Loshan,font=("arial",16),bd=7,relief=SUNKEN).grid(row=5,column=1,padx=1,pady=10)



        # bath_lbl=Label(F2,text="Bath Soap",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        # bath_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=6,column=1,padx=1,pady=10)
        #
        # Face_Cream_lbl=Label(F2,text="Face Cream",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=7,column=0,padx=10,pady=10,sticky="w")
        # Face_Cream_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=7,column=1,padx=1,pady=10)
        #
        # Face_w_lbl=Label(F2,text="Face Wash",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=8,column=0,padx=10,pady=10,sticky="w")
        # Face_w_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=8,column=1,padx=1,pady=10)
        #
        # Hair_s_lbl=Label(F2,text="Hair Spray",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=9,column=0,padx=10,pady=10,sticky="w")
        # Hair_s_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=9,column=1,padx=1,pady=10)
        #
        # Hair_g_lbl=Label(F2,text="Hair Gell",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=10,column=0,padx=10,pady=10,sticky="w")
        # Hair_g_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=10,column=1,padx=1,pady=10)
        #
        # Body_l_lbl=Label(F2,text="Loshan",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=11,column=0,padx=10,pady=10,sticky="w")
        # Body_l_text=Entry(F2,width=10,font=("arial",16),bd=7,relief=SUNKEN).grid(row=11,column=1,padx=1,pady=10)

        # scrol_y = Scrollbar(F2, orient=VERTICAL)
        # self.textarea = Text(F2, yscrollcommand=scrol_y.set)
        # scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y.config(command=self.textarea.yview)
        # self.textarea.pack(fill=BOTH, expand=1)
        #========================= Grocery Frame=========================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),)
        F3.place(x=340,y=180,width=325,height=395)

        rice_lbl=Label(F3,text="Rice",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_text=Entry(F3,width=10,textvariable=self.Rice,font=("arial",16),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Food_O_lbl=Label(F3,text="Cooking Oil",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_O_text=Entry(F3,width=10,textvariable=self.Food_Oil,font=("arial",16),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_text=Entry(F3,width=10,textvariable=self.Daal,font=("arial",16),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl=Label(F3,text="Wheat",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_text=Entry(F3,width=10,textvariable=self.Wheat,font=("arial",16),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl=Label(F3,text="Sugar",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_text=Entry(F3,width=10,textvariable=self.Sugar,font=("arial",16),bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tea_lbl=Label(F3,text="Tea",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_text=Entry(F3,width=10,textvariable=self.Tea,font=("arial",16),bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #========================= Cold Drink Frame=========================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),)
        F4.place(x=675,y=180,width=325,height=395)

        Maza_lbl=Label(F4,text="Mirinda",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Maza_text=Entry(F4,width=10,textvariable=self.Mirinda,font=("arial",16),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Coke_lbl=Label(F4,text="Coka Cola",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Coke_text=Entry(F4,width=10,textvariable=self.Coca_Cola,font=("arial",16),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Fanta_lbl=Label(F4,text="Fanta",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Fanta_text=Entry(F4,width=10,textvariable=self.Fanta,font=("arial",16),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Dew_lbl=Label(F4,text="Dew",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Dew_text=Entry(F4,width=10,textvariable=self.Dew,font=("arial",16),bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sprite_lbl=Label(F4,text="Sprite",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sprite_text=Entry(F4,width=10,textvariable=self.Sprite,font=("arial",16),bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Pepsi_lbl=Label(F4,text="Pepsi",fg=p_color,bg=bg_color,font=("times new roman",16,"bold"),).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Pepsi_text=Entry(F4,width=10,textvariable=self.pepsi,font=("arial",16),bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====================== Bill Area =========================
        F5=Frame(self.root,bd=10,relief=GROOVE,)
        F5.place(x=1010,y=180,width=335,height=395)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #========================== Button Frame ========================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",bg=bg_color,fg="gold",font=("times new roman",15,"bold"),)
        F6.place(x=0,y=580,relwidth=1,height=150)

        tcos_p_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        tcos_p_text = Entry(F6, width=18,textvariable=self.cosmetics_price, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        tgoc_p_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
        tgoc_p_text = Entry(F6, width=18,textvariable=self.grocery_price, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=5)

        tcd_p_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        tcd_p_text = Entry(F6, width=18,textvariable=self.drinks_price, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)


        tcos_t_lbl=Label(F6,text="Cosmetic Tex",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        tcos_t_text = Entry(F6, width=18,textvariable=self.cosmetics_tex, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        tgoc_t_lbl=Label(F6,text="Grocery Tex",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=5,sticky="w")
        tgoc_t_text = Entry(F6, width=18,textvariable=self.grocery_tex, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=5)

        tcd_t_lbl=Label(F6,text="Cold Drink Tex",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        tcd_t_text = Entry(F6, width=18,textvariable=self.drinks_tex, font=("arial", 10), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=740,width=585,height=110)

        Total_btn=Button(btn_F,text="Total",command=self.total,bg=btn_color,fg="white",pady=15,width=10,bd=3,font="arial 15 bold").grid(row=0, column=0, padx=5, pady=10)
        GBill_btn=Button(btn_F,text="Gentare Bill",command=self.bill_area,bg=btn_color,fg="white",pady=15,width=10,bd=3,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=10)
        Cleare_btn=Button(btn_F,text="Cleare",command=self.clear_data, bg=btn_color,fg="white",pady=15,width=10,bd=3,font="arial 15 bold").grid(row=0, column=2, padx=5, pady=10)
        Exit_btn=Button(btn_F,text="Exit",command=self.ext_app, bg=btn_color,fg="white",pady=15,width=10,bd=3,font="arial 15 bold").grid(row=0, column=3, padx=5, pady=10)


        #==================== Coppy Right Frame================
        LabelFrame(self.root, text="Designe By Muhammad Salman @ Copyright by graphictech", font="arial 8 bold",bg="White",  fg="black" ,borderwidth=0,labelanchor=S,).place(x=0, y=728, relwidth=1, height=15)
        self.wellcome_bill()
    def total(self):
        self.c_s_p=self.Bath_Soap.get() * 90
        self.c_fc_p=self.Face_Cream.get() * 150
        self.c_fw_p=self.Face_Wash.get() * 250
        self.c_hs_p=self.Hair_Spray.get() * 180
        self.c_hg_p=self.Hair_Gell.get() * 320
        self.c_l_p=self.Loshan.get() * 170
        self.total_cosmetics_price=float(
                                            self.c_s_p +
                                            self.c_fc_p +
                                            self.c_fw_p +
                                            self.c_hs_p +
                                            self.c_hg_p +
                                            self.c_l_p
                                         )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
        self.c_tex=round((self.total_cosmetics_price*0.05),2)
        self.cosmetics_tex.set("Rs. "+str(self.c_tex))

        self.g_r_p=self.Rice.get() * 210
        self.g_fo_p=self.Food_Oil.get() * 530
        self.g_d_p=self.Daal.get() * 240
        self.g_w_p=self.Wheat.get() * 90
        self.g_s_p=self.Sugar.get() * 100
        self.g_t_p=self.Tea.get() * 230
        self.total_grocery_price = float(
                                            self.g_r_p +
                                            self.g_fo_p +
                                            self.g_d_p +
                                            self.g_w_p +
                                            self.g_s_p +
                                            self.g_t_p

                                        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tex=round((self.total_grocery_price * 0.1),2)
        self.grocery_tex.set("Rs. " + str(self.g_tex))

        self.cd_m_p=self.Mirinda.get() * 70
        self.cd_cc_p=self.Coca_Cola.get() * 150
        self.cd_f_p=self.Fanta.get() * 120
        self.cd_d_p=self.Dew.get() * 150
        self.cd_s_p=self.Sprite.get() * 150
        self.cd_p_p=self.pepsi.get() * 150
        self.total_cold_drinks_price = float(
                                            self.cd_m_p +
                                            self.cd_cc_p +
                                            self.cd_f_p +
                                            self.cd_d_p +
                                            self.cd_s_p +
                                            self.cd_p_p
                                        )
        self.drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.d_tex=round((self.total_cold_drinks_price * 0.05),2)
        self.drinks_tex.set("Rs. " + str(self.d_tex))

        # ===========Totle Bill With out tex==========
        self.tolal_bill = float(self.total_cosmetics_price +
                                self.total_cold_drinks_price +
                                self.total_grocery_price+
                                self.c_tex+
                                self.g_tex+
                                self.d_tex)
    def wellcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWell Come To Apple Mart")
        self.textarea.insert(END,f"\n\n Bill Number   :   {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :   {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number  :   {self.c_phone.get()}")
        self.textarea.insert(END,f"\n\n ==================================")
        self.textarea.insert(END,f"\n Product\t\t QTY\t   Price")
        self.textarea.insert(END,f"\n ==================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error", " Customer Details are Must")
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", " No Product purchased")
        else:
            self.wellcome_bill()
            #============ Cosmetics===========
            if self.Bath_Soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t {self.Bath_Soap.get()}\t   {self.c_s_p}")
            if self.Face_Cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t {self.Face_Cream.get()}\t   {self.c_fc_p}")
            if self.Face_Wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t {self.Face_Wash.get()}\t   {self.c_fw_p}")
            if self.Hair_Spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t {self.Hair_Spray.get()}\t   {self.c_hs_p}")
            if self.Hair_Gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell\t\t {self.Hair_Gell.get()}\t   {self.c_hg_p}")
            if self.Loshan.get()!=0:
                self.textarea.insert(END,f"\n Loshan\t\t {self.Loshan.get()}\t   {self.c_l_p}")

            # ============ grocery===========
            if self.Rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t {self.Rice.get()}\t   {self.g_r_p}")
            if self.Food_Oil.get()!=0:
                self.textarea.insert(END,f"\n Cooking Oil\t\t {self.Food_Oil.get()}\t   {self.g_fo_p}")
            if self.Daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t {self.Daal.get()}\t   {self.g_d_p}")
            if self.Wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t {self.Wheat.get()}\t   {self.g_w_p}")
            if self.Sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t {self.Sugar.get()}\t   {self.g_s_p}")
            if self.Tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t {self.Loshan.get()}\t   {self.g_t_p}")

            # ============ Cold Drinks===========
            if self.Mirinda.get()!=0:
                self.textarea.insert(END,f"\n Mirinda\t\t {self.Mirinda.get()}\t   {self.cd_m_p}")
            if self.Coca_Cola.get()!=0:
                self.textarea.insert(END,f"\n Coca Cola\t\t {self.Coca_Cola.get()}\t   {self.cd_cc_p}")
            if self.Fanta.get()!=0:
                self.textarea.insert(END,f"\n Fanta\t\t {self.Fanta.get()}\t   {self.cd_f_p}")
            if self.Dew.get()!=0:
                self.textarea.insert(END,f"\n Dew\t\t {self.Dew.get()}\t   {self.cd_d_p}")
            if self.Sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite\t\t {self.Sprite.get()}\t   {self.cd_s_p}")
            if self.pepsi.get()!=0:
                self.textarea.insert(END,f"\n Pepsi\t\t {self.pepsi.get()}\t   {self.cd_p_p}")


            self.textarea.insert(END, f"\n ----------------------------------")

            if self.cosmetics_tex.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tex\t\t\t {self.cosmetics_tex.get()}")
            if self.grocery_tex.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\n Grocery Tex\t\t\t {self.grocery_tex.get()}")
            if self.drinks_tex.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tex\t\t\t {self.drinks_tex.get()}")

            self.textarea.insert(END, f"\n ----------------------------------")
            self.textarea.insert(END, f"\n Total Bill\t\t\t Rs. {self.tolal_bill}")
            self.textarea.insert(END, "\n\n\n\n\tThanks For Shopping")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Save Bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("Bill/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {self.bill_no.get()} Saved Successfuly")
        else:
            return
    def Find_Bill(self):
        present="no"
        for i in os.listdir("Bill/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bill/{i}", "r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Search")

    def clear_data(self):
        opt = messagebox.askyesno("Clear", "Do You Want To Clear Data?")
        if opt > 0:
            # =============Cosmatic===============
            self.Bath_Soap.set(0)
            self.Face_Cream.set(0)
            self.Face_Wash.set(0)
            self.Hair_Spray.set(0)
            self.Hair_Gell.set(0)
            self.Loshan.set(0)

            # =============Grocery===============
            self.Rice.set(0)
            self.Food_Oil.set(0)
            self.Daal.set(0)
            self.Wheat.set(0)
            self.Sugar.set(0)
            self.Tea.set(0)

            # =============Cold Drink===============
            self.Mirinda.set(0)
            self.Coca_Cola.set(0)
            self.Fanta.set(0)
            self.Dew.set(0)
            self.Sprite.set(0)
            self.pepsi.set(0)

            # =============Total Product Price & Tex================
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            self.cosmetics_tex.set("")
            self.grocery_tex.set("")
            self.drinks_tex.set("")

            # ==============Customer================
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.wellcome_bill()
    def ext_app(self):
        opt=messagebox.askyesno("Exit","Do You Want To Exit?")
        if opt>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()