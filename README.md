# libhex
Essa biblioteca foi desenvolvida para simplificar o acesso a informações dentro da plataforma HackerWars.

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
