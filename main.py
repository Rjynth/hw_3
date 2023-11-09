files = ['1.txt', '2.txt', '3.txt']

contents = []

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.readlines()
        contents.append((file, len(file_content), file_content))

contents.sort(key=lambda x: x[1])

with open('result.txt', 'w') as f:
    for content in contents:
        file_name, file_lines, file_content = content
        f.write(f'{file_name}\n{file_lines}\n')
        f.write(''.join(file_content))
