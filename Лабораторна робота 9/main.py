def create_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def read_and_modify_file(input_filename, output_filename):
    with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
        for line in f_in:
            line = line.rstrip('\n')
            if len(line) < 20:
                line = line.ljust(20)
            else:
                line = line[:20]
            f_out.write(line + '\n')

def print_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')

# створюємо файл TF9_1
lines = ['Це перший рядок', 'Це другий рядок, який трохи довший', 'Це третій рядок']
create_file('TF9_1.txt', lines)

# читаємо вміст файла TF9_1, модифікуємо рядки і записуємо їх у файл TF9_2
read_and_modify_file('TF9_1.txt', 'TF9_2.txt')

# читаємо вміст файла TF9_2 і друкуємо його по рядках
print_file('TF9_2.txt')
