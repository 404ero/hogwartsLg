#定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
#see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
# 如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
#fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
# 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
class TongLao:
    TL_hp = 2000
    TL_power = 300

    def __init__(self,hp_enemy,power_enemy,name):
        self.hp_enemy = hp_enemy
        self.power_enemy = power_enemy
        self.name = name
    
    def see_people(self):
        if(self.name=='WYZ'):
            print('师弟！！！!')
        elif(self.name=='LQS'):
            print('呸！贱人！')
        elif(self.name=='DCQ'):
            print('叛徒！我杀了你！')

    def fight_zms(self):
        print('准备战斗！')
        self.TL_power = self.TL_power*10
        self.TL_hp = self.TL_hp/2
        # 开始进行回合制对打
        TL_hp = self.TL_hp-self.power_enemy
        hp_enemy = self.hp_enemy - self.TL_power
        # 判断各自的血量
        if(TL_hp > hp_enemy):
            print(f'天山童姥获胜！hp-hp1:{self.TL_hp-self.power_enemy>self.hp_enemy-self.TL_power}')
        elif(TL_hp == hp_enemy):
            print('满足虚竹！打平手了')
        else:
            print(f'{self.name}获胜！天山童姥over!')




        