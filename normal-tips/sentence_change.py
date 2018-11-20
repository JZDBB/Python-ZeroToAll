import os

def main():
    file_dir = './caption'
    filenames = os.listdir(file_dir)
    for filename in filenames:
        file = os.path.join(file_dir, filename)
        f = open(file, encoding='utf-8')
        try:
            line = f.readline()
            list_line = line.split(' ')
            list_line[1].capitalize()
            list_line[-1].replace('.', '')
            list_line[-1].join('.')
            line_w = os.path.join(word + ' ' for word in list_line)
            with open(os.path.join(file_dir, 'label.txt'), 'a+', encoding="UTF-8") as f:
                f.write(line_w)
                f.write('\n')
        except:
            continue


if __name__ == '__main__':
    main()