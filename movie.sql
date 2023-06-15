CREATE TABLE "actors" (
  "IMDb" text NOT NULL,
  "actor_name" text NOT NULL,
  PRIMARY KEY ("IMDb", "actor_name"),
  CONSTRAINT "fk_actors_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

CREATE TABLE "Administrator" (
  "username" text NOT NULL,
  "password" text NOT NULL,
  PRIMARY KEY ("username")
);

CREATE TABLE "basic" (
  "IMDb" text NOT NULL,
  "cname" text NOT NULL,
  "fname" text,
  "pic_link" text NOT NULL,
  "director" text NOT NULL,
  "location" text NOT NULL,
  "language" text NOT NULL,
  "uptime" text NOT NULL,
  "score" real NOT NULL,
  "rated" integer NOT NULL,
  "instruction" text NOT NULL,
  PRIMARY KEY ("IMDb")
);
CREATE TRIGGER "insert_log"
AFTER INSERT
ON "basic"
BEGIN
  INSERT INTO insertlog(IMDb, opt_time) VALUES (new.IMDb, datetime('now'));
END;

CREATE TABLE "comments" (
  "IMDb" text NOT NULL,
  "nickname" text NOT NULL,
  "content" text NOT NULL,
  PRIMARY KEY ("IMDb", "nickname", "content"),
  CONSTRAINT "fk_comments_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

CREATE TABLE "insertlog" (
  "IMDb" text NOT NULL,
  "opt_time" text NOT NULL,
  PRIMARY KEY ("opt_time", "IMDb"),
  CONSTRAINT "fk_insertlog_basic_1" FOREIGN KEY ("IMDb") REFERENCES "basic" ("IMDb") ON DELETE CASCADE
);

