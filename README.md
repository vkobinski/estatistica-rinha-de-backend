## Minha análise estatística sobre minha API da Rinha de Backend

### Introdução

Realizei minha submissão para a rinha de backend em Rust. E consegui resultados muito bons, como percentil 75 de 3ms.
E julguei que minha API não era mais rápida por conta das operações simultâneas que realizava.
Então, precisava utilizar dados com várias variáveis para um trabalho de faculdade, e decidi juntar o útil ao agradável.

### Conclusão

Meu chute inicial era que o que mais influenciava no tempo de resposta era a quantidade de operações simultâneas.
Mas utilizando análise estatística, conclui que o que mais interfere é o quão distante do início do teste a operação é realizada.
Basicamente: quanto mais tempo passa, mais rápido ficam as respostas.

### O porquê

Como existem centenas de variáveis nesse sistema, fica muito difícil avaliar o que mais influencia no tempo de resposta, mas a correlação entre o tempo de resposta e o tempo de início da operação em relação ao início do teste é de -50%, logo as grandezas são inversamente proporcionais. Logo, há mais dados que podiam ser extraídos do ambiente que dariam uma análise mais precisa. Mas, isso tudo só prova o quão errado eu estava sobre o gargalo da minha API.
