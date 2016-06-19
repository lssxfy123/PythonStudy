#集合类
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, tuple))


Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(1, 1, 5)
print(circle.x, circle.y, circle.r)

#双向队列
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
print(q[0])
q.pop()
print(q)
q.popleft()
print(q)

#defaultdict
#除了在key不存在时，返回默认值之外，与dict完全相同
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#OrderedDict，有序的dict
#dict的key值是无序的
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) #按插入的顺序排列

od1 = OrderedDict()
od1['z'] = 1
od1['x'] = 2
od1['y'] = 3
print(od1)
print(list(od1.keys()))

#计数器Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    
print(c)