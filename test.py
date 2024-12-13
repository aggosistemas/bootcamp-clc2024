# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'),"<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Troca de Cores</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            transition: background-color 0.5s ease; /* Suaviza a transição de cores */
        }
        h1 {
            color: #333;
        }
        label {
            font-size: 18px;
            margin-right: 10px;
        }
        select {
            font-size: 16px;
            padding: 5px 10px;
        }
    </style>
</head>
<body>
    <h1>Estudo: Troca de Cores na Página</h1>
    <p>Escolha uma cor no menu abaixo para alterar o fundo da página.</p>
    <div>
        <label for="colorSelector">Escolha uma cor:</label>
        <select id="colorSelector">
            <option value="">Selecione uma cor</option>
            <option value="white">Branco</option>
            <option value="lightblue">Azul Claro</option>
            <option value="lightgreen">Verde Claro</option>
            <option value="lightcoral">Coral Claro</option>
            <option value="yellow">Amarelo</option>
            <option value="pink">Rosa</option>
        </select>
    </div>
    <script>
        const colorSelector = document.getElementById('colorSelector');

        colorSelector.addEventListener('change', function() {
            const selectedColor = this.value; // Obtém a cor selecionada
            if (selectedColor) {
                document.body.style.backgroundColor = selectedColor; // Aplica a cor ao fundo
            }
        });
    </script>
</body>
</html>")