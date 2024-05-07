/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - ref
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ref` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `ref`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add assignworksup_table',7,'add_assignworksup_table'),
(26,'Can change assignworksup_table',7,'change_assignworksup_table'),
(27,'Can delete assignworksup_table',7,'delete_assignworksup_table'),
(28,'Can view assignworksup_table',7,'view_assignworksup_table'),
(29,'Can add dailydetails_table',8,'add_dailydetails_table'),
(30,'Can change dailydetails_table',8,'change_dailydetails_table'),
(31,'Can delete dailydetails_table',8,'delete_dailydetails_table'),
(32,'Can view dailydetails_table',8,'view_dailydetails_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add supervisor_table',10,'add_supervisor_table'),
(38,'Can change supervisor_table',10,'change_supervisor_table'),
(39,'Can delete supervisor_table',10,'delete_supervisor_table'),
(40,'Can view supervisor_table',10,'view_supervisor_table'),
(41,'Can add worker_table',11,'add_worker_table'),
(42,'Can change worker_table',11,'change_worker_table'),
(43,'Can delete worker_table',11,'delete_worker_table'),
(44,'Can view worker_table',11,'view_worker_table'),
(45,'Can add tosuprvsrcomplaint_table',12,'add_tosuprvsrcomplaint_table'),
(46,'Can change tosuprvsrcomplaint_table',12,'change_tosuprvsrcomplaint_table'),
(47,'Can delete tosuprvsrcomplaint_table',12,'delete_tosuprvsrcomplaint_table'),
(48,'Can view tosuprvsrcomplaint_table',12,'view_tosuprvsrcomplaint_table'),
(49,'Can add resources_table',13,'add_resources_table'),
(50,'Can change resources_table',13,'change_resources_table'),
(51,'Can delete resources_table',13,'delete_resources_table'),
(52,'Can view resources_table',13,'view_resources_table'),
(53,'Can add feedback_table',14,'add_feedback_table'),
(54,'Can change feedback_table',14,'change_feedback_table'),
(55,'Can delete feedback_table',14,'delete_feedback_table'),
(56,'Can view feedback_table',14,'view_feedback_table'),
(57,'Can add doubt_table',15,'add_doubt_table'),
(58,'Can change doubt_table',15,'change_doubt_table'),
(59,'Can delete doubt_table',15,'delete_doubt_table'),
(60,'Can view doubt_table',15,'view_doubt_table'),
(61,'Can add complaint_table',16,'add_complaint_table'),
(62,'Can change complaint_table',16,'change_complaint_table'),
(63,'Can delete complaint_table',16,'delete_complaint_table'),
(64,'Can view complaint_table',16,'view_complaint_table'),
(65,'Can add chat_table',17,'add_chat_table'),
(66,'Can change chat_table',17,'change_chat_table'),
(67,'Can delete chat_table',17,'delete_chat_table'),
(68,'Can view chat_table',17,'view_chat_table'),
(69,'Can add assignworkworker_table',18,'add_assignworkworker_table'),
(70,'Can change assignworkworker_table',18,'change_assignworkworker_table'),
(71,'Can delete assignworkworker_table',18,'delete_assignworkworker_table'),
(72,'Can view assignworkworker_table',18,'view_assignworkworker_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'ref_app','assignworksup_table'),
(18,'ref_app','assignworkworker_table'),
(17,'ref_app','chat_table'),
(16,'ref_app','complaint_table'),
(8,'ref_app','dailydetails_table'),
(15,'ref_app','doubt_table'),
(14,'ref_app','feedback_table'),
(9,'ref_app','login_table'),
(13,'ref_app','resources_table'),
(10,'ref_app','supervisor_table'),
(12,'ref_app','tosuprvsrcomplaint_table'),
(11,'ref_app','worker_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-03-22 10:17:45.848074'),
(2,'auth','0001_initial','2024-03-22 10:17:46.259321'),
(3,'admin','0001_initial','2024-03-22 10:17:46.352510'),
(4,'admin','0002_logentry_remove_auto_add','2024-03-22 10:17:46.352510'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-03-22 10:17:46.368696'),
(6,'contenttypes','0002_remove_content_type_name','2024-03-22 10:17:46.447391'),
(7,'auth','0002_alter_permission_name_max_length','2024-03-22 10:17:46.483778'),
(8,'auth','0003_alter_user_email_max_length','2024-03-22 10:17:46.510589'),
(9,'auth','0004_alter_user_username_opts','2024-03-22 10:17:46.513449'),
(10,'auth','0005_alter_user_last_login_null','2024-03-22 10:17:46.558669'),
(11,'auth','0006_require_contenttypes_0002','2024-03-22 10:17:46.558669'),
(12,'auth','0007_alter_validators_add_error_messages','2024-03-22 10:17:46.576648'),
(13,'auth','0008_alter_user_username_max_length','2024-03-22 10:17:46.621935'),
(14,'auth','0009_alter_user_last_name_max_length','2024-03-22 10:17:46.670028'),
(15,'auth','0010_alter_group_name_max_length','2024-03-22 10:17:46.685013'),
(16,'auth','0011_update_proxy_permissions','2024-03-22 10:17:46.701048'),
(17,'auth','0012_alter_user_first_name_max_length','2024-03-22 10:17:46.733058'),
(18,'ref_app','0001_initial','2024-03-22 10:17:47.476621'),
(19,'sessions','0001_initial','2024-03-22 10:17:47.508357'),
(20,'ref_app','0002_auto_20240407_1319','2024-04-07 07:50:06.982874');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('47u6tj7x1jxn9gn1cfkdztkgwx1cv4f5','eyJsaWQiOjJ9:1rpo3v:pAkBDmA3bct4NG7j0DiRGjnvbskGM6CoKZfGKGrkYtw','2024-04-11 11:36:51.914488'),
('aoms5slvn6e4jtzzq0ukseqta0ropzxe','eyJsaWQiOjIsIm5paGFsIjo0LCJlZCI6MSwiYXNzaW5pZCI6IjgiLCJjb21pZCI6MTJ9:1rvXmp:qawgVOp8r-HfzxnZsNu0FzrZuLr9PiFIDVxwYNZ8AE0','2024-04-27 07:26:55.557011'),
('cu3jtgeezlyu30kxdw92w4fwfqozfnoe','eyJsaWQiOjF9:1roeiZ:VqOWmuiLzvHKSdSUsNCfB5kDfs1EJplR1yCZCqoNzEE','2024-04-08 07:26:03.272693'),
('dyji8689w44qdk82bcpaz1s4tu9881af','eyJsaWQiOjF9:1rrVob:iOjVDVXCPCmNlhQTSpwxBFAozbxomsLZ1LA2w8wfBXE','2024-04-16 04:32:05.580005'),
('ebfo1sx32f2sj5m557qwhhqx1a72330r','eyJsaWQiOjIsImFzc2luaWQiOiI3IiwibmloYWwiOjQsImNvbWlkIjoxMCwic2NpZCI6IjMifQ:1rpnnf:tXNAsZ51MJb-hBrfuC5gbnb57Sn40YGS-5qwno1KJrg','2024-04-11 11:20:03.220993'),
('mq0wt31alq5s52wc7mo8k4971nwt18ci','.eJyrVsrJTFGyMtFRygfRRjpKqUDKUEcpOT8XKpBYXJyZB2IrmSrpKBUng5mGQGZeZkZiDlBJLQCgYRNA:1roMfC:CBTmmOocuRG2llMZqglrtTgacEU9eFYRErfCPAmjMu8','2024-04-07 12:09:22.173285'),
('naulhdvkkukbdv445wkcp6tk7r0a82nd','eyJsaWQiOjJ9:1rvbiD:_l5dj8_AWvDT6cutAgcg_SvvdpcGMeuuEvFapgU8jlE','2024-04-27 11:38:25.117868'),
('pjl4zreopxc5fdbxomh7tt31phm3x2lx','eyJsaWQiOjJ9:1rpnte:ivCD1SLLFWEo6W07GBjwR58UwHPLLL9gPLj2Q2vU6-I','2024-04-11 11:26:14.060916'),
('x13d5z5c9gn7rvwy7eqp5pfdvgnkj94a','eyJsaWQiOjIsImFzc2luaWQiOiI0IiwibmloYWwiOjQsImNvbWlkIjo2LCJzY2lkIjoiMiJ9:1rpKwt:OBGlzMk0dyDgX4UPrSQlAp6thz-RqetS5OP4Utk2vFY','2024-04-10 04:31:39.096161');

/*Table structure for table `ref_app_assignworksup_table` */

DROP TABLE IF EXISTS `ref_app_assignworksup_table`;

CREATE TABLE `ref_app_assignworksup_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `work` varchar(300) NOT NULL,
  `details` varchar(200) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `RESOURCE_id` bigint NOT NULL,
  `SUPERVISOR_id` bigint NOT NULL,
  `updated_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_assignworksu_RESOURCE_id_719bc341_fk_ref_app_r` (`RESOURCE_id`),
  KEY `ref_app_assignworksu_SUPERVISOR_id_666dcce4_fk_ref_app_s` (`SUPERVISOR_id`),
  CONSTRAINT `ref_app_assignworksu_RESOURCE_id_719bc341_fk_ref_app_r` FOREIGN KEY (`RESOURCE_id`) REFERENCES `ref_app_resources_table` (`id`),
  CONSTRAINT `ref_app_assignworksu_SUPERVISOR_id_666dcce4_fk_ref_app_s` FOREIGN KEY (`SUPERVISOR_id`) REFERENCES `ref_app_supervisor_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_assignworksup_table` */

