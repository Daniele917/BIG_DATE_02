-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 11-Out-2024 às 21:14
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
-- Banco de dados: `maternidade`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `bebe`
--

CREATE TABLE `bebe` (
  `Codigo` int(11) NOT NULL,
  `Nome` varchar(100) DEFAULT NULL,
  `Data_Nascimento` date DEFAULT NULL,
  `Peso` decimal(5,2) DEFAULT NULL,
  `Altura` decimal(5,2) DEFAULT NULL,
  `CRM_Medico` varchar(20) DEFAULT NULL,
  `CPF_Mae` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mae`
--

CREATE TABLE `mae` (
  `CPF` varchar(20) NOT NULL,
  `Nome` varchar(100) DEFAULT NULL,
  `Endereco` varchar(255) DEFAULT NULL,
  `Telefone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `medico`
--

CREATE TABLE `medico` (
  `CRM` varchar(20) NOT NULL,
  `Nome` varchar(100) DEFAULT NULL,
  `Telefone` varchar(20) DEFAULT NULL,
  `Especialidade` varchar(100) DEFAULT NULL,
  `Codigo_Eq` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `parturiente`
--

CREATE TABLE `parturiente` (
  `CPF_Mae` varchar(20) NOT NULL,
  `Codigo_Bebe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `realizacao_parto`
--

CREATE TABLE `realizacao_parto` (
  `CRM_Medico` varchar(20) NOT NULL,
  `Codigo_Bebe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `rel_equipe_medica_medico`
--

CREATE TABLE `rel_equipe_medica_medico` (
  `Codigo_Eq` int(11) NOT NULL,
  `CRM_Medico` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `bebe`
--
ALTER TABLE `bebe`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `CRM_Medico` (`CRM_Medico`),
  ADD KEY `CPF_Mae` (`CPF_Mae`);

--
-- Índices para tabela `mae`
--
ALTER TABLE `mae`
  ADD PRIMARY KEY (`CPF`);

--
-- Índices para tabela `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`CRM`),
  ADD KEY `Codigo_Eq` (`Codigo_Eq`);

--
-- Índices para tabela `parturiente`
--
ALTER TABLE `parturiente`
  ADD PRIMARY KEY (`CPF_Mae`,`Codigo_Bebe`),
  ADD KEY `Codigo_Bebe` (`Codigo_Bebe`);

--
-- Índices para tabela `realizacao_parto`
--
ALTER TABLE `realizacao_parto`
  ADD PRIMARY KEY (`CRM_Medico`,`Codigo_Bebe`),
  ADD KEY `Codigo_Bebe` (`Codigo_Bebe`);

--
-- Índices para tabela `rel_equipe_medica_medico`
--
ALTER TABLE `rel_equipe_medica_medico`
  ADD PRIMARY KEY (`Codigo_Eq`,`CRM_Medico`),
  ADD KEY `CRM_Medico` (`CRM_Medico`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `bebe`
--
ALTER TABLE `bebe`
  ADD CONSTRAINT `bebe_ibfk_1` FOREIGN KEY (`CRM_Medico`) REFERENCES `medico` (`CRM`),
  ADD CONSTRAINT `bebe_ibfk_2` FOREIGN KEY (`CPF_Mae`) REFERENCES `mae` (`CPF`);

--
-- Limitadores para a tabela `medico`
--
ALTER TABLE `medico`
  ADD CONSTRAINT `medico_ibfk_1` FOREIGN KEY (`Codigo_Eq`) REFERENCES `equipe_medica` (`Codigo_Eq`);

--
-- Limitadores para a tabela `parturiente`
--
ALTER TABLE `parturiente`
  ADD CONSTRAINT `parturiente_ibfk_1` FOREIGN KEY (`CPF_Mae`) REFERENCES `mae` (`CPF`),
  ADD CONSTRAINT `parturiente_ibfk_2` FOREIGN KEY (`Codigo_Bebe`) REFERENCES `bebe` (`Codigo`);

--
-- Limitadores para a tabela `realizacao_parto`
--
ALTER TABLE `realizacao_parto`
  ADD CONSTRAINT `realizacao_parto_ibfk_1` FOREIGN KEY (`CRM_Medico`) REFERENCES `medico` (`CRM`),
  ADD CONSTRAINT `realizacao_parto_ibfk_2` FOREIGN KEY (`Codigo_Bebe`) REFERENCES `bebe` (`Codigo`);

--
-- Limitadores para a tabela `rel_equipe_medica_medico`
--
ALTER TABLE `rel_equipe_medica_medico`
  ADD CONSTRAINT `rel_equipe_medica_medico_ibfk_1` FOREIGN KEY (`Codigo_Eq`) REFERENCES `equipe_medica` (`Codigo_Eq`),
  ADD CONSTRAINT `rel_equipe_medica_medico_ibfk_2` FOREIGN KEY (`CRM_Medico`) REFERENCES `medico` (`CRM`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
