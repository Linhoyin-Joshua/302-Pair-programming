married_allowances = 264000
tax_level1 = 50000 * 0.02
tax_level2 = 50000 * 0.06
tax_level3 = 50000 * 0.1
tax_level4 = 50000 * 0.14

def joint_calculation(s_income,sp_income):
    joint_income = sp_income + s_income

    s_MPF = s_income * 0.05
    if (s_MPF > 18000):
        s_MPF = 18000

    sp_MPF = sp_income * 0.05
    if (sp_MPF > 18000):
        sp_MPF = 18000


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
    return joint_tax