insert  into `ref_app_assignworksup_table`(`id`,`work`,`details`,`status`,`date`,`RESOURCE_id`,`SUPERVISOR_id`,`updated_date`) values 
(8,'It have a scratch on its right side of corner, manage it.','Should done before March 15','Pending','2024-04-07',1,1,'2024-04-07');

/*Table structure for table `ref_app_assignworkworker_table` */

DROP TABLE IF EXISTS `ref_app_assignworkworker_table`;

CREATE TABLE `ref_app_assignworkworker_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `work` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `ASSIGNWORK_id` bigint NOT NULL,
  `WORKER_id` bigint NOT NULL,
  `updated_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_assignworkwo_ASSIGNWORK_id_56405fee_fk_ref_app_a` (`ASSIGNWORK_id`),
  KEY `ref_app_assignworkwo_WORKER_id_3b3f8830_fk_ref_app_w` (`WORKER_id`),
  CONSTRAINT `ref_app_assignworkwo_ASSIGNWORK_id_56405fee_fk_ref_app_a` FOREIGN KEY (`ASSIGNWORK_id`) REFERENCES `ref_app_assignworksup_table` (`id`),
  CONSTRAINT `ref_app_assignworkwo_WORKER_id_3b3f8830_fk_ref_app_w` FOREIGN KEY (`WORKER_id`) REFERENCES `ref_app_worker_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_assignworkworker_table` */

/*Table structure for table `ref_app_chat_table` */

DROP TABLE IF EXISTS `ref_app_chat_table`;

CREATE TABLE `ref_app_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `fromid_id` bigint NOT NULL,
  `toid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_chat_table_fromid_id_6784a633_fk_ref_app_login_table_id` (`fromid_id`),
  KEY `ref_app_chat_table_toid_id_aea06e4f_fk_ref_app_login_table_id` (`toid_id`),
  CONSTRAINT `ref_app_chat_table_fromid_id_6784a633_fk_ref_app_login_table_id` FOREIGN KEY (`fromid_id`) REFERENCES `ref_app_login_table` (`id`),
  CONSTRAINT `ref_app_chat_table_toid_id_aea06e4f_fk_ref_app_login_table_id` FOREIGN KEY (`toid_id`) REFERENCES `ref_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_chat_table` */

