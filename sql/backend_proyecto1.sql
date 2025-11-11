-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-11-2025 a las 18:37:25
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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre`, `descripcion`) VALUES
(1, 'Original', 'Departamento origianl'),
(2, 'Lotus', 'poto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indicadores_economicos`
--

CREATE TABLE `indicadores_economicos` (
  `id_consulta` int(11) NOT NULL,
  `rut_usuario` varchar(12) NOT NULL,
  `fecha_actual` date DEFAULT NULL,
  `nombre_indicador` varchar(45) DEFAULT NULL,
  `valor` decimal(18,2) DEFAULT NULL,
  `fecha_consulta` date DEFAULT NULL,
  `proveedor` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `indicadores_economicos`
--

INSERT INTO `indicadores_economicos` (`id_consulta`, `rut_usuario`, `fecha_actual`, `nombre_indicador`, `valor`, `fecha_consulta`, `proveedor`) VALUES
(1, '30000000-0', '0000-00-00', 'euro', 1.09, '0000-00-00', 'mindicador.cl'),
(2, '10000000-0', '2025-11-09', 'dolar', 948.77, '0000-00-00', 'mindicador.cl');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `descripcion` text NOT NULL,
  `fecha` date NOT NULL,
  `id_informe` int(11) NOT NULL,
  `rut_usuario` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `informe`
--

INSERT INTO `informe` (`descripcion`, `fecha`, `id_informe`, `rut_usuario`) VALUES
('Ojala que no cague esta wuea', '2025-11-05', 2, '10000000-0'),
('Buena, a la primera', '2025-11-05', 3, '30000000-0'),
('peo', '2025-11-09', 5, '10000000-0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `id_proyecto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` text NOT NULL,
  `fecha_inicio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id_proyecto`, `nombre`, `descripcion`, `fecha_inicio`) VALUES
(1, 'El Diego Es Diego', 'A veces es Diego', '2025-11-08'),
(2, 'Zzz', 'mu weno', '2025-11-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto_has_usuario_detalle`
--

CREATE TABLE `proyecto_has_usuario_detalle` (
  `id_proyecto` int(11) NOT NULL,
  `rut_usuario` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `proyecto_has_usuario_detalle`
--

INSERT INTO `proyecto_has_usuario_detalle` (`id_proyecto`, `rut_usuario`) VALUES
(1, '10000000-0'),
(2, '10000000-0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
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
-- Estructura de tabla para la tabla `usuario_basico`
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
-- Volcado de datos para la tabla `usuario_basico`
--

INSERT INTO `usuario_basico` (`rut_usuario`, `nombres`, `apellido_paterno`, `apellido_materno`, `fecha_nacimiento`, `numero_telefonico`, `direccion`, `contraseña`, `email`) VALUES
('10000000-0', 'Admin', 'Admin', 'Original', '0000-00-00', '+56 9 4141 4142', 'calle', '$2b$12$f4slJ1u3xcZKm/2YYYoGz.T70jmDYmetyJnVlwvLlzA3W1wyljvie', 'correoAdmin@inacapcorreo.cl'),
('20000000-0', 'Gerente', 'Gerente', 'Original', '0000-00-00', '+56 9 4141 4143', 'calle', '$2b$12$JRXMG3yzZvXEcGFTMEZOYOMtCmrx.lq5ZlP/29ccUNvA/7gMlMKy2', 'correoGerente@inacapcorreo.cl'),
('20929825-K', 'Juan', 'Navarro', 'Dober', '2002-12-11', '+56 9 6865 9674', 'Av calle calle 456', '$2b$12$O4bhCvOgraJ2uU2cvHlwHeQLSCtjFE5ahlGeW1QHxJGpcSklCCXde', 'juanchomcjuancho@gmail.com'),
('30000000-0', 'Empleado', 'Empleado', 'Original', '0000-00-00', '+56 9 4141 4144', 'calle', '$2b$12$KT.N5ksz8ZRMQxzqjsPqsOeTmWmepD3DM3o2VbEb6bvDLPVSWgpa6', 'correoAdmin@inacapcorreo.cl');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_detalle`
--

CREATE TABLE `usuario_detalle` (
  `rut_usuario` varchar(12) NOT NULL,
  `fecha_inicio_contrato` date NOT NULL,
  `salario` int(11) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `id_departamento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuario_detalle`
--

INSERT INTO `usuario_detalle` (`rut_usuario`, `fecha_inicio_contrato`, `salario`, `rol`, `id_departamento`) VALUES
('10000000-0', '0000-00-00', 1000000, 'Administrador', 1),
('20000000-0', '0000-00-00', 1000000, 'gerente', 2),
('20929825-K', '2025-12-11', 1000000, 'Empleado', 1),
('30000000-0', '0000-00-00', 1000000, 'Empleado', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indices de la tabla `indicadores_economicos`
--
ALTER TABLE `indicadores_economicos`
  ADD PRIMARY KEY (`id_consulta`),
  ADD KEY `fk_table1_usuario_basico1_idx` (`rut_usuario`);

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
  ADD PRIMARY KEY (`id_proyecto`);

--
-- Indices de la tabla `proyecto_has_usuario_detalle`
--
ALTER TABLE `proyecto_has_usuario_detalle`
  ADD PRIMARY KEY (`id_proyecto`,`rut_usuario`),
  ADD KEY `fk_proyecto_has_usuario_detalle_usuario_detalle1_idx` (`rut_usuario`),
  ADD KEY `fk_proyecto_has_usuario_detalle_proyecto1_idx` (`id_proyecto`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`id_registro_tiempo`),
  ADD KEY `fk_RegistroTiempo_Usuario1_idx` (`rut_usuario`),
  ADD KEY `fk_RegistroTiempo_Proyecto1_idx` (`id_proyecto`);

--
-- Indices de la tabla `usuario_basico`
--
ALTER TABLE `usuario_basico`
  ADD PRIMARY KEY (`rut_usuario`);

--
-- Indices de la tabla `usuario_detalle`
--
ALTER TABLE `usuario_detalle`
  ADD PRIMARY KEY (`rut_usuario`),
  ADD KEY `fk_Usuario_Detalle_Departamento1_idx` (`id_departamento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_departamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `indicadores_economicos`
--
ALTER TABLE `indicadores_economicos`
  MODIFY `id_consulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `informe`
--
ALTER TABLE `informe`
  MODIFY `id_informe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `id_proyecto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  MODIFY `id_registro_tiempo` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `indicadores_economicos`
--
ALTER TABLE `indicadores_economicos`
  ADD CONSTRAINT `fk_table1_usuario_basico1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `informe`
--
ALTER TABLE `informe`
  ADD CONSTRAINT `fk_Informe_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `proyecto_has_usuario_detalle`
--
ALTER TABLE `proyecto_has_usuario_detalle`
  ADD CONSTRAINT `fk_proyecto_has_usuario_detalle_proyecto1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_proyecto_has_usuario_detalle_usuario_detalle1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_detalle` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `fk_RegistroTiempo_Proyecto1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_RegistroTiempo_Usuario1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuario_detalle`
--
ALTER TABLE `usuario_detalle`
  ADD CONSTRAINT `fk_Usuario_Detalle_Departamento1` FOREIGN KEY (`id_departamento`) REFERENCES `departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Usuario_Detalle_Usuario_basico1` FOREIGN KEY (`rut_usuario`) REFERENCES `usuario_basico` (`rut_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
