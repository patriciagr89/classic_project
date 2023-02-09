CREATE TABLE "coins" (
	"idCoin"	INTEGER NOT NULL UNIQUE,
	"coinName"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("idCoin" AUTOINCREMENT)
);

INSERT INTO coins(idCoin,coinName) values(1,"BTC");
INSERT INTO coins(idCoin,coinName) values(2,"ETH");
INSERT INTO coins(idCoin,coinName) values(3,"BNB");
INSERT INTO coins(idCoin,coinName) values(4,"ADA");
INSERT INTO coins(idCoin,coinName) values(5,"DOT");
INSERT INTO coins(idCoin,coinName) values(6,"USDT");
INSERT INTO coins(idCoin,coinName) values(7,"XRP");
INSERT INTO coins(idCoin,coinName) values(8,"SOL");
INSERT INTO coins(idCoin,coinName) values(9,"MATIC");
INSERT INTO coins(idCoin,coinName) values(10,"EUR");
