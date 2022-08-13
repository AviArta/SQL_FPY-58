create table if not exists genres_of_music (
	id_genre SERIAL primary key,
	name_genre text not null
);

create table if not exists artists (
	id_artist SERIAL primary key,
	name_artist text unique not null,
	genre_artist integer not null references genres_of_music(id_genre)
);

create table if not exists albums (
	id_album SERIAL primary key,
	title_album text not null,
	release_year_album smallint not null,
	name_artist_album integer not null references artists(id_artist)
);

create table if not exists tracks (
	id_track SERIAL primary key,
	name_track text not null,
	duration_track integer not null,
	album_track integer not null references albums(id_album)
);

create table if not exists collections (
	id_collection SERIAL primary key,
	title_collection text not null,
	release_year_collection integer not null
);

create table if not exists genres_artists (
	genre_id integer references genres_of_music(id_genre),
	artist_id integer references artists(id_artist),
	constraint pk_genre_artist primary key (genre_id, artist_id)
);

create table if not exists artists_albums (
	artist_id_ integer references artists(id_artist),
	album_id integer references albums(id_album),
	constraint pk_artist_album primary key (artist_id_, album_id)
);

create table if not exists collections_tracks (
	collection_id integer references collections(id_collection),
	track_id integer references tracks(id_track),
	constraint pk_collection_track primary key (collection_id, track_id)
);

