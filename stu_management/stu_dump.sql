-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: stu_management
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add administrator',7,'add_administrator'),(26,'Can change administrator',7,'change_administrator'),(27,'Can delete administrator',7,'delete_administrator'),(28,'Can view administrator',7,'view_administrator'),(29,'Can add class',8,'add_class'),(30,'Can change class',8,'change_class'),(31,'Can delete class',8,'delete_class'),(32,'Can view class',8,'view_class'),(33,'Can add suggestions',9,'add_suggestions'),(34,'Can change suggestions',9,'change_suggestions'),(35,'Can delete suggestions',9,'delete_suggestions'),(36,'Can view suggestions',9,'view_suggestions'),(37,'Can add student',10,'add_student'),(38,'Can change student',10,'change_student'),(39,'Can delete student',10,'delete_student'),(40,'Can view student',10,'view_student'),(41,'Can add stu_msg',11,'add_stu_msg'),(42,'Can change stu_msg',11,'change_stu_msg'),(43,'Can delete stu_msg',11,'delete_stu_msg'),(44,'Can view stu_msg',11,'view_stu_msg'),(45,'Can add school_expression',12,'add_school_expression'),(46,'Can change school_expression',12,'change_school_expression'),(47,'Can delete school_expression',12,'delete_school_expression'),(48,'Can view school_expression',12,'view_school_expression'),(49,'Can add points',13,'add_points'),(50,'Can change points',13,'change_points'),(51,'Can delete points',13,'delete_points'),(52,'Can view points',13,'view_points'),(53,'Can add leave_school',14,'add_leave_school'),(54,'Can change leave_school',14,'change_leave_school'),(55,'Can delete leave_school',14,'delete_leave_school'),(56,'Can view leave_school',14,'view_leave_school'),(57,'Can add change_class',15,'add_change_class'),(58,'Can change change_class',15,'change_change_class'),(59,'Can delete change_class',15,'delete_change_class'),(60,'Can view change_class',15,'view_change_class');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$E0SWcUCSdixM$umt7WNI6TuJvuelI5bpMxjrx0KJlkVzLl5KAj/XBJls=','2020-04-09 04:49:08.047426',1,'roy','','','anroy@qq.com',1,1,'2020-04-09 04:48:45.909285');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-09 04:50:53.059260','1','Class object (1)',1,'[{\"added\": {}}]',8,1),(2,'2020-04-09 04:50:56.912880','1','Student object (1)',1,'[{\"added\": {}}]',10,1),(3,'2020-04-09 04:52:51.263208','1','Student object (1)',2,'[{\"changed\": {\"fields\": [\"Stu num\"]}}]',10,1),(4,'2020-04-09 05:52:28.678770','1','Administrator object (1)',1,'[{\"added\": {}}]',7,1),(5,'2020-04-10 01:23:24.430347','1','School_expression object (1)',1,'[{\"added\": {}}]',12,1),(6,'2020-04-10 01:33:29.016068','1','Stu_msg object (1)',1,'[{\"added\": {}}]',11,1),(7,'2020-04-10 08:40:14.208266','2','Administrator object (2)',1,'[{\"added\": {}}]',7,1),(8,'2020-04-13 06:26:31.204756','3','Administrator object (3)',1,'[{\"added\": {}}]',7,1),(9,'2020-04-14 00:32:54.365484','2','Class object (2)',1,'[{\"added\": {}}]',8,1),(10,'2020-04-14 02:59:25.210411','4','Administrator object (4)',1,'[{\"added\": {}}]',7,1),(11,'2020-04-14 06:13:58.007050','3','Class object (3)',1,'[{\"added\": {}}]',8,1),(12,'2020-04-14 06:24:38.794637','3','Class object (3)',2,'[{\"changed\": {\"fields\": [\"teacher_name\"]}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'stu_app','administrator'),(15,'stu_app','change_class'),(8,'stu_app','class'),(14,'stu_app','leave_school'),(13,'stu_app','points'),(12,'stu_app','school_expression'),(11,'stu_app','stu_msg'),(10,'stu_app','student'),(9,'stu_app','suggestions');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-09 04:46:29.082368'),(2,'auth','0001_initial','2020-04-09 04:46:30.307947'),(3,'admin','0001_initial','2020-04-09 04:46:34.994687'),(4,'admin','0002_logentry_remove_auto_add','2020-04-09 04:46:35.969577'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-09 04:46:35.992512'),(6,'contenttypes','0002_remove_content_type_name','2020-04-09 04:46:36.533068'),(7,'auth','0002_alter_permission_name_max_length','2020-04-09 04:46:36.767440'),(8,'auth','0003_alter_user_email_max_length','2020-04-09 04:46:36.813317'),(9,'auth','0004_alter_user_username_opts','2020-04-09 04:46:36.825285'),(10,'auth','0005_alter_user_last_login_null','2020-04-09 04:46:36.950949'),(11,'auth','0006_require_contenttypes_0002','2020-04-09 04:46:36.954938'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-09 04:46:36.966907'),(13,'auth','0008_alter_user_username_max_length','2020-04-09 04:46:37.115509'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-09 04:46:37.261119'),(15,'auth','0010_alter_group_name_max_length','2020-04-09 04:46:37.287051'),(16,'auth','0011_update_proxy_permissions','2020-04-09 04:46:37.300014'),(17,'sessions','0001_initial','2020-04-09 04:46:37.361963'),(18,'stu_app','0001_initial','2020-04-09 04:46:38.145753');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4wnxiab6t3gtdw61e4mvv9c2ekqpifoz','NWYxYmU2MWUxMmI4Yjk0OWY1ZDIyODQzODkwMjRjNmEyZDQ3NTEyZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjdmOWU1ZWYxMGIzMjM3NWMwZGQ0OTA4MDZlMzI5ZTQzOGI2NWU5In0=','2020-04-23 04:49:08.074356');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_administrator`
--

DROP TABLE IF EXISTS `stu_app_administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_administrator` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `permission` int(11) NOT NULL,
  `job_num` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `job_num` (`job_num`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_administrator`
--

LOCK TABLES `stu_app_administrator` WRITE;
/*!40000 ALTER TABLE `stu_app_administrator` DISABLE KEYS */;
INSERT INTO `stu_app_administrator` VALUES (1,'黎明',1,'202049','123456'),(2,'王源',0,'202020','12345'),(3,'黎明',1,'202030','1234567'),(4,'花生',2,'303030','12367');
/*!40000 ALTER TABLE `stu_app_administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_change_class`
--

DROP TABLE IF EXISTS `stu_app_change_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_change_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(6) NOT NULL,
  `before_class` varchar(6) NOT NULL,
  `teacher_evaluate` longtext NOT NULL,
  `change_class_reason` longtext NOT NULL,
  `res` longtext NOT NULL,
  `status` varchar(2) NOT NULL,
  `stu_num_id` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_app_change_class_stu_num_id_4bf260df_fk_stu_app_s` (`stu_num_id`),
  CONSTRAINT `stu_app_change_class_stu_num_id_4bf260df_fk_stu_app_s` FOREIGN KEY (`stu_num_id`) REFERENCES `stu_app_student` (`stu_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_change_class`
--

LOCK TABLES `stu_app_change_class` WRITE;
/*!40000 ALTER TABLE `stu_app_change_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `stu_app_change_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_class`
--

DROP TABLE IF EXISTS `stu_app_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(6) NOT NULL,
  `profession` varchar(8) NOT NULL,
  `teacher_name` varchar(15) NOT NULL,
  `teach_name` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `class_name` (`class_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_class`
--

LOCK TABLES `stu_app_class` WRITE;
/*!40000 ALTER TABLE `stu_app_class` DISABLE KEYS */;
INSERT INTO `stu_app_class` VALUES (1,'3308班','python','匿名','里面'),(2,'3309班','java','不知道','哈哈哈'),(3,'1904班','python','黎明','哈哈哈');
/*!40000 ALTER TABLE `stu_app_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_leave_school`
--

DROP TABLE IF EXISTS `stu_app_leave_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_leave_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` longtext NOT NULL,
  `res` longtext NOT NULL,
  `status` varchar(2) NOT NULL,
  `stu_num_id` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stu_num_id` (`stu_num_id`),
  CONSTRAINT `stu_app_leave_school_stu_num_id_e110ed38_fk_stu_app_s` FOREIGN KEY (`stu_num_id`) REFERENCES `stu_app_student` (`stu_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_leave_school`
--

LOCK TABLES `stu_app_leave_school` WRITE;
/*!40000 ALTER TABLE `stu_app_leave_school` DISABLE KEYS */;
INSERT INTO `stu_app_leave_school` VALUES (1,'不知道','','0','s202049');
/*!40000 ALTER TABLE `stu_app_leave_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_points`
--

DROP TABLE IF EXISTS `stu_app_points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_points` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_time` varchar(10) NOT NULL,
  `write_points` int(11) NOT NULL,
  `competer_points` int(11) NOT NULL,
  `total_points` int(11) NOT NULL,
  `stu_num_id` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_app_points_stu_num_id_e9e32dc0_fk_stu_app_student_stu_num` (`stu_num_id`),
  CONSTRAINT `stu_app_points_stu_num_id_e9e32dc0_fk_stu_app_student_stu_num` FOREIGN KEY (`stu_num_id`) REFERENCES `stu_app_student` (`stu_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_points`
--

LOCK TABLES `stu_app_points` WRITE;
/*!40000 ALTER TABLE `stu_app_points` DISABLE KEYS */;
/*!40000 ALTER TABLE `stu_app_points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_school_expression`
--

DROP TABLE IF EXISTS `stu_app_school_expression`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_school_expression` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` longtext NOT NULL,
  `punish` longtext NOT NULL,
  `result` varchar(3) NOT NULL,
  `status` varchar(2) NOT NULL,
  `time` datetime(6) NOT NULL,
  `stu_num_id` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_app_school_expre_stu_num_id_4b2c0622_fk_stu_app_s` (`stu_num_id`),
  CONSTRAINT `stu_app_school_expre_stu_num_id_4b2c0622_fk_stu_app_s` FOREIGN KEY (`stu_num_id`) REFERENCES `stu_app_student` (`stu_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_school_expression`
--

LOCK TABLES `stu_app_school_expression` WRITE;
/*!40000 ALTER TABLE `stu_app_school_expression` DISABLE KEYS */;
INSERT INTO `stu_app_school_expression` VALUES (1,'不知道','哈哈哈哈','+10','0','2020-04-10 01:23:24.386464','s202049');
/*!40000 ALTER TABLE `stu_app_school_expression` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_stu_msg`
--

DROP TABLE IF EXISTS `stu_app_stu_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_stu_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_num` varchar(18) NOT NULL,
  `age` varchar(3) NOT NULL,
  `address` varchar(30) NOT NULL,
  `time_of_enrollment` varchar(20) NOT NULL,
  `recruiter` varchar(15) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `parent` varchar(15) NOT NULL,
  `parent_phone` varchar(11) NOT NULL,
  `tuition` varchar(6) NOT NULL,
  `loans` varchar(6) NOT NULL,
  `stu_num_id` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_num` (`id_num`),
  UNIQUE KEY `stu_num_id` (`stu_num_id`),
  CONSTRAINT `stu_app_stu_msg_stu_num_id_c1d62dd8_fk_stu_app_student_stu_num` FOREIGN KEY (`stu_num_id`) REFERENCES `stu_app_student` (`stu_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_stu_msg`
--

LOCK TABLES `stu_app_stu_msg` WRITE;
/*!40000 ALTER TABLE `stu_app_stu_msg` DISABLE KEYS */;
INSERT INTO `stu_app_stu_msg` VALUES (1,'1','19','河南','2019-6-9','哈哈','123456789','bbb','qwe456789','123456','123456','s202049');
/*!40000 ALTER TABLE `stu_app_stu_msg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_student`
--

DROP TABLE IF EXISTS `stu_app_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `stu_num` varchar(13) NOT NULL,
  `password` varchar(15) NOT NULL,
  `credit` int(11) NOT NULL,
  `permission` int(11) NOT NULL,
  `class_name_id` varchar(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stu_num` (`stu_num`),
  KEY `stu_app_student_class_name_id_2692e554_fk_stu_app_c` (`class_name_id`),
  CONSTRAINT `stu_app_student_class_name_id_2692e554_fk_stu_app_c` FOREIGN KEY (`class_name_id`) REFERENCES `stu_app_class` (`class_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_student`
--

LOCK TABLES `stu_app_student` WRITE;
/*!40000 ALTER TABLE `stu_app_student` DISABLE KEYS */;
INSERT INTO `stu_app_student` VALUES (1,'刘华','男','s202049','123456',100,4,'3308班'),(2,'刘海','女','s232323','123456',100,4,'3309班'),(3,'花花','男','s123123','12345',100,4,'3308班'),(4,'水水','女','s234234','123456',100,4,'1904班'),(5,'哈哈','男','s909090','123456',100,4,'1904班');
/*!40000 ALTER TABLE `stu_app_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_app_suggestions`
--

DROP TABLE IF EXISTS `stu_app_suggestions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stu_app_suggestions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suggestion` longtext NOT NULL,
  `time` datetime(6) NOT NULL,
  `status` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_app_suggestions`
--

LOCK TABLES `stu_app_suggestions` WRITE;
/*!40000 ALTER TABLE `stu_app_suggestions` DISABLE KEYS */;
/*!40000 ALTER TABLE `stu_app_suggestions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-14 15:12:47
