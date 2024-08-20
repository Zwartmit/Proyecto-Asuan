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
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Administrador',7,'add_administrador'),(26,'Can change Administrador',7,'change_administrador'),(27,'Can delete Administrador',7,'delete_administrador'),(28,'Can view Administrador',7,'view_administrador'),(29,'Can add categoria',8,'add_categoria'),(30,'Can change categoria',8,'change_categoria'),(31,'Can delete categoria',8,'delete_categoria'),(32,'Can view categoria',8,'view_categoria'),(33,'Can add cliente',9,'add_cliente'),(34,'Can change cliente',9,'change_cliente'),(35,'Can delete cliente',9,'delete_cliente'),(36,'Can view cliente',9,'view_cliente'),(37,'Can add marca',10,'add_marca'),(38,'Can change marca',10,'change_marca'),(39,'Can delete marca',10,'delete_marca'),(40,'Can view marca',10,'view_marca'),(41,'Can add mesero',11,'add_mesero'),(42,'Can change mesero',11,'change_mesero'),(43,'Can delete mesero',11,'delete_mesero'),(44,'Can view mesero',11,'view_mesero'),(45,'Can add Operador',12,'add_operador'),(46,'Can change Operador',12,'change_operador'),(47,'Can delete Operador',12,'delete_operador'),(48,'Can view Operador',12,'view_operador'),(49,'Can add plato',13,'add_plato'),(50,'Can change plato',13,'change_plato'),(51,'Can delete plato',13,'delete_plato'),(52,'Can view plato',13,'view_plato'),(53,'Can add presentacion',14,'add_presentacion'),(54,'Can change presentacion',14,'change_presentacion'),(55,'Can delete presentacion',14,'delete_presentacion'),(56,'Can view presentacion',14,'view_presentacion'),(57,'Can add producto',15,'add_producto'),(58,'Can change producto',15,'change_producto'),(59,'Can delete producto',15,'delete_producto'),(60,'Can view producto',15,'view_producto'),(61,'Can add venta',16,'add_venta'),(62,'Can change venta',16,'change_venta'),(63,'Can delete venta',16,'delete_venta'),(64,'Can view venta',16,'view_venta'),(65,'Can add factura',17,'add_factura'),(66,'Can change factura',17,'change_factura'),(67,'Can delete factura',17,'delete_factura'),(68,'Can view factura',17,'view_factura'),(69,'Can add detalle_de_venta',18,'add_detalle_venta'),(70,'Can change detalle_de_venta',18,'change_detalle_venta'),(71,'Can delete detalle_de_venta',18,'delete_detalle_venta'),(72,'Can view detalle_de_venta',18,'view_detalle_venta'),(73,'Can add detalle_venta_cuenta',19,'add_detalle_venta_cuenta'),(74,'Can change detalle_venta_cuenta',19,'change_detalle_venta_cuenta'),(75,'Can delete detalle_venta_cuenta',19,'delete_detalle_venta_cuenta'),(76,'Can view detalle_venta_cuenta',19,'view_detalle_venta_cuenta');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$riXMmaIqpEQ5EFX6Sof9pi$DgxwEBCYzsA2B6PsAGRWNQ/68OI3cC2ccIA4irFCxlQ=','2024-08-20 19:44:53.340317',1,'admin','','','admin@gmail.com',1,1,'2024-08-20 18:36:33.611207');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (2,'gadfa');
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
-- Table structure for table `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad_producto` int unsigned NOT NULL,
  `id_producto_id` bigint NOT NULL,
  `id_venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Detalle_venta_id_producto_id_cc6290ad_fk_Producto_id` (`id_producto_id`),
  KEY `Detalle_venta_id_venta_id_498f595f_fk_Venta_id` (`id_venta_id`),
  CONSTRAINT `Detalle_venta_id_producto_id_cc6290ad_fk_Producto_id` FOREIGN KEY (`id_producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `Detalle_venta_id_venta_id_498f595f_fk_Venta_id` FOREIGN KEY (`id_venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalle_venta_chk_1` CHECK ((`cantidad_producto` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_venta`
--

LOCK TABLES `detalle_venta` WRITE;
/*!40000 ALTER TABLE `detalle_venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_venta_cuenta`
--

DROP TABLE IF EXISTS `detalle_venta_cuenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta_cuenta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad_producto` int unsigned NOT NULL,
  `cantidad_plato` int unsigned NOT NULL,
  `id_cliente_id` bigint NOT NULL,
  `id_mesero_id` bigint NOT NULL,
  `id_plato_id` bigint NOT NULL,
  `id_producto_id` bigint NOT NULL,
  `id_venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Detalle_venta_cuenta_id_cliente_id_6a36ba75_fk_Cliente_id` (`id_cliente_id`),
  KEY `Detalle_venta_cuenta_id_mesero_id_d85945fd_fk_Mesero_id` (`id_mesero_id`),
  KEY `Detalle_venta_cuenta_id_plato_id_2ed938ca_fk_Plato_id` (`id_plato_id`),
  KEY `Detalle_venta_cuenta_id_producto_id_986bd410_fk_Producto_id` (`id_producto_id`),
  KEY `Detalle_venta_cuenta_id_venta_id_0fd26c6e_fk_Venta_id` (`id_venta_id`),
  CONSTRAINT `Detalle_venta_cuenta_id_cliente_id_6a36ba75_fk_Cliente_id` FOREIGN KEY (`id_cliente_id`) REFERENCES `cliente` (`id`),
  CONSTRAINT `Detalle_venta_cuenta_id_mesero_id_d85945fd_fk_Mesero_id` FOREIGN KEY (`id_mesero_id`) REFERENCES `mesero` (`id`),
  CONSTRAINT `Detalle_venta_cuenta_id_plato_id_2ed938ca_fk_Plato_id` FOREIGN KEY (`id_plato_id`) REFERENCES `plato` (`id`),
  CONSTRAINT `Detalle_venta_cuenta_id_producto_id_986bd410_fk_Producto_id` FOREIGN KEY (`id_producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `Detalle_venta_cuenta_id_venta_id_0fd26c6e_fk_Venta_id` FOREIGN KEY (`id_venta_id`) REFERENCES `venta` (`id`),
  CONSTRAINT `detalle_venta_cuenta_chk_1` CHECK ((`cantidad_producto` >= 0)),
  CONSTRAINT `detalle_venta_cuenta_chk_2` CHECK ((`cantidad_plato` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_venta_cuenta`
--

LOCK TABLES `detalle_venta_cuenta` WRITE;
/*!40000 ALTER TABLE `detalle_venta_cuenta` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_venta_cuenta` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app','administrador'),(8,'app','categoria'),(9,'app','cliente'),(18,'app','detalle_venta'),(19,'app','detalle_venta_cuenta'),(17,'app','factura'),(10,'app','marca'),(11,'app','mesero'),(12,'app','operador'),(13,'app','plato'),(14,'app','presentacion'),(15,'app','producto'),(16,'app','venta'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-20 18:36:03.898146'),(2,'auth','0001_initial','2024-08-20 18:36:04.467268'),(3,'admin','0001_initial','2024-08-20 18:36:04.591880'),(4,'admin','0002_logentry_remove_auto_add','2024-08-20 18:36:04.599447'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-20 18:36:04.606441'),(6,'app','0001_initial','2024-08-20 18:36:05.559790'),(7,'app','0002_alter_categoria_categoria','2024-08-20 18:36:05.577636'),(8,'app','0003_rename_nombre_producto_producto_producto_and_more','2024-08-20 18:36:05.637815'),(9,'app','0004_alter_administrador_tipo_documento_and_more','2024-08-20 18:36:05.645270'),(10,'app','0005_alter_administrador_numero_documento_and_more','2024-08-20 18:36:05.667572'),(11,'app','0006_alter_administrador_numero_documento_and_more','2024-08-20 18:36:05.741485'),(12,'app','0007_alter_administrador_numero_documento_and_more','2024-08-20 18:36:05.814344'),(13,'app','0008_rename_nombre_plato_plato_plato','2024-08-20 18:36:05.837576'),(14,'app','0009_alter_cliente_numero_documento_and_more','2024-08-20 18:36:05.867150'),(15,'app','0010_alter_cliente_numero_documento','2024-08-20 18:36:05.871848'),(16,'app','0011_alter_cliente_numero_documento_and_more','2024-08-20 18:36:06.025658'),(17,'app','0012_alter_cliente_numero_documento_and_more','2024-08-20 18:36:06.362579'),(18,'app','0013_alter_cliente_numero_documento','2024-08-20 18:36:06.367531'),(19,'app','0014_alter_administrador_numero_documento_and_more','2024-08-20 18:36:06.382405'),(20,'app','0015_cliente_pais_telefono','2024-08-20 18:36:06.411645'),(21,'app','0016_mesero_pais_telefono_operador_pais_telefono','2024-08-20 18:36:06.471400'),(22,'app','0017_alter_cliente_email','2024-08-20 18:36:06.476767'),(23,'app','0018_alter_administrador_email_alter_mesero_email_and_more','2024-08-20 18:36:06.487644'),(24,'app','0019_remove_factura_id_metodo_alter_producto_id_categoria_and_more','2024-08-20 18:36:06.587519'),(25,'app','0020_venta_metodo_pago_alter_venta_id_admin_and_more','2024-08-20 18:36:06.924151'),(26,'app','0021_administrador_conf_contraseña','2024-08-20 18:36:06.952394'),(27,'app','0022_alter_administrador_conf_contraseña','2024-08-20 18:36:06.957083'),(28,'app','0023_remove_administrador_email_administrador_user','2024-08-20 18:36:07.056738'),(29,'app','0024_alter_administrador_options_and_more','2024-08-20 18:36:07.189926'),(30,'app','0025_rename_conf_contraseña_administrador_conf_contrasena_and_more','2024-08-20 18:36:07.239013'),(31,'app','0026_alter_operador_options_remove_operador_contraseña_and_more','2024-08-20 18:36:07.451732'),(32,'app','0027_alter_venta_options_alter_venta_metodo_pago','2024-08-20 18:36:07.473907'),(33,'app','0028_alter_venta_options_alter_venta_metodo_pago','2024-08-20 18:36:07.495750'),(34,'app','0029_alter_venta_metodo_pago','2024-08-20 18:36:07.510185'),(35,'app','0030_alter_venta_metodo_pago','2024-08-20 18:36:07.524398'),(36,'app','0031_alter_venta_order_with_respect_to_and_more','2024-08-20 18:36:08.297225'),(37,'contenttypes','0002_remove_content_type_name','2024-08-20 18:36:08.381224'),(38,'auth','0002_alter_permission_name_max_length','2024-08-20 18:36:08.447723'),(39,'auth','0003_alter_user_email_max_length','2024-08-20 18:36:08.487956'),(40,'auth','0004_alter_user_username_opts','2024-08-20 18:36:08.500053'),(41,'auth','0005_alter_user_last_login_null','2024-08-20 18:36:08.564956'),(42,'auth','0006_require_contenttypes_0002','2024-08-20 18:36:08.567247'),(43,'auth','0007_alter_validators_add_error_messages','2024-08-20 18:36:08.575483'),(44,'auth','0008_alter_user_username_max_length','2024-08-20 18:36:08.642193'),(45,'auth','0009_alter_user_last_name_max_length','2024-08-20 18:36:08.708432'),(46,'auth','0010_alter_group_name_max_length','2024-08-20 18:36:08.728588'),(47,'auth','0011_update_proxy_permissions','2024-08-20 18:36:08.742912'),(48,'auth','0012_alter_user_first_name_max_length','2024-08-20 18:36:08.808522'),(49,'sessions','0001_initial','2024-08-20 18:36:08.840146');
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
INSERT INTO `django_session` VALUES ('b5aju5ddysjj7gg8vgcsgq0gsayu55sx','.eJxVjMsOwiAQRf-FtSEMbXm4dO83EJgZpGogKe3K-O_apAvd3nPOfYkQt7WErfMSZhJnAeL0u6WID647oHustyax1XWZk9wVedAur434eTncv4MSe_nW2iUzZcsZGUkBGRpNZoOOk7fjABMxZiaISluGQbsMoL2x2kWVfELx_gANCziY:1sgUmj:UmVBsk430yoGqyRyL1dtz6c82OG9pfYvIyuY4sPorls','2024-09-03 19:44:53.345276'),('fnqdqz7wu7hsq2lu0wddyskpv3to4z7l','.eJxVjMsOwiAQRf-FtSEMbXm4dO83EJgZpGogKe3K-O_apAvd3nPOfYkQt7WErfMSZhJnAeL0u6WID647oHustyax1XWZk9wVedAur434eTncv4MSe_nW2iUzZcsZGUkBGRpNZoOOk7fjABMxZiaISluGQbsMoL2x2kWVfELx_gANCziY:1sgUY6:vQtvV_4HbLL60kuHBppmI14ZvJsx8fsb643cdMPGsMo','2024-09-03 19:29:46.518374');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (1,'fg');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presentacion`
--

LOCK TABLES `presentacion` WRITE;
/*!40000 ALTER TABLE `presentacion` DISABLE KEYS */;
INSERT INTO `presentacion` VALUES (1,'gu');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'ad',4,454.00,0,2,1,1);
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
  `total_venta` decimal(8,2) NOT NULL,
  `fecha_venta` datetime(6) NOT NULL,
  `metodo_pago` varchar(3) NOT NULL,
  `_order` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-20 15:06:57
