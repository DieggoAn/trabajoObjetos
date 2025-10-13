-- ESQUEMA DE LA BASE DE DATOS, VERSION 1.1

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-10-2025 a las 23:01:31
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `backend_proyecto`
--
CREATE DATABASE IF NOT EXISTS `backend_proyecto` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `backend_proyecto`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

DROP TABLE IF EXISTS `departamento`;
CREATE TABLE `departamento` (
  `id_departamento` varchar(15) NOT NULL,
  `nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre`) VALUES
('DEP01', 'Recursos Humanos'),
('DEP02', 'Finanzas'),
('DEP03', 'TI'),
('DEP04', 'Marketing');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

DROP TABLE IF EXISTS `informe`;
CREATE TABLE `informe` (
  `id_informe` varchar(15) NOT NULL,
  `descripcion` text NOT NULL,
  `formato` varchar(45) DEFAULT NULL,
  `fecha` date NOT NULL,
  `rut_usuario` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
CREATE TABLE `proyecto` (
  `id_proyecto` varchar(15) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `id_departamento` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrotiempo`
--

DROP TABLE IF EXISTS `registrotiempo`;
CREATE TABLE `registrotiempo` (
  `id_registro_tiempo` varchar(15) NOT NULL,
  `fecha` date NOT NULL,
  `horas_trabajadas` int(11) NOT NULL,
  `descripcion_tarea` varchar(150) NOT NULL,
  `rut_usuario` varchar(12) NOT NULL,
  `id_proyecto` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `rut_usuario` varchar(12) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellido_paterno` varchar(45) NOT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `fecha_inicio_contrato` date NOT NULL,
  `salario` int(11) NOT NULL,
  `numero_telefonico` varchar(15) NOT NULL,
  `rol` varchar(30) NOT NULL,
  `id_departamento` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`id_informe`),
  ADD KEY `fk_Informe_Usuario1_idx` (`rut_usuario`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `fk_Proyecto_Departamento1_idx` (`id_departamento`);

--
-- Indices de la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  ADD PRIMARY KEY (`id_registro_tiempo`),
  ADD KEY `fk_RegistroTiempo_Usuario1_idx` (`rut_usuario`),
  ADD KEY `fk_RegistroTiempo_Proyecto1_idx` (`id_proyecto`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`rut_usuario`),
  ADD KEY `fk_Usuario_Departamento1_idx` (`id_departamento`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `informe`
--
ALTER TABLE `informe`
  ADD CONSTRAINT `fk_Informe_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD CONSTRAINT `fk_Proyecto_Departamento1` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  ADD CONSTRAINT `fk_RegistroTiempo_Proyecto1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_RegistroTiempo_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_Usuario_Departamento1` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;