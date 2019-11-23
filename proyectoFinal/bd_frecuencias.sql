-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.38-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.0.0.5460
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para resguardo_sumas_3
CREATE DATABASE IF NOT EXISTS `resguardo_sumas_3` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `resguardo_sumas_3`;

-- Volcando estructura para tabla resguardo_sumas_3.envios
CREATE TABLE IF NOT EXISTS `envios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_origen` varchar(15) NOT NULL,
  `nombre_equipo` text,
  `date_added` datetime NOT NULL,
  `num_jugador` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla resguardo_sumas_3.envios: ~2 rows (aproximadamente)
DELETE FROM `envios`;
/*!40000 ALTER TABLE `envios` DISABLE KEYS */;
INSERT INTO `envios` (`id`, `ip_origen`, `nombre_equipo`, `date_added`, `num_jugador`) VALUES
	(27, '10.100.76.126', 'iAngelMx-Laptop', '2019-11-21 19:16:42', 1),
	(29, '10.100.76.126', 'iAngelMx-Laptop', '2019-11-21 19:17:42', 1);
/*!40000 ALTER TABLE `envios` ENABLE KEYS */;

-- Volcando estructura para tabla resguardo_sumas_3.frecuencias
CREATE TABLE IF NOT EXISTS `frecuencias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_envio` int(11) DEFAULT NULL,
  `numero` int(11) DEFAULT NULL,
  `frecuencia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla resguardo_sumas_3.frecuencias: ~0 rows (aproximadamente)
DELETE FROM `frecuencias`;
/*!40000 ALTER TABLE `frecuencias` DISABLE KEYS */;
/*!40000 ALTER TABLE `frecuencias` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
