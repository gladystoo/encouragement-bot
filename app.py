print("Title of program: EM Matching Personality test")
print()
print("Welcome to DHS! Please answer the following questions truthfully and we'll suggest an EM for you!")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

creativearts1 = input("I am good at English.")

sportscience1 = input("I have an interest in sports.")

mootparliament1 = input("I want to learn more about how the government works.")

creativearts2 = input("I enjoy writing poems.")

sportscience2 = input("I am inquisitive when learning about science/doing science experiments.")

mootparliament2 = input("I have an interest in debate.")


creativearts_final = int(creativearts1) + int(creativearts2)
sportscience_final = int(sportscience1) + int(sportscience2)
mootparliament_final = int(mootparliament1)+ int(mootparliament2)

print()

if creativearts_final > sportscience_final and creativearts_final > mootparliament_final:
  print("You might be suitable for Infocomm club!")
elif sportscience_final > mootparliament_final:
  print("You might be stuiable for Sport Science!")
else:
  print("You might be suitable for Moot Parliament!")
