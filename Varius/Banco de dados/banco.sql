-- produtos
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL
);

-- fornecedores
CREATE TABLE Fornecedores (
    FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    CNPJ VARCHAR(18)
);
--  ESTOQUE COM RELAÇÕES
CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);
-- FULL JOIN E GROUP BY
SELECT p.ProdutoID, p.Nome AS NomeProduto, e.Quantidade, e.DataEntrada
FROM Produtos p
LEFT JOIN Estoque e ON p.ProdutoID = e.ProdutoID

UNION

SELECT p.ProdutoID, p.Nome AS NomeProduto, e.Quantidade, e.DataEntrada
FROM Produtos p
RIGHT JOIN Estoque e ON p.ProdutoID = e.ProdutoID;

-- GROUP BY: Total de produtos recebidos por fornecedor
SELECT f.FornecedorID, f.Nome AS NomeFornecedor, SUM(e.Quantidade) AS TotalRecebido
FROM Fornecedores f
JOIN Estoque e ON f.FornecedorID = e.FornecedorID
GROUP BY f.FornecedorID, f.Nome;

-- Adicionando uma coluna de observações
ALTER TABLE Estoque
ADD Observacao VARCHAR(255);
