TABLE users {
  user_id INTEGER [PK, NOT NULL]
  first_name VARCHAR(50) [NOT NULL]
  last_name VARCHAR(50) [NOT NULL]
  date_of_birth date [NOT NULL]
  city_of_birth VARCHAR(50) [NOT NULL]
  city_of_residence VARCHAR(50) [NOT NULL]
  username VARCHAR(50) [UNIQUE, NOT NULL]
  email VARCHAR(100) [UNIQUE, NOT NULL]
  country VARCHAR(50) [NOT NULL]
  active BOOL [NOT NULL]
  created_at TIMESTAMP [NOT NULL]
}

TABLE media {
  media_id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  genre media_genres [NOT NULL]
  audiovisual_type media_types [NOT NULL]
  age_restriction age_restrictions [NOT NULL]
  created_at DATE [NOT NULL]
  created_in countrys [NOT NULL]
}

TABLE song {
  song_id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  song_genre music_genres [NOT NULL]
  song_rating music_ratings [NOT NULL]
  created_at DATE [NOT NULL]
  created_in countrys [NOT NULL]
}

TABLE favorite_media {
  user_id INTEGER [NOT NULL, REF: > users.user_id]
  media_id INTEGER [NOT NULL, REF: > media.media_id]
  stars INT [NOT NULL]
  added_at TIMESTAMP [NOT NULL]
  indexes {
    (user_id, media_id) [PK]
  }
}

TABLE favorite_songs {
  user_id INTEGER [NOT NULL, REF: > users.user_id]
  song_id INTEGER [NOT NULL, REF: > song.song_id]
  stars INT [NOT NULL]
  added_at TIMESTAMP [NOT NULL]
  indexes {
    (user_id, song_id) [PK]
  }
}