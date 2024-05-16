#print("Tentativa {1} de {0}".format(3,10))
    #Podemos alterar a ordem dos números com (0,1,2,3,....) Sequências por ordem
import random

#print("R$ {:.2f}".format(1.5))
    #{:f} serve para indicarmos que o valor dentro do format() será FLOAT
    #{:.2f} o .2 depois dos : e antes do f serve para indicar quantas casas vamos querer depois do .//ex:14.>90<

print("R$ {:07.2f}".format(10.12))
# O 7 é o total de caracteres contidos dentro do format e o 2 são os que estão depois do ponto >/.\<
# se colocarmos {:07.2f}, será imprimidos 0 até preencher o numero
# para indicar um numero inteiro, o "d" representa d = int = digito/d\

#print("Data {:02d}/{:02d}".format(19,11))
