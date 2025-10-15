-- SCRIPT DEL ESQUEMA DE LA BASE DE DATOS, VERSION 1.3

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema backend_proyecto
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `backend_proyecto` ;

-- -----------------------------------------------------
-- Schema backend_proyecto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `backend_proyecto` DEFAULT CHARACTER SET utf8 ;
USE `backend_proyecto` ;

-- -----------------------------------------------------
-- Table `backend_proyecto`.`usuario_basico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`usuario_basico` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`usuario_basico` (
  `rut_usuario` VARCHAR(12) NOT NULL,
  `nombres` VARCHAR(45) NOT NULL,
  `apellido_paterno` VARCHAR(45) NOT NULL,
  `apellido_materno` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `numero_telefonico` VARCHAR(15) NOT NULL,
  `contraseña` VARCHAR(60) NOT NULL,
  `rol` VARCHAR(45) NOT NULL DEFAULT 'Empleado',
  PRIMARY KEY (`rut_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`informe`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`informe` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`informe` (
  `descripcion` TEXT NOT NULL,
  `formato` VARCHAR(45) NULL,
  `fecha` DATE NOT NULL,
  `id_informe` INT NOT NULL AUTO_INCREMENT,
  `rut_usuario` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`id_informe`),
  INDEX `fk_Informe_Usuario1_idx` (`rut_usuario` ASC),
  CONSTRAINT `fk_Informe_Usuario1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `backend_proyecto`.`usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`proyecto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`proyecto` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`proyecto` (
  `id_proyecto` INT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  PRIMARY KEY (`id_proyecto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`departamento` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`departamento` (
  `id_departamento` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(150) NULL,
  PRIMARY KEY (`id_departamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`registro_tiempo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`registro_tiempo` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`registro_tiempo` (
  `fecha` DATE NOT NULL,
  `horas_trabajadas` INT NOT NULL,
  `descripcion_tarea` VARCHAR(150) NOT NULL,
  `id_registro_tiempo` INT NOT NULL AUTO_INCREMENT,
  `rut_usuario` VARCHAR(12) NOT NULL,
  `id_proyecto` INT NOT NULL,
  PRIMARY KEY (`id_registro_tiempo`),
  INDEX `fk_RegistroTiempo_Usuario1_idx` (`rut_usuario` ASC),
  INDEX `fk_RegistroTiempo_Proyecto1_idx` (`id_proyecto` ASC),
  CONSTRAINT `fk_RegistroTiempo_Usuario1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `backend_proyecto`.`usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_RegistroTiempo_Proyecto1`
    FOREIGN KEY (`id_proyecto`)
    REFERENCES `backend_proyecto`.`proyecto` (`id_proyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`usuario_detalle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`usuario_detalle` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`usuario_detalle` (
  `rut_usuario` VARCHAR(12) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `fecha_inicio_contrato` DATE NOT NULL,
  `salario` INT NOT NULL,
  `rol` VARCHAR(20) NOT NULL,
  `id_departamento` INT NOT NULL,
  PRIMARY KEY (`rut_usuario`),
  INDEX `fk_Usuario_Detalle_Departamento1_idx` (`id_departamento` ASC),
  CONSTRAINT `fk_Usuario_Detalle_Usuario_basico1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `backend_proyecto`.`usuario_basico` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Detalle_Departamento1`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `backend_proyecto`.`departamento` (`id_departamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `backend_proyecto`.`proyecto_has_usuario_detalle`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `backend_proyecto`.`proyecto_has_usuario_detalle` ;

CREATE TABLE IF NOT EXISTS `backend_proyecto`.`proyecto_has_usuario_detalle` (
  `id_proyecto` INT NOT NULL,
  `rut_usuario` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`id_proyecto`, `rut_usuario`),
  INDEX `fk_proyecto_has_usuario_detalle_usuario_detalle1_idx` (`rut_usuario` ASC),
  INDEX `fk_proyecto_has_usuario_detalle_proyecto1_idx` (`id_proyecto` ASC),
  CONSTRAINT `fk_proyecto_has_usuario_detalle_proyecto1`
    FOREIGN KEY (`id_proyecto`)
    REFERENCES `backend_proyecto`.`proyecto` (`id_proyecto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_proyecto_has_usuario_detalle_usuario_detalle1`
    FOREIGN KEY (`rut_usuario`)
    REFERENCES `backend_proyecto`.`usuario_detalle` (`rut_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
