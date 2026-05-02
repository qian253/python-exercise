import pygame
import random

# -------------------------- 初始化部分 --------------------------
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python 贪吃蛇游戏")

# 颜色定义（RGB格式）
BLACK = (0, 0, 0)  # 背景色
WHITE = (255, 255, 255)  # 文字色
RED = (255, 0, 0)  # 食物颜色
GREEN = (0, 255, 0)  # 蛇的颜色

# 游戏基础参数
GRID_SIZE = 20  # 格子大小（蛇和食物的单位）
SPEED = 10  # 游戏帧率（越大越快）
clock = pygame.time.Clock()


# -------------------------- 游戏重置函数 --------------------------
def reset_game():
    """重置游戏状态，初始化蛇、食物、方向和分数"""
    # 蛇的初始身体（列表存储每个格子的坐标）
    snake = [
        [WIDTH // 2, HEIGHT // 2],
        [WIDTH // 2 - GRID_SIZE, HEIGHT // 2],
        [WIDTH // 2 - 2 * GRID_SIZE, HEIGHT // 2]
    ]
    # 随机生成食物（必须对齐格子）
    food = [
        random.randrange(0, WIDTH, GRID_SIZE),
        random.randrange(0, HEIGHT, GRID_SIZE)
    ]
    # 初始方向（向右）
    dir_x, dir_y = GRID_SIZE, 0
    # 初始分数
    score = 0
    return snake, food, dir_x, dir_y, score


# 初始化游戏状态
snake, food, dir_x, dir_y, score = reset_game()
game_over = False

# -------------------------- 主游戏循环 --------------------------
while True:
    # 1. 事件监听（处理关闭窗口、按键操作）
    for event in pygame.event.get():
        # 关闭窗口
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 方向控制（防止直接掉头）
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir_y != GRID_SIZE:
                dir_x, dir_y = 0, -GRID_SIZE
            elif event.key == pygame.K_DOWN and dir_y != -GRID_SIZE:
                dir_x, dir_y = 0, GRID_SIZE
            elif event.key == pygame.K_LEFT and dir_x != GRID_SIZE:
                dir_x, dir_y = -GRID_SIZE, 0
            elif event.key == pygame.K_RIGHT and dir_x != -GRID_SIZE:
                dir_x, dir_y = GRID_SIZE, 0

    # 2. 游戏逻辑更新（未结束时执行）
    if not game_over:
        # 蛇头移动（在列表最前面插入新头部）
        head = [snake[0][0] + dir_x, snake[0][1] + dir_y]
        snake.insert(0, head)

        # 吃到食物：不删除尾部，蛇变长；否则删除尾部，保持长度
        if head[0] == food[0] and head[1] == food[1]:
            score += 10
            # 重新生成食物（避免生成在蛇身上）
            while True:
                food = [
                    random.randrange(0, WIDTH, GRID_SIZE),
                    random.randrange(0, HEIGHT, GRID_SIZE)
                ]
                if food not in snake:
                    break
        else:
            snake.pop()

        # 碰撞检测：撞墙 / 撞到自己
        if (head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake[1:]):
            game_over = True

    # 3. 绘制画面
    screen.fill(BLACK)  # 填充背景

    # 画食物
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    # 画蛇（遍历每个身体格子）
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # 4. 显示分数（已修复字体问题）
    font = pygame.font.Font(None, 30)  # 兼容性写法，不会报错
    score_text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 5. 游戏结束提示
    if game_over:
        end_text = font.render("游戏结束！按 R 重新开始", True, WHITE)
        screen.blit(end_text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))
        # 按R键重置游戏
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            snake, food, dir_x, dir_y, score = reset_game()
            game_over = False

    # 更新画面 & 控制帧率
    pygame.display.update()
    clock.tick(SPEED)