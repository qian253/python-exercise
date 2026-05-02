# 人教版六年级下册语文学习助手
def print_title():
    """打印程序标题"""
    print("=" * 50)
    print("🎓 六年级下册语文学习助手 🎓")
    print("=" * 50)

def menu():
    """主菜单"""
    print("\n📖 请选择学习内容：")
    print("1. 重点生字学习")
    print("2. 核心词语听写/释义")
    print("3. 必背古诗词大全")
    print("4. 重点课文主旨总结")
    print("5. 随堂小练习")
    print("0. 退出程序")
    return input("请输入数字选择：")

# 1. 重点生字（拼音+组词）
def shengzi():
    print("\n📝 六年级下册重点生字（带拼音+组词）")
    print("-" * 40)
    words = {
        "醋(cù)": "陈醋、米醋",
        "饺(jiǎo)": "饺子、水饺",
        "宵(xiāo)": "元宵、通宵",
        "燃(rán)": "燃烧、点燃",
        "戚(qī)": "亲戚、悲戚",
        "浒(hǔ)": "水浒",
        "熏(xūn)": "熏陶、熏肉",
        "祭(jì)": "祭祀、祭奠",
        "恃(shì)": "自恃、有恃无恐",
        "疆(jiāng)": "边疆、疆土"
    }
    for zimu, info in words.items():
        print(f"{zimu}：{info}")

# 2. 核心词语
def ciyu():
    print("\n📚 六年级下册核心词语（释义）")
    print("-" * 40)
    words = {
        "万象更新": "一切事物都改换了样子，出现了一番新气象。",
        "截然不同": "形容两件事物毫无共同之处。",
        "焉知非福": "比喻一时虽然受到损失，也许反而因此能得到好处。",
        "死得其所": "死得有价值，有意义。",
        "五湖四海": "指全国各地，有时也指世界各地。"
    }
    for word, meaning in words.items():
        print(f"{word}：{meaning}")

    # 简易听写功能
    print("\n✍️ 词语小听写（输入答案按回车，输入q退出听写）")
    dict_words = ["饺子", "元宵", "燃烧", "截然不同", "死得其所"]
    for w in dict_words:
        input("请写出词语：")
        print(f"正确答案：{w}\n")

# 3. 必背古诗词
def gushi():
    print("\n🌸 六年级下册必背古诗词")
    print("-" * 40)
    poems = {
        "《寒食》- 韩翃": "春城无处不飞花，寒食东风御柳斜。日暮汉宫传蜡烛，轻烟散入五侯家。",
        "《十五夜望月》- 王建": "中庭地白树栖鸦，冷露无声湿桂花。今夜月明人尽望，不知秋思落谁家。",
        "《石灰吟》- 于谦": "千锤万凿出深山，烈火焚烧若等闲。粉骨碎身浑不怕，要留清白在人间。",
        "《竹石》- 郑燮": "咬定青山不放松，立根原在破岩中。千磨万击还坚劲，任尔东西南北风。"
    }
    for title, content in poems.items():
        print(f"{title}\n{content}\n")

# 4. 重点课文主旨
def text():
    print("\n📖 重点课文主旨总结")
    print("-" * 40)
    texts = {
        "《北京的春节》": "描绘了老北京春节的民风民俗，展现了节日的温馨和美好。",
        "《匆匆》": "紧扣“匆匆”二字，表达了对时光流逝的无奈和惋惜。",
        "《十六年前的回忆》": "回忆李大钊烈士，表现了革命先烈的坚贞不屈。",
        "《为人民服务》": "阐明了共产党人全心全意为人民服务的宗旨。"
    }
    for name, zhuzhi in texts.items():
        print(f"{name}：{zhuzhi}")

# 5. 随堂小练习
def practice():
    print("\n✅ 随堂小练习（选择题）")
    print("-" * 40)
    questions = [
        {
            "题目": "《石灰吟》的作者是？",
            "选项": ["A. 李白 B. 于谦 C. 杜甫"],
            "答案": "B"
        },
        {
            "题目": "“死得其所”中“所”的意思是？",
            "选项": ["A. 处所，地方 B. 所以 C. 所有"],
            "答案": "A"
        },
        {
            "题目": "《匆匆》告诉我们要？",
            "选项": ["A. 珍惜时间 B. 热爱劳动 C. 努力学习"],
            "答案": "A"
        }
    ]
    score = 0
    for q in questions:
        print(q["题目"])
        print(q["选项"][0])
        ans = input("请输入答案（A/B/C）：").upper()
        if ans == q["答案"]:
            print("✅ 回答正确！")
            score += 1
        else:
            print(f"❌ 回答错误，正确答案：{q['答案']}")
        print()
    print(f"🏆 最终得分：{score}/{len(questions)}")

# 主程序运行
if __name__ == "__main__":
    print_title()
    while True:
        choice = menu()
        if choice == "1":
            shengzi()
        elif choice == "2":
            ciyu()
        elif choice == "3":
            gushi()
        elif choice == "4":
            text()
        elif choice == "5":
            practice()
        elif choice == "0":
            print("\n👋 学习结束，加油！下次再见！")
            break
        else:
            print("❌ 输入错误，请输入0-5的数字！")