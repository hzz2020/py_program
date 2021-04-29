# 批量生成随机名字
import random

fn_path = 'fn.txt'
ln_path = 'ln.txt'
fn = []
ln1 = []
ln2 = []

with open(fn_path, 'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])
# print(tuple(fn))

with open(ln_path, 'r') as f:
    for line in f.readlines():
        ss = line.split('\n')[0]
        if len(ss) == 1:
            ln1.append(ss)
        else:
            ln2.append(ss)


# print(tuple(ln1))
# print(tuple(ln2))

class FakeUser:
    def fake_name(self, amount=1, one_world=False, two_worlds=False):
        n = 0
        while n <= amount:
            if one_world:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_worlds:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1

    def fake_sex(self, amount=1):
        n = 0
        while n <= amount:
            sex = random.choice(['男', '女', '未知'])
            yield sex
            n += 1


class SnsUser(FakeUser):
    def fake_follow(self, amount=1, few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                follows = random.randrange(1, 50)
            else:
                follows = random.randrange(200, 10000)
            yield follows
            n += 1


user_a = FakeUser()
for name in user_a.fake_name(30):
    print(name)

user_b = SnsUser()
for follow in user_b.fake_follow(30, few=False, a_lot=True):
    print(follow)
