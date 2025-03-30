import subprocess
import sys
import urllib.parse

POTPLAYER_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"


def main():
    try:
        # 获取并解码URL
        url = sys.argv[1]

        # 解码路径
        encoded_path = url.split(":")[1]
        path = urllib.parse.unquote(encoded_path).strip("/")
        #
        # # 确保路径存在
        # if not Path(path).exists():
        #     raise FileNotFoundError(f"找不到文件: {path}")
        #
        # # 确保 PotPlayer 存在
        # if not Path(POTPLAYER_PATH).exists():
        #     raise FileNotFoundError(f"找不到 PotPlayer: {POTPLAYER_PATH}")
        #
        subprocess.Popen([POTPLAYER_PATH, path])
    except Exception as e:
        print(f"错误: {str(e)}")
        input("按回车键退出...")  # 在出错时暂停


if __name__ == "__main__":
    main()
