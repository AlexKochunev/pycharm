import json


avg_profit = 0
good_companies = 0
companies = dict()
with open("text_7.txt", "r", encoding="UTF-8") as my_file:
    context = my_file.readlines()
    for s in context:
        companies[s.split()[0]] = int(s.split()[2]) - int(s.split()[3])
        if companies[s.split()[0]] > 0:
            avg_profit += companies[s.split()[0]]
            good_companies += 1
my_list = [companies, {'average_profit': avg_profit/good_companies}]
with open("text_7.json", "w", encoding="UTF-8") as my_file:
    json.dump(my_list, my_file, sort_keys=True, indent=4, ensure_ascii=False)
