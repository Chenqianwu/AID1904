def parse_html():
    for item in range(2):
        yield item

    print('生成器结束')

g = parse_html()
while True:
    try:
        print(g.__next__())
    except:
        break








