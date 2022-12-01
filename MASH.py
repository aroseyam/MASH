import random

#INTRO
print("╔═.♥.═══════════════════════════════════════════════╗")
print("   Discover your future with a story-telling game")
print("      M.A.S.H. (Mansion Apartment Shack House)")
print("╚═══════════════════════════════════════════════.♥.═╝")
name = input("     Please Enter Name to start: ") 
print("Welcome", name)

# 1 COLLEGE
print("Choose 3 Colleges - Suggestions dream college, current or random college you've seen on TV")
college_one = input("1: ")
college_two = input("2: ")
college_three = input("3: ")
college = [college_one, college_two, college_three]
num = random.randrange(0, 2)
college = college[num]

# 2 MARRY
print()
print("Name 3 People - Suggestions you might marry, a close friend, or crush ")
marry_one = input("1: ")
marry_two = input("2: ")
marry_three =input("3: ")
marry = [marry_one, marry_two, marry_three]
num = random.randrange(0, 2)
marry = marry[num]

# 3 CITY
print()
print("Choice 3 Cities - Suggestions somewhere currently live, a dream destination, or you parents house.")
city_one = input("1: ")
city_two = input("2: ")
city_three =input("3: ")
city = [city_one, city_two, city_three]
num = random.randrange(0, 2)
city = city[num]

# 4 KID 
print()
print("Pick your top 3 numbers - Suggested range around 0-5")
kid_one = input("1: ")
kid_two = input("2: ")
kid_three = input("3: ")
kid = [kid_one, kid_two, kid_three]
num = random.randrange(0, 2)
kid = kid[num]

# 5 MAJOR 
print()
print("Name 3 majors that interest you or that you possibly graduated from")
major_one = input("1: ")
major_two = input("2: ")
major_three = input("3: ")
major = [major_one, major_two, major_three] 
num = random.randrange(0, 2)
major = major[num]

# 6 JOB
print()
print("Name 3 jobs - did you have a dream job?, your current job, or a friends job")
job_one = input("1: ")
job_two = input("2: ")
job_three = input("3: ")
job = [job_one, job_two, job_three]
num = random.randrange(0, 2)
job = job[num]

#MASH
mash = ["Mansion", "Apartment"," Shack", "House"]
num = random.randrange(0, 2)
mash = mash[num]

print("You will graduate,", 
college, "& Major in", 
major, ", and after graduating you'll marry", 
marry, "You'll settle down in", 
city, "and live in a", 
mash, "and spend your days as a", 
job, "You &", 
marry, "will have", 
kid, "kids")

print()
print("Thanks for playing", name)