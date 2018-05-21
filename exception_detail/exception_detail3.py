# Copyright(C) 2018 刘珅珅
# Environment: python 3.6.4
# Date: 2018.5.12
# with/as环境管理


class TraceBlock:
    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test1')
        print('reached')

    with TraceBlock() as action2:
        action2.message('test 2')
        raise TypeError
        print('not reached')
