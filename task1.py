def total_salary(path):
    count = 0
    total = 0
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.split(',')
                if len(parts) != 2:
                    print('Line is in incorrect format: ' + line)
                else:
                    count += 1
                    total += float(parts[1])
    except Exception as ex:
        print('File is not accessible or damaged')
        print(ex)
        return (0, 0)

    if count == 0:
        return (0, 0)

    return (total, total/count)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
