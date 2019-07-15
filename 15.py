#class student(object):

#    @property
#    def score(self):
#        return self._score

#    @score.setter
#    def score(self,cj):
#        if not isinstance(cj,int):
#            raise ValueError('尊敬的用户您好，我是你爹')
#        if cj < 0 or cj > 100:
#            raise ValueError('尊敬的用户您好，我是你大爷')
#        self._score = cj


#    @property
#    def brith(self):
#        return self._brith

#    @brith.setter
#    def brith(self,nl):
#        self._brith = nl

#    @property
#    def age(self):
#        return 2019 - self._brith


# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,val):
        self._width = val
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val):
        self._height = val
    @property
    def resolution(self):
        return self._height * self._width
    


        
