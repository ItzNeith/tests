import file_example

import pytest

# Testa a função soma para verificar se a soma de dois números está correta
def test_file_example_soma():
    assert file_example.soma(2, 3) == 5
    assert file_example.soma(-1, 1) == 0
    assert file_example.soma(0, 0) == 0

# Testa a função saudacao para verificar se a saudação está correta
def test_file_example_saudacao():
    assert file_example.saudacao("Maria") == "Olá, Maria!"
    assert file_example.saudacao("João") == "Olá, João!"

# Testa a função esta_ativo para verificar se o estado ativo é identificado corretamente
def test_file_example_esta_ativo():
    assert file_example.esta_ativo(True) is True
    assert file_example.esta_ativo(False) is False
    assert file_example.esta_ativo(None) is False

# Testa a função subtracao para verificar se a subtração de dois números está correta
def test_file_example_subtracao():
    assert file_example.subtracao(5, 3) == 2
    assert file_example.subtracao(0, 0) == 0
    assert file_example.subtracao(-1, -1) == 0

# Testa a função multiplicacao para verificar se a multiplicação de dois números está correta
def test_file_example_multiplicacao():
    assert file_example.multiplicacao(3, 4) == 12
    assert file_example.multiplicacao(0, 5) == 0
    assert file_example.multiplicacao(-1, 1) == -1

# Testa a função dividir para verificar se a divisão de dois números está correta e se a exceção é lançada
def test_file_example_dividir():
    assert file_example.dividir(10, 2) == 5
    assert file_example.dividir(-10, 2) == -5
    with pytest.raises(ValueError, match="Divisão por zero!"):
        file_example.dividir(10, 0)

# Testa a função classificar para verificar se a classificação está correta
def test_file_example_classificar():
    assert file_example.classificar(9.5) == "Aprovado"
    assert file_example.classificar(9.4) == "Reprovado"
    assert file_example.classificar(10) == "Aprovado"