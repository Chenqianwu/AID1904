import re

html = '''<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>'''

pattern = re.compile(
    '<div class="animal">.*?title="(.*?)".*?'
    'class="content">(.*?)</p>',
    re.S
)
r_list = pattern.findall(html)
# r_list:[('Tiger', '\n\t\tTwo tigers two tigers run fast\n    '), ('Rabbit', '\n\t\tSmall white rabbit white and white\n    ')]
# 处理数据都是一条一条处理
for rt in r_list:
    print('动物名称:',rt[0].strip())
    print('动物描述:',rt[1].strip())
    print('*' * 50)


# 'hello world'.strip()  --> 'hello world'
# 'hello world'.split(' ')  --> ['hello','world']
# 'hello world'.replace(' ','#') -> 'hello#world'









