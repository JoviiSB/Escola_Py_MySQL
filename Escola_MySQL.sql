CREATE DATABASE IF NOT EXISTS escola;  -- Cria o banco de dados 'escola' se ele não existir

USE escola;  -- Seleciona o banco de dados 'escola' para executar os comandos abaixo

-- Cria a tabela 'alunos' com os campos necessários
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    turma VARCHAR(50) NOT NULL
);
