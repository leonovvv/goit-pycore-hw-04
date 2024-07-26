def get_cats_info(path):
    result = []
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print('Line is in incorrect format: ' + line)
                else:
                    result.append({
                        "id" : parts[0],
                        "name" : parts[1],
                        "age" : parts[2]
                        })
    except Exception as ex:
        print('File is not accessible or damaged')
        print(ex)

    return result

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
