first_team_name = input().split()
second_team_number = input().split()
for i in first_team_name:
    s, y = map(str, input().split())
    if s != "A" and y != "B":
        print("None of them will be active on Monday or Tuesday")
    else:
        print("The Team will be active on Monday")

for j in second_team_number:
     first_attempt = int(input())
     print(f"The name {j} for the team will be shown ", j)

