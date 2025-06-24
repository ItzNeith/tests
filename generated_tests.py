import file_example

import pytest

# Testa a função soma com valores positivos
def test_file_example_soma():
    assert file_example.soma(2, 3) == 5

# Testa a função soma com valores negativos
def test_file_example_soma_negativos():
    assert file_example.soma(-1, -1) == -2

# Testa a função soma com zero
def test_file_example_soma_zero():
    assert file_example.soma(0, 5) == 5

# Testa a função saudacao com um nome
def test_file_example_saudacao():
    assert file_example.saudacao("Maria") == "Olá, Maria!"

# Testa a função saudacao com um nome vazio
def test_file_example_saudacao_nome_vazio():
    assert file_example.saudacao("") == "Olá, !"

# Testa a função esta_ativo com True
def test_file_example_esta_ativo_true():
    assert file_example.esta_ativo(True) is True

# Testa a função esta_ativo com False
def test_file_example_esta_ativo_false():
    assert file_example.esta_ativo(False) is False

# Testa a função subtracao com valores positivos
def test_file_example_subtracao():
    assert file_example.subtracao(5, 3) == 2

# Testa a função subtracao com resultado negativo
def test_file_example_subtracao_negativo():
    assert file_example.subtracao(3, 5) == -2

# Testa a função multiplicacao com valores positivos
def test_file_example_multiplicacao():
    assert file_example.multiplicacao(3, 4) == 12

# Testa a função multiplicacao com zero
def test_file_example_multiplicacao_zero():
    assert file_example.multiplicacao(0, 5) == 0

# Testa a função dividir com valores válidos
def test_file_example_dividir():
    assert file_example.dividir(10, 2) == 5

# Testa a função dividir com divisão por zero
def test_file_example_dividir_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero!"):
        file_example.dividir(10, 0)

# Testa a função classificar com nota alta
def test_file_example_classificar_aprovado():
    assert file_example.classificar(9.5) == "Aprovado"

# Testa a função classificar com nota baixa
def test_file_example_classificar_reprovado():
    assert file_example.classificar(9.4) == "Reprovado"

# Testa a função classificar com nota limite
def test_file_example_classificar_limite():
    assert file_example.classificar(9.499999) == "Reprovado"

# Testa a função inutil para garantir que retorna a string esperada
def test_file_example_inutil():
    assert file_example.inutil() == "Nunca sou chamada"