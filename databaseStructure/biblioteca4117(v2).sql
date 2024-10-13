-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-10-2024 a las 02:34:06
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
-- Base de datos: `biblioteca4117`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `id_curso` int(11) NOT NULL,
  `curso` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `curso`
--

INSERT INTO `curso` (`id_curso`, `curso`) VALUES
(1, 'Primero'),
(2, 'Segundo'),
(3, 'Tercero'),
(4, 'Cuarto'),
(5, 'Quinto'),
(6, 'Sexto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_prestamo`
--

CREATE TABLE `detalle_prestamo` (
  `id_detalle_prestamo` int(11) NOT NULL,
  `id_prestamo_fk` int(11) NOT NULL,
  `id_ejemplar_fk` int(11) NOT NULL,
  `fecha_prestado` date NOT NULL,
  `fecha_devuelto` date DEFAULT NULL,
  `finalizado` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_prestamo`
--

INSERT INTO `detalle_prestamo` (`id_detalle_prestamo`, `id_prestamo_fk`, `id_ejemplar_fk`, `fecha_prestado`, `fecha_devuelto`, `finalizado`) VALUES
(1, 1, 3, '2024-08-20', '2024-08-20', 1),
(2, 2, 1, '2024-08-20', '2024-08-20', 1),
(3, 3, 6, '2024-08-29', '2024-09-29', 1),
(4, 3, 7, '2024-08-29', '2024-08-29', 1),
(5, 4, 9, '2024-08-29', NULL, 0),
(6, 4, 10, '2024-08-29', NULL, 0),
(7, 5, 9, '2024-08-29', NULL, NULL),
(8, 5, 10, '2024-08-29', NULL, NULL),
(9, 6, 9, '2024-08-29', '2024-08-29', 1),
(10, 6, 10, '2024-08-29', '2024-08-29', 1),
(11, 6, 11, '2024-08-29', NULL, NULL),
(12, 7, 2, '2024-09-26', '2024-09-29', 1),
(13, 8, 4, '2024-09-26', '2024-09-29', 1),
(14, 9, 5, '2024-09-26', '2024-09-29', 1),
(15, 10, 7, '2024-09-26', '2024-09-26', 1),
(16, 11, 3, '2024-09-29', NULL, NULL),
(17, 11, 4, '2024-09-29', NULL, NULL),
(18, 11, 5, '2024-09-29', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `divicion`
--

CREATE TABLE `divicion` (
  `id_divicion` int(11) NOT NULL,
  `divicion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `divicion`
--

INSERT INTO `divicion` (`id_divicion`, `divicion`) VALUES
(1, 'Primera'),
(2, 'Segunda'),
(3, 'Tercera'),
(4, 'Cuarta'),
(5, 'Quinta'),
(6, 'Sexta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejemplar`
--

CREATE TABLE `ejemplar` (
  `id_ejemplar` int(11) NOT NULL,
  `id_obra_fk` int(11) NOT NULL,
  `disponibilidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ejemplar`
--

INSERT INTO `ejemplar` (`id_ejemplar`, `id_obra_fk`, `disponibilidad`) VALUES
(1, 1, 0),
(2, 1, 0),
(3, 1, 16),
(4, 1, 17),
(5, 1, 18),
(6, 2, 0),
(7, 2, 0),
(8, 2, 0),
(9, 2, 0),
(10, 2, 0),
(11, 2, 11),
(12, 3, 0),
(13, 3, 0),
(14, 3, 0),
(15, 3, 0),
(16, 3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id_estudiante` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `telefono` bigint(11) NOT NULL,
  `dni` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id_estudiante`, `nombre`, `telefono`, `dni`) VALUES
(1, 'Juan peres1', 2604344312, 40566241),
(2, 'maria dolores de espalda', 2604552436, 41000000),
(3, 'marcos con minuscula', 2604303030, 30025123),
(4, 'Jorge martinez', 2603445512, 42025129),
(7, 'NIno de los peques', 111111111111111, 39011342);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obraliteraria`
--

CREATE TABLE `obraliteraria` (
  `id_obra` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `editorial` varchar(100) NOT NULL,
  `portada` varchar(500) DEFAULT NULL,
  `resumen` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `obraliteraria`
--

INSERT INTO `obraliteraria` (`id_obra`, `titulo`, `autor`, `editorial`, `portada`, `resumen`) VALUES
(1, 'La vuelta al mundo en 80 días ', 'Julio Verne', 'Santillana', 'D:\\Proyectos en python\\Biblioteca\\resources\\covers\\1.PNG', NULL),
(2, 'De la tierra a la luna', 'Julio Verne', 'Alfa Omega', NULL, NULL),
(3, 'Dracula', 'Bram Stoker', 'Omega', 'D://Proyectos en python//Biblioteca//resources//covers//3.PNG ', 'D://Proyectos en python//Biblioteca//resources//summaries//3.txt');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `id_prestamo` int(11) NOT NULL,
  `id_curso_fk` int(11) NOT NULL,
  `id_divicion_fk` int(11) NOT NULL,
  `id_estudiante_fk` int(11) DEFAULT NULL,
  `tipo_prestamo` tinyint(4) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_finaliza` date DEFAULT NULL,
  `estado_prestamo` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamo`
--

INSERT INTO `prestamo` (`id_prestamo`, `id_curso_fk`, `id_divicion_fk`, `id_estudiante_fk`, `tipo_prestamo`, `fecha_inicio`, `fecha_finaliza`, `estado_prestamo`) VALUES
(1, 1, 3, 1, 1, '2024-08-20', '2024-08-20', 1),
(2, 2, 1, NULL, 0, '2024-08-20', '2024-08-20', 1),
(3, 2, 2, NULL, 0, '2024-08-29', '2024-09-29', 1),
(4, 3, 2, NULL, 0, '2024-08-29', NULL, NULL),
(5, 3, 2, 1, 1, '2024-08-29', NULL, NULL),
(6, 3, 2, 1, 1, '2024-08-29', '2024-08-29', 1),
(7, 4, 1, NULL, 0, '2024-09-26', '2024-09-29', 1),
(8, 2, 1, NULL, 0, '2024-09-26', '2024-09-29', 1),
(9, 3, 4, 2, 1, '2024-09-26', '2024-09-29', 1),
(10, 5, 3, NULL, 0, '2024-09-26', '2024-09-26', 1),
(11, 3, 5, 1, 1, '2024-09-29', NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indices de la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  ADD PRIMARY KEY (`id_detalle_prestamo`),
  ADD KEY `Relacion con prestamo y ejemplar` (`id_prestamo_fk`,`id_ejemplar_fk`),
  ADD KEY `id_ejemplar_fk` (`id_ejemplar_fk`);

--
-- Indices de la tabla `divicion`
--
ALTER TABLE `divicion`
  ADD PRIMARY KEY (`id_divicion`);

--
-- Indices de la tabla `ejemplar`
--
ALTER TABLE `ejemplar`
  ADD PRIMARY KEY (`id_ejemplar`),
  ADD KEY `Relacion obraLit y ejemplar` (`id_obra_fk`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `obraliteraria`
--
ALTER TABLE `obraliteraria`
  ADD PRIMARY KEY (`id_obra`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`id_prestamo`),
  ADD KEY `Relacion curso divicion estudiante` (`id_curso_fk`,`id_divicion_fk`,`id_estudiante_fk`),
  ADD KEY `id_divicion_fk` (`id_divicion_fk`),
  ADD KEY `id_estudiante_fk` (`id_estudiante_fk`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `curso`
--
ALTER TABLE `curso`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  MODIFY `id_detalle_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `divicion`
--
ALTER TABLE `divicion`
  MODIFY `id_divicion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ejemplar`
--
ALTER TABLE `ejemplar`
  MODIFY `id_ejemplar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `obraliteraria`
--
ALTER TABLE `obraliteraria`
  MODIFY `id_obra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  MODIFY `id_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `detalle_prestamo`
--
ALTER TABLE `detalle_prestamo`
  ADD CONSTRAINT `detalle_prestamo_ibfk_1` FOREIGN KEY (`id_prestamo_fk`) REFERENCES `prestamo` (`id_prestamo`),
  ADD CONSTRAINT `detalle_prestamo_ibfk_2` FOREIGN KEY (`id_ejemplar_fk`) REFERENCES `ejemplar` (`id_ejemplar`);

--
-- Filtros para la tabla `ejemplar`
--
ALTER TABLE `ejemplar`
  ADD CONSTRAINT `ejemplar_ibfk_1` FOREIGN KEY (`id_obra_fk`) REFERENCES `obraliteraria` (`id_obra`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `prestamo_ibfk_1` FOREIGN KEY (`id_divicion_fk`) REFERENCES `divicion` (`id_divicion`),
  ADD CONSTRAINT `prestamo_ibfk_2` FOREIGN KEY (`id_curso_fk`) REFERENCES `curso` (`id_curso`),
  ADD CONSTRAINT `prestamo_ibfk_3` FOREIGN KEY (`id_estudiante_fk`) REFERENCES `estudiante` (`id_estudiante`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
