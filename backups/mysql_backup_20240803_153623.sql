-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: asuan_db
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` int unsigned NOT NULL,
  `telefono` int unsigned NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `conf_contrasena` varchar(128) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Administrador_numero_documento_fa238ef2_uniq` (`numero_documento`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Administrador_user_id_949907f5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrador_chk_1` CHECK ((`numero_documento` >= 0)),
  CONSTRAINT `administrador_chk_2` CHECK ((`telefono` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Administrador',7,'add_administrador'),(26,'Can change Administrador',7,'change_administrador'),(27,'Can delete Administrador',7,'delete_administrador'),(28,'Can view Administrador',7,'view_administrador'),(29,'Can add categoria',8,'add_categoria'),(30,'Can change categoria',8,'change_categoria'),(31,'Can delete categoria',8,'delete_categoria'),(32,'Can view categoria',8,'view_categoria'),(33,'Can add cliente',9,'add_cliente'),(34,'Can change cliente',9,'change_cliente'),(35,'Can delete cliente',9,'delete_cliente'),(36,'Can view cliente',9,'view_cliente'),(37,'Can add marca',10,'add_marca'),(38,'Can change marca',10,'change_marca'),(39,'Can delete marca',10,'delete_marca'),(40,'Can view marca',10,'view_marca'),(41,'Can add mesero',11,'add_mesero'),(42,'Can change mesero',11,'change_mesero'),(43,'Can delete mesero',11,'delete_mesero'),(44,'Can view mesero',11,'view_mesero'),(45,'Can add Operador',12,'add_operador'),(46,'Can change Operador',12,'change_operador'),(47,'Can delete Operador',12,'delete_operador'),(48,'Can view Operador',12,'view_operador'),(49,'Can add plato',13,'add_plato'),(50,'Can change plato',13,'change_plato'),(51,'Can delete plato',13,'delete_plato'),(52,'Can view plato',13,'view_plato'),(53,'Can add presentacion',14,'add_presentacion'),(54,'Can change presentacion',14,'change_presentacion'),(55,'Can delete presentacion',14,'delete_presentacion'),(56,'Can view presentacion',14,'view_presentacion'),(57,'Can add cuenta',15,'add_cuenta'),(58,'Can change cuenta',15,'change_cuenta'),(59,'Can delete cuenta',15,'delete_cuenta'),(60,'Can view cuenta',15,'view_cuenta'),(61,'Can add producto',16,'add_producto'),(62,'Can change producto',16,'change_producto'),(63,'Can delete producto',16,'delete_producto'),(64,'Can view producto',16,'view_producto'),(65,'Can add venta',17,'add_venta'),(66,'Can change venta',17,'change_venta'),(67,'Can delete venta',17,'delete_venta'),(68,'Can view venta',17,'view_venta'),(69,'Can add factura',18,'add_factura'),(70,'Can change factura',18,'change_factura'),(71,'Can delete factura',18,'delete_factura'),(72,'Can view factura',18,'view_factura');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$GF1C4HaMIhvZ9LquqqCAmF$6EmBDrF33diCXNY3cVqUdH4k4G5fwuDyneApcGThr7c=','2024-08-03 15:41:26.119621',1,'admin','','','asuan.adso@gmail.com',1,1,'2024-08-03 03:34:30.362282');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `categoria` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Categoria_categoria_4061e22a_uniq` (`categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Bebidas'),(3,'Insumos'),(2,'Lacteos');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` int unsigned NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` int unsigned NOT NULL,
  `pais_telefono` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Cliente_numero_documento_3f4d400b_uniq` (`numero_documento`),
  CONSTRAINT `cliente_chk_2` CHECK ((`telefono` >= 0)),
  CONSTRAINT `Cliente_numero_documento_3f4d400b_check` CHECK ((`numero_documento` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuenta`
--

DROP TABLE IF EXISTS `cuenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuenta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `subtotal` decimal(8,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `id_cliente_id` bigint NOT NULL,
  `id_mesero_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Cuenta_id_cliente_id_315de25c_fk_Cliente_id` (`id_cliente_id`),
  KEY `Cuenta_id_mesero_id_05d3f281_fk_Mesero_id` (`id_mesero_id`),
  CONSTRAINT `Cuenta_id_cliente_id_315de25c_fk_Cliente_id` FOREIGN KEY (`id_cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `Cuenta_id_mesero_id_05d3f281_fk_Mesero_id` FOREIGN KEY (`id_mesero_id`) REFERENCES `mesero` (`id`),
  CONSTRAINT `cuenta_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuenta`
--

LOCK TABLES `cuenta` WRITE;
/*!40000 ALTER TABLE `cuenta` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuenta_id_plato`
--

DROP TABLE IF EXISTS `cuenta_id_plato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuenta_id_plato` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cuenta_id` bigint NOT NULL,
  `plato_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Cuenta_id_plato_cuenta_id_plato_id_35049a8f_uniq` (`cuenta_id`,`plato_id`),
  KEY `Cuenta_id_plato_plato_id_c3e8eaa9_fk_Plato_id` (`plato_id`),
  CONSTRAINT `Cuenta_id_plato_cuenta_id_0e5fdd43_fk_Cuenta_id` FOREIGN KEY (`cuenta_id`) REFERENCES `cuenta` (`id`),
  CONSTRAINT `Cuenta_id_plato_plato_id_c3e8eaa9_fk_Plato_id` FOREIGN KEY (`plato_id`) REFERENCES `plato` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuenta_id_plato`
--

LOCK TABLES `cuenta_id_plato` WRITE;
/*!40000 ALTER TABLE `cuenta_id_plato` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuenta_id_plato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app','administrador'),(8,'app','categoria'),(9,'app','cliente'),(15,'app','cuenta'),(18,'app','factura'),(10,'app','marca'),(11,'app','mesero'),(12,'app','operador'),(13,'app','plato'),(14,'app','presentacion'),(16,'app','producto'),(17,'app','venta'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-03 03:31:13.609024'),(2,'auth','0001_initial','2024-08-03 03:31:13.953291'),(3,'admin','0001_initial','2024-08-03 03:31:14.038910'),(4,'admin','0002_logentry_remove_auto_add','2024-08-03 03:31:14.043897'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-03 03:31:14.049970'),(6,'app','0001_initial','2024-08-03 03:31:14.726096'),(7,'app','0002_alter_categoria_categoria','2024-08-03 03:31:14.738872'),(8,'app','0003_rename_nombre_producto_producto_producto_and_more','2024-08-03 03:31:14.779273'),(9,'app','0004_alter_administrador_tipo_documento_and_more','2024-08-03 03:31:14.785257'),(10,'app','0005_alter_administrador_numero_documento_and_more','2024-08-03 03:31:14.804206'),(11,'app','0006_alter_administrador_numero_documento_and_more','2024-08-03 03:31:14.860627'),(12,'app','0007_alter_administrador_numero_documento_and_more','2024-08-03 03:31:14.925961'),(13,'app','0008_rename_nombre_plato_plato_plato','2024-08-03 03:31:14.942948'),(14,'app','0009_alter_cliente_numero_documento_and_more','2024-08-03 03:31:14.968224'),(15,'app','0010_alter_cliente_numero_documento','2024-08-03 03:31:14.971842'),(16,'app','0011_alter_cliente_numero_documento_and_more','2024-08-03 03:31:15.080554'),(17,'app','0012_alter_cliente_numero_documento_and_more','2024-08-03 03:31:15.273997'),(18,'app','0013_alter_cliente_numero_documento','2024-08-03 03:31:15.276988'),(19,'app','0014_alter_administrador_numero_documento_and_more','2024-08-03 03:31:15.286263'),(20,'app','0015_cliente_pais_telefono','2024-08-03 03:31:15.306932'),(21,'app','0016_mesero_pais_telefono_operador_pais_telefono','2024-08-03 03:31:15.349841'),(22,'app','0017_alter_cliente_email','2024-08-03 03:31:15.353838'),(23,'app','0018_alter_administrador_email_alter_mesero_email_and_more','2024-08-03 03:31:15.360818'),(24,'app','0019_remove_factura_id_metodo_alter_producto_id_categoria_and_more','2024-08-03 03:31:15.440921'),(25,'app','0020_venta_metodo_pago_alter_venta_id_admin_and_more','2024-08-03 03:31:15.694705'),(26,'app','0021_administrador_conf_contraseña','2024-08-03 03:31:15.716032'),(27,'app','0022_alter_administrador_conf_contraseña','2024-08-03 03:31:15.720020'),(28,'app','0023_remove_administrador_email_administrador_user','2024-08-03 03:31:15.794357'),(29,'app','0024_alter_administrador_options_and_more','2024-08-03 03:31:15.902477'),(30,'app','0025_rename_conf_contraseña_administrador_conf_contrasena_and_more','2024-08-03 03:31:15.937601'),(31,'app','0026_alter_operador_options_remove_operador_contraseña_and_more','2024-08-03 03:31:16.100773'),(32,'contenttypes','0002_remove_content_type_name','2024-08-03 03:31:16.163179'),(33,'auth','0002_alter_permission_name_max_length','2024-08-03 03:31:16.211750'),(34,'auth','0003_alter_user_email_max_length','2024-08-03 03:31:16.233447'),(35,'auth','0004_alter_user_username_opts','2024-08-03 03:31:16.240428'),(36,'auth','0005_alter_user_last_login_null','2024-08-03 03:31:16.285708'),(37,'auth','0006_require_contenttypes_0002','2024-08-03 03:31:16.287703'),(38,'auth','0007_alter_validators_add_error_messages','2024-08-03 03:31:16.293686'),(39,'auth','0008_alter_user_username_max_length','2024-08-03 03:31:16.348113'),(40,'auth','0009_alter_user_last_name_max_length','2024-08-03 03:31:16.397450'),(41,'auth','0010_alter_group_name_max_length','2024-08-03 03:31:16.418394'),(42,'auth','0011_update_proxy_permissions','2024-08-03 03:31:16.431126'),(43,'auth','0012_alter_user_first_name_max_length','2024-08-03 03:31:16.480446'),(44,'sessions','0001_initial','2024-08-03 03:31:16.504933');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
INSERT INTO `django_session` VALUES ('yat5xqtv87tsw74ovoikvryqspvoj0e4','.eJxVjEEOwiAQRe_C2pDiwAAu3fcMZBhAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hSuIilDj9bpH4kdsO0p3abZY8t3WZotwVedAuxznl5_Vw_w4q9fqtzRnYMHjy1riCUVtI2pLLDpXzCAV1BnRqYGMLawRMyQ5aGypYiFm8P8BIN2Y:1saGso:YRZRYeTHtnL1DeVt_k7dWtLdctkHE6mu1dTCnTn1WGI','2024-08-17 15:41:26.122614');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_emision_factura` datetime(6) NOT NULL,
  `id_venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Factura_id_venta_id_56e07d2e_fk_Venta_id` (`id_venta_id`),
  CONSTRAINT `Factura_id_venta_id_56e07d2e_fk_Venta_id` FOREIGN KEY (`id_venta_id`) REFERENCES `venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `marca` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Marca_marca_706bdc27_uniq` (`marca`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mesero`
--

DROP TABLE IF EXISTS `mesero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesero` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` int unsigned NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` int unsigned NOT NULL,
  `pais_telefono` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Mesero_numero_documento_582a65fb_uniq` (`numero_documento`),
  CONSTRAINT `mesero_chk_2` CHECK ((`telefono` >= 0)),
  CONSTRAINT `Mesero_numero_documento_582a65fb_check` CHECK ((`numero_documento` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesero`
--

LOCK TABLES `mesero` WRITE;
/*!40000 ALTER TABLE `mesero` DISABLE KEYS */;
/*!40000 ALTER TABLE `mesero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operador`
--

DROP TABLE IF EXISTS `operador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operador` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` int unsigned NOT NULL,
  `telefono` int unsigned NOT NULL,
  `conf_contrasena` varchar(128) NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Operador_numero_documento_2ec1fdff_uniq` (`numero_documento`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Operador_user_id_17453727_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `operador_chk_1` CHECK ((`numero_documento` >= 0)),
  CONSTRAINT `operador_chk_2` CHECK ((`telefono` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operador`
--

LOCK TABLES `operador` WRITE;
/*!40000 ALTER TABLE `operador` DISABLE KEYS */;
/*!40000 ALTER TABLE `operador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plato`
--

DROP TABLE IF EXISTS `plato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plato` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `plato` varchar(50) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plato`
--

LOCK TABLES `plato` WRITE;
/*!40000 ALTER TABLE `plato` DISABLE KEYS */;
/*!40000 ALTER TABLE `plato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presentacion`
--

DROP TABLE IF EXISTS `presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `presentacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `presentacion` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Presentacion_presentacion_0e222490_uniq` (`presentacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presentacion`
--

LOCK TABLES `presentacion` WRITE;
/*!40000 ALTER TABLE `presentacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `producto` varchar(50) NOT NULL,
  `cantidad` int unsigned NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `id_categoria_id` bigint NOT NULL,
  `id_marca_id` bigint NOT NULL,
  `id_presentacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Producto_id_categoria_id_25096c94_fk_Categoria_id` (`id_categoria_id`),
  KEY `Producto_id_marca_id_d863f11f_fk_Marca_id` (`id_marca_id`),
  KEY `Producto_id_presentacion_id_02f8c93a_fk_Presentacion_id` (`id_presentacion_id`),
  CONSTRAINT `Producto_id_categoria_id_25096c94_fk_Categoria_id` FOREIGN KEY (`id_categoria_id`) REFERENCES `categoria` (`id`),
  CONSTRAINT `Producto_id_marca_id_d863f11f_fk_Marca_id` FOREIGN KEY (`id_marca_id`) REFERENCES `marca` (`id`),
  CONSTRAINT `Producto_id_presentacion_id_02f8c93a_fk_Presentacion_id` FOREIGN KEY (`id_presentacion_id`) REFERENCES `presentacion` (`id`),
  CONSTRAINT `producto_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad_producto` int unsigned NOT NULL,
  `total_venta` decimal(8,2) NOT NULL,
  `total_venta_iva` decimal(8,2) NOT NULL,
  `fecha_venta` datetime(6) NOT NULL,
  `id_admin_id` bigint DEFAULT NULL,
  `id_cuenta_id` bigint NOT NULL,
  `id_operador_id` bigint DEFAULT NULL,
  `metodo_pago` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Venta_id_cuenta_id_6a5a5443_fk_Cuenta_id` (`id_cuenta_id`),
  KEY `Venta_id_admin_id_15ee83d9_fk_Administrador_id` (`id_admin_id`),
  KEY `Venta_id_operador_id_9354ec3b_fk_Operador_id` (`id_operador_id`),
  CONSTRAINT `Venta_id_admin_id_15ee83d9_fk_Administrador_id` FOREIGN KEY (`id_admin_id`) REFERENCES `administrador` (`id`),
  CONSTRAINT `Venta_id_cuenta_id_6a5a5443_fk_Cuenta_id` FOREIGN KEY (`id_cuenta_id`) REFERENCES `cuenta` (`id`),
  CONSTRAINT `Venta_id_operador_id_9354ec3b_fk_Operador_id` FOREIGN KEY (`id_operador_id`) REFERENCES `operador` (`id`),
  CONSTRAINT `venta_chk_1` CHECK ((`cantidad_producto` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta_id_producto`
--

DROP TABLE IF EXISTS `venta_id_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta_id_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `venta_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Venta_id_producto_venta_id_producto_id_a8c20661_uniq` (`venta_id`,`producto_id`),
  KEY `Venta_id_producto_producto_id_94805695_fk_Producto_id` (`producto_id`),
  CONSTRAINT `Venta_id_producto_producto_id_94805695_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `Venta_id_producto_venta_id_fb5ac1e5_fk_Venta_id` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta_id_producto`
--

LOCK TABLES `venta_id_producto` WRITE;
/*!40000 ALTER TABLE `venta_id_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta_id_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-03 15:36:24
