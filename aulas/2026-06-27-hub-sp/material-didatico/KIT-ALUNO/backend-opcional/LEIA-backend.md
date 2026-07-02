# Sobre o backend opcional

O `promptforge.py` é o **motor de referência** que calcula a densidade semiótica
de forma reproduzível. Use-o se quiser o número exato.

⚠️ **As skills (.md) são a versão ATUALIZADA do método.** O `promptforge.py` é de
junho/2026 e está um passo atrás dos refinamentos embutidos nas skills (RFI=FI×DA,
classificação rigorosa priming/enforcement, etc.). Para forjar e temperar, use as
skills; o backend serve só para fechar o número da densidade.

## Como rodar
```
python promptforge.py --domain business "seu pedido cru"
```
Domínios: juridico · business · engenharia · pesquisa · marketing · medico
Sem Python? Abra o `colab-fallback.ipynb` no Google Colab — roda no navegador.
