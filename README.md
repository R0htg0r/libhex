# libhex
Esta biblioteca foi cuidadosamente projetada e implementada com o objetivo primordial de aprimorar a experiência dos desenvolvedores ao realizar chamadas e manipular informações dentro do ecossistema abrangente e dinâmico da plataforma HackerWars, proporcionando-lhes uma ferramenta robusta e eficiente para explorar e interagir com os recursos disponíveis nesse ambiente complexo e multifacetado.

# Retornando informações simples.
```py
import libhex

jogador = hacker()

print("Seu Nome: " + jogador.nome())
print("Seu IP: " + jogador.ip())
print("Sua reputação: " + jogador.rp())
print("Sua classificação: " + jogador.rk())

```
```
Seu nome: Logo Frozen
Seu IP: 245.212.96.231
Sua reputação: 1500
Sua classificação: #69
```

# Retornando parte do Financeiro
```py
import libhex

financeiro = bitcoins()

print("Chave Público: " + financeiro.publico())
print("Chave Privado: " + financeiro.privado())
print("Satoshi: " + financeiro.satoshi())
```
```
Chave Público: Pyk....
Chave Privada: Xcd....
Satoshi: 0.00000000
```
