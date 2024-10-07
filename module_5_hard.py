import time

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)
    def __repr__(self) -> str:
        return self.nickname
    def __str__(self) -> str:
        return self.nickname
    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and self.password == other.password
        else:
            return 'Неверный класс объекта. Для корректной работы метода представьте объект класса User'

class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __repr__(self) -> str:
        return self.title
    def __str__(self) -> str:
        return self.title
    def watch(self):
        for sec in range(self.time_now + 1, self.duration + 1):
            print(sec, end=" ")
            time.sleep(1)
        print("Конец видео")

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        int_us_n = [i.nickname for i in self.users]
        if nickname in int_us_n:
            ind_ = int_us_n.index(nickname)
            value_ = self.users[ind_]
            if hash(password) == value_.password:
                self.current_user = value_
            else:
                print("Неверный пароль!")
        else:
            print("Пользователь не найден!")
    def register(self, nickname, password, age):
        if nickname not in [i.nickname for i in self.users]:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
        else:
            print(f"Пользователь {nickname} уже существует")
    def log_out(self):
        self.current_user = None
    def add(self, *args):
        for ep in args:
            if type(ep) == Video and ep not in self.videos:
                self.videos.append(ep)
    def get_videos(self, title):
        int_list = []
        for ep in self.videos:
            if title.lower() in ep.title.lower():
                int_list.append(ep.title)
        return int_list
    def watch_video(self, title_: str):
        if type(self.current_user) != User:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            int_tit_ = [i.title for i in self.videos]
            if title_ in int_tit_:
                ind_vi = int_tit_.index(title_)
                value_vi = self.videos[ind_vi]
                if value_vi.adult_mode == True:
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    else:
                        value_vi.watch()
                else:
                    value_vi.watch()
            else:
                pass



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
