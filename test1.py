"""
 * Project name(项目名称)：Python_pathlib模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 20:31
 * Version(版本): 1.0
 * Description(描述)：
 PurePath 类会将路径看做是一个普通的字符串，它可以实现将多个指定的字符串拼接成适用于当前操作系统的路径格式，
 同时还可以判断任意两个路径是否相等。注意，使用 PurePath 操作的路径，它并不会关心该路径是否真实有效。
PurePosixPath 和 PureWindowsPath 是 PurePath 的子类，前者用于操作 UNIX（包括 Mac OS X）风格的路径，后者用于操作 Windows 风格的路径。
Path 类和以上 3 个类不同，它操作的路径一定是真实有效的。Path 类提供了判断路径是否真实存在的方法。
PosixPath 和 WindowPath 是 Path 的子类，分别用于操作 Unix（Mac OS X）风格的路径和 Windows 风格的路径。
 """
from pathlib import PurePath, PurePosixPath, PureWindowsPath

if __name__ == '__main__':
    path = PurePath('file.txt')
    print(type(path))
    path = PurePath("D:", "files", "file.txt")
    print(path)
    path = PurePath("D:", "E:", "files", "file.txt")
    print(path)
    path = PurePath("D:\\.\\files\\file.txt")
    print(path)
    path = PurePath("D:\\files\\..\\file.txt")
    print(path)
    print(PurePosixPath('C://file.txt') == PurePosixPath('c://file.txt'))
    print(PureWindowsPath('C://file.txt') == PureWindowsPath('c://file.txt'))