insert  into `ref_app_chat_table`(`id`,`message`,`date`,`fromid_id`,`toid_id`) values 
(28,'hi','2024-03-24',3,2),
(29,'hloo','2024-03-24',4,3),
(30,'hlo','2024-03-24',3,4),
(31,'hiiiiiiiiiiiiiiiiiiiiiiiiii','2024-03-24',4,3),
(38,'yeah','2024-03-26',2,3),
(41,'How is everything going on','2024-03-26',2,3),
(42,'Everything is going perfectly as planned, will notice if anything is wrong','2024-03-26',3,2),
(43,'What about all the resources that you have added, is they all working good','2024-03-26',2,3),
(44,'Everything is working, no issues had found, will notice you if any ','2024-03-26',3,2),
(45,'Great','2024-03-26',2,3),
(46,'Hi Supervisor','2024-03-26',5,2),
(47,'Yes','2024-03-26',2,5),
(51,'hi','2024-03-26',2,5),
(52,'Good','2024-03-26',2,3),
(53,'Hi supervisor','2024-03-27',3,2),
(54,'Yess','2024-03-27',2,3),
(55,'hi supervisor','2024-03-28',1,2),
(56,'pls reply','2024-03-28',1,2),
(57,'hii','2024-03-28',2,1),
(58,'Hello','2024-03-28',2,1),
(59,'hii','2024-03-29',3,2),
(60,'hi','2024-04-02',3,2),
(61,'hello','2024-04-02',3,2),
(62,'mmms','2024-04-02',2,3);

/*Table structure for table `ref_app_complaint_table` */

DROP TABLE IF EXISTS `ref_app_complaint_table`;

