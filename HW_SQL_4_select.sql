-- 1. количество исполнителей в каждом жанре;
select name_genre, count(id_artist) from artists
join genres_of_music g on g.id_genre = artists.genre_artist 
group by name_genre 

-- 2. количество треков, вошедших в альбомы 2019-2020 годов;
select count(id_track) from tracks t
join albums a on t.album_track = a.id_album 
where release_year_album between 2019 and 2020 

-- 3. средняя продолжительность треков по каждому альбому;
select id_album, title_album, avg(duration_track) from tracks t
join albums a on t.album_track = a.id_album
group by id_album, title_album
order by id_album asc

-- 4. все исполнители, которые не выпустили альбомы в 2020 году;
select name_artist from artists 
join albums on artists.id_artist = albums.name_artist_album
group by name_artist
having name_artist not in (select name_artist from artists
join albums on artists.id_artist = albums.name_artist_album
where release_year_album = 2020)

-- 5. названия сборников, в которых присутствует конкретный исполнитель;
select title_collection from collections
join collections_tracks on collections.id_collection = collections_tracks.collection_id 
join tracks on collections_tracks.track_id = tracks.id_track 
join albums on tracks.album_track = albums.name_artist_album 
join artists_albums on albums.name_artist_album = artists_albums.artist_id_ 
join artists on artists_albums.artist_id_ = artists.id_artist
group by title_collection, name_artist
having name_artist like 'Artic%'

-- 6. название альбомов, в которых присутствуют исполнители более 1 жанра;
select title_album from albums a 
join artists ar on a.name_artist_album = ar.id_artist 
group by id_album, id_artist
having id_artist = (select artist_id from genres_artists
group by artist_id
having count(artist_id) > 1)


-- 7. наименование треков, которые не входят в сборники;
select name_track from tracks t
full join collections_tracks ct on t.id_track = ct.track_id 
where ct.track_id is null
-- рабочий, но некрасивый вариант:
-- group by name_track, id_track, collection_id, track_id
-- having id_track not in (select distinct track_id from collections_tracks)

-- 8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select name_artist from artists a
join albums on a.id_artist = albums.name_artist_album 
join tracks t on t.album_track = albums.id_album 
group by name_artist, duration_track
having duration_track = (select min(duration_track) from tracks)

-- 9. название альбомов, содержащих наименьшее количество треков. 
select title_album from albums
join tracks t on t.album_track = albums.id_album
group by title_album
having count(album_track) = (select count(album_track) from albums
join tracks t on t.album_track = albums.id_album
group by title_album
order by count(album_track) asc
limit 1)