"""
 * Project name(项目名称)：Python_pathlib模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 20:36
 * Version(版本): 1.0
 * Description(描述)：
 PurePath.parts	返回路径字符串中所包含的各部分。
PurePath.drive	返回路径字符串中的驱动器盘符。
PurePath.root	返回路径字符串中的根路径。
PurePath.anchor	返回路径字符串中的盘符和根路径。
PurePath.parents	返回当前路径的全部父路径。
PurPath.parent	返回当前路径的上一级路径，相当于 parents[0] 的返回值。
PurePath.name	返回当前路径中的文件名。
PurePath.suffixes	返回当前路径中的文件所有后缀名。
PurePath.suffix	返回当前路径中的文件后缀名。相当于 suffixes 属性返回的列表的最后一个元素。
PurePath.stem	返回当前路径中的主文件名。
PurePath.as_posix()	将当前路径转换成 UNIX 风格的路径。
PurePath.as_uri()	将当前路径转换成 URL。只有绝对路径才能转换，否则将会引发 ValueError。
PurePath.is_absolute()	判断当前路径是否为绝对路径。
PurePath.joinpath(*other)	将多个路径连接在一起，作用类似于前面介绍的斜杠（/）连接符。
PurePath.match(pattern)	判断当前路径是否匹配指定通配符。
PurePath.relative_to(*other)	获取当前路径中去除基准路径之后的结果。
PurePath.with_name(name)	将当前路径中的文件名替换成新文件名。如果当前路径中没有文件名，则会引发 ValueError。
PurePath.with_suffix(suffix)	将当前路径中的文件后缀名替换成新的后缀名。如果当前路径中没有后缀名，则会添加新的后缀名。
 """
from pathlib import PurePath

if __name__ == '__main__':
    path = PurePath("D:\\", "files", "file.txt")
    print(path)
    print(path.parts)
    print(path.drive)
    print(path.root)
    print(path.anchor)
    print(path.parents)
    print(path.parent)
    print(path.name)
    print(path.suffixes)
    print(path.suffix)
    print(path.stem)
    print(path.as_posix())
    print(path.as_uri())
    print(path.is_absolute())