CREATE TABLE `ref_app_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_complaint_ta_LOGIN_id_507b2536_fk_ref_app_l` (`LOGIN_id`),
  CONSTRAINT `ref_app_complaint_ta_LOGIN_id_507b2536_fk_ref_app_l` FOREIGN KEY (`LOGIN_id`) REFERENCES `ref_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_complaint_table` */

insert  into `ref_app_complaint_table`(`id`,`complaint`,`reply`,`date`,`LOGIN_id`) values 
(1,'Cilmmbb','OK','2024-03-22',3),
(3,'qwert','ok','2024-03-25',2),
(5,'fdsasdr','esdrfghjnmkl','2024-03-26',2),
(6,'Pkskaakakman','dfgvhbjnm','2024-03-26',3),
(7,'Wqqw','ok','2024-03-27',3),
(8,'vvvv','ok','2024-03-27',2),
(9,'qwertyui','Entha mole','2024-03-28',6),
(10,'ftkktkktkt','okk','2024-03-28',3),
(11,'fgfdfg','OK','2024-04-02',2),
(12,'hahah','ok','2024-04-02',3);

/*Table structure for table `ref_app_dailydetails_table` */

DROP TABLE IF EXISTS `ref_app_dailydetails_table`;

CREATE TABLE `ref_app_dailydetails_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `unit` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_dailydetails_table` */

/*Table structure for table `ref_app_doubt_table` */

DROP TABLE IF EXISTS `ref_app_doubt_table`;

CREATE TABLE `ref_app_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `WORKER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_doubt_table_WORKER_id_dc624275_fk_ref_app_w` (`WORKER_id`),
  CONSTRAINT `ref_app_doubt_table_WORKER_id_dc624275_fk_ref_app_w` FOREIGN KEY (`WORKER_id`) REFERENCES `ref_app_worker_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_doubt_table` */

/*Table structure for table `ref_app_feedback_table` */

DROP TABLE IF EXISTS `ref_app_feedback_table`;

CREATE TABLE `ref_app_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `RESOURCE_id` bigint NOT NULL,
  `WORKER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_feedback_tab_RESOURCE_id_05c43386_fk_ref_app_r` (`RESOURCE_id`),
  KEY `ref_app_feedback_tab_WORKER_id_fd82e77d_fk_ref_app_w` (`WORKER_id`),
  CONSTRAINT `ref_app_feedback_tab_RESOURCE_id_05c43386_fk_ref_app_r` FOREIGN KEY (`RESOURCE_id`) REFERENCES `ref_app_resources_table` (`id`),
  CONSTRAINT `ref_app_feedback_tab_WORKER_id_fd82e77d_fk_ref_app_w` FOREIGN KEY (`WORKER_id`) REFERENCES `ref_app_worker_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_feedback_table` */

insert  into `ref_app_feedback_table`(`id`,`feedback`,`date`,`RESOURCE_id`,`WORKER_id`) values 
(1,'afghgf','2024-03-22',2,1),
(2,'Qiqiiwieieiejwjej','2024-03-26',5,1),
(3,'ddddddd','2024-03-28',1,1),
(4,'qwer','2024-04-02',6,1);

/*Table structure for table `ref_app_login_table` */

DROP TABLE IF EXISTS `ref_app_login_table`;

CREATE TABLE `ref_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_login_table` */

insert  into `ref_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'Hari','Hari12345','supervisor'),
(3,'Nihal','Nihal123','Worker'),
(4,'Nihal123','Nihal1234','supervisor'),
(5,'Mishab','Mishab123','Worker'),
(6,'Niya','Niya123','Worker'),
(8,'Aleefa123','Aleefa1234','Rejected');

/*Table structure for table `ref_app_resources_table` */

DROP TABLE IF EXISTS `ref_app_resources_table`;

CREATE TABLE `ref_app_resources_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `product_type` varchar(100) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `manufacturer` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `model_number` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `SUPERVISOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_resources_ta_SUPERVISOR_id_9a0a1624_fk_ref_app_s` (`SUPERVISOR_id`),
  CONSTRAINT `ref_app_resources_ta_SUPERVISOR_id_9a0a1624_fk_ref_app_s` FOREIGN KEY (`SUPERVISOR_id`) REFERENCES `ref_app_supervisor_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_resources_table` */

