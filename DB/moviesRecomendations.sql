DROP TABLE IF EXISTS favorite_songs;
DROP TABLE IF EXISTS favorite_media;
DROP TABLE IF EXISTS codemail;
DROP TABLE IF EXISTS singer;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS song_singer;
DROP TABLE IF EXISTS media_actor;
DROP TABLE IF EXISTS actor;
DROP TABLE IF EXISTS media;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  user_id SERIAL PRIMARY KEY NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE NOT NULL,
  city_of_birth VARCHAR(50) NOT NULL,
  city_of_residence VARCHAR(50) NOT NULL,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  country VARCHAR(50) NOT NULL,
  active BOOLEAN NOT NULL,
  created_at DATE NOT NULL
);

CREATE TABLE codemail (
    id SERIAL PRIMARY KEY NOT NULL,
    code VARCHAR(12),
    date TIMESTAMP NOT NULL,
    email VARCHAR(100) NOT NULL, 
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE media (
  media_id SERIAL PRIMARY KEY NOT NULL,
  title VARCHAR(100) NOT NULL,
  genre VARCHAR(50) NOT NULL,
  audiovisual_type VARCHAR(50) NOT NULL,
  age_restriction VARCHAR(50) NOT NULL,
  actor_ids VARCHAR[],
  created_at DATE NOT NULL,
  created_country VARCHAR(50) NOT NULL
);

CREATE TABLE actor (
  actor_id SERIAL PRIMARY KEY,
  api_id VARCHAR(100) UNIQUE NOT NULL,
  actor_name VARCHAR(100) NOT NULL
);

CREATE TABLE media_actor (
  media_id INTEGER NOT NULL,
  actor_id INTEGER NOT NULL,
  PRIMARY KEY (media_id, actor_id)
);

CREATE TABLE song (
  song_id SERIAL PRIMARY KEY NOT NULL,
  title VARCHAR(100) NOT NULL,
  song_genre VARCHAR(50) NOT NULL,
  song_rating VARCHAR(50) NOT NULL,
  artist_ids VARCHAR[],
  created_at DATE NOT NULL,
  created_country VARCHAR(50) NOT NULL
);

CREATE TABLE singer (
  singer_id SERIAL PRIMARY KEY,
  api_id VARCHAR(100) UNIQUE NOT NULL,
  singer_name VARCHAR(100) NOT NULL
);

CREATE TABLE song_singer (
  song_id INTEGER NOT NULL,
  singer_id INTEGER NOT NULL,
  PRIMARY KEY (song_id, singer_id)
);

CREATE TABLE favorite_media (
  user_id INTEGER NOT NULL,
  media_id INTEGER NOT NULL,
  stars INTEGER NOT NULL,
  added_at TIMESTAMP NOT NULL,
  PRIMARY KEY (user_id, media_id)
);

CREATE TABLE favorite_songs (
  user_id INTEGER NOT NULL,
  song_id INTEGER NOT NULL,
  stars INTEGER NOT NULL,
  added_at TIMESTAMP NOT NULL,
  PRIMARY KEY (user_id, song_id)
);

select COUNT(*) from pg_catalog.pg_tables where schemaname = 'public';

INSERT INTO users (first_name, last_name, date_of_birth, city_of_birth, city_of_residence, username, email, country, active, created_at)
VALUES ('Juan', 'Nipaz', '2007-10-23', 'Cali', 'Jamundi', 'JJNipaz', 'jjnipaz@gmai.com', 'Colombia', True, NOW());


select * from users;