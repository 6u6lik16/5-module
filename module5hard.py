import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.nickname}"

    def __repr__(self):
        return f"User(nickname={self.nickname!r})"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.curent_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.curent_user = user
                    return
        print("Ошибка входа!")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Ошибка: никнейм '{nickname}' уже занят.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        if self.curent_user:
            print(f"Пользователь {self.curent_user.nickname} вышел.")
            self.curent_user = None
        else:
            print("Никто не вошел в систему.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
            else:
                print(f"Ошибка: видео с названием '{video.title}' уже существует.")

    def watch_video(self, title):
        if self.curent_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.curent_user.age < 18:
                    print("Вам нет 18 лет.")
                    return
                print(f"Воспроизведение видео: '{video.title}'")
                for second in range(video.duration):
                    print(f"Прошло {second + 1} секунд.")
                    time.sleep(1)
                print("Конец видео.")
                return
        print(f"Ошибка: видео с названием '{title}' не найдено.")

    def get_videos(self, search_term):
        matching_videos = [video.title for video in self.videos if search_term.lower() in video.title.lower()]
        return matching_videos


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
print(ur.curent_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
