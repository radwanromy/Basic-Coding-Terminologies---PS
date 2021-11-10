from __future__ import division
n = input()
arr = map(int,raw_input().split())
c1 = len(filter(lambda x:x>0,arr))
c2 = len(filter(lambda x:x<0,arr))
c3 = len(filter(lambda x:x==0,arr))
print '%.7f' % (c1/n)
print '%.7f' % (c2/n)
print '%.7f' % (c3/n)