insert  into `ref_app_resources_table`(`id`,`date`,`product_type`,`product_name`,`manufacturer`,`details`,`model_number`,`photo`,`SUPERVISOR_id`) values 
(1,'2024-03-22','Wind Mill','SP1','Jang gua Prt Limitd','Wind mill','CX12233','1461880_hLZBkYQ.jpg',1),
(2,'2024-03-22','Solar Panel','SP123','Jang gua Prt Limited',' Solar panel','DE2665543','wp4041931-solar-panel-wallpapers_CNAJKKF.jpg',1),
(4,'2024-03-23','Wind Mill','SP123','Jang gua Prt Limited',' Solar panel','CX122334','2907768_fgFgLOR.jpg',2),
(5,'2024-03-24','Solar Panel','SP123','Jang gua Prt Limited',' Solar panel','dfghjkl','wp4041864-solar-panel-wallpapers_2fnP9bG.jpg',2),
(6,'2024-03-28','Wind Mill','SP123','Jang gua Prt Limited',' Solar panel','dfghjkl','wp6988976.jpg',1);

/*Table structure for table `ref_app_supervisor_table` */

DROP TABLE IF EXISTS `ref_app_supervisor_table`;

CREATE TABLE `ref_app_supervisor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `joindate` date NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `proof` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_supervisor_t_LOGIN_id_f537dd8b_fk_ref_app_l` (`LOGIN_id`),
  CONSTRAINT `ref_app_supervisor_t_LOGIN_id_f537dd8b_fk_ref_app_l` FOREIGN KEY (`LOGIN_id`) REFERENCES `ref_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_supervisor_table` */

insert  into `ref_app_supervisor_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`email`,`qualification`,`dob`,`joindate`,`pin`,`phone`,`photo`,`proof`,`LOGIN_id`) values 
(1,'Hari','Krishnan','Male','Mannarkaad','Unnikulam','nihalbacrak@gmail.com','Ma electronics','2004-12-24','2024-03-22',673574,8606585275,'icon-256x256_T5B8dzI.png','aadhaar-card_0y2qEqi.webp',2),
(2,'Nihal','Backer','Male','Poonoor','Unnikulam','nihalbackerak@gmail.com','Ma electronics','2004-12-01','2024-03-23',673574,8606585275,'icon-256x256_q8DqCzN.png','aadhaar-card_ydBNUZd.webp',4);

/*Table structure for table `ref_app_tosuprvsrcomplaint_table` */

DROP TABLE IF EXISTS `ref_app_tosuprvsrcomplaint_table`;

CREATE TABLE `ref_app_tosuprvsrcomplaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `SUPERVISOR_id` bigint NOT NULL,
  `WORKEER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_tosuprvsrcom_SUPERVISOR_id_4890c3c8_fk_ref_app_s` (`SUPERVISOR_id`),
  KEY `ref_app_tosuprvsrcom_WORKEER_id_d36a29d1_fk_ref_app_w` (`WORKEER_id`),
  CONSTRAINT `ref_app_tosuprvsrcom_SUPERVISOR_id_4890c3c8_fk_ref_app_s` FOREIGN KEY (`SUPERVISOR_id`) REFERENCES `ref_app_supervisor_table` (`id`),
  CONSTRAINT `ref_app_tosuprvsrcom_WORKEER_id_d36a29d1_fk_ref_app_w` FOREIGN KEY (`WORKEER_id`) REFERENCES `ref_app_worker_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_tosuprvsrcomplaint_table` */

insert  into `ref_app_tosuprvsrcomplaint_table`(`id`,`complaint`,`reply`,`date`,`SUPERVISOR_id`,`WORKEER_id`) values 
(1,'asafsgshsh','ok','2024-03-24',1,1),
(2,'nsnananakaj','dxfgvbhm','2024-03-26',1,1),
(3,'yddhhjdrh','fccgbjm,','2024-03-28',1,1);

/*Table structure for table `ref_app_worker_table` */

DROP TABLE IF EXISTS `ref_app_worker_table`;

CREATE TABLE `ref_app_worker_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ref_app_worker_table_LOGIN_id_9ddbdeed_fk_ref_app_login_table_id` (`LOGIN_id`),
  CONSTRAINT `ref_app_worker_table_LOGIN_id_9ddbdeed_fk_ref_app_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `ref_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `ref_app_worker_table` */

insert  into `ref_app_worker_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`email`,`dob`,`pin`,`phone`,`photo`,`LOGIN_id`) values 
(1,'Nihal','Backer','Male','Poonoor','Poonoor','nihalbackerak@gmail.com ','2001-01-24',673574,8606585275,'IMG-20240308-WA0039.jpg',3),
(2,'Mishab','Ochath','Male','Balussery ','Balussery ','mishabo380@gmail.com ','2001-03-12',673574,8686582275,'IMG-20240212-WA0011.jpg',5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
