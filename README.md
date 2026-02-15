# 🧀🍄 Simulação do Crescimento Fúngico em Queijos Azuis  
### Utilizando Autômatos Celulares Tridimensionais

Este projeto foi desenvolvido durante a disciplina de **Autômatos Celulares**, no curso de  
**Bacharelado em Sistemas de Informação** da **Universidade Federal Rural de Pernambuco (UFRPE)**.

O objetivo do trabalho é simular o crescimento do fungo *Penicillium roqueforti* em queijos azuis
por meio de um **autômato celular tridimensional**, analisando a influência da oxigenação e da
estrutura interna do queijo nos padrões de crescimento fúngico.

---

## ▶️ Instruções de Execução

Para iniciar a simulação, execute o arquivo:

```bash
python main.py
```

### Controles e Navegação

- O autômato celular é **tridimensional (70 × 70 × 70)**.
- É possível navegar entre as camadas do autômato utilizando:
  - ⬆️ **Seta para cima (Up Arrow)**: camada superior  
  - ⬇️ **Seta para baixo (Down Arrow)**: camada inferior  

- Ao iniciar a simulação, o usuário é posicionado na **camada 35 de 70**, que é a camada
analisada no artigo.

---

## 🧩 Estrutura das Camadas

- A **camada 0** é composta exclusivamente por **células brancas**, representando uma região
sem crescimento fúngico.
- As camadas imediatamente acima da camada 0 apresentam um **maior número de células fúngicas**,
uma vez que são regiões com **maior disponibilidade de oxigênio**.

> Esse comportamento está de acordo com o processo real de maturação de queijos azuis,
no qual a oxigenação desempenha um papel fundamental no desenvolvimento do fungo.

---

## 📄 Artigo

O artigo completo descrevendo o modelo, a metodologia e os resultados pode ser encontrado em:

📄 **Simulação do Crescimento Fúngico em Queijos Azuis Utilizando Autômatos Celulares.pdf**

---

## 🧪 Experimentos

Os experimentos computacionais e visualizações adicionais estão disponíveis no notebook:

📓 **experiments.ipynb**

---

## 📌 Observações Finais

Este projeto tem caráter acadêmico e foi desenvolvido com fins didáticos, servindo como
uma aplicação prática do uso de **autômatos celulares tridimensionais** na modelagem de
processos biológicos complexos.
