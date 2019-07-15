class student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    
    def xg_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('值输入错误')
            


    def print_s(self):
        print('%s %s' % (self.__name,self.__score))

    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    
