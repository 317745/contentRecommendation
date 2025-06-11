Table users {
  user_id int [pk, not null]
  first_name varchar(50) [not null]
  last_name varchar(50) [not null]
  date_of_birth date [not null]
  city_of_birth varchar(50) [not null]
  city_of_residence varchar(50) [not null]
  username varchar(50) [unique, not null]
  email varchar(100) [unique, not null]
  country varchar(50) [not null]
  active boolean [not null]
  created_at timestamp [not null]
}

Table media {
  media_id int [pk, not null]
  title varchar(100) [not null]
  genre varchar(50) [not null]
  audiovisual_type varchar(50) [not null]
  age_restriction varchar(50) [not null]
  actor_ids varchar[] 
  created_at timestamp [not null]
  created_country varchar(50) [not null]
}

Table actor {
  actor_id serial [pk]
  api_id varchar(100) [unique, not null]
  actor_name varchar(100) [not null]
}

Table media_actor {
  media_id int [not null, ref: > media.media_id]
  actor_id int [not null, ref: > actor.actor_id]
  primary key (media_id, actor_id)
}

Table song {
  song_id int [pk, not null]
  title varchar(100) [not null]
  song_genre varchar(50) [not null]
  song_rating varchar(50) [not null]
  artist_ids varchar[] 
  created_at date [not null]
  created_country varchar(50) [not null]
}

Table singer {
  singer_id serial [pk]
  api_id varchar(100) [unique, not null]
  singer_name varchar(100) [not null]
}

Table song_singer {
  song_id int [not null, ref: > song.song_id]
  singer_id int [not null, ref: > singer.singer_id]
  primary key (song_id, singer_id)
}

Table favorite_media {
  user_id int [not null, ref: > users.user_id]
  media_id int [not null, ref: > media.media_id]
  stars int [not null]
  added_at timestamp [not null]
  primary key (user_id, media_id)
}

Table favorite_songs {
  user_id int [not null, ref: > users.user_id]
  song_id int [not null, ref: > song.song_id]
  stars int [not null]
  added_at timestamp [not null]
  primary key (user_id, song_id)
}
