# 六年级下册 趣味英语课堂
import time
import random

# 全局积分
score = 0

# 美化标题
def show_title():
    print("=" * 45)
    print("🍭 六年级下册 趣味英语小课堂 🍭")
    print("💡 边玩边学，英语越学越简单！")
    print("=" * 45)

# 主菜单
def show_menu():
    print("\n📚 请选择你要玩的学习项目：")
    print("1️⃣  六下必背单词")
    print("2️⃣  英语选择题闯关")
    print("3️⃣  趣味猜单词小游戏")
    print("4️⃣  简单日常英语短句")
    print("0️⃣  退出课堂")
    choose = input("\n输入数字选择：")
    return choose

# 1. 六年级下册必背核心单词
def word_study():
    global score
    print("\n📝 六年级下册重点单词｜中英对照")
    print("-" * 40)
    words = [
        ("festival", "节日"),
        ("spring", "春天；春季"),
        ("summer", "夏天；夏季"),
        ("holiday", "假期"),
        ("delicious", "美味的"),
        ("beautiful", "漂亮的"),
        ("important", "重要的"),
        ("celebrate", "庆祝"),
        ("family", "家庭"),
        ("friend", "朋友")
    ]
    for eng, chn in words:
        time.sleep(0.6)
        print(f"✅ {eng}  ——  {chn}")
    print("\n🎉 单词学习完成！+5分")
    score += 5

# 2. 英语选择题闯关
def english_choice():
    global score
    print("\n🎯 英语小闯关，开始答题！")
    print("-" * 40)
    questions = [
        {
            "q": "1. 春天 的英文是？\nA. summer   B. spring   C. winter",
            "ans": "B"
        },
        {
            "q": "2. 美味的 英文是？\nA. delicious   B. happy   C. cold",
            "ans": "A"
        },
        {
            "q": "3. friend 是什么意思？\nA. 家人   B. 老师   C. 朋友",
            "ans": "C"
        },
        {
            "q": "4. 节日 的英文？\nA. food   B. festival   C. book",
            "ans": "B"
        }
    ]
    for q in questions:
        print(q["q"])
        res = input("写下你的答案(A/B/C)：").upper()
        if res == q["ans"]:
            print("✔️ 太棒啦！回答正确 +3分\n")
            score += 3
        else:
            print(f"❌ 加油哦！正确答案是：{q['ans']}\n")

# 3. 趣味猜单词小游戏
def guess_word():
    global score
    print("\n🎮 猜单词小游戏！看中文，说出英文～")
    print("输入英文即可作答！")
    game_words = {
        "假期": "holiday",
        "漂亮的": "beautiful",
        "庆祝": "celebrate",
        "家庭": "family"
    }
    item_list = list(game_words.items())
    random.shuffle(item_list)
    for chn, eng in item_list:
        user = input(f"\n中文：{chn}  英文是：")
        if user.lower() == eng:
            print("🥳 厉害！猜对啦 +4分")
            score += 4
        else:
            print(f"😜 差一点点～正确：{eng}")

# 4. 简单日常英语短句
def daily_sentence():
    print("\n🌟 超好记的日常英语短句")
    print("-" * 40)
    sentences = [
        "Happy holiday!      假期快乐！",
        "I love my family.   我爱我的家人。",
        "What a beautiful day! 多么美好的一天！",
        "Food is delicious.   食物很美味。",
        "Spring is coming.    春天来了。"
    ]
    for s in sentences:
        time.sleep(0.5)
        print(s)
    print("\n💬 多读几遍，轻松背下来～")

# 主程序运行
if __name__ == "__main__":
    show_title()
    while True:
        op = show_menu()
        if op == "1":
            word_study()
        elif op == "2":
            english_choice()
        elif op == "3":
            guess_word()
        elif op == "4":
            daily_sentence()
        elif op == "0":
            print(f"\n🏁 本节课结束！你的总积分：{score} 分")
            print("✨ 每天学一点，英语超厉害，拜拜～")
            break
        else:
            print("\n⚠️ 只能输入 0~4 的数字哦，重新来！")
    input("\n按回车键关闭窗口～")