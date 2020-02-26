# -*- coding: utf-8 -*-

class Question(object):
    """
    问题对象，没有使用策略模式之前的作法
    """

    def __init__(self, admin=True):
        self._admin = admin

    def show(self):
        """
        根据是否是管理员显示不同的信息
        """
        if self._admin is True:
            return "show page with admin"
        else:
            return "show page with user"


if __name__ == '__main__':
    q = Question(admin=False)
    print(q.show())