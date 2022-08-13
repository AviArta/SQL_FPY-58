-- название и год выхода альбомов, вышедших в 2018 году
select title_album, release_year_album from albums
where release_year_album = 2018

-- название и продолжительность самого длительного трека
select name_track, duration_track from tracks
order by duration_track desc 
limit 1

-- название треков, продолжительность которых не менее 3,5 минуты
select name_track from tracks
where duration_track >= 210

-- названия сборников, вышедших в период с 2018 по 2020 год включительно
select title_collection from collections
where release_year_collection between 2018 and 2020

-- исполнители, чье имя состоит из 1 слова
select name_artist from artists
where name_artist not like '% %'

-- название треков, которые содержат слово "мой"/"my"
select name_track from tracks
where name_track like '%мой%' or name_track like '%my%'

