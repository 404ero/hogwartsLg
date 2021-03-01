from hogwarts.LG3_task.Game.XuZhu import XuZhu
from hogwarts.LG3_task.Game.TongLao import TongLao
class Fight:

  if __name__ == '__main__':

    xuZhu = XuZhu(1000,100,'LQS')
    xuZhu.read()
    xuZhu.see_people()
    xuZhu.fight_zms()

    tongLao = TongLao(2000,2000,'DCQ')
    tongLao.see_people()
    tongLao.fight_zms()