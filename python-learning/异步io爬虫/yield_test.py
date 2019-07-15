


# def comm():
#     r = ''
#     while True:
#         n = yield r
#         print("Comm to %s"%n)
#         r = '200ok'
#
# def pro(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         print("web c")
#         r = c.send(n)
#         print("%s oK" %r)
#         n += 1
#     c.close()
#
# if __name__ == "__main__":
#     c = comm()
#     pro(c)









