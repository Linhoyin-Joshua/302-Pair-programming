from tkinter import *
import tkinter.messagebox as MSB

sing_allowances = 132000
married_allowances = 264000
tax_level1 = int(50000 * 0.02)
tax_level2 = int(50000 * 0.06)
tax_level3 = int(50000 * 0.1)
tax_level4 = int(50000 * 0.14)


def single_calculation():
    try:
        s_income = int(s_tax_income.get())
        joint_list.delete(0, joint_list.size())
        sp_list.delete(0, sp_list.size())
        s_list.delete(0, s_list.size())

    except ValueError as error:
        MSB.showinfo("Status", "invalid input, please input an int")
    # MPF calculation
    s_MPF = s_income * 0.05
    if (s_MPF > 18000):
        s_MPF = 18000

    # net income for self
    s_netincome = int(s_income - sing_allowances - s_MPF)
    if (s_netincome >= 1890050):
        s_tax = int((s_income -18000) * 0.15)
    elif (s_netincome <= 0):
        s_tax = 0
    elif (s_netincome <= 50000 and s_netincome >= 0):
        s_tax = int(s_netincome * 0.02)
    elif (s_netincome <= 100000 and s_netincome >= 50001):
        s_tax = int(tax_level1 + (s_netincome - 50000) * 0.06)
    elif (s_netincome <= 150000 and s_netincome >= 100001):
        s_tax = int(tax_level1 + tax_level2 + (s_netincome - 100000) * 0.1)
    elif (s_netincome <= 200000 and s_netincome >= 150001):
        s_tax = int(tax_level1 + tax_level2 + tax_level3 + (s_netincome - 150000) * 0.14)
    elif (s_netincome <= 1890049 and s_netincome >= 200001):
        s_tax = int(tax_level1 + tax_level2 + tax_level3 + tax_level4 + (s_netincome - 200000) * 0.17)

    s_list.insert(s_list.size() + 1, "Self tax pay:" + str(s_tax))


def married_calculation():
    global s_list
    try:
        global s_MPF
        global s_income
        s_income = int(s_tax_income.get())

        s_list.delete(0, s_list.size())
        # MPF calculation
        s_MPF = s_income * 0.05
        if (s_MPF > 18000):
            s_MPF = 18000

        # MPF for joint

        s_netincome = int(s_income - sing_allowances - s_MPF)

        # self
        if (s_netincome >= 1890040):
            s_tax = int((s_income-18000) * 0.15)
        elif (s_netincome <= 0):
            s_tax = 0
        elif (s_netincome <= 50000 and s_netincome >= 0):
            s_tax = int(s_netincome * 0.02)
        elif (s_netincome <= 100000 and s_netincome >= 50001):
            s_tax = int(tax_level1 + (s_netincome - 50000) * 0.06)
        elif (s_netincome <= 150000 and s_netincome >= 100001):
            s_tax = int(tax_level1 + tax_level2 + (s_netincome - 100000) * 0.1)

        elif (s_netincome <= 200000 and s_netincome >= 150001):
            s_tax = int(tax_level1 + tax_level2 + tax_level3 + (s_netincome - 150000) * 0.14)
        elif (s_netincome <= 1890049 and s_netincome >= 200001):
            s_tax = int(tax_level1 + tax_level2 + tax_level3 + tax_level4 + (s_netincome - 200000) * 0.17)
        s_list.insert(s_list.size() + 1, str(s_tax))
        spouse()
    except ValueError as error:
        MSB.showinfo("Status", "invalid input, please input an int")



# spouse
def spouse():
    global sp_list
    try:
        global sp_MPF
        global sp_income
        sp_list.delete(0, sp_list.size())
        sp_income = int(sp_tax_income.get())

        sp_MPF = sp_income * 0.05
        # MPF for spouse
        if (sp_MPF > 18000):
            sp_MPF = 18000
        sp_netincome = int(sp_income - sing_allowances - sp_MPF)

        if (sp_netincome >= 1890040):
            sp_tax = int((sp_income-18000) * 0.15)
        elif (sp_netincome <= 0):
            sp_tax = 0
        elif (sp_netincome <= 50000 and sp_netincome >= 0):
            sp_tax = int(sp_netincome * 0.02)
        elif (sp_netincome <= 100000 and sp_netincome >= 50001):
            sp_tax = int(tax_level1 + (sp_netincome - 50000) * 0.06)
        elif (sp_netincome <= 150000 and sp_netincome >= 100001):
            sp_tax = int(tax_level1 + tax_level2 + (sp_netincome - 100000) * 0.1)
        elif (sp_netincome <= 200000 and sp_netincome >= 150001):
            sp_tax = int(tax_level1 + tax_level2 + tax_level3 + (sp_netincome - 150000) * 0.14)

        elif (sp_netincome <= 1890039 and sp_netincome >= 200001):
            sp_tax = int(tax_level1 + tax_level2 + tax_level3 + tax_level4 + (sp_netincome - 200000) * 0.17)

        sp_list.insert(sp_list.size() + 1, str(sp_tax))
        Joint()
    except ValueError as error:
        MSB.showinfo("Status", "invalid input, please input an int")




