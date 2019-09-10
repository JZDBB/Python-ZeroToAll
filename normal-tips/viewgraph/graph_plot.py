import matplotlib.pyplot as plt

f = open("result.csv", "r+")
names = f.readline().split(",")

acc = {}
prec = {}
recall = {}
f1 = {}
epoch = []

for i in range(10):
    acc[str(i)] = []
    prec[str(i)] = []
    recall[str(i)] = []
    f1[str(i)] = []
for i in range(80):
    epoch.append(i)

msg = f.readline()
while msg:
    msg.replace("\n", " ")
    result = msg.split(",")
    acc[result[1]].append(result[2])
    prec[result[1]].append(result[3])
    recall[result[1]].append(result[4])
    f1[result[1]].append(result[5])
    msg = f.readline()

plt.figure()
with plt.style.context('Solarize_Light2'):
    # for i in range(10):
    plt.plot(epoch, prec[str(3)], marker=".")
# Number of accent colors in the color scheme
plt.title('10 line')
plt.xlabel('x label', fontsize=14)
plt.ylabel('y label', fontsize=14)

plt.show()
