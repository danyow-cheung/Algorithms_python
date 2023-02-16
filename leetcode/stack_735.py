import collections
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # res = collections.defaultdict
        res = []
        for i in asteroids:
            print('res',res)
            
            # 方向相同，不会发生碰撞
            
            res.append(i)
            # 方向不同，留大的再压进栈
            if i<0:
                pop = res.pop()
                print('pop',pop,'i',i)
                if abs(pop) >abs(i):
                    print('')
                    res.append(pop)
                elif pop+i==0:
                    print('距离相同，两个都爆炸')
                    # res = res.pop()
                    continue
                else:
                    res.append(i)
        print(res)
        # while
        # 当返回里面有负数，需要进行再一次对比 ,再次处理
        while  len(res)!=0  and min(res) <0:
            min_idx = res.index(min(res))
            
            # 首先是个负数，ok如果比任意左右都小，就删除
            if min_idx<len(res)-1 and abs(res[min_idx]) <abs(res[min_idx+1]):
                res.remove(min(res))

            elif min_idx>0 and  abs(res[min_idx]<res[min_idx-1]):
                res.remove(min(res))
            else:
                # 刚好是最后一位
                if abs(min(res))<res[-2]:
                    res.remove(min(res))



        print(res)
        return res 

    def asteroidCollision_v2(self, asteroids):
        res = []
        for i in asteroids:
            

            if len(res)==0:
                res.append(i)
            else:
                last = res.pop()
                # 符号相同不变化
                print('res',res,'last',last,'cur',i)

                if (i <0 and last<0) or(i>0 and last>0):
                    res.append(last)
                    res.append(i)
                else:
                    if abs(last)>abs(i):
                        res.append(last)
                    elif abs(last)==abs(i):
                        print('abs== do somthing')
                        continue
                    else:
                        res.append(i)
        print(res)
        # 当返回里面有负数，需要进行再一次对比 ,再次处理
        while  len(res)!=0  and min(res) <0:
            min_idx = res.index(min(res))
            
            # 首先是个负数，ok如果比任意左右都小，就删除
            if min_idx<len(res)-1 and abs(res[min_idx]) <abs(res[min_idx+1]):
                res.remove(min(res))

            elif min_idx>0 and  abs(res[min_idx]<res[min_idx-1]):
                res.remove(min(res))
            else:
                # 刚好是最后一位
                if abs(min(res))<res[-2]:
                    res.remove(min(res))



        # print(res)
        return res 



asteroids = [5,10,-5]
asteroids = [8,-8]
asteroids = [10,2,-5]
asteroids = [-2,-1,1,2] # 返回应该为[原数组]




# obj = Solution().asteroidCollision(asteroids)
obj = Solution().asteroidCollision_v2(asteroids)
