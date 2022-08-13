insert into genres_of_music (name_genre)
values ('Эстрадная музыка'), ('Рок музыка'), ('Хип-хоп'), ('Метал'), ('Классическая музыка')

insert into artists (name_artist, genre_artist)
values ('Artic & Asti', 1), ('Mari Kraimbrery', 1), ('Niletto', 1), ('Земфира', 2), ('Сплин', 2), 
('Мумий Тролль', 2), ('Каста', 3), ('Баста', 3), ('Noize MC', 3), ('Ария', 4), ('Кипелов', 4),
('Мастер', 4),('Пётр Чайковский', 5), ('Михаил Глинка', 5), ('Модест Мусоргский', 5)

insert into genres_artists (genre_id, artist_id)
values (1, 1), (1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 7), (3, 8), (3, 9), (4, 10), (4, 11), (4, 12),
(5, 13), (5, 1), (5, 14), (5, 15)

insert into albums (title_album, release_year_album, name_artist_album)
values ('Миллениум Х', 2021, 1), ('Номер 1', 2022, 1), 
('Переобулась', 2018, 2), ('Нас узнает весь мир', 2019, 2),
('Хентай', 2018, 3), ('Криолит', 2022, 3),
('Земфира', 1999, 4), ('Вендетта', 2005, 4),
('Встречная полоса', 2018, 5), ('Вира и майна', 2020, 5),
('Восток Х Северозапад', 2018, 6), ('После зла', 2020, 6),
('Об изъяне понятно', 2019, 7), ('Чернила осьминога', 2020, 7), 
('Папа на рейве', 2019, 8), ('Баста 40', 2020, 8),
('Царь горы', 2016, 9), ('Хипхопера', 2018, 9),
('Феникс', 2011, 10), ('Проклятье морей', 2018, 10),
('Жить вопреки', 2011, 11), ('Звёзды и кресты', 2017, 11),
('33 жизни', 2004, 12), ('VIII', 2010, 12), 
('Лебединое озеро', 1877, 13), ('Евгений Онегин', 1878, 13),
('Руслан и Людмила', 1842, 14), ('Вальс-фантазия', 1856, 14),
('Женитьба', 1868, 15), ('Борис Годунов', 1874, 15)

insert into artists_albums (artist_id_, album_id)
values (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 8), (5, 9), (5, 10),
(6, 11), (6, 12), (7, 13), (7, 14), (8, 15), (8, 16), (9, 17), (9, 18), (10, 19), (10, 20),
(11, 21), (11, 22), (12, 23), (12, 24), (13, 25), (13, 26), (14, 27), (14, 28), (15, 29), (15, 30)

insert into tracks (name_track, duration_track, album_track)
values ('Она не я', 214, 1), ('Миллениум', 191, 1),
('Таких не бывает', 180, 2), ('Ангел', 227, 2), 
('Не в адеквате', 187, 3), ('Том и Джери', 211, 3), 
('Океан', 208, 4), ('Самолёт', 188, 4), 
('Шапка', 214, 5), ('Угольки', 168, 5), 
('Ангел мой', 157, 6), ('Лёд', 158, 6), 
('-140', 233, 7), ('Ракеты', 169, 7), 
('Дыши', 250, 8), ('Самолёт', 147, 8), 
('На утро', 243, 9), ('Шпионы', 106, 9), 
('Призрак', 253, 10), ('Дежавю', 253, 10), 
('Планы', 266, 11), ('Карты', 183, 11), 
('Лира', 185, 12), ('Солист', 241, 12), 
('Фотка', 154, 13), ('Прошёл через', 260, 13),
('Пароль от почты', 272, 14), ('Всё в розовом', 74, 14), 
('Монстры', 269, 15), ('Делюга', 207, 15),
('Интро', 145, 16), ('Лампочка', 390, 16), 
('Гвозди', 210, 17), ('Грабли', 277, 17), 
('На вершине', 173, 18), ('Не мой', 166, 18), 
('Чёрная легенда', 483, 19), ('Аттила', 476, 19), 
('Варяг', 398, 20), ('Живой', 535, 20), 
('Интро', 95, 21), ('На грани', 303, 21), 
('Дама пик', 395, 22), ('Белый ад', 247, 22), 
('Игра', 229, 23), ('Экспресс', 246, 23), 
('Восьмая дверь', 63, 24), ('Воздух', 295, 24), 
('Акт 1', 900, 25), ('Акт 4', 900, 25), 
('Акт 1', 600, 26), ('Картина 7', 240, 26), 
('Действие 1', 1800, 27), ('Действие 5', 1800, 27), 
('Вальс-фантазия', 540, 28),
('Действие 1', 600, 29), ('Действие 3', 600, 29), 
('Картина 1', 300, 30), ('Картина 2', 300, 30)

insert into collections (title_collection, release_year_collection) 
values ('Сборник 2021', 2021), ('Топ 10', 2021), ('Весь хип-хоп', 2020), ('Жара', 2018), 
('РОК 2005', 2005), ('Рок хиты 2018', 2018), ('Без времени', 2000), ('Классика', 2002)

insert into collections_tracks (collection_id, track_id)
values (1, 1), (1, 3), (1, 4), (2, 2), (2, 4), (3, 27), (3, 29), (4, 3), (4, 5), (5, 13), (5, 14), (5, 23), (5, 24),
(6, 15), (6, 17), (6, 21), (7, 49), (7, 50), (8, 53), (8, 55)