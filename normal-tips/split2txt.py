import os



def main():
    with open('汇总.txt', 'r+') as f:
        all_line = f.read()
        mesgs = all_line.split('\n')
        for mesg in mesgs:
            list_word = mesg.split('\t')
            id = list_word.pop(0)
            line = ' '.join(list_word)
            try:
                filename = './result/' + str(id) + '.txt'
                f = open(filename, 'w+')
                f.write(line)
                f.close()
            except:
                f = open('./result/error.txt', 'a+')
                f.write(str(id) + '\t')
                f.write(line)
                f.close()

if __name__ == '__main__':
    main()