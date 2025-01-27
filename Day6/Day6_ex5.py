new_mem = input("Add a new member: ") + "\n"


file = open('members.txt', 'r')
prev_members = file.readlines()
file.close()


prev_members.append(new_mem)
members = prev_members


file = open('members.txt', 'w')
file.writelines(members)
file.close()
