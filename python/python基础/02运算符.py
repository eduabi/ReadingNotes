# 01.赋值运算符：将运算符右边的值(或计算结果)赋给运算符左边
num1 = 2
num2 = 6

# 02.算术运算符：主要用于两个变量值的算数计算(加减乘除等运算)
# 加法：+
print(num1 + num2)  # 输出：8
# 减法：-
print(num2 - num1)  # 输出：4
# 乘法：*
print(num2 * num1)  # 输出：12
# 除法：/
print(num2 / num1)  # 输出：3.0
# 取整除(取商的整数部分): //
print(num1 // num2)  # 输出：0
# 取模(返回除法运算后的余数)：%
print(num1 % num2)  # 输出：2
# 幂运算：**
print(num1 ** num2)  # 输出：64

# 03.关系运算符：用于两个值比较
# 等于：==
print(num1 == num2)  # 输出：False
# 不等于：!=
print(num1 != num2)  # 输出：True
# 大于：>
print(num1 > num2)  # 输出：False
# 小于：<
print(num1 < num2)  # 输出：True
# 大于等于：>=
print(num1 >= num2)  # 输出：False
# 小于等于：<=
print(num1 <= num2)  # 输出：True

# 04.逻辑运算符：用于逻辑运算(与或非等)
# 与运算：and
print(num1 and num2)  # 输出：6
# 或运算：or
print(num1 or num2)  # 输出：2
# 非运算：not
print(not num1)  # 输出：False

# 05.位运算符：用来对二进制位进行操作
# 按位与(对应的两个二进制位都为1,则该位的结果为1,否则为0)：&
print(num1 & num2)  # 输出：2
# 按位或(只要对应的两个二进制位有一个为1时，结果位就为1)：|
print(num1 | num2)  # 输出：6
# 按位异或(对应的两个二进制位不同时，结果为1)
print(num1 ^ num2)  # 输出：4
# 按位取反运算符(对数据的每个二进制位取反,即把1变为0,把0变为1):~
print(~num1)  # 输出：-3
# 左移动算符：运算数的各二进制位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
print(num1 << 2)  # 输出：8
# 右移动运算符：把">>"左边的运算数的各二进制位全部右移若干位，">>"右边的数指定移动的位数
print(num1 >> 2)  # 输出：0

# 06.成员运算符：判断一个对象是否包含另一个对象
str1 = 'x'
str2 = 'xyz'
# in：如果在指定的序列中找到值返回 True，否则返回 False
print(str1 in str2)  # 输出：True
# not in: 如果在指定的序列中没有找到值返回 True，否则返回 False
print(str1 not in str2)  # 输出：False

# 07:身份运算符：判断是不是引用自一个对象
# is: 判断两个标识符是不是引用自一个对象
print(id(str1) is id(str2))  # 输出：False
# is not: 判断两个标识符是不是引用自不同对象
print(id(str1) is not id(str2))  # 输出：True
