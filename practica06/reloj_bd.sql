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


-- Volcando estructura de base de datos para reloj_utc
CREATE DATABASE IF NOT EXISTS `reloj_utc` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `reloj_utc`;

-- Volcando estructura para tabla reloj_utc.hora_central
CREATE TABLE IF NOT EXISTS `hora_central` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hora_previa` datetime DEFAULT NULL,
  `hora_utc` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc.hora_central: ~6 rows (aproximadamente)
DELETE FROM `hora_central`;
/*!40000 ALTER TABLE `hora_central` DISABLE KEYS */;
INSERT INTO `hora_central` (`id`, `hora_previa`, `hora_utc`) VALUES
	(1, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(2, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(3, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(4, '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
	(5, '2019-10-14 18:13:09', '0000-00-00 00:00:00'),
	(6, '2019-10-14 02:00:09', '0000-00-00 00:00:00'),
	(7, '2019-10-14 18:57:06', '2019-10-14 20:31:50'),
	(8, '2019-10-14 18:57:58', '2019-10-14 20:32:43'),
	(9, '2019-10-14 10:06:32', '2019-10-14 20:34:15'),
	(10, '2019-10-14 10:07:27', '2019-10-14 20:35:10'),
	(11, '2019-10-14 10:18:01', '2019-10-14 20:37:08'),
	(12, '2019-10-14 10:18:04', '2019-10-14 20:37:10'),
	(13, '2019-10-14 10:18:06', '2019-10-14 20:37:13'),
	(14, '2019-10-14 10:18:08', '2019-10-14 20:37:15'),
	(15, '2019-10-14 10:18:10', '2019-10-14 20:37:17'),
	(16, '2019-10-14 10:18:46', '2019-10-14 20:37:53'),
	(17, '2019-10-14 09:13:50', '2019-10-14 20:42:32'),
	(18, '2019-10-14 09:13:51', '2019-10-14 20:42:33'),
	(19, '2019-10-14 09:14:02', '2019-10-14 20:42:45'),
	(20, '2019-10-14 09:14:14', '2019-10-14 20:42:56'),
	(21, '2019-10-14 09:14:25', '2019-10-14 20:43:07'),
	(22, '2019-10-14 09:14:36', '2019-10-14 20:43:18'),
	(23, '2019-10-14 09:14:47', '2019-10-14 20:43:30'),
	(24, '2019-10-14 09:14:59', '2019-10-14 20:43:41'),
	(25, '2019-10-14 09:15:10', '2019-10-14 20:43:52'),
	(26, '2019-10-14 09:05:39', '2019-10-14 20:48:07'),
	(27, '2019-10-14 09:05:40', '2019-10-14 20:48:07'),
	(28, '2019-10-14 09:05:50', '2019-10-14 20:48:18'),
	(29, '2019-10-14 09:05:51', '2019-10-14 20:48:18'),
	(30, '2019-10-14 09:06:02', '2019-10-14 20:48:29'),
	(31, '2019-10-14 09:06:02', '2019-10-14 20:48:30'),
	(32, '2019-10-14 09:06:13', '2019-10-14 20:48:40'),
	(33, '2019-10-14 09:06:13', '2019-10-14 20:48:41'),
	(34, '2019-10-14 11:45:10', '2019-10-14 20:48:47'),
	(35, '2019-10-14 11:45:11', '2019-10-14 20:48:47'),
	(36, '2019-10-14 11:45:22', '2019-10-14 20:48:58'),
	(37, '2019-10-14 11:45:22', '2019-10-14 20:48:58'),
	(38, '2019-10-14 11:45:33', '2019-10-14 20:49:09'),
	(39, '2019-10-14 11:45:33', '2019-10-14 20:49:10'),
	(40, '2019-10-14 11:45:44', '2019-10-14 20:49:21'),
	(41, '2019-10-14 11:45:44', '2019-10-14 20:49:21'),
	(42, '2019-10-14 11:45:55', '2019-10-14 20:49:32'),
	(43, '2019-10-14 11:45:56', '2019-10-14 20:49:32'),
	(44, '2019-10-14 11:46:06', '2019-10-14 20:49:43'),
	(45, '2019-10-14 11:46:07', '2019-10-14 20:49:44'),
	(46, '2019-10-14 11:46:18', '2019-10-14 20:49:54'),
	(47, '2019-10-14 11:46:18', '2019-10-14 20:49:55'),
	(48, '2019-10-14 11:46:29', '2019-10-14 20:50:06'),
	(49, '2019-10-14 11:46:29', '2019-10-14 20:50:06'),
	(50, '2019-10-14 11:46:40', '2019-10-14 20:50:17'),
	(51, '2019-10-14 11:46:40', '2019-10-14 20:50:17'),
	(52, '2019-10-14 11:46:51', '2019-10-14 20:50:28'),
	(53, '2019-10-14 11:46:52', '2019-10-14 20:50:28'),
	(54, '2019-10-14 11:47:02', '2019-10-14 20:50:39'),
	(55, '2019-10-14 11:47:03', '2019-10-14 20:50:40'),
	(56, '2019-10-14 11:47:14', '2019-10-14 20:50:51'),
	(57, '2019-10-14 11:47:14', '2019-10-14 20:50:51'),
	(58, '2019-10-14 11:47:25', '2019-10-14 20:51:02'),
	(59, '2019-10-14 11:47:25', '2019-10-14 20:51:02'),
	(60, '2019-10-14 11:47:36', '2019-10-14 20:51:13'),
	(61, '2019-10-14 11:47:36', '2019-10-14 20:51:13'),
	(62, '2019-10-14 11:47:47', '2019-10-14 20:51:24'),
	(63, '2019-10-14 11:47:48', '2019-10-14 20:51:25'),
	(64, '2019-10-14 11:47:59', '2019-10-14 20:51:35'),
	(65, '2019-10-14 11:47:59', '2019-10-14 20:51:36'),
	(66, '2019-10-14 11:48:10', '2019-10-14 20:51:47'),
	(67, '2019-10-14 11:48:10', '2019-10-14 20:51:47'),
	(68, '2019-10-14 11:48:21', '2019-10-14 20:51:58'),
	(69, '2019-10-14 11:48:21', '2019-10-14 20:51:58'),
	(70, '2019-10-14 11:48:32', '2019-10-14 20:52:09'),
	(71, '2019-10-14 11:48:32', '2019-10-14 20:52:09'),
	(72, '2019-10-14 11:48:43', '2019-10-14 20:52:20'),
	(73, '2019-10-14 11:48:44', '2019-10-14 20:52:21'),
	(74, '2019-10-14 11:48:55', '2019-10-14 20:52:32'),
	(75, '2019-10-14 11:48:55', '2019-10-14 20:52:32'),
	(76, '2019-10-14 11:49:06', '2019-10-14 20:52:43'),
	(77, '2019-10-14 11:49:06', '2019-10-14 20:52:43'),
	(78, '2019-10-14 11:49:17', '2019-10-14 20:52:54'),
	(79, '2019-10-14 11:49:17', '2019-10-14 20:52:54'),
	(80, '2019-10-14 11:49:28', '2019-10-14 20:53:05'),
	(81, '2019-10-14 11:49:28', '2019-10-14 20:53:05'),
	(82, '2019-10-14 11:49:39', '2019-10-14 20:53:17'),
	(83, '2019-10-14 11:49:40', '2019-10-14 20:53:17'),
	(84, '2019-10-14 11:49:51', '2019-10-14 20:53:28'),
	(85, '2019-10-14 11:49:51', '2019-10-14 20:53:28'),
	(86, '2019-10-14 11:50:02', '2019-10-14 20:53:39'),
	(87, '2019-10-14 11:50:02', '2019-10-14 20:53:39'),
	(88, '2019-10-14 11:50:13', '2019-10-14 20:53:50'),
	(89, '2019-10-14 11:50:13', '2019-10-14 20:53:50'),
	(90, '2019-10-14 11:50:24', '2019-10-14 20:54:01'),
	(91, '2019-10-14 11:50:24', '2019-10-14 20:54:01'),
	(92, '2019-10-14 11:50:35', '2019-10-14 20:54:13'),
	(93, '2019-10-14 11:50:36', '2019-10-14 20:54:13'),
	(94, '2019-10-14 11:50:47', '2019-10-14 20:54:24'),
	(95, '2019-10-14 11:50:47', '2019-10-14 20:54:24'),
	(96, '2019-10-14 11:50:58', '2019-10-14 20:54:35'),
	(97, '2019-10-14 11:50:58', '2019-10-14 20:54:35'),
	(98, '2019-10-14 11:51:09', '2019-10-14 20:54:46'),
	(99, '2019-10-14 11:51:09', '2019-10-14 20:54:46'),
	(100, '2019-10-14 11:51:20', '2019-10-14 20:54:57'),
	(101, '2019-10-14 11:51:20', '2019-10-14 20:54:57'),
	(102, '2019-10-14 11:51:31', '2019-10-14 20:55:09'),
	(103, '2019-10-14 11:51:32', '2019-10-14 20:55:09'),
	(104, '2019-10-14 11:51:43', '2019-10-14 20:55:20'),
	(105, '2019-10-14 11:51:43', '2019-10-14 20:55:20'),
	(106, '2019-10-14 11:51:54', '2019-10-14 20:55:31'),
	(107, '2019-10-14 11:51:54', '2019-10-14 20:55:31'),
	(108, '2019-10-14 11:52:05', '2019-10-14 20:55:42'),
	(109, '2019-10-14 11:52:05', '2019-10-14 20:55:42'),
	(110, '2019-10-14 11:52:16', '2019-10-14 20:55:53'),
	(111, '2019-10-14 11:52:16', '2019-10-14 20:55:53'),
	(112, '2019-10-14 11:52:27', '2019-10-14 20:56:04'),
	(113, '2019-10-14 11:52:27', '2019-10-14 20:56:04'),
	(114, '2019-10-14 11:52:38', '2019-10-14 20:56:16'),
	(115, '2019-10-14 11:52:38', '2019-10-14 20:56:16'),
	(116, '2019-10-14 11:52:49', '2019-10-14 20:56:27'),
	(117, '2019-10-14 11:52:49', '2019-10-14 20:56:27'),
	(118, '2019-10-14 11:53:00', '2019-10-14 20:56:38'),
	(119, '2019-10-14 11:53:00', '2019-10-14 20:56:38'),
	(120, '2019-10-14 11:53:12', '2019-10-14 20:56:49'),
	(121, '2019-10-14 11:53:12', '2019-10-14 20:56:49'),
	(122, '2019-10-14 11:53:23', '2019-10-14 20:57:00'),
	(123, '2019-10-14 11:53:23', '2019-10-14 20:57:00'),
	(124, '2019-10-14 11:53:34', '2019-10-14 20:57:11'),
	(125, '2019-10-14 11:53:34', '2019-10-14 20:57:11'),
	(126, '2019-10-14 11:53:45', '2019-10-14 20:57:22'),
	(127, '2019-10-14 11:53:45', '2019-10-14 20:57:22'),
	(128, '2019-10-14 11:53:56', '2019-10-14 20:57:33'),
	(129, '2019-10-14 11:53:56', '2019-10-14 20:57:33'),
	(130, '2019-10-14 11:54:07', '2019-10-14 20:57:44'),
	(131, '2019-10-14 11:54:07', '2019-10-14 20:57:44'),
	(132, '2019-10-14 11:54:18', '2019-10-14 20:57:55'),
	(133, '2019-10-14 11:54:18', '2019-10-14 20:57:55'),
	(134, '2019-10-14 11:54:29', '2019-10-14 20:58:06'),
	(135, '2019-10-14 11:54:29', '2019-10-14 20:58:06'),
	(136, '2019-10-14 11:54:40', '2019-10-14 20:58:18'),
	(137, '2019-10-14 11:54:40', '2019-10-14 20:58:18'),
	(138, '2019-10-14 11:54:51', '2019-10-14 20:58:29'),
	(139, '2019-10-14 11:54:51', '2019-10-14 20:58:29'),
	(140, '2019-10-14 11:55:03', '2019-10-14 20:58:40'),
	(141, '2019-10-14 11:55:03', '2019-10-14 20:58:40'),
	(142, '2019-10-14 11:55:14', '2019-10-14 20:58:51'),
	(143, '2019-10-14 11:55:14', '2019-10-14 20:58:51'),
	(144, '2019-10-14 11:55:25', '2019-10-14 20:59:03'),
	(145, '2019-10-14 11:55:25', '2019-10-14 20:59:03'),
	(146, '2019-10-14 11:55:36', '2019-10-14 20:59:14'),
	(147, '2019-10-14 11:55:36', '2019-10-14 20:59:14'),
	(148, '2019-10-14 11:55:48', '2019-10-14 20:59:25'),
	(149, '2019-10-14 11:55:48', '2019-10-14 20:59:25'),
	(150, '2019-10-14 11:55:59', '2019-10-14 20:59:36'),
	(151, '2019-10-14 11:55:59', '2019-10-14 20:59:36'),
	(152, '2019-10-14 11:56:10', '2019-10-14 20:59:48'),
	(153, '2019-10-14 11:56:10', '2019-10-14 20:59:48'),
	(154, '2019-10-14 11:56:21', '2019-10-14 20:59:59'),
	(155, '2019-10-14 11:56:21', '2019-10-14 20:59:59'),
	(156, '2019-10-14 11:56:33', '2019-10-14 21:00:10'),
	(157, '2019-10-14 11:56:33', '2019-10-14 21:00:10'),
	(158, '2019-10-14 21:05:52', '2019-10-14 21:05:51'),
	(159, '2019-10-14 21:05:52', '2019-10-14 21:05:52'),
	(160, '2019-10-14 19:30:03', '2019-10-14 21:06:02'),
	(161, '2019-10-14 19:30:04', '2019-10-14 21:06:03'),
	(162, '2019-10-14 19:30:14', '2019-10-14 21:06:13'),
	(163, '2019-10-14 19:30:15', '2019-10-14 21:06:14'),
	(164, '2019-10-14 21:06:26', '2019-10-14 21:06:24'),
	(165, '2019-10-14 21:06:27', '2019-10-14 21:06:25'),
	(166, '2019-10-14 20:07:37', '2019-10-14 21:06:35'),
	(167, '2019-10-14 20:07:38', '2019-10-14 21:06:36'),
	(168, '2019-10-14 21:07:48', '2019-10-14 21:06:46'),
	(169, '2019-10-14 21:07:49', '2019-10-14 21:06:47'),
	(170, '2019-10-14 21:06:59', '2019-10-14 21:06:57'),
	(171, '2019-10-14 21:07:00', '2019-10-14 21:06:58'),
	(172, '2019-10-14 21:07:10', '2019-10-14 21:07:08'),
	(173, '2019-10-14 21:07:11', '2019-10-14 21:07:09'),
	(174, '2019-10-14 21:08:21', '2019-10-14 21:07:19'),
	(175, '2019-10-14 21:08:22', '2019-10-14 21:07:20'),
	(176, '2019-10-14 21:07:31', '2019-10-14 21:07:30'),
	(177, '2019-10-14 21:07:32', '2019-10-14 21:07:31'),
	(178, '2019-10-14 21:07:42', '2019-10-14 21:07:41'),
	(179, '2019-10-14 21:07:43', '2019-10-14 21:07:42'),
	(180, '2019-10-14 21:07:53', '2019-10-14 21:07:52'),
	(181, '2019-10-14 21:07:54', '2019-10-14 21:07:53'),
	(182, '2019-10-14 21:08:04', '2019-10-14 21:08:03'),
	(183, '2019-10-14 21:08:05', '2019-10-14 21:08:04'),
	(184, '2019-10-14 21:09:15', '2019-10-14 21:08:15'),
	(185, '2019-10-14 21:09:16', '2019-10-14 21:08:15'),
	(186, '2019-10-14 21:08:27', '2019-10-14 21:08:26'),
	(187, '2019-10-14 21:08:28', '2019-10-14 21:08:26'),
	(188, '2019-10-14 21:08:38', '2019-10-14 21:08:37'),
	(189, '2019-10-14 21:08:39', '2019-10-14 21:08:37'),
	(190, '2019-10-14 21:09:44', '2019-10-14 21:09:43'),
	(191, '2019-10-14 21:09:55', '2019-10-14 21:09:54'),
	(192, '2019-10-14 21:10:06', '2019-10-14 21:10:05'),
	(193, '2019-10-14 21:11:18', '2019-10-14 21:10:16'),
	(194, '2019-10-14 19:33:29', '2019-10-14 21:10:27'),
	(195, '2019-10-14 19:33:40', '2019-10-14 21:10:38'),
	(196, '2019-10-14 21:10:51', '2019-10-14 21:10:49'),
	(197, '2019-10-14 21:11:04', '2019-10-14 21:11:03'),
	(198, '2019-10-14 21:11:15', '2019-10-14 21:11:14'),
	(199, '2019-10-14 19:29:26', '2019-10-14 21:11:25'),
	(200, '2019-10-14 21:11:38', '2019-10-14 21:11:36'),
	(201, '2019-10-14 21:11:49', '2019-10-14 21:11:47'),
	(202, '2019-10-14 21:12:00', '2019-10-14 21:11:58'),
	(203, '2019-10-14 21:12:11', '2019-10-14 21:12:09'),
	(204, '2019-10-14 21:12:22', '2019-10-14 21:12:20'),
	(205, '2019-10-14 21:12:33', '2019-10-14 21:12:31'),
	(206, '2019-10-14 21:12:44', '2019-10-14 21:12:42'),
	(207, '2019-10-14 21:12:55', '2019-10-14 21:12:53'),
	(208, '2019-10-14 21:13:11', '2019-10-14 21:13:09'),
	(209, '2019-10-14 21:13:22', '2019-10-14 21:13:20'),
	(210, '2019-10-14 19:29:33', '2019-10-14 21:13:31'),
	(211, '2019-10-14 21:13:50', '2019-10-14 21:13:48'),
	(212, '2019-10-14 21:14:01', '2019-10-14 21:13:59'),
	(213, '2019-10-14 21:14:12', '2019-10-14 21:14:10'),
	(214, '2019-10-14 21:14:23', '2019-10-14 21:14:21'),
	(215, '2019-10-14 21:14:34', '2019-10-14 21:14:33'),
	(216, '2019-10-14 21:14:45', '2019-10-14 21:14:44'),
	(217, '2019-10-14 21:14:56', '2019-10-14 21:14:55'),
	(218, '2019-10-14 21:15:07', '2019-10-14 21:15:06'),
	(219, '2019-10-14 21:15:19', '2019-10-14 21:15:17'),
	(220, '2019-10-14 21:15:30', '2019-10-14 21:15:28'),
	(221, '2019-10-14 21:15:41', '2019-10-14 21:15:39'),
	(222, '2019-10-14 21:15:52', '2019-10-14 21:15:50'),
	(223, '2019-10-14 21:16:03', '2019-10-14 21:16:01'),
	(224, '2019-10-14 21:16:13', '2019-10-14 21:16:12'),
	(225, '2019-10-14 21:16:24', '2019-10-14 21:16:23'),
	(226, '2019-10-14 21:16:35', '2019-10-14 21:16:34'),
	(227, '2019-10-14 21:16:46', '2019-10-14 21:16:45'),
	(228, '2019-10-14 21:16:57', '2019-10-14 21:16:56'),
	(229, '2019-10-14 21:17:08', '2019-10-14 21:17:07'),
	(230, '2019-10-14 21:17:21', '2019-10-14 21:17:18'),
	(231, '2019-10-14 21:17:32', '2019-10-14 21:17:29'),
	(232, '2019-10-14 21:18:23', '2019-10-14 21:18:21'),
	(233, '2019-10-14 21:19:13', '2019-10-14 21:19:12'),
	(234, '2019-10-14 21:19:13', '2019-10-14 21:19:12'),
	(235, '2019-10-14 19:29:24', '2019-10-14 21:19:23'),
	(236, '2019-10-14 19:29:25', '2019-10-14 21:19:23'),
	(237, '2019-10-14 19:29:35', '2019-10-14 21:19:34'),
	(238, '2019-10-14 19:29:36', '2019-10-14 21:19:34'),
	(239, '2019-10-14 21:19:46', '2019-10-14 21:19:45'),
	(240, '2019-10-14 21:19:47', '2019-10-14 21:19:45'),
	(241, '2019-10-14 21:19:57', '2019-10-14 21:19:56'),
	(242, '2019-10-14 21:19:58', '2019-10-14 21:19:56'),
	(243, '2019-10-14 21:20:08', '2019-10-14 21:20:07'),
	(244, '2019-10-14 21:20:09', '2019-10-14 21:20:07'),
	(245, '2019-10-14 21:20:19', '2019-10-14 21:20:18'),
	(246, '2019-10-14 21:20:20', '2019-10-14 21:20:18'),
	(247, '2019-10-14 21:20:30', '2019-10-14 21:20:29'),
	(248, '2019-10-14 21:20:31', '2019-10-14 21:20:29'),
	(249, '2019-10-14 21:20:41', '2019-10-14 21:20:40'),
	(250, '2019-10-14 21:20:42', '2019-10-14 21:20:40'),
	(251, '2019-10-14 21:20:52', '2019-10-14 21:20:51'),
	(252, '2019-10-14 21:20:53', '2019-10-14 21:20:52'),
	(253, '2019-10-14 21:21:03', '2019-10-14 21:21:02'),
	(254, '2019-10-14 21:21:04', '2019-10-14 21:21:03'),
	(255, '2019-10-14 21:21:14', '2019-10-14 21:21:13'),
	(256, '2019-10-14 21:21:15', '2019-10-14 21:21:14'),
	(257, '2019-10-14 21:21:25', '2019-10-14 21:21:24'),
	(258, '2019-10-14 21:21:26', '2019-10-14 21:21:25'),
	(259, '2019-10-14 20:20:36', '2019-10-14 21:21:35'),
	(260, '2019-10-14 20:20:37', '2019-10-14 21:21:36'),
	(261, '2019-10-14 21:21:47', '2019-10-14 21:21:46'),
	(262, '2019-10-14 21:21:48', '2019-10-14 21:21:47'),
	(263, '2019-10-14 21:21:58', '2019-10-14 21:21:57'),
	(264, '2019-10-14 21:21:59', '2019-10-14 21:21:58'),
	(265, '2019-10-14 21:22:09', '2019-10-14 21:22:08'),
	(266, '2019-10-14 21:22:10', '2019-10-14 21:22:09'),
	(267, '2019-10-14 21:22:21', '2019-10-14 21:22:19'),
	(268, '2019-10-14 21:22:22', '2019-10-14 21:22:20'),
	(269, '2019-10-14 21:22:36', '2019-10-14 21:22:34'),
	(270, '2019-10-14 21:22:47', '2019-10-14 21:22:45'),
	(271, '2019-10-14 21:22:58', '2019-10-14 21:22:56'),
	(272, '2019-10-14 21:23:09', '2019-10-14 21:23:07'),
	(273, '2019-10-14 21:23:20', '2019-10-14 21:23:18'),
	(274, '2019-10-14 21:23:31', '2019-10-14 21:23:29'),
	(275, '2019-10-14 21:23:42', '2019-10-14 21:23:40'),
	(276, '2019-10-14 21:37:53', '2019-10-14 21:23:51'),
	(277, '2019-10-14 21:38:04', '2019-10-14 21:24:02'),
	(278, '2019-10-14 22:29:15', '2019-10-14 21:24:13'),
	(279, '2019-10-14 22:29:26', '2019-10-14 21:24:24'),
	(280, '2019-10-14 21:24:38', '2019-10-14 21:24:35'),
	(281, '2019-10-14 21:24:49', '2019-10-14 21:24:46'),
	(282, '2019-10-14 21:25:00', '2019-10-14 21:24:58'),
	(283, '2019-10-14 21:25:14', '2019-10-14 21:25:13'),
	(284, '2019-10-14 21:25:26', '2019-10-14 21:25:25'),
	(285, '2019-10-14 19:29:37', '2019-10-14 21:25:36'),
	(286, '2019-10-14 21:25:48', '2019-10-14 21:25:47'),
	(287, '2019-10-14 22:29:59', '2019-10-14 21:25:58'),
	(288, '2019-10-14 22:30:10', '2019-10-14 21:26:09'),
	(289, '2019-10-14 21:26:21', '2019-10-14 21:26:20'),
	(290, '2019-10-14 22:39:32', '2019-10-14 21:26:31'),
	(291, '2019-10-14 22:39:43', '2019-10-14 21:26:42'),
	(292, '2019-10-14 21:26:54', '2019-10-14 21:26:53'),
	(293, '2019-10-14 21:27:05', '2019-10-14 21:27:04'),
	(294, '2019-10-14 21:27:17', '2019-10-14 21:27:15');
/*!40000 ALTER TABLE `hora_central` ENABLE KEYS */;

-- Volcando estructura para tabla reloj_utc.hora_servidores
CREATE TABLE IF NOT EXISTS `hora_servidores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idHoraCentral` int(11) DEFAULT NULL,
  `idServidor` int(11) DEFAULT NULL,
  `ajuste` double DEFAULT NULL,
  `ralentizar` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_hora_servidores_hora_central` (`idHoraCentral`),
  KEY `FK_hora_servidores_servidores` (`idServidor`),
  CONSTRAINT `FK_hora_servidores_hora_central` FOREIGN KEY (`idHoraCentral`) REFERENCES `hora_central` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_hora_servidores_servidores` FOREIGN KEY (`idServidor`) REFERENCES `servidores` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc.hora_servidores: ~4 rows (aproximadamente)
DELETE FROM `hora_servidores`;
/*!40000 ALTER TABLE `hora_servidores` DISABLE KEYS */;
INSERT INTO `hora_servidores` (`id`, `idHoraCentral`, `idServidor`, `ajuste`, `ralentizar`) VALUES
	(1, 1, 1, 0.7121452088775635, 1),
	(4, 4, 1, 0.8894298444519043, 1),
	(5, 5, 1, 0.9382187415924073, 1),
	(6, 6, 1, 0.8129221043395995, 1),
	(7, 7, 1, 0.8150927807006836, 1),
	(8, 8, 1, 0.9488426918792725, 6),
	(9, 9, 1, 0.8231025019531251, 6),
	(10, 10, 1, 0.8630220848693848, 6),
	(11, 11, 1, 0.8745747214050292, 6),
	(12, 12, 1, 0.90647177444458, 6),
	(13, 13, 1, 0.76940601902771, 6),
	(14, 14, 1, 0.7823228164520264, 6),
	(15, 15, 1, 0.7672076260223388, 6),
	(16, 16, 1, 0.7821605357666015, 1),
	(17, 17, 1, 0.9450878260650635, 6),
	(18, 18, 1, 0.8215439614562988, 6),
	(19, 19, 1, 0.8259574314727783, 6),
	(20, 20, 1, 1.0889072027130127, 6),
	(21, 21, 1, 0.8494684536285401, 6),
	(22, 22, 1, 0.8305157140655517, 6),
	(23, 23, 1, 0.820921929977417, 6),
	(24, 24, 1, 0.821057802810669, 6),
	(25, 25, 1, 0.8259667616424561, 1),
	(26, 26, 1, 0.9485838892059326, 1),
	(27, 27, 1, 0.8259608086090088, 1),
	(28, 28, 1, 0.8602870943603516, 1),
	(29, 29, 1, 0.8281147285461425, 1),
	(30, 30, 1, 0.8406689741363526, 1),
	(31, 31, 1, 0.8284805485382081, 1),
	(32, 32, 1, 0.8342572721252441, 1),
	(33, 33, 1, 0.8300862845916748, 1),
	(34, 34, 1, 1.1163544409332276, 1),
	(35, 35, 1, 0.8329314630584717, 1),
	(36, 36, 1, 0.8291158176269531, 1),
	(37, 37, 1, 0.8299640825653076, 1),
	(38, 38, 1, 0.8352156692962647, 1),
	(39, 39, 1, 0.8321763303070069, 1),
	(40, 40, 1, 0.8256689040985108, 1),
	(41, 41, 1, 0.8252702241210937, 1),
	(42, 42, 1, 0.8440137606506348, 1),
	(43, 43, 1, 1.0951019887847901, 1),
	(44, 44, 1, 0.8541689070129395, 1),
	(45, 45, 1, 0.8301840246124268, 1),
	(46, 46, 1, 0.8490874826660156, 1),
	(47, 47, 1, 0.854927790725708, 1),
	(48, 48, 1, 0.856730196762085, 1),
	(49, 49, 1, 0.8428626269836426, 1),
	(50, 50, 1, 0.8316508438873291, 1),
	(51, 51, 1, 0.8285936524047852, 1),
	(52, 52, 1, 0.8351048248291015, 1),
	(53, 53, 1, 0.8408782568817139, 1),
	(54, 54, 1, 0.9719820288085937, 1),
	(55, 55, 1, 0.8571546680297851, 1),
	(56, 56, 1, 0.8757510039062499, 1),
	(57, 57, 1, 0.8600365085601807, 1),
	(58, 58, 1, 0.8636332302246094, 1),
	(59, 59, 1, 0.8690247875976562, 1),
	(60, 60, 1, 0.8566189708404541, 1),
	(61, 61, 1, 0.8715567803344726, 1),
	(62, 62, 1, 0.895988591003418, 1),
	(63, 63, 1, 0.860897457321167, 1),
	(64, 64, 1, 0.8626023050994873, 1),
	(65, 65, 1, 0.8597848496551513, 1),
	(66, 66, 1, 0.8596401407775879, 1),
	(67, 67, 1, 0.8595927100372315, 1),
	(68, 68, 1, 0.9013253113250732, 1),
	(69, 69, 1, 0.8577576315155029, 1),
	(70, 70, 1, 0.8609729335784913, 1),
	(71, 71, 1, 0.8560840390472412, 1),
	(72, 72, 1, 0.8659464009704589, 1),
	(73, 73, 1, 0.8582021579742432, 1),
	(74, 74, 1, 0.892787555633545, 1),
	(75, 75, 1, 0.859633915435791, 1),
	(76, 76, 1, 0.8702549162597656, 1),
	(77, 77, 1, 0.8629769564361572, 1),
	(78, 78, 1, 0.8624900883483887, 1),
	(79, 79, 1, 0.8621868604278564, 1),
	(80, 80, 1, 0.8602324588928223, 1),
	(81, 81, 1, 0.8606876970825195, 1),
	(82, 82, 1, 0.9529840035247803, 1),
	(83, 83, 1, 0.837494208694458, 1),
	(84, 84, 1, 0.8371718466033935, 1),
	(85, 85, 1, 0.8330522904815674, 1),
	(86, 86, 1, 0.833978208908081, 1),
	(87, 87, 1, 0.8567625177459717, 1),
	(88, 88, 1, 0.8346257787017822, 1),
	(89, 89, 1, 0.8595575975189209, 1),
	(90, 90, 1, 0.851872145111084, 1),
	(91, 91, 1, 0.8503307612304687, 1),
	(92, 92, 1, 0.8963978817596435, 1),
	(93, 93, 1, 0.8648417041473389, 1),
	(94, 94, 1, 0.8375840532684327, 1),
	(95, 95, 1, 0.8412852767791748, 1),
	(96, 96, 1, 0.8357354093322754, 1),
	(97, 97, 1, 0.8352895439300537, 1),
	(98, 98, 1, 0.8345741266632081, 1),
	(99, 99, 1, 0.8363279980010987, 1),
	(100, 100, 1, 0.8348632392425537, 1),
	(101, 101, 1, 0.832817151977539, 1),
	(102, 102, 1, 0.8645858613433838, 1),
	(103, 103, 1, 0.8952157118530273, 1),
	(104, 104, 1, 0.8581266977539063, 1),
	(105, 105, 1, 0.8371296615142823, 1),
	(106, 106, 1, 0.8351152448883057, 1),
	(107, 107, 1, 0.8399018108062744, 1),
	(108, 108, 1, 0.8441511823883057, 1),
	(109, 109, 1, 0.8394047109985352, 1),
	(110, 110, 1, 0.8610617950286865, 1),
	(111, 111, 1, 0.7397045832824707, 1),
	(112, 112, 1, 0.7484573865509033, 1),
	(113, 113, 1, 0.7412968090515136, 1),
	(114, 115, 1, 0.7423336671752929, 1),
	(115, 115, 1, 0.7481809008789062, 1),
	(116, 116, 1, 0.7379170167541504, 1),
	(117, 117, 1, 0.7346170809783935, 1),
	(118, 118, 1, 0.7580015471038818, 1),
	(119, 119, 1, 0.7521881332092285, 1),
	(120, 120, 1, 0.7398039055023193, 1),
	(121, 121, 1, 0.7450921086425781, 1),
	(122, 122, 1, 0.7490828252868652, 1),
	(123, 123, 1, 0.7537251921386718, 1),
	(124, 124, 1, 0.737598966369629, 1),
	(125, 125, 1, 0.7360573570251465, 1),
	(126, 126, 1, 0.7369695235443116, 1),
	(127, 127, 1, 0.7433668493957519, 1),
	(128, 129, 1, 0.7417376820526123, 1),
	(129, 129, 1, 0.7435784221343994, 1),
	(130, 131, 1, 0.7425372180480957, 1),
	(131, 131, 1, 0.7473617924041748, 1),
	(132, 132, 1, 0.7437527566223144, 1),
	(133, 133, 1, 0.7487533668518066, 1),
	(134, 134, 1, 0.7424021475372314, 1),
	(135, 135, 1, 0.7506541428985596, 1),
	(136, 136, 1, 0.7417373163299561, 1),
	(137, 137, 1, 0.7417001392211914, 1),
	(138, 138, 1, 0.9698743665924072, 1),
	(139, 139, 1, 0.972446027923584, 1),
	(140, 141, 1, 0.9413403985595703, 1),
	(141, 141, 1, 0.9332317438659667, 1),
	(142, 142, 1, 0.9014388029174805, 1),
	(143, 143, 1, 0.9096370990600586, 1),
	(144, 144, 1, 0.8897673492584228, 1),
	(145, 145, 1, 0.8861740000762939, 1),
	(146, 147, 1, 0.8816485682373048, 1),
	(147, 147, 1, 0.8899738798980713, 1),
	(148, 148, 1, 0.8705068134002686, 1),
	(149, 149, 1, 0.8680898457641602, 1),
	(150, 151, 1, 0.8895852543182373, 1),
	(151, 151, 1, 0.9072672211151123, 1),
	(152, 152, 1, 0.8751947317810058, 1),
	(153, 153, 1, 0.8875436583404541, 1),
	(154, 154, 1, 0.9066180689086913, 1),
	(155, 155, 1, 0.8770061165313721, 1),
	(156, 156, 1, 0.8762787436676025, 1),
	(157, 157, 1, 0.8723025256195068, 1),
	(158, 158, 1, 0.0225015, 6),
	(159, 159, 1, 0.012003, 1),
	(160, 160, 1, 0.007503, 6),
	(161, 161, 1, 0.0074985, 1),
	(162, 162, 1, 0.009006, 6),
	(163, 163, 1, 0.0075, 1),
	(164, 164, 1, 0.008997, 6),
	(165, 165, 1, 0.0089985, 1),
	(166, 166, 1, 0.008997, 6),
	(167, 167, 1, 0.00903, 1),
	(168, 168, 1, 0.009, 6),
	(169, 169, 1, 0.0075015, 1),
	(170, 170, 1, 0.0090015, 6),
	(171, 171, 1, 0.0074835, 1),
	(172, 172, 1, 0.0089985, 6),
	(173, 173, 1, 0.007551, 1),
	(174, 174, 1, 0.010497, 6),
	(175, 175, 1, 0.0090015, 1),
	(176, 176, 1, 0.0179955, 6),
	(177, 177, 1, 0.0074985, 1),
	(178, 178, 1, 0.0090015, 6),
	(179, 179, 1, 0.0075015, 1),
	(180, 180, 1, 0.0090015, 6),
	(181, 181, 1, 0.009003, 1),
	(182, 182, 1, 0.021003, 6),
	(183, 183, 1, 0.007452, 1),
	(184, 184, 1, 0.007452, 6),
	(185, 185, 1, 0.012, 1),
	(186, 186, 1, 0.0090015, 6),
	(187, 187, 1, 0.009, 1),
	(188, 188, 1, 0.017997, 6),
	(189, 189, 1, 0.011997, 1),
	(190, 190, 1, 0.0239955, 1),
	(191, 191, 1, 0.008955, 1),
	(192, 192, 1, 0.0104985, 1),
	(193, 193, 1, 0.008958, 1),
	(194, 194, 1, 0.0089775, 1),
	(195, 195, 1, 0.0134985, 1),
	(196, 196, 1, 0.0105015, 1),
	(197, 197, 1, 0.0164985, 1),
	(198, 198, 1, 0.0090015, 1),
	(199, 199, 1, 0.007455, 1),
	(200, 200, 1, 0.0105045, 1),
	(201, 201, 1, 0.009, 1),
	(202, 202, 1, 0.0090015, 1),
	(203, 203, 1, 0.0075, 1),
	(204, 204, 1, 0.0089985, 1),
	(205, 205, 1, 0.0104985, 1),
	(206, 206, 1, 0.0089985, 1),
	(207, 207, 1, 0.016455, 1),
	(208, 208, 1, 0.0194985, 1),
	(209, 209, 1, 0.008949, 1),
	(210, 210, 1, 0.0089535, 1),
	(211, 211, 1, 0.009003, 1),
	(212, 212, 1, 0.009, 1),
	(213, 213, 1, 0.0104985, 1),
	(214, 214, 1, 0.008997, 1),
	(215, 215, 1, 0.0105075, 1),
	(216, 216, 1, 0.0089745, 1),
	(217, 217, 1, 0.0074475, 1),
	(218, 218, 1, 0.0104985, 1),
	(219, 219, 1, 0.016497, 1),
	(220, 220, 1, 0.0449985, 1),
	(221, 221, 1, 0.0090015, 1),
	(222, 222, 1, 0.0075, 1),
	(223, 223, 1, 0.0135, 1),
	(224, 224, 1, 0.0089985, 1),
	(225, 225, 1, 0.0075, 1),
	(226, 226, 1, 0.0074985, 1),
	(227, 227, 1, 0.011997, 1),
	(228, 228, 1, 0.0120015, 1),
	(229, 229, 1, 0.0104985, 1),
	(230, 230, 1, 0.0104535, 1),
	(231, 231, 1, 0.0090015, 1),
	(232, 232, 1, 0.015, 1),
	(233, 233, 1, 0.0119985, 1),
	(234, 234, 1, 0.0075, 1),
	(235, 235, 1, 0.009, 6),
	(236, 236, 1, 0.007497, 6),
	(237, 237, 1, 0.0074955, 1),
	(238, 238, 1, 0.009, 1),
	(239, 239, 1, 0.0135, 1),
	(240, 240, 1, 0.007452, 1),
	(241, 241, 1, 0.010497, 1),
	(242, 242, 1, 0.0074535, 6),
	(243, 243, 1, 0.0074985, 6),
	(244, 244, 1, 0.008496, 6),
	(245, 245, 1, 0.007503, 6),
	(246, 246, 1, 0.0074505, 6),
	(247, 247, 1, 0.0075, 6),
	(248, 248, 1, 0.0089535, 6),
	(249, 249, 1, 0.0085, 6),
	(250, 250, 1, 0.0074985, 6),
	(251, 251, 1, 0.009003, 6),
	(252, 252, 1, 0.010497, 6),
	(253, 253, 1, 0.0329955, 6),
	(254, 254, 1, 0.007455, 6),
	(255, 255, 1, 0.0089985, 6),
	(256, 256, 1, 0.0104535, 6),
	(257, 257, 1, 0.009003, 6),
	(258, 258, 1, 0.010497, 6),
	(259, 259, 1, 0.0074955, 6),
	(260, 260, 1, 0.012, 6),
	(261, 261, 1, 0.0075015, 1),
	(262, 262, 1, 0.0105, 1),
	(263, 263, 1, 0.010503, 1),
	(264, 264, 1, 0.0089985, 1),
	(265, 265, 1, 0.0075015, 6),
	(266, 266, 1, 0.007452, 1),
	(267, 267, 1, 0.0090195, 6),
	(268, 268, 1, 0.0090045, 6),
	(269, 269, 1, 0.0270045, 6),
	(270, 270, 1, 0.0089505, 6),
	(271, 271, 1, 0.010497, 6),
	(272, 272, 1, 0.012, 6),
	(273, 273, 1, 0.0089535, 6),
	(274, 274, 1, 0.008982, 6),
	(275, 275, 1, 0.009, 6),
	(276, 276, 1, 0.0105, 6),
	(277, 277, 1, 0.007449, 6),
	(278, 278, 1, 0.008997, 6),
	(279, 279, 1, 0.0104955, 6),
	(280, 280, 1, 0.007452, 6),
	(281, 281, 1, 0.0089535, 1),
	(282, 282, 1, 0.008997, 1),
	(283, 283, 1, 0.0134865, 1),
	(284, 284, 1, 0.013449, 1),
	(285, 285, 1, 0.008961, 6),
	(286, 286, 1, 0.008455, 1),
	(287, 287, 1, 0.007479, 1),
	(288, 288, 1, 0.007524, 6),
	(289, 289, 1, 0.0089985, 6),
	(290, 290, 1, 0.008979, 6),
	(291, 291, 1, 0.0089535, 6),
	(292, 292, 1, 0.0090015, 6),
	(293, 293, 1, 0.008952, 6),
	(294, 294, 1, 0.0135015, 6);
/*!40000 ALTER TABLE `hora_servidores` ENABLE KEYS */;

-- Volcando estructura para tabla reloj_utc.servidores
CREATE TABLE IF NOT EXISTS `servidores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(30) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `latencia` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla reloj_utc.servidores: ~1 rows (aproximadamente)
DELETE FROM `servidores`;
/*!40000 ALTER TABLE `servidores` DISABLE KEYS */;
INSERT INTO `servidores` (`id`, `ip`, `nombre`, `latencia`) VALUES
	(1, '10.100.70.115', 'Server 1', 4500.5);
/*!40000 ALTER TABLE `servidores` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
