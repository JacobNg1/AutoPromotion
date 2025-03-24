from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import os, time
# 创建时间戳
timestamp = int(time.time())  # 获取当前时间戳（单位：秒）


def create_moment(avatar_path, user_id, content, image_paths, comments, output_path, bg_color=(245, 245, 245)):
    """
    生成朋友圈风格的图片，包含头像、正文、图片区域、评论区。
    """
    # 创建画布
    #img = Image.new('RGB', (1242, 2208), color=bg_color)
    img = Image.new('RGB', (1348, 2000), color=bg_color)
    draw = ImageDraw.Draw(img)

    # 加载字体（请自行提供苹方字体文件）
    font_path = "苹方黑体-准-简.ttf"
    id_font = ImageFont.truetype(font_path, 46)
    content_font = ImageFont.truetype(font_path, 44)
    meta_font = ImageFont.truetype(font_path, 40)
    comment_font = ImageFont.truetype(font_path, 44)

    # ===== 头像处理（圆角矩形） =====
    avatar_size = (112, 112)
    avatar = Image.open(avatar_path).resize(avatar_size)
    mask = Image.new('L', avatar_size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, *avatar_size), radius=20, fill=255)
    img.paste(avatar, (72, 96), mask)

    # ===== 用户ID =====
    id_x = 72 + avatar_size[0] + 36
    id_y = 100
    draw.text((id_x, id_y), user_id, font=id_font, fill="#878e99")

    # ===== 正文内容 =====
    content_width = 1100
    y_position = 168
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        lines = textwrap.wrap(para, width=25)
        for line in lines:
            draw.text((72 + avatar_size[0] + 36, y_position), line, font=content_font, fill=(15, 15, 15))
            y_position += 54
        y_position += 30

    # ===== 图片区域（朋友圈图片） =====
    if image_paths:
        y_position = add_moment_images(draw, img, image_paths, y_position)

    # ===== 时间信息 =====
    time_y = y_position + 36
    draw.text((72 + avatar_size[0] + 36, time_y), "3分钟前", font=meta_font, fill=(140, 140, 140))

    # 删除图标处理
    delete_icon_path = 'delete_icon.png'
    delete_icon = Image.open(delete_icon_path).resize((36, 36))

    # 如果图标有透明背景，使用 alpha 通道作为掩码
    if delete_icon.mode == 'RGBA':
        mask = delete_icon.split()[3]  # 获取 alpha 通道作为掩码
    else:
        mask = Image.new('L', delete_icon.size, 255)  # 若无 alpha 通道，创建一个全不透明的掩码

    # 计算图标显示位置
    icon_x = 72 + avatar_size[0] + 36 + 200
    icon_y = time_y + 8

    # 将图标粘贴到背景图上
    img.paste(delete_icon, (icon_x, icon_y), mask)

    # # ===== 评论区背景（浅灰色+圆角） =====
    # comment_bg_y = time_y + 96
    # comment_bg = (230, 230, 230)
    # comment_area = (72, comment_bg_y, 1242 - 72, comment_bg_y + len(comments) * 88 + 60)
    # draw.rounded_rectangle(comment_area, radius=30, fill=comment_bg)

    # # ===== 评论区内容 =====
    # comment_y = comment_bg_y + 30
    # for comment in comments:
    #     draw.text((96, comment_y), comment, font=comment_font, fill=(80, 80, 80))
    #     comment_y += 88
    #
    # 设置保存路径和文件名
    output_dir = 'output'  # 输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 如果目录不存在则创建

    output_path = os.path.join(output_dir, f"wechat_moment_{timestamp}.jpg")

    # 保存图片
    img.save(output_path, quality=95)
    print(f'Save as {output_path}')


def add_moment_images(draw, img, image_paths, y_position):
    """朋友圈 Post 图片处理"""
    if not image_paths:
        return y_position

    image_count = len(image_paths)
    max_width = 900  # 单张图最大宽度
    gap = 20  # 图片间距

    if image_count == 1:
        # **单张图片 - 保持原比例**
        post_img = Image.open(image_paths[0])
        w, h = post_img.size
        ratio = min(max_width / w, 1)  # 确保不会超出最大宽度
        new_size = (int(w * ratio), int(h * ratio))
        post_img = post_img.resize(new_size)
        img.paste(post_img, (72 + 112 + 32, y_position))
        return y_position + new_size[1] + gap

    elif image_count == 4:
        # **4 张图片 - 2x2 布局**
        grid_size = 320  # 统一大小
        for idx, img_path in enumerate(image_paths[:4]):
            row, col = divmod(idx, 2)
            img_x = 72 + 112 + 32 + col * (grid_size + gap)
            img_y = y_position + row * (grid_size + gap)
            post_img = Image.open(img_path).resize((grid_size, grid_size))
            img.paste(post_img, (img_x, img_y))
        return y_position + 2 * (grid_size + gap)

    else:
        # **2-3 / 5-9 张图片 - 九宫格**
        grid_size = 280  # 控制图片大小
        cols = 3  # 每行最多3列
        for idx, img_path in enumerate(image_paths[:9]):
            row, col = divmod(idx, cols)
            img_x = 72 + 112 + 32 + col * (grid_size + gap)
            img_y = y_position + row * (grid_size + gap)
            post_img = Image.open(img_path).resize((grid_size, grid_size))
            img.paste(post_img, (img_x, img_y))
        rows = (image_count - 1) // cols + 1
        return y_position + rows * (grid_size + gap)





# 示例调用
create_moment(
    avatar_path="input_avatar2.png",
    user_id="Oxygen",
    content="""我最爱吴卓波了\n\n希望可以在一起一辈子❤""",
    image_paths=["pp.jpg"],
    comments=["用户A: 这也太棒了吧！", "用户B: 真的很喜欢这个设计"],
    output_path="output_.jpg"
)