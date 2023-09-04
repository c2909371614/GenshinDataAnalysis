-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: genshin
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `element` varchar(45) DEFAULT NULL,
  `weaponType` varchar(45) DEFAULT NULL,
  `rankStar` varchar(45) DEFAULT NULL,
  `baseATK` int DEFAULT NULL,
  `baseHP` int DEFAULT NULL,
  `baseDEF` int DEFAULT NULL,
  `rateATK` double DEFAULT '0',
  `PDBonus` double DEFAULT '0',
  `EDBonus` double DEFAULT '0',
  `baseCR` double DEFAULT '0.05',
  `baseCD` double DEFAULT '0.5',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
INSERT INTO `characters` VALUES (1,'刻晴','雷','单手剑','五星',323,13103,799,NULL,0,0,0.05,0.884),(2,'迪卢克','火','双手剑','五星',335,12981,784,NULL,0,0,0.242,0.5),(3,'优菈','冰','双手剑','五星',342,13226,751,NULL,0,0,0.05,0.884),(4,'胡桃','火','长枪','五星',107,15552,876,NULL,0,0,0.05,0.884),(5,'魈','风','长枪','五星',349,12736,799,NULL,0,0,0.242,0.5),(6,'甘雨','冰','弓','五星',335,9797,630,NULL,0,0,0.05,0.884),(7,'钟离','岩','长枪','五星',251,14695,738,NULL,0,0.288,0.05,0.5),(8,'达达利亚','水','弓','五星',302,13103,815,NULL,0,0.288,0.05,0.5),(9,'可莉','火','法典','五星',311,10287,615,NULL,0,0.288,0.05,0.5),(10,'温蒂','风','弓','五星',263,10531,669,NULL,0,0,0.05,0.5),(11,'莫娜','水','法典','五星',287,10409,653,NULL,0,0,0.05,0.5),(12,'七七','冰','单手剑','五星',287,12368,922,NULL,0,0,0.05,0.5),(13,'琴','风','单手剑','五星',239,14695,769,NULL,0,0,0.05,0.5),(14,'阿贝多','岩','单手剑','五星',251,13226,876,NULL,0,0.288,0.05,0.5),(15,'烟绯','火','法典','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(16,'罗莎莉亚','冰','长枪','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(17,'辛焱','火','双手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(18,'迪奥娜','冰','弓','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(19,'砂糖','风','法典','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(20,'重云','冰','双手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(21,'诺艾尔','岩','双手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(22,'班尼特','火','单手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(23,'菲谢尔','雷','弓','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(24,'凝光','岩','法典','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(25,'行秋','水','单手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(26,'北斗','雷','双手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(27,'香菱','火','长枪','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(28,'雷泽','雷','双手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(29,'芭芭拉','水','法典','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(30,'丽莎','雷','法典','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(31,'凯亚','冰','单手剑','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(32,'安伯','火','弓','四星',NULL,NULL,NULL,NULL,0,0,0.05,0.5),(33,'旅行者','风岩','单手剑','五星',NULL,NULL,NULL,NULL,0,0,0.05,0.5);
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-24 23:55:59
