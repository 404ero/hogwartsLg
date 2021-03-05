import pytest

'''
# 如果出现导包出错时，可以采用sys.path.append('..')
将当前文件的上级目录加到sys.path里
'''

from pytestCode.testCode.calculator import Calculator
import yaml

'''
pytest命名规则：
文件名：以test_ 开头,(test_*.py)
类名：以Test开头
方法名：以test_ 开头

测试用例常用参数：
pytest -x 文件名：pytest test_cal.py -vs -x 一旦运行到报错，就直接终止后面的所有测试用例的执行  如应用在冒烟测试中
pytest --maxfail=num  当运行的产生错误数达到最大值num时，则停止运行
pytest -k "类名 and not 方法名" 执行某个关键字的用法
pytest -m [标记名]  @pytest.mark.[标记名] 将运行有这个标记的测试用例
--lf  pytest test_cal.py -vs --lf  运行上一次执行失败的用例，上一次没有失败的则全部执行
--ff  pytest test_cal.py -vs --ff  先执行上一次失败的用例，后执行上一次成功的用例
pytest --collect-only   pytest test_cal.py -vs --cpllect-only  只收集用例  不执行用例
pytest --junitxml=./result.xml  生成执行结果文件
pytest --setup-show  回溯fixture的执行过程
'''

'''
# 可以在类外面加参数化，前提是类中的方法用的同一套参数
@pytest.mark.parametrize('a,b,expect',[
        (1,1,2),
        (0.1,0.1,0.2),
        (1,1,3),
        (100,200,301),
        (1000,1000,2000)
    ],ids=['int','float','int2','int100','int1000'])
'''


# 读取测试数据
def get_datas():
    list = []
    with open('../data/calc.yaml', encoding='utf-8') as f:
        myDatas = yaml.safe_load(f)
        addDatas = myDatas['add']['datas']
        ids = myDatas['add']['myIds']
        subDatas = myDatas['sub']['datas']
        sub_ids = myDatas['sub']['myIds']
        list.append(addDatas)
        list.append(ids)
        list.append(subDatas)
        list.append(sub_ids)
    return list


class TestCalc:
    '''
      测试相加
    '''

    # 类级别的setup，只在类实例化的时候调用一次
    def setup_class(self):
        print('开始计算')
        self.calc = Calculator()

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        print('测试相加')
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', [
        (0.1, 0.1, 0.2),
        (0.1, 0.2, 0.3)
    ], ids=['float', 'float2'])
    def test_add_float(self, a, b, expect):
        print('测试相加')
        # result=0.300000000000004 此时由于Python的运算机制导致浮点型出现丢位的情况
        # 通过round()方法处理
        result = round(self.calc.add(a, b), 2)
        print(result)
        assert expect == result

    @pytest.mark.add
    def test_add2(self):
        print('测试相加')
        result = self.calc.add(100, 200)
        assert 301 == result

    @pytest.mark.add
    @pytest.mark.parametrize('a', [1, 2, 3])
    @pytest.mark.parametrize('b', [4, 5, 6, 7])
    def test_case2(self, a, b, expect):
        print(f'测试类似笛卡尔积的，a={a} b={b}')

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_sub(self, a, b, expect):
        print('测试相减')
        result = self.calc.sub(a, b)
        assert expect == result

    # 小数相减会出现浮点型的丢位情况  round进行四舍五入
    @pytest.mark.parametrize('a,b,expect', [
        (0.2, 0.1, 0.1),
        (0.1, 0.2, -0.1)
    ], ids=['float', 'float2'])
    def test_sub_float(self, a, b, expect):
        print('测试浮点型的相减')
        # result=0.300000000000004 此时由于Python的运算机制导致浮点型出现丢位的情况
        # 通过round()方法处理
        result = round(self.calc.sub(a, b), 2)
        print(result)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    @pytest.mark.div
    def test_div2(self, a, b, expect):
        print('测试相除')
        result = self.calc.div(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    @pytest.mark.mul
    def test_div2(self, a, b, expect):
        print('测试相乘')
        result = self.calc.mul(a, b)
        assert expect == result
