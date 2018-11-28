import os

def main():
    file_dir = './caption'
    filenames = os.listdir(file_dir)
    mesg_list = []
    for filename in filenames:
        file = os.path.join(file_dir, filename)
        f = open(file)
        message = f.read()
        messages = message.split('\n')
        for mesg in messages:
            try:
                list_line = mesg.split(' ')
                list_line[1] = list_line[1].capitalize()
                list_line[-1] = list_line[-1].replace('.', '')
                # list_line[-1] = list_line[-1].replace('\n', '')
                list_line[-1] = list_line[-1] + '.'# + '\n'
                # line_w = ' '.join(list_line)
                mesg_list.append(list_line)
            except:
                continue

    dict_mesg = {}
    for one in mesg_list:
        key = one.pop(0)
        if key in dict_mesg:
            dict_mesg[key].append(' '.join(one))
        else:
            dict_mesg[key] = [' '.join(one)]

    for i in range(11000):
        if str(i) in dict_mesg:
            l1 = dict_mesg[str(i)]
            mesg = sorted(set(l1), key=l1.index)
            m = ' '.join(mesg)
            num = m.count('.')
            if num >= 5:
                filename = './result/' + str(i) + '.txt'
                f = open(filename, 'w+')
                f.write(m)
                f.close()
            else:
                f = open('./result/error.txt', 'a+')
                f.write(str(i) + '\t')
                f.write(m)
                f.write('\t')
                f.write(str(num))
                f.write('\n')
                f.close()


if __name__ == '__main__':
    main()