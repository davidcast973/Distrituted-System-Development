-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.36-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win32
-- HeidiSQL Versión:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para reloj_utc_c1
CREATE DATABASE IF NOT EXISTS `reloj_utc_c1` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `reloj_utc_c1`;

-- Volcando estructura para tabla reloj_utc_c1.hora_central
CREATE TABLE IF NOT EXISTS `hora_central` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hora_previa` datetime DEFAULT NULL,
  `hora_utc` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc_c1.hora_central: ~294 rows (aproximadamente)
/*!40000 ALTER TABLE `hora_central` DISABLE KEYS */;
INSERT IGNORE INTO `hora_central` (`id`, `hora_previa`, `hora_utc`) VALUES
	(1, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(2, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(3, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(4, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(5, '2019-10-14 18:13:09', '0000-00-00 00:00:00'),
	(6, '2019-10-14 02:00:09', '0000-00-00 00:00:00'),
	(7, '2019-10-14 18:57:06', '2019-10-14 20:31:50'),
	(8, '2019-10-14 18:57:58', '2019-10-14 20:32:43'),
	(9, '2019-10-14 10:06:32', '2019-10-14 20:34:15'),
	(10, '2019-10-14 10:07:27', '2019-10-14 20:35:10');
/*!40000 ALTER TABLE `hora_central` ENABLE KEYS */;

-- Volcando estructura para tabla reloj_utc_c1.hora_servidores
CREATE TABLE IF NOT EXISTS `hora_servidores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idHoraCentral` int(11) DEFAULT NULL,
  `idServidor` int(11) DEFAULT NULL,
  `ajuste` double DEFAULT NULL,
  `ralentizar` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_hora_servidores_hora_central` (`idHoraCentral`),
  KEY `FK_hora_servidores_servidores` (`idServidor`),
  CONSTRAINT `FK_hora_servidores_hora_central` FOREIGN KEY (`idHoraCentral`) REFERENCES `hora_central` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_hora_servidores_servidores` FOREIGN KEY (`idServidor`) REFERENCES `servidores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc_c1.hora_servidores: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `hora_servidores` DISABLE KEYS */;
INSERT IGNORE INTO `hora_servidores` (`id`, `idHoraCentral`, `idServidor`, `ajuste`, `ralentizar`) VALUES
	(1, 1, 1, 0.7121452088775635, 1),
	(4, 4, 1, 0.8894298444519043, 1),
	(5, 5, 1, 0.9382187415924073, 1),
	(6, 6, 1, 0.8129221043395995, 1),
	(7, 7, 1, 0.8150927807006836, 1),
	(8, 8, 1, 0.9488426918792725, 6),
	(9, 9, 1, 0.8231025019531251, 6),
	(10, 10, 1, 0.8630220848693848, 6);
/*!40000 ALTER TABLE `hora_servidores` ENABLE KEYS */;

-- Volcando estructura para tabla reloj_utc_c1.servidores
CREATE TABLE IF NOT EXISTS `servidores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(30) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `latencia` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc_c1.servidores: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT IGNORE INTO `servidores` (`id`, `ip`, `nombre`, `latencia`) VALUES
	(1, '10.100.70.115', 'Server 1', 4500.5),
	(2, '192.168.0.9', 'Server2', NULL);
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
