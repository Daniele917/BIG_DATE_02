-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 14-Out-2024 às 21:27
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
-- Banco de dados: `restaurante_02`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cardapio`
--

CREATE TABLE `cardapio` (
  `id` int(11) NOT NULL,
  `id_produto` int(11) DEFAULT NULL,
  `descricao` text,
  `preco` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `garcom`
--

CREATE TABLE `garcom` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `setor` enum('Área Esquerda','Área Direita','Área Central','Mezanino') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `mesa`
--

CREATE TABLE `mesa` (
  `id` int(11) NOT NULL,
  `numero` int(11) DEFAULT NULL,
  `quantidade_cadeiras` int(11) DEFAULT NULL,
  `setor` enum('Área Esquerda','Área Direita','Área Central','Mezanino') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedido`
--

CREATE TABLE `pedido` (
  `id` int(11) NOT NULL,
  `numero_pedido` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT NULL,
  `id_mesa` int(11) DEFAULT NULL,
  `id_garcom` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE `produto` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `descricao` text,
  `preco` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cardapio`
--
ALTER TABLE `cardapio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_produto` (`id_produto`);

--
-- Índices para tabela `garcom`
--
ALTER TABLE `garcom`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `mesa`
--
ALTER TABLE `mesa`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_mesa` (`id_mesa`),
  ADD KEY `id_garcom` (`id_garcom`);

--
-- Índices para tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cardapio`
--
ALTER TABLE `cardapio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `garcom`
--
ALTER TABLE `garcom`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `mesa`
--
ALTER TABLE `mesa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `cardapio`
--
ALTER TABLE `cardapio`
  ADD CONSTRAINT `cardapio_ibfk_1` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id`);

--
-- Limitadores para a tabela `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`id_mesa`) REFERENCES `mesa` (`id`),
  ADD CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`id_garcom`) REFERENCES `garcom` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
