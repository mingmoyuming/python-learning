def gen_func():
    html = yield "http://print.com"
    print(html)
    yield 2
    yield 3
    return "body"
#1.生成器不止可以产出值，还可以接受值


if __name__ == "__main__":
    gen = gen_func()
    #启动生成器两种方式，next(),，一个是send
    url = next(gen)
    html = "boby"
    gen.send(html)#send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield生成器
    #print(next(gen))
    #print(next(gen))
    #print(next(gen))
    #print(next(gen))
