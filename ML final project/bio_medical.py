from tkinter import *
from PIL import Image,ImageTk
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from scipy import stats
import math
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
df = pd.read_csv("states.csv",index_col="State")
class Biomedicaltoolkit:
    def __init__(self):
        self.homePage()
    def homePage(self):
        self.root =Tk()
        self.root.geometry('626x600')
        self.root.config(bg='gray75')
        self.root.title("Bio-Medical ToolKit")
        self.root.resizable(0,0)
        
        image=Image.open('Health.jpg')
        photo = ImageTk.PhotoImage(image)
        label=Label(image=photo,bg="grey88",border=0)
        label.place(x=0,y=5)
        
        
        Button(self.root,text="Prediction of Diabetes",font=('Helivetica',20,"bold"),fg="Dark Blue",bg="khaki",width=20,height=2,command=self.Prediction_of_Diabetes).place(x=150,y=80)
        
        Button(self.root,text="Prediction of BMI",font=('Helivetica',20,"bold"),fg="Dark Blue",bg="khaki",width=20,height=2,command=self.Prediction_of_Weight).place(x=150,y=200)
        Button(self.root,text="Prediction of Heart failure",font=('Helivetica',20,"bold"),fg="Dark Blue",bg="khaki",width=20,height=2,command=self.Prediction_of_heart_failure).place(x=150,y=320)
        
        Button(self.root,text="Covid Analysis",font=('Helivetica',20,"bold"),command=self.Data_analysis,fg="Dark Blue",bg="khaki",width=20,height=2).place(x=150,y=440)
        
        
        mainloop()
    def decision_algo(self):
        df = pd.read_csv("diabetes2.csv")
        feature_col = ['Pregnancies','Glucose','BP','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
        feature_data = df[feature_col]
        target_data = df['Outcome']
        
        x = pd.DataFrame([int(self.p.get()),int(self.g.get()),int(self.bp.get()),int(self.st.get()),int(self.i.get()),float(self.bmi.get()),float(self.d.get()),int(self.a.get())]).transpose()
        clf =DecisionTreeClassifier()
        clf = clf.fit(feature_data, target_data)
        y_predict = clf.predict(x)
        
        
        if y_predict[0]==0:
            Label(self.root1,text="  NO diabetes            ",fg="Green",font=("Helvetica",15,"bold"),bg='gray75').place(x=200,y=500)
            
        else:
            Label(self.root1,text="     Diabetes!!!!           ",fg="Red",font=("Helvetica",15,"bold"),bg='gray75').place(x=200,y=500)
    

    def algo(self):

        if self.g.get()=="" or self.bp.get()=="" or self.st.get()=="" or self.i.get()=="" or self.bmi.get()=="" or self.d.get()=="" or self.a.get()=="":

            Label(self.root1,text=" All Fields are required ",fg="Red",font=("Helvetica",15),bg='gray75').place(x=200,y=500)
        else:
            self.decision_algo()
    def Prediction_of_Diabetes(self):
        self.root.destroy()
        self.root1 =Tk()
        self.root1.geometry('626x600')
        self.root1.config(bg='gray75')
        self.root1.title("Prediction of Diabetes")
        self.root1.resizable(0,0)
        
        Label(self.root1,text="Prediction of Diabetes",font=("Helvetica",20,"bold"),bg='gray75').place(x=150,y=20)


        Label(self.root1,text="Pregnancies",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=100)
        self.p =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.p.place(x=320,y=100)
        
        Label(self.root1,text="Glucose",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=150)
        self.g =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.g.place(x=320,y=150)
        
        Label(self.root1,text="Blood Pressure",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=200)
        self.bp =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.bp.place(x=320,y=200)
        
        Label(self.root1,text="SkinThickness",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=250)
        self.st =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.st.place(x=320,y=250)
        
        Label(self.root1,text="Insulin",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=300)
        self.i =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.i.place(x=320,y=300)
        
        
        Label(self.root1,text="BMI",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=350)
        self.bmi=Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.bmi.place(x=320,y=350)
    
        Label(self.root1,text="DiabetesPedigreeFunction",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=400)
        self.d=Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.d.place(x=320,y=400)
        
        Label(self.root1,text="Age",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=450)
        self.a =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.a.place(x=320,y=450)
        Button(self.root1,text="Submit",command=self.algo,font=("Helvetica",15,"bold")).place(x=150,y=530)
        Button(self.root1,text="Back",command=self.Back,font=("Helvetica",15,"bold")).place(x=255,y=530)
        Button(self.root1,text="Clear",command=self.clear_d,font=("Helvetica",15,"bold")).place(x=350,y=530)
        mainloop()
    
    def clear_d(self):
        self.p.delete(0,END)
        self.g.delete(0,END)
        self.d.delete(0,END)
        self.bmi.delete(0,END)
        self.a.delete(0,END)
        self.bp.delete(0,END)
        self.i.delete(0,END)
        self.st.delete(0,END)
        
    def Back(self):
        self.root1.destroy()
        self.homePage()
        
    def k_means(self):
        df = pd.read_csv("heart_failure.csv")
        feature_col =['age','anaemia','creatinine','diabetes','ejection','high_BP','platelets','sodium','sex','smoking','time']
        feature_data = df[feature_col]
        target_data = df['death']
    
    
    
        model =KNeighborsClassifier(n_neighbors=3)
        model = model.fit(feature_data,target_data)
        
        y_predict = model.predict([[int(self.age.get()),int(self.anaemia.get()),int(self.creatinine.get()),int(self.diabetes.get()),int(self.ejection.get()),int(self.bp.get()),int(self.platelets.get()),int(self.sodium.get()),int(self.sex.get()),int(self.smoking.get()),int(self.time.get())]])
        if y_predict[0]==0:
            Label(self.root1,text=" \t\t\t\t\t\t ",font=("Helvetica",15),bg='gray75').place(x=200,y=700)
            Label(self.root1,text="No chance of heart failure",fg="Green",font=("Helvetica",15,"bold"),bg='gray75').place(x=200,y=700)
            
        else:
            Label(self.root1,text=" \t\t\t\t\t\t ",font=("Helvetica",15),bg='gray75').place(x=200,y=700)
            Label(self.root1,text="Chances of heart failure",fg="Red",font=("Helvetica",15,"bold"),bg='gray75').place(x=200,y=700)
        
    def algo1(self):

        if self.age.get()=="" or self.anaemia.get()=="" or self.creatinine.get()=="" or self.diabetes.get()=="" or self.ejection.get()=="" or self.bp.get()=="" or self.platelets.get()=="" or self.sodium.get()=="" or self.sex.get()=="" or self.smoking.get()=="" or self.time.get()=="":
            Label(self.root1,text=" \t\t\t\t\t\t ",font=("Helvetica",15),bg='gray75').place(x=200,y=700)
            Label(self.root1,text=" All Fields are required ",fg="Red",font=("Helvetica",15),bg='gray75').place(x=200,y=700)
        else:
            self.k_means()
            
    def Prediction_of_heart_failure(self):
        self.root.destroy()
        self.root1 =Tk()
        self.root1.geometry('750x750')
        self.root1.config(bg='gray75')
        self.root1.title("Prediction of Heart Failure")
        self.root1.resizable(0,0)
       
        Label(self.root1,text="Prediction of Heart Failure",font=("Helvetica",20,"bold"),bg='gray75').place(x=150,y=20)


        Label(self.root1,text="Age",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=100)
        self.age =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.age.place(x=320,y=100)
        
        Label(self.root1,text="Anaemia",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=150)
        self.anaemia =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.anaemia.place(x=320,y=150)
        
        Label(self.root1,text="Creatinine",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=200)
        self.creatinine =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.creatinine.place(x=320,y=200)
        
        Label(self.root1,text="Diabetes",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=250)
        self.diabetes =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.diabetes.place(x=320,y=250)
        
        Label(self.root1,text="Ejection",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=300)
        self.ejection =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.ejection.place(x=320,y=300)
        
        
        Label(self.root1,text="Blood Pressure",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=350)
        self.bp=Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.bp.place(x=320,y=350)
    
        Label(self.root1,text="Platelets",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=400)
        self.platelets=Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.platelets.place(x=320,y=400)
        
        Label(self.root1,text="Sodium",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=450)
        self.sodium =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.sodium.place(x=320,y=450)
        
        Label(self.root1,text="Sex",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=500)
        self.sex =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.sex.place(x=320,y=500)
        
        Label(self.root1,text="Smoking",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=550)
        self.smoking =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.smoking.place(x=320,y=550)
        
        Label(self.root1,text="Time",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=600)
        self.time =Entry(self.root1,font=("Helvetica",15,"bold")) 
        self.time.place(x=320,y=600)
        
        Button(self.root1,text="Submit",command=self.algo1,font=("Helvetica",15,"bold")).place(x=150,y=650)
        Button(self.root1,text="Back",command=self.Back,font=("Helvetica",15,"bold")).place(x=255,y=650)
        Button(self.root1,text="Clear",command=self.clear_d1,font=("Helvetica",15,"bold")).place(x=350,y=650)
        mainloop()
        
    def clear_d1(self):
        self.age.delete(0,END)
        self.anaemia.delete(0,END)
        self.creatinine.delete(0,END)
        self.diabetes.delete(0,END)
        self.ejection.delete(0,END)
        self.bp.delete(0,END)
        self.platelets.delete(0,END)
        self.sodium.delete(0,END)
        self.sex.delete(0,END)
        self.smoking.delete(0,END)
        self.time.delete(0,END)
        
    def linearRegresion(self):

        if self.h.get()=="" or self.w.get()=="" or self.g.get()=="" :

            Label(self.root1,text=" All Fields are required ",fg="Red",font=("Helvetica",15),bg='gray75').place(x=200,y=400)
        
        else:
            Label(self.root1,text=" \t\t\t\t\t\t ",font=("Helvetica",15),bg='gray75').place(x=200,y=400)
            df = pd.read_csv("weight.csv")
    
            outcome =  df['Index']
            data = list(df['h/w'])
            
            
            outcome_data = list(outcome)
            
            def myfunc(x):
                return x*slope+intercept
        
            slope,intercept , r,p,sd = stats.linregress(data,outcome_data)
            model=list(map(myfunc,data))
            try:
                if int(self.h.get())<15:
                    raise EXCEPTION
                status1 = (myfunc(int(self.h.get())/int(self.w.get())))
            
                status = math.floor(status1)
            
                if status == 0:
                    res="  Extremely weak "
                    color="red"
                elif status1<1.5 :
                    res="      Weak           " 
                    color="orange"
                elif status1<2.5 :
                    res="     Normal          "
                    color="green"
                elif status1<3.5 :
                    res="    Overweight      "
                    color="orange"
                elif status1<4.5 :
                    res="     Obesity         "
                    color="red"
                else:
                    res="    Extreme Obesity    "
                    color="dark red"
                Label(self.root1,text=res,font=("Helvetica",15,"bold"),fg=color,bg='gray75').place(x=220,y=400)
        
            except:
                Label(self.root1,text="Invalid Data",font=("Helvetica",15,"bold"),fg="red",bg='gray75').place(x=220,y=400)
        
    def Prediction_of_Weight(self):
        self.root.destroy()
        self.root1 =Tk()
        self.root1.geometry('626x600')
        self.root1.config(bg='gray75')
        self.root1.title("Prediction of BMI")
        self.root1.resizable(0,0)
        
        Label(self.root1,text="Prediction of BMI",font=("Helvetica",20,"bold"),bg='gray75').place(x=150,y=20)


        Label(self.root1,text="Height",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=100)
        self.h = Entry(self.root1,font=("Helvetica",15,"bold"))
        self.h.place(x=320,y=100)
        
        Label(self.root1,text="Weight",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=150)
        self.w = Entry(self.root1,font=("Helvetica",15,"bold"))
        self.w.place(x=320,y=150)
        
        Label(self.root1,text="Gender",font=("Helvetica",15,"bold"),bg='gray75').place(x=55,y=200)
        self.g = ttk.Combobox(self.root1,font=("Helvetica",15,"bold"))
        self.g['values']=['Male','Female']
        self.g.place(x=320,y=200)
        self.g.current(0)
        Button(self.root1,text="Submit",font=("Helvetica",15,"bold"),command=self.linearRegresion).place(x=150,y=350)
        Button(self.root1,text="Back",command=self.Back,font=("Helvetica",15,"bold")).place(x=250,y=350)
        Button(self.root1,text="Clear",command=self.clear_d2,font=("Helvetica",15,"bold")).place(x=350,y=350)
        mainloop()
                
    
    def clear_d2(self):
        self.h.delete(0,END)
        self.w.delete(0,END)
        
    def Data_analysis(self):
        self.root.destroy()
        df = pd.read_csv("states.csv",index_col="State")
        self.root1=Tk()
        self.root1.geometry('600x650')
        self.root1.title("Covid data analysis")
        self.root1.config(bg='gray75')

        self.root1.resizable(0,0)
        Label(self.root1,text="Covid-19 Data Analysis",font=("Helvetica",15,"bold"),bg='gray75').place(x=160,y=20)
        Label(self.root1,text="Select the state:",font=("Helvetica",10,"bold"),bg='gray75').place(x=100,y=100)
        val=StringVar()
        self.state1=ttk.Combobox(self.root1,font=("Helvetica",10,"bold"))
        self.state1['values'] = ['Karnataka','Kerala','Delhi','Uttar Pradesh','Uttarakhand','Bihar','Tripura','Tamil Nadu','Andaman and Nicobar Islands','Arunachal Pradesh','Assam','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Goa','Gujarat','Haryana','Himachal Pradesh','India','Jammu and Kashmir','Jharkhand','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',"Nagaland","Odisha",'Puducherry','Punjab','Rajasthan','Sikkim','Telangana','Tripura','West Bengal']
        self.state1.place(x=250,y=100)
        self.state1.current(0)
        Label(self.root1,text="Choose a Date",font=("Helvetica",10,"bold"),bg='gray75').place(x=100,y=150)
        self.cal=DateEntry(self.root1,width=12,year=2020,month=4,day=1,bg='blue',borderwidth=8,date_pattern="YYYY-MM-DD",maxdate=datetime.date(2020, 10, 2),mindate=datetime.date(2020,1,30))
        self.cal.place(x=250,y=150)
        
        Button(self.root1,text="State_Date wise",command=self.state_date_wise,font=("Helvetica",10,"bold")).place(x=200,y=200)
        Button(self.root1,text="Date wise",command=self.State_wise,font=("Helvetica",10,"bold")).place(x=420,y=100)
        Button(self.root1,text="State wise",command=self.date_wise,font=("Helvetica",10,"bold")).place(x=350,y=150)
        Button(self.root1,text="Clear",command=self.clear,font=("Helvetica",10,"bold")).place(x=350,y=200)
        Button(self.root1,text="Back",command=self.Back,font=("Helvetica",10,"bold")).place(x=150,y=200)
        mainloop()
    def state_date_wise(self):
        self.clear()
        date=self.cal.get()
        choose_state=self.state1.get()
        try:
            df1=df[df["Date"]==date]
            state = df1.loc[choose_state]
            confirm= state['Confirmed']
            recovered =state['Recovered']
            death = state['Deceased']
            data = {'Confirmed':confirm,"Recovered":recovered,"Death":death}
            fg1 = plt.Figure(figsize=(5,3),dpi=90)#contains figure figsize=height,width -- dpi is depth
            ax1 = fg1.add_subplot()#to display subplot
            self.graph = FigureCanvasTkAgg(fg1,self.root1)#contains graph
            bargraph1 = self.graph.get_tk_widget().place(x=80,y=240)#wdget to display graph
            df2 = pd.DataFrame({choose_state:[confirm,recovered,death]},index=data.keys())
            df2.plot.bar(rot=0,ax=ax1)
            details="Total confirmed cases on "+date+" is "+str(confirm)+"\n\nTotal recovered on "+date+" is "+str(recovered)+"\n\nTotal death on "+date+" is "+str(death)
            self.label = Label(self.root1,text=details,fg="dark green",font=(10),bg='gray75')
            self.label.place(x=100,y=550)
        except:
            try:
               self.clear()
            except:
                pass
            self.label=Label(self.root1,text="Data not found",fg="Red",font=("Helvetica",15,"bold"),bg='gray75')
            self.label.place(x=150,y=300)

    def State_wise(self):
        self.clear()
        choose_state=self.state1.get()
        try:
            state = df.loc[choose_state]
            confirm= state['Confirmed']
            recovered =state['Recovered']
            death = state['Deceased']
            date = state['Date']
    
            fg1 = plt.Figure(figsize=(5,3),dpi=90)#contains figure figsize=height,width -- dpi is depth
            ax1 = fg1.add_subplot()#to display subplot
     
            self.graph = FigureCanvasTkAgg(fg1,self.root1)#contains graph
            bargraph1 = self.graph.get_tk_widget().place(x=80,y=240)#wdget to display graph
        
            df2 = pd.DataFrame({"date":date,"confirm":confirm,"recover":recovered,"death":death})
            df2.plot.bar(x="date",y=["confirm","recover","death"],ax=ax1)
            details="Total confirmed cases on  is "+str(sum(confirm))+"\t\t"+"\n\nTotal recovered on  is "+str(sum(recovered))+"\t\t" +"\n\nTotal death on is "+str(sum(death))+"\t\t"
            self.label = Label(self.root1,text=details,fg="dark green",font=(10),bg='gray75')
            self.label.place(x=100,y=550)
        except:
            try:
               self.clear()
            except:
                pass
            self.label=Label(self.root1,text="Data not found",fg="Red",font=("Helvetica",15,"bold"),bg='gray75')
            self.label.place(x=150,y=300)
    def date_wise(self):
        self.clear()
        df = pd.read_csv("states.csv")
        date=self.cal.get()
        try:
            date_data =df[df["Date"]==date]
            confirm= date_data['Confirmed']
            recovered =date_data['Recovered']
            death = date_data['Deceased']
            state = date_data['State']
            data = {'Confirmed':confirm,"Recovered":recovered,"Death":death}
            fg1 = plt.Figure(figsize=(5,3),dpi=90)
            ax1 = fg1.add_subplot()
            self.graph = FigureCanvasTkAgg(fg1,self.root1)#contains graph
            bargraph1 = self.graph.get_tk_widget().place(x=80,y=240)
            df2 = pd.DataFrame({"State":state,"confirm":confirm,"recover":recovered,"death":death})
            df2.plot.bar(x="State",y=["confirm","recover","death"],ax=ax1)
            details="Total confirmed cases is "+str(sum(confirm))+"\t\t"+"\n\nTotal recovered  is "+str(sum(recovered))+"\t\t" +"\n\nTotal death is "+str(sum(death))+"\t\t"
            self.label=Label(self.root1,text=details,fg="dark green",font=(10),bg='gray75')
      
            self.label.place(x=100,y=550)
        except:
            try:
               self.clear()
            except:
                pass
            
            self.label=Label(self.root1,text="Data not found",fg="Red",font=("Helvetica",15,"bold"),bg='gray75')
            self.label.place(x=150,y=300)
    def clear(self):
        try:
            self.graph.get_tk_widget().place_forget()
            self.label.destroy()
        except:
            pass
Biomedicaltoolkit()