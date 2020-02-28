[返回](../README.md)

```
# -*- conding: utf-8 -*-
import threading 
from threading import local

class Singleton(object):

    """
    单例类-装饰器
    用于需要实现单例的任何类
    注意，不能用于多线程
    """
    _instance_lock = threading.Lock()

    def __init__(self, cls):
        """
            参数： cls 类参数
        """

        self._cls = cls

    def __del__(self):
        pass

    def Instance(self):
        """
            返回 实例
        """
        if not hasattr(self, "_instance"):
            with self._instance_lock:
                if not hasattr(self, "_instance"):
                    # 如果实例不存在则赋值
                    self._instance = self._cls()
        return self._instance

    def __call__(self):
        # 防止单例类函数调用
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __insstancecheck__(self, inst):
        # 判断一个对象是否是一个已知的类型
        return isinstance(inst, self._decorated)

# 装饰器
@Singleton
class A:
    """一个需要单列模式的类"""
    def __init__(self):
        pass

    def display(self):
        return id(self)


def add(i):
    s1 = A.Instance()
    print(i, s1, s1.display())

if __name__ == '__main__':
    # 创建两个实例
    for i in range(40):
        th = threading.Thread(target=add, args=(i,))
        th.start()

```