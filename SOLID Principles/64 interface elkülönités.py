# class Employee:
#     def work(self):
#         pass
#
#     def manage(self):
#         pass


class Workable:
    def work(self):
        pass


class Manageable:
    def manage(self):
        pass

class Employee(Workable):
    def work(self):
        print('Melozik')


class Maneeger(Workable, Manageable):
    def work(self):
        print('Melozik')

    def manage(self):
        print('Vezet')
