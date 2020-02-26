# -*- coding: utf-8 -*-
import threading 
import time

exitFlag = 0

class Singleton:

    """
    单例类装饰器，可以用于想实现单例的任何类。注意，不能用于多线程环境。
    """

    def __init__(self, cls):
        """ 需要的参数是一个类 """
        self._cls = cls

    def Instance(self):
        """
        返回真正的实例
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        print("__instancecheck__")
        return isinstance(inst, self._decorated)


# 装饰器
@Singleton
class A:
    """一个需要单列模式的类"""
    def __init__(self):
        pass

    def display(self):
        return id(self)

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        s2 = A.Instance()
        print(s2, s2.display())
        #print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

if __name__ == '__main__':
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    s1 = A.Instance()
    #s2 = A.Instance()
    print(s1, s1.display())
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    #print(s2, s2.display())
    #print(s1 is s2)