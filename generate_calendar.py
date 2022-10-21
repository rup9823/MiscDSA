days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

month_days = [[] for _ in range(7)]
day = "Saturday"
day = days_list.index(day)
j = 1
for i in range(day, day+7):
    if i < 7:
        month_days[i].append(j)
    else:
        month_days[i % 7].append(" ")
        month_days[i % 7].append(j)
    j += 1

for i in range(7):
    if month_days[i][0] == " ":
        start = month_days[i][1]
    else:
        start = month_days[i][0]
    while start <= 24:
        start += 7
        month_days[i].append(start)

for i in range(7):
    output = [days_list[i]] + month_days[i]
    row_format = "{:>15}" * len(output)
    print(row_format.format(*output))
