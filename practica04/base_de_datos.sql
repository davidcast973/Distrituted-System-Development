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


-- Volcando estructura de base de datos para resguardo_sumas
CREATE DATABASE IF NOT EXISTS `resguardo_sumas` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `resguardo_sumas`;

-- Volcando estructura para tabla resguardo_sumas.resultados_envios
CREATE TABLE IF NOT EXISTS `resultados_envios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_origen` varchar(15) NOT NULL,
  `nombre_equipo` text,
  `date_added` datetime NOT NULL,
  `num_jugador` tinyint(4) NOT NULL,
  `resultado_suma` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla resguardo_sumas.resultados_envios: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `resultados_envios` DISABLE KEYS */;
INSERT IGNORE INTO `resultados_envios` (`id`, `ip_origen`, `nombre_equipo`, `date_added`, `num_jugador`, `resultado_suma`) VALUES
	(1, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 14:17:09', 1, 37),
	(2, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 14:22:43', 1, 37),
	(3, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 14:23:13', 1, 37),
	(4, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 14:24:32', 1, 37),
	(5, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 14:41:07', 1, 40),
	(6, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:15:30', 1, 40),
	(7, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:17:14', 1, 15),
	(8, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:21:24', 1, 15),
	(9, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:23:25', 1, 15),
	(10, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:25:19', 1, 5),
	(11, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:30:09', 1, 6),
	(12, '127.0.0.1', 'DESKTOP-P1J8UQN', '2019-09-21 15:30:24', 1, 10);
/*!40000 ALTER TABLE `resultados_envios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
