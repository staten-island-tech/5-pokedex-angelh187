wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}


for people, dep in wards.items():
    for deps in dep:
        if dep not in staff:
            staff[deps] = [people]
        else:
            staff[deps].append(people)

print(staff['Bob'])


            
