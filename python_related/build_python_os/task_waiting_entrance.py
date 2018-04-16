#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/16 下午3:41
from python_related.build_python_os.pyos2 import Scheduler
from python_related.build_python_os.system_call import NewTask, WaitTask

# 这个方法只存在两个协程，一个是main， 另一个是foo


"""
设计讨论

without WaitTask:

I'm foo
waiting for child
child done
Task 1 terminated
I'm foo
I'm foo
I'm foo
I'm foo
Task 2 terminated

with WaitTask:

I'm foo
waiting for child
I'm foo
I'm foo
I'm foo
I'm foo
Task 2 terminated
child done
Task 1 terminated

这是一个封装和安全策略

它可以保持任务分离（存疑）

它将所有的任务管理放置在调度程序中(这才是它应该在的地方)

"""

if __name__ == '__main__':
    def foo():
        for i in xrange(5):
            print "I'm foo"
            yield

    # 这里main方法必须等到foo()遍历完成才能继续执行(从 exit_waiting 重新回到 ready)
    def main():
        child = yield NewTask(foo())
        print "waiting for child"
        yield WaitTask(child)
        print "child done"

    sched = Scheduler()
    sched.new(main())
    sched.mainloop()
