first_team_name = input().split()
second_team_number = input().split()
for i in first_team:
    s, y = map(int, input().split())
    if s != "A" and y != "B":
        print("None of them will be active on Monday or Tuesday")
    else:
        print("The Team will be active on Monday")

for j in range(1, second_team):
     first_attempt = int(input())
     print(f"The attempt {j} for the team will be in ratio of ", 2 * j, ":", 1)

