command = input().split(" -> ")
all_companies = {}
while command[0] != "End":
    company_name = command[0]
    employee_id = command[1]
    if company_name not in all_companies:
        all_companies[company_name] = [employee_id]
    else:
        if employee_id not in all_companies[company_name]:
            all_companies[company_name].append(employee_id)
    command = input().split(" -> ")
sort_companies = sorted(all_companies.items(), key=lambda kvpt: kvpt[0])
for company_name, employee_id in sort_companies:
    print(f"{company_name}")
    for employee in employee_id:
        print(f"-- {employee}")
