class User():
    """список пользователей"""

    def __init__(self, nickname=str, password=int, age=int):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # пароль в хэшированном виде, число
        self.age = age  # возраст, число

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)

class Video():
    """список видеофайлов"""

    def __init__(self, title=str, duration=int, time_now=0, adult_mode=False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now
        self.adult_mode = adult_mode  # ограничение по возрасту

    def __repr__(self):
        """Формальное строковое представление."""
        return f'{self.title} '

class UrTube():
    """список просмотра видео пользователем"""

    def __init__(self):
        self.videos = []  # список объектов Video
        self.users = []  # список объектов Users
        self.current_user = None

    def log_in(self, nickname, password):
        self.current_user = nickname
        return self.current_user

    def register(self, nickname, password, age):

        self.nickname = nickname
        self.password = password
        self.age = age
        self.user = User(self.nickname, self.password, self.age)

        if self.user not in self.users:
            self.users.append(self.user)
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self, current_user):
        self.current_user = None
        return self.current_user

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        self.urtube_list = []
        for w in self.videos:
            if str(w).lower().count(word.lower()) > 0:
                self.urtube_list.append(w)
        return self.urtube_list

    def watch_video(self, video_name):

        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')

        else:
            for video in self.videos:
                if video_name == video.title:
                    if self.age < 18 and video.adult_mode == True:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        import time
                        for t in range(1, 11):
                            time.sleep(1)
                            print(str(t), end=' ')
                        print('Конец видео')


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
