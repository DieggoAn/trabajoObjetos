-- SCRIPT DEL ESQUEMA DE LA BASE DE DATOS, VERSION 1.2

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema backend_proyecto
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `backend_proyecto` ;
CREATE SCHEMA IF NOT EXISTS `backend_proyecto` DEFAULT CHARACTER SET utf8 ;
USE `backend_proyecto` ;

-- -----------------------------------------------------
-- Table `Usuario_basico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Usuario_basico` ;
CREATE TABLE `Usuario_basico` (
  `rut_usuario` VARCHAR(12) NOT NULL,
  `nombres` VARCHAR(45) NOT NULL,
  `apellido_paterno` VARCHAR(45) NOT NULL,
  `apellido_materno` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `numero_telefonico` VARCHAR(15) NOT NULL,
  `contraseña` VARCHAR(60) NOT NULL,
  `rol` VARCHAR(45) NOT NULL DEFAULT 'Empleado',
  PRIMARY KEY (`rut_usuario`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Informe`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Informe` ;
CREATE TABLE `Informe` (
  `descripcion` TEXT NOT NULL,
  `formato` VARCHAR(45) NULL,
  `fecha` DATE NOT NULL,
  `id_informe` VARCHAR(15) NOT NULL,
  `rut_usuario` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`id_informe`),
  INDEX `fk_Informe_Usuario1_idx` (`rut_usuario` ASC),
  CONSTRAINT `fk_Informe_Usuario1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `Usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Departamento` ;
CREATE TABLE `Departamento` (
  `id_departamento` VARCHAR(15) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_departamento`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Proyecto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Proyecto` ;
CREATE TABLE `Proyecto` (
  `id_proyecto` VARCHAR(15) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(150) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `id_departamento` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id_proyecto`),
  INDEX `fk_Proyecto_Departamento1_idx` (`id_departamento` ASC),
  CONSTRAINT `fk_Proyecto_Departamento1`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `Departamento` (`id_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `RegistroTiempo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RegistroTiempo` ;
CREATE TABLE `RegistroTiempo` (
  `id_registro_tiempo` VARCHAR(15) NOT NULL,
  `fecha` DATE NOT NULL,
  `horas_trabajadas` INT NOT NULL,
  `descripcion_tarea` VARCHAR(150) NOT NULL,
  `id_departamento` VARCHAR(15) NOT NULL,
  `rut_usuario` VARCHAR(12) NOT NULL,
  `id_proyecto` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`id_registro_tiempo`),
  INDEX `fk_RegistroTiempo_Usuario1_idx` (`rut_usuario` ASC),
  INDEX `fk_RegistroTiempo_Proyecto1_idx` (`id_proyecto` ASC),
  INDEX `fk_RegistroTiempo_Departamento1_idx` (`id_departamento` ASC),
  CONSTRAINT `fk_RegistroTiempo_Usuario1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `Usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RegistroTiempo_Proyecto1`
    FOREIGN KEY (`id_proyecto`)
    REFERENCES `Proyecto` (`id_proyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RegistroTiempo_Departamento1`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `Departamento` (`id_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Usuario_Detalle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Usuario_Detalle` ;
CREATE TABLE `Usuario_Detalle` (
  `rut_usuario` VARCHAR(12) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `fecha_inicio_contrato` DATE NOT NULL,
  `salario` INT NOT NULL,
  `rol` VARCHAR(20) NOT NULL,
  `id_departamento` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`rut_usuario`),
  INDEX `fk_Usuario_Detalle_Departamento1_idx` (`id_departamento` ASC),
  CONSTRAINT `fk_Usuario_Detalle_Usuario_basico1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `Usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Detalle_Departamento1`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `Departamento` (`id_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Restore settings
-- -----------------------------------------------------
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;