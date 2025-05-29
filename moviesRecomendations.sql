CREATE TYPE "countrys" AS ENUM (
  'USA',
  'MEX',
  'ESP',
  'CAN',
  'FRA',
  'GER',
  'ITA',
  'BRA',
  'ARG',
  'CHN',
  'JPN',
  'IND',
  'RUS',
  'AUS',
  'GBR'
);

CREATE TYPE "media_types" AS ENUM (
  'Movie',
  'Series',
  'Documentary',
  'ShortFilm',
  'MusicVideo',
  'Animation',
  'Commercial',
  'Trailer',
  'LivePerformance'
);

CREATE TYPE "media_genres" AS ENUM (
  'Action',
  'Adventure',
  'Animation',
  'Biography',
  'Comedy',
  'Crime',
  'Documentary',
  'Drama',
  'Family',
  'Fantasy',
  'Historical',
  'Horror',
  'Musical',
  'Mystery',
  'Romance',
  'SciFi',
  'Sport',
  'Thriller',
  'War',
  'Western'
);

CREATE TYPE "music_genres" AS ENUM (
  'Pop',
  'Rock',
  'HipHop',
  'Rap',
  'Jazz',
  'Classical',
  'Electronic',
  'Country',
  'Reggae',
  'Blues',
  'Metal',
  'RnB',
  'Latin',
  'Folk',
  'Indie',
  'Soul',
  'Punk'
);

CREATE TYPE "age_restrictions" AS ENUM (
  'G',
  'PG',
  'PG13',
  'R',
  'NC17',
  'UNRATED'
);

CREATE TYPE "music_ratings" AS ENUM (
  'None',
  'Explicit',
  'Clean',
  'ParentalAdvisory',
  'Instrumental'
);

CREATE TABLE "users" (
  "user_id" INTEGER PRIMARY KEY NOT NULL,
  "first_name" VARCHAR(50) NOT NULL,
  "last_name" VARCHAR(50) NOT NULL,
  "date_of_birth" date NOT NULL,
  "city_of_birth" VARCHAR(50) NOT NULL,
  "city_of_residence" VARCHAR(50) NOT NULL,
  "username" VARCHAR(50) UNIQUE NOT NULL,
  "email" VARCHAR(100) UNIQUE NOT NULL,
  "country" countrys NOT NULL,
  "active" BOOL NOT NULL,
  "created_at" TIMESTAMP NOT NULL
);

CREATE TABLE "media" (
  "media_id" INTEGER PRIMARY KEY NOT NULL,
  "title" VARCHAR(100) NOT NULL,
  "genre" media_genres NOT NULL,
  "audiovisual_type" media_types NOT NULL,
  "age_restriction" age_restrictions NOT NULL,
  "created_at" DATE NOT NULL,
  "created_in" countrys NOT NULL
);

CREATE TABLE "song" (
  "song_id" INTEGER PRIMARY KEY NOT NULL,
  "title" VARCHAR(100) NOT NULL,
  "song_genre" music_genres NOT NULL,
  "song_rating" music_ratings NOT NULL,
  "created_at" DATE NOT NULL,
  "created_in" countrys NOT NULL
);

CREATE TABLE "favorite_media" (
  "user_id" INTEGER NOT NULL,
  "media_id" INTEGER NOT NULL,
  "stars" DECIMAL(2,1) NOT NULL,
  "added_at" TIMESTAMP NOT NULL,
  PRIMARY KEY ("user_id", "media_id")
);

CREATE TABLE "favorite_songs" (
  "user_id" INTEGER NOT NULL,
  "song_id" INTEGER NOT NULL,
  "stars" DECIMAL(2,1) NOT NULL,
  "added_at" TIMESTAMP NOT NULL,
  PRIMARY KEY ("user_id", "song_id")
);

ALTER TABLE "favorite_media" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "favorite_media" ADD FOREIGN KEY ("media_id") REFERENCES "media" ("media_id");

ALTER TABLE "favorite_songs" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "favorite_songs" ADD FOREIGN KEY ("song_id") REFERENCES "song" ("song_id");
