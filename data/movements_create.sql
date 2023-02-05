CREATE TABLE "movements" (
	"id"	INTEGER NOT NULL UNIQUE,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"coins_from"	TEXT NOT NULL,
	"quantity_from"	REAL NOT NULL,
	"coins_to"	TEXT NOT NULL,
	"quantity_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);