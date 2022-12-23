import file01 as base

officeStaff1 = base.Staff('Basic', 'Yvonne', 0)
print(officeStaff1)
officeStaff1.position = 'Manager'
print(officeStaff1.position)
officeStaff1.calculatePay()
print(officeStaff1)
#