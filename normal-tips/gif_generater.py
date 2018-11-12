import imageio


def create_gif(image_list, gif_name, duration=1):
    """
    生成 gif 文件，原始图片仅支持 png 格式
    gif_name ： 字符串，所生成的 gif 文件名，带 .gif 后缀
    path :     需要合成为 gif 的图片所在路径
    duration :  gif 图像时间间隔, 小詹这默认设置为 1 s
    """

    frames = []
    # 把图片 append 进列表
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # 保存为 gif 图
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)

    return


def main():
    # 这里小詹放的自己公号的图片
    image_list = ['1.png', '2.png', '3.png', '4.png']
    gif_name = 'new.gif'
    duration = 1.5
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()
