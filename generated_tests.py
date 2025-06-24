import file_example

import pytest

# Testa a função soma para verificar se a soma de dois números está correta.
def test_file_example_soma():
    assert file_example.soma(2, 3) == 5
    assert file_example.soma(-1, 1) == 0
    assert file_example.soma(0, 0) == 0

# Testa a função saudacao para garantir que a saudação está formatada corretamente.
def test_file_example_saudacao():
    assert file_example.saudacao("João") == "Olá, João!"
    assert file_example.saudacao("") == "Olá, !"

# Testa a função esta_ativo para verificar se retorna True apenas quando a flag é True.
def test_file_example_esta_ativo():
    assert file_example.esta_ativo(True) is True
    assert file_example.esta_ativo(False) is False
    assert file_example.esta_ativo(None) is False

# Testa a função subtracao para garantir que a subtração de dois números está correta.
def test_file_example_subtracao():
    assert file_example.subtracao(5, 3) == 2
    assert file_example.subtracao(0, 0) == 0
    assert file_example.subtracao(3, 5) == -2

# Testa a função multiplicacao para verificar se a multiplicação de dois números está correta.
def test_file_example_multiplicacao():
    assert file_example.multiplicacao(2, 3) == 6
    assert file_example.multiplicacao(-1, 1) == -1
    assert file_example.multiplicacao(0, 5) == 0

# Testa a função dividir para garantir que a divisão está correta e que a exceção é lançada para divisão por zero.
def test_file_example_dividir():
    assert file_example.dividir(6, 3) == 2
    assert file_example.dividir(-6, 3) == -2
    assert file_example.dividir(0, 1) == 0
    with pytest.raises(ValueError, match="Divisão por zero!"):
        file_example.dividir(1, 0)

# Testa a função classificar para verificar se a classificação está correta com base na nota.
def test_file_example_classificar():
    assert file_example.classificar(9.5) == "Aprovado"
    assert file_example.classificar(9.4) == "Reprovado"
    assert file_example.classificar(10) == "Aprovado"

# Testa a função inutil para garantir que retorna a string esperada.
def test_file_example_inutil():
    assert file_example.inutil() == "Nunca sou chamada"