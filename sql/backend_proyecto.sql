-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2025 at 02:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;



--
-- Database: `backend_proyecto`
--

-- --------------------------------------------------------
DROP SCHEMA IF EXISTS `backend_proyecto` ;
CREATE SCHEMA IF NOT EXISTS `backend_proyecto` DEFAULT CHARACTER SET utf8 ;
USE `backend_proyecto` ;


--
-- Table structure for table `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre`, `descripcion`) VALUES
(1, 'Original', 'Departamento origianl');

-- --------------------------------------------------------

--
-- Table structure for table `informe`
--

CREATE TABLE `informe` (
  `descripcion` text NOT NULL,
  `fecha` date NOT NULL,
  `id_informe` int(11) NOT NULL,
  `rut_usuario` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proyecto`
--

CREATE TABLE `proyecto` (
  `id_proyecto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text NOT NULL,
  `fecha_inicio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `proyecto_has_usuario_detalle`
--

CREATE TABLE `proyecto_has_usuario_detalle` (
  `id_proyecto` int(11) NOT NULL,
  `rut_usuario` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `fecha` date NOT NULL,
  `horas_trabajadas` int(11) NOT NULL,
  `descripcion_tarea` varchar(150) NOT NULL,
  `id_registro_tiempo` int(11) NOT NULL,
  `rut_usuario` varchar(12) DEFAULT NULL,
  `id_proyecto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usuario_basico`
--

CREATE TABLE `usuario_basico` (
  `rut_usuario` varchar(12) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `apellido_paterno` varchar(45) NOT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `fecha_nacimiento` date NOT NULL,
  `numero_telefonico` varchar(15) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `contraseña` varchar(60) NOT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `usuario_basico`
--

INSERT INTO `usuario_basico` (`rut_usuario`, `nombres`, `apellido_paterno`, `apellido_materno`, `fecha_nacimiento`, `numero_telefonico`, `direccion`, `contraseña`, `email`) VALUES
('10000000-0', 'Admin', 'Admin', 'Original', '0000-00-00', '+56 9 4141 4142', 'calle', '$2b$12$f4slJ1u3xcZKm/2YYYoGz.T70jmDYmetyJnVlwvLlzA3W1wyljvie', 'correoAdmin@inacapcorreo.cl');

-- --------------------------------------------------------

--
-- Table structure for table `usuario_detalle`
--

CREATE TABLE `usuario_detalle` (
  `rut_usuario` varchar(12) NOT NULL,
  `fecha_inicio_contrato` date NOT NULL,
  `salario` int(11) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `id_departamento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `usuario_detalle`
--

INSERT INTO `usuario_detalle` (`rut_usuario`, `fecha_inicio_contrato`, `salario`, `rol`, `id_departamento`) VALUES
('10000000-0', '0000-00-00', 1000000, 'Administrador', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indexes for table `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`id_informe`),
  ADD KEY `fk_Informe_Usuario1_idx` (`rut_usuario`);

--
-- Indexes for table `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id_proyecto`);

--
-- Indexes for table `proyecto_has_usuario_detalle`
--
ALTER TABLE `proyecto_has_usuario_detalle`
  ADD PRIMARY KEY (`id_proyecto`,`rut_usuario`),
  ADD KEY `fk_proyecto_has_usuario_detalle_usuario_detalle1_idx` (`rut_usuario`),
  ADD KEY `fk_proyecto_has_usuario_detalle_proyecto1_idx` (`id_proyecto`);

--
-- Indexes for table `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`id_registro_tiempo`),
  ADD KEY `fk_RegistroTiempo_Usuario1_idx` (`rut_usuario`),
  ADD KEY `fk_RegistroTiempo_Proyecto1_idx` (`id_proyecto`);

--
-- Indexes for table `usuario_basico`
--
ALTER TABLE `usuario_basico`
  ADD PRIMARY KEY (`rut_usuario`);

--
-- Indexes for table `usuario_detalle`
--
ALTER TABLE `usuario_detalle`
  ADD PRIMARY KEY (`rut_usuario`),
  ADD KEY `fk_Usuario_Detalle_Departamento1_idx` (`id_departamento`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_departamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `informe`
--
ALTER TABLE `informe`
  MODIFY `id_informe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `id_proyecto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  MODIFY `id_registro_tiempo` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `informe`
--
ALTER TABLE `informe`
  ADD CONSTRAINT `fk_Informe_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `proyecto_has_usuario_detalle`
--
ALTER TABLE `proyecto_has_usuario_detalle`
  ADD CONSTRAINT `fk_proyecto_has_usuario_detalle_proyecto1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_proyecto_has_usuario_detalle_usuario_detalle1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_detalle` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `fk_RegistroTiempo_Proyecto1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_RegistroTiempo_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `usuario_detalle`
--
ALTER TABLE `usuario_detalle`
  ADD CONSTRAINT `fk_Usuario_Detalle_Departamento1` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Usuario_Detalle_Usuario_basico1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

