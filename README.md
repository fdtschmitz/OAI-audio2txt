# Como gerar atas de reuniões usando o ChatGPT

Ter uma IA para transcrever reuniões oferece uma maior precisão e velocidade na captura de informações discutidas, além de possibilitar a busca e análise rápida de conteúdo posteriormente, otimizando o tempo e aumentando a eficiência da equipe.

O objetivo deste artigo é mostrar como a simples implementação da API da OpenAI pode se tornar uma ferramenta poderosa de produtividade.

### Como funciona?

Dentre as diversas funcionalidades da API disponibilizada pela OpenAI, temos o modelo [Whisper](https://openai.com/research/whisper). Este modelo tem a capacidade tanto de transcrever como traduzir audios. Para nossa implementação, iremos utilizar o modo de transcrição. Neste modo, a API recebe o arquivo de audio como entrada e o formato de saída. Por padrão a resposta é dada em um json com o texto bruto incluído. 

```json
{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger.
....
}
```

Aliado ao modelo Whisper, também utilizaremos o modelo GPT ([GPT-4](https://openai.com/gpt-4) ou [GPT-3.5 Turbo](https://platform.openai.com/docs/guides/chat)) para analizar o texto e produzir os resultados que esperamos. Com uma requisição você envia uma lista de mensagens, onde para cada mensagem é atribuida uma função (`system`, `user`, `assistant`). Estas funções servem para determinar o comportamento do modelo, bem como determinar o que esperamos de resposta.

A documentação oficial possui excelentes exemplos de utilização, tanto para o [Whisper](https://platform.openai.com/docs/api-reference/audio) quanto para o [Chat](https://platform.openai.com/docs/api-reference/chat).

### Restrições

O modelo GPT, assim como outros modelos de linguagem, trabalha com o conceito de `tokens` que podem ser entendidos como pedaços de texto. Um `token` pode ser apenas um caractere ou uma palavra inteira (ex. `a` ou `banana`). Em alguns idiomas, um `token` pode ser ainda menor que um caracter ou conter mais de uma palavra.

Por exemplo, a string `"ChatGPT is great!"` é codificada em 6 `tokens`: `["Chat","G", "PT", " is", " great", "!"]`.

O numero total de `tokens` afeta diretamente no uso da API. Seja na usabilidade, preço de utilização ou quantidamente máxima aceita pelo modelo. Além disso, ambos `tokens` de entrada e saída são contabilizados. Por exemplo, se a requisição enviada possui 10 `tokens` e a resposta possui 20 `tokens`, a cobrança será feita por 30 `tokens`. Você pode ver o preço cobrado por `token` [aqui](https://openai.com/pricing).

A quantidade máxima aceita varia de acordo com o modelo adotado. Por exemplo, o `GPT-3.5-Turbo-0125` pode receber até 16.385 `tokens`, porém sua resposta está limitada a 4.096 `tokens`. [Nesta página](https://platform.openai.com/docs/models/continuous-model-upgrades) você pode visualizar as limitações de cada modelo.

Para o Whisper, os arquivos de áudio devem ter no máximo 25mb e os formatos aceitos são: `mp3`, `mp4`, `mpeg`, `mpga`, `m4a`, `wav` e `webm`. Além disso, o modelo possui atualmente o custo de $0.006 dólares por minuto.

---

“Talk is chep, show me the code!” Agora vamos ao que interessa 🧑🏽‍💻

### Capítulos

...em breve