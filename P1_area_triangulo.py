def main():
    '''
    **P1 Área do Triângulo!**
    Nosso objetivo é fazer um programa que receba 3 valores que representem lados de um triângulo e, então, 
    responda qual a área deste triângulo.

    Você pode calcular a área de um triângulo a partir da medida de seus lados utilizando a fórmula de Heron (https://pt.wikipedia.org/wiki/Teorema_de_Her%C3%A3o). 

    Você pode calcular a raiz quadrada de um número elevando ele a 1/2 (meio) — lembre-se que em Python a potenciação pode ser feita com o operador **.
    Ex: 4**(1/2) resulta em 2.0.

    Repare que não é qualquer combinação de 3 valores que pode representar lados de um triângulo (condição de existência de um triângulo - https://mundoeducacao.uol.com.br/matematica/condicao-existencia-um-triangulo.htm).
    Regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
    | b - c | < a < b + c
    | a - c | < b < a + c
    | a - b | < c < a + b
    Caso os números recebidos não possam ser usados como lados de um triângulo, seu programa deve informar isso ao usuário.
    '''
    
    a = float(input("Digite um valor para o lado 'a' do triângulo: "))
    b = float(input("Digite um valor para o lado 'b' do triângulo: "))
    c = float(input("Digite um valor para o lado 'c' do triângulo: "))
    
    # existe triângulo?
    if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
        # fórmula de Heron
        p = (a + b + c) / 2
        area = (p*(p - a)*(p - b)*(p - c)) ** (1/2)
        print(f"A área do triângulo é {area}.")
    else:
        print("Não obedece à regra, portanto não é possível existir um triângulo.")

if __name__ == "__main__":
    main()