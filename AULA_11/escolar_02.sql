-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 14-Out-2024 às 21:21
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escolar_02`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `aluno`
--

CREATE TABLE `aluno` (
  `matricula` int(11) NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `idade` int(11) DEFAULT NULL,
  `numero_turma` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `aluno`
--

INSERT INTO `aluno` (`matricula`, `nome`, `sexo`, `idade`, `numero_turma`) VALUES
(1100, 'João', 'M', 15, 1001),
(1200, 'Maria', 'F', 14, 1002),
(1300, 'Antônio', 'M', 16, 2001),
(1400, 'Julio', 'M', 16, 2001),
(1500, 'Andreia', 'F', 15, 1001);

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `codigo` int(11) NOT NULL,
  `descricao` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `disciplina`
--

INSERT INTO `disciplina` (`codigo`, `descricao`) VALUES
(11, 'matematica'),
(12, 'portugues'),
(13, 'fisica'),
(14, 'quimica'),
(15, 'ingles');

-- --------------------------------------------------------

--
-- Estrutura da tabela `estuda`
--

CREATE TABLE `estuda` (
  `id_estuda` int(11) NOT NULL,
  `matricula` int(11) DEFAULT NULL,
  `codigo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `estuda`
--

INSERT INTO `estuda` (`id_estuda`, `matricula`, `codigo`) VALUES
(1, 1100, 11),
(2, 1100, 12),
(3, 1100, 15),
(4, 1500, 13),
(5, 1500, 14),
(6, 1500, 11),
(7, 1400, 11),
(8, 1500, 12);

-- --------------------------------------------------------

--
-- Estrutura da tabela `turma`
--

CREATE TABLE `turma` (
  `numero` int(11) NOT NULL,
  `sala` int(11) DEFAULT NULL,
  `andar` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `turma`
--

INSERT INTO `turma` (`numero`, `sala`, `andar`) VALUES
(1001, 101, 1),
(1002, 102, 1),
(2001, 201, 2),
(2004, 202, 2),
(3005, 301, 3);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `numero_turma` (`numero_turma`);

--
-- Índices para tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `estuda`
--
ALTER TABLE `estuda`
  ADD PRIMARY KEY (`id_estuda`),
  ADD KEY `matricula` (`matricula`),
  ADD KEY `codigo` (`codigo`);

--
-- Índices para tabela `turma`
--
ALTER TABLE `turma`
  ADD PRIMARY KEY (`numero`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `estuda`
--
ALTER TABLE `estuda`
  MODIFY `id_estuda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `aluno`
--
ALTER TABLE `aluno`
  ADD CONSTRAINT `aluno_ibfk_1` FOREIGN KEY (`numero_turma`) REFERENCES `turma` (`numero`);

--
-- Limitadores para a tabela `estuda`
--
ALTER TABLE `estuda`
  ADD CONSTRAINT `estuda_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `aluno` (`matricula`),
  ADD CONSTRAINT `estuda_ibfk_2` FOREIGN KEY (`codigo`) REFERENCES `disciplina` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
