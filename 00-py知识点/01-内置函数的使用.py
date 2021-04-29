# 分别输入学生成绩，算出班级总成绩，平均分，最高分，最低分
score = []
total = inscore = 0
while inscore != -1:
    inscore = int(input("请输入学生%d的成绩:" % (len(score)+1)))
    score.append(inscore)
score.pop()  # pop方法:移除最后一个元素
if len(score) > 0:
    print("共有【%d】位学生" % len(score))
    print("本班总成绩:【%d】分\n平均成绩:【%5.2f】分" % (sum(score), sum(score)/len(score)))
    print("最高分：【%d】" % max(score))
    print("最低分：【%d】" % min(score))
    print('排名为：{}'.format(sorted(score, reverse=True)))
else:
    print('没有学生')