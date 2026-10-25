# 学生成绩管理命令行版

stu = [{"姓名":"张三","语文": 88,"数学": 85,"英语": 74},
       {"姓名":"李四","语文": 35,"数学": 48,"英语": 64},
       {"姓名":"王五","语文": 95,"数学": 78,"英语": 82}
       ]

# 统一输入整数
def input_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("输入无效，请输入整数！")


# 统一输入100范围内的数字
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("输入无效，请输入数字！")
            continue
        if not (0 <= value <= 100):
            print("成绩应在 0~100 之间，请重新输入！")
            continue
        return value


# 计算总分
def total_score(student):
    return student["语文"]+student["数学"]+student["英语"]

# 1、添加学生
def add_stu():
    name = input("请输入想要添加学生的姓名：").strip()
    
    if name == "" :
        print("姓名不能为空！")
        return
    
    for i in stu:
        if i["姓名"] == name:
            choose = input("该学生已存在，如要继续添加重名学生请选1，放弃请选2：").strip()
            if choose != "1":
                print("该学生已存在，放弃添加！")
                return
            break          # 只判断一次，避免重复询问
    score1 = input_float("请输入该学生的语文成绩：")
    score2 = input_float("请输入该学生的数学成绩：")
    score3 = input_float("请输入该学生的英语成绩：")
    stu.append({"姓名": name, "语文": score1, "数学": score2, "英语": score3})
    print("添加学生成功！")

       

# 2、显示全部学生
def get_name():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    print("全部的学生如下：")
    for i in stu:
        print(f"{i['姓名']}：语文{i['语文']}，数学{i['数学']}，英语{i['英语']}，总分{total_score(i)}")


# 3、查询学生成绩
def get_score():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    name = input("请输入要查询的学生姓名：").strip()
    flag = False

    for i in stu:
        if i["姓名"] == name:
            print(f"{name}的成绩如下：语文{i['语文']}分，数学{i['数学']}分，英语{i['英语']}分")
            flag = True

    if flag == False:
        print("没有找到该学生，请输入正确的姓名！")


# 4、修改学生成绩
def change_score():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    flag = False
    name = input("请输入要修改成绩的学生姓名：").strip()

    for i in stu:
        if i["姓名"] == name:
            score1 = input_float("请输入该学生的语文成绩：")
            score2 = input_float("请输入该学生的数学成绩：")
            score3 = input_float("请输入该学生的英语成绩：")

            i["语文"] = score1
            i["数学"] = score2
            i["英语"] = score3
            flag = True
            break          

    if flag == False:
        print("没有找到该学生，请输入正确的姓名！")
    else:
        print("成绩修改成功！")


# 5、删除学生
def del_stu():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    flag = False
    name = input("请输入要删除学生的姓名：").strip()

    for i in stu:
        if i["姓名"] == name:
            stu.remove(i)
            flag = True
            break

    if flag == False:
        print("没有找到该学生，请输入正确的姓名！")
    else:
        print("删除学生成功！")


# 6、按总分排序显示
def sort_score():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    result = sorted(stu, key=total_score, reverse = True)
    print("各学生成绩按总分从大到小排序如下：")
    for i in result:
        print(f"{i['姓名']}：总分{total_score(i)}，语文{i['语文']}，数学{i['数学']}，英语{i['英语']}")


# 7、统计各科平均分/最高分/最低分
def count_score():

    if len(stu) == 0:
        print("当前没有任何学生信息。")
        return
    
    avg_score1 = 0
    avg_score2 = 0
    avg_score3 = 0
    max_score1 = stu[0]["语文"]
    max_score2 = stu[0]["数学"]
    max_score3 = stu[0]["英语"]
    min_score1 = stu[0]["语文"]
    min_score2 = stu[0]["数学"]
    min_score3 = stu[0]["英语"]

    for i in stu:
        avg_score1 += i["语文"]
        avg_score2 += i["数学"]
        avg_score3 += i["英语"]

        if i["语文"] > max_score1:
            max_score1 = i["语文"]
        if i["语文"] < min_score1:
            min_score1 = i["语文"]

        if i["数学"] > max_score2:
            max_score2 = i["数学"]
        if i["数学"] < min_score2:
            min_score2 = i["数学"]

        if i["英语"] > max_score3:
            max_score3 = i["英语"]
        if i["英语"] < min_score3:
            min_score3 = i["英语"]

    avg_score1 /= len(stu)
    avg_score2 /= len(stu)
    avg_score3 /= len(stu)

    print("语文的平均分为：%.2f，最高分为：%.2f，最低分为：%.2f" % (avg_score1,max_score1,min_score1))
    print("数学的平均分为：%.2f，最高分为：%.2f，最低分为：%.2f" % (avg_score2,max_score2,min_score2))
    print("英语的平均分为：%.2f，最高分为：%.2f，最低分为：%.2f" % (avg_score3,max_score3,min_score3))



# 8、主菜单
def main():

    while True:
        print("\n---------------------主菜单---------------------")
        print("欢迎来到学生成绩管理系统，请根据以下数字选择功能")
        print("1：添加学生")
        print("2：显示全部学生名单")
        print("3：查询学生成绩")
        print("4：修改学生成绩")
        print("5：删除学生")
        print("6：按总分排序显示所有学生的成绩")
        print("7：统计各科平均分/最高分/最低分")
        print("8：退出")

        choose = input_int("请输入对应数字选择功能：")
        print("")

        if choose == 1:
            add_stu()
        elif choose == 2:
            get_name()
        elif choose == 3:
            get_score()
        elif choose == 4:
            change_score()
        elif choose == 5:
            del_stu()
        elif choose == 6:
            sort_score()
        elif choose == 7:
            count_score()
        elif choose == 8:
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请输入 1~8 之间的数字。")


if __name__ == "__main__":
    main()