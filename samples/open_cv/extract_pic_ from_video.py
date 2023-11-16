import cv2


def transfer(video, save):  # 定义转换过程
    cap = cv2.VideoCapture(video)
    num = 0
    while True:
        if cap.grab():
            num += 1
            if num % 60 == 1:  # 每60帧截取一个图片
                flag, frame = cap.retrieve()  #解码并返回一个帧
                if not flag:
                    continue
                else:
                    cv2.imshow('video', frame)
                    new = save + "\\" + str(int(num / 60)) + ".jpg"
                    print('正在输出：' + str(int(num / 60)) + ".jpg(按Esc停止运行)")
                    cv2.imencode('.jpg', frame)[1].tofile(new)
        else:  # 运行完毕自动退出
            break
        if cv2.waitKey(10) == 27:  # 检测到按下Esc时退出
            break


print('欢迎来到视频连续截图自动生成系统！')
video = input('请输入你的视频文件路径(要包含文件名后缀，如：F:/四级核心.mp4)：')  # 在此处设置你的视频文件路径以及图片输出路径
save = input('请输入你的图片输出文件夹路径(要用/单斜杠隔开)：')
transfer(video, save)  # 主程序启动
print('运行完毕！')