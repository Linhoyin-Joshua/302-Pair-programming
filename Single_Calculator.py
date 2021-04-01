def single_calculation(s_income):
    #try:
        #s_income = int(s_tax_income.get())
        #joint_list.delete(0, joint_list.size())
        #sp_list.delete(0, sp_list.size())
        #s_list.delete(0, s_list.size())

    #except ValueError as error:
     #   MSB.showinfo("Status", "invalid input, please input an int")
    # MPF calculation
    sing_allowances = 132000
    #married_allowances = 264000
    tax_level1 = 50000 * 0.02
    tax_level2 = 50000 * 0.06
    tax_level3 = 50000 * 0.1
    tax_level4 = 50000 * 0.14

    s_MPF = s_income * 0.05
    if (s_MPF > 18000):
        s_MPF = 18000

    # net income for self
    s_netincome = int(s_income - sing_allowances - s_MPF)
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
    elif (s_netincome <= 1890039 and s_netincome >= 200001):
        s_tax = int(tax_level1 + tax_level2 + tax_level3 + tax_level4 + (s_netincome - 200000) * 0.17)

    return s_tax