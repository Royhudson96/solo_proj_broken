BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Solo_Project_App_portfolio" (
	"id"	integer NOT NULL,
	"title"	varchar(55) NOT NULL,
	"price"	decimal NOT NULL,
	"portfolio_image"	varchar(100),
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"content_creator_id"	integer NOT NULL,
	FOREIGN KEY("content_creator_id") REFERENCES "Solo_Project_App_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Solo_Project_App_media" (
	"id"	integer NOT NULL,
	"facebook"	text NOT NULL,
	"linkedin"	text NOT NULL,
	"instagram"	text NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"user_media_id"	integer NOT NULL,
	"twitter"	text NOT NULL,
	FOREIGN KEY("user_media_id") REFERENCES "Solo_Project_App_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Solo_Project_App_portfolio_portfolio_item" (
	"id"	integer NOT NULL,
	"portfolio_id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	FOREIGN KEY("portfolio_id") REFERENCES "Solo_Project_App_portfolio"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "Solo_Project_App_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Solo_Project_App_user" (
	"id"	integer NOT NULL,
	"first_name"	text NOT NULL,
	"last_name"	text NOT NULL,
	"city"	text NOT NULL,
	"state"	varchar(2) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"password"	text NOT NULL,
	"created_at"	datetime NOT NULL,
	"updated_at"	datetime NOT NULL,
	"profile_pic"	varchar(100),
	"bio"	text NOT NULL,
	"website"	text,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Solo_Project_App_portfolio" VALUES (5,'Happy Roy',0,'images/IMG_E06792_lDccve7.JPG','2021-04-18 03:32:37.211065','2021-04-18 03:32:37.211065',9);
INSERT INTO "Solo_Project_App_portfolio" VALUES (6,'Making It Through',29,'images/IMG_E05781_h2nxObr.JPG','2021-04-18 03:37:11.968379','2021-04-18 03:37:11.969377',9);
INSERT INTO "Solo_Project_App_portfolio" VALUES (7,'Staring in Space',200,'images/IMG_E06781_s8nxp4H.JPG','2021-04-18 05:16:20.847470','2021-04-18 05:16:20.847470',9);
INSERT INTO "Solo_Project_App_portfolio" VALUES (8,'Message of the Cross',25,'images/IMG_00921.JPG','2021-04-19 04:13:13.563092','2021-04-19 04:13:13.563092',10);
INSERT INTO "Solo_Project_App_portfolio" VALUES (9,'Beloved of HIM',45,'images/BYNN00761.JPG','2021-04-19 04:29:17.405560','2021-04-19 04:29:17.405560',10);
INSERT INTO "Solo_Project_App_portfolio" VALUES (10,'Little Cutie',5,'images/IMG_02321.JPG','2021-04-19 04:31:04.209805','2021-04-19 04:31:04.209805',10);
INSERT INTO "Solo_Project_App_portfolio" VALUES (11,'Man of God',15,'images/YDPO83861_KbH4ScK.JPG','2021-04-19 07:08:45.328448','2021-04-19 07:08:45.328448',9);
INSERT INTO "Solo_Project_App_portfolio" VALUES (12,'Beloved of HIM',35,'images/Rosie_B_arHS87g.jpg','2021-04-20 07:39:11.615946','2021-04-20 07:39:11.616942',12);
INSERT INTO "Solo_Project_App_user" VALUES (9,'Roy','Hudson','Oakland','CA','rlhudson@ucdavis.edu','$2b$12$E.htI5c2TSAwOrSLhgcnyeyYx6PlmvXsJH2aajfl8oyRvCqGX15kG','2021-04-18 03:11:20.028363','2021-04-19 07:08:07.062803','images/IMG_E06791_9N1kX4r.JPG','Please update your bio!','N/A');
INSERT INTO "Solo_Project_App_user" VALUES (10,'Evangeline','Hsiao','Los Angeles','CA','Evangeline@gmail.com','$2b$12$V6.cUAKHR8i/6wTC5X9y5ep/bQCtpA//mYLBOzEI/j6FKfgmM38s6','2021-04-18 04:14:45.681868','2021-04-21 04:59:58.273232','images/IMG_E06191.JPG','Hello! My name is Evangeline Hsiao and I am a daughter of the Most High! Currently working in a supervisory position as a UX/UI designer and am absolutely in love with my position! I love Roy dearly! He is such a wonderful and kind man of God! He''s handsome too! Feel free to view some of my portfolio items and send me an email if you have any questions about them!','N/A');
INSERT INTO "Solo_Project_App_user" VALUES (11,'Juanita','Valdes','Santa Clara','CA','juanita@gmail.com','$2b$12$eIKzR4CYX/euSbSi/h/qVONBF6FWYiK5lhjvjHKYAn9MbMT69Ebxi','2021-04-19 07:00:39.827292','2021-04-19 07:00:39.827292','images/IMG_E06831.JPG','Please update your bio!','N/A');
INSERT INTO "Solo_Project_App_user" VALUES (12,'Rosie','Bustamante','Los Angeles','CA','Rosie@gmail.com','$2b$12$v0eVaShtm0gAptqrCZiJe.KYoB7LEAe7IgZzjVy3gbM3LJDQ2kcvq','2021-04-19 07:06:46.252827','2021-04-19 07:06:46.252827','images/Rosie_B.jpg','Please update your bio!','N/A');
INSERT INTO "Solo_Project_App_user" VALUES (13,'Juliya','Mapp','San Leandro','CA','juliya@gmail.com','$2b$12$GJHzu8BjCvkPasy.I/UPZeRshFtLmanq0flHE2Tsr4Dc.AJuEZOmi','2021-04-19 07:12:29.470836','2021-04-19 07:12:29.470836','images/IMG_01171.JPG','Please update your bio!','N/A');
CREATE INDEX IF NOT EXISTS "Solo_Project_App_portfolio_content_creator_id_549e97f6" ON "Solo_Project_App_portfolio" (
	"content_creator_id"
);
CREATE INDEX IF NOT EXISTS "Solo_Project_App_media_user_media_id_23d935aa" ON "Solo_Project_App_media" (
	"user_media_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "Solo_Project_App_portfolio_portfolio_item_portfolio_id_user_id_d87b6183_uniq" ON "Solo_Project_App_portfolio_portfolio_item" (
	"portfolio_id",
	"user_id"
);
CREATE INDEX IF NOT EXISTS "Solo_Project_App_portfolio_portfolio_item_portfolio_id_9a50dd51" ON "Solo_Project_App_portfolio_portfolio_item" (
	"portfolio_id"
);
CREATE INDEX IF NOT EXISTS "Solo_Project_App_portfolio_portfolio_item_user_id_26c212d1" ON "Solo_Project_App_portfolio_portfolio_item" (
	"user_id"
);
COMMIT;