def Joint():
    global joint_list
    try:
        joint_list.delete(0, joint_list.size())
        joint_income = sp_income + s_income

        joint_MPF = s_MPF + sp_MPF

        joint_netincome = int(joint_income - married_allowances - joint_MPF)
        # joint
        if (joint_income >= 3162050):
            joint_tax = int((joint_income - joint_MPF) * 0.15)
        elif (joint_netincome <= 0):
            joint_tax = 0
        elif (joint_netincome <= 50000 and joint_netincome >= 0):
            joint_tax = int(joint_netincome * 0.02)
        elif (joint_netincome <= 100000 and joint_netincome >= 50001):
            joint_tax = int(tax_level1 + (joint_netincome - 50000) * 0.06)
        elif (joint_netincome <= 150000 and joint_netincome >= 100001):
            joint_tax = int(tax_level1 + tax_level2 + (joint_netincome - 100000) * 0.1)
        elif (joint_netincome <= 200000 and joint_netincome >= 150001):
            joint_tax = int(tax_level1 + tax_level2 + tax_level3 + (joint_netincome - 150000) * 0.14)
        elif (joint_netincome <= 3162049 and joint_netincome >= 200001):
            joint_tax = int(tax_level1 + tax_level2 + tax_level3 + tax_level4 + (joint_netincome - 200000) * 0.17)
        joint_list.insert(joint_list.size() + 1, str(joint_tax))
        compare()
    except ValueError as error:
        MSB.showinfo("Status", "invalid input, please input an int")



def compare():
    for self in s_list.get(0, 1):
        for joint in joint_list.get(0, 1):
            for spouse in sp_list.get(0, 1):
                joint = round(float(joint))
                total = round(float(self)) + round(float(spouse))
                if (total > joint):
                    joint_list.insert(joint_list.size() + 1, 'Recommend with Joint')
                    joint_list.insert(joint_list.size() + 1, 'total of ' + str(joint))
                else:
                    sp_list.insert(sp_list.size() + 1, 'Recommended with Seperate')
                    sp_list.insert(sp_list.size() + 1, 'total of ' + str(total) + "$")


root = Tk()
root.geometry("600x600");
root.title('Tax Calculator')

# labels help users know each box represant
topic = Label(root, text='Self HK$', font=('bold', 10))
topic.place(x=20, y=10)

topic2 = Label(root, text='Spouse HK$', font=('bold', 10))
topic2.place(x=300, y=10)

s_inputs = Label(root, text="Enter Income($)", font=('bold', 10))
s_inputs.place(x=20, y=30)

sp_inputs = Label(root, text="Enter Income($)", font=('bold', 10))
sp_inputs.place(x=300, y=30)

# inputing income
s_tax_income = Entry()
s_tax_income.place(x=150, y=30)

sp_tax_income = Entry()
sp_tax_income.place(x=430, y=30)

# Buttons
married_calculate = Button(root, text=("Married Calculate"), font=("italic", 10), bg="white",
                           command=married_calculation)
married_calculate.place(x=20, y=100)

single_calculate = Button(root, text=("Single Calculate"), font=("italic", 10), bg="white", command=single_calculation)
single_calculate.place(x=200, y=100)

# Frame
result = Label(root, text='Self', font=('bold', 10))
result.place(x=10, y=180)

result = Label(root, text='Spouse', font=('bold', 10))
result.place(x=220, y=180)

result = Label(root, text='Joint', font=('bold', 10))
result.place(x=430, y=180)

s_list = Listbox(root)
s_list.place(x=10, y=200, width=150)

sp_list = Listbox(root)
sp_list.place(x=200, y=200, width=150)

joint_list = Listbox(root)
joint_list.place(x=400, y=200, width=150)

root.mainloop()