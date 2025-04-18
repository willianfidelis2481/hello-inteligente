# Importa a classe datetime do módulo datetime
from datetime import datetime  

# Obtém a hora atual e formata como HH:MM:SS
# datetime.now() retorna a data e hora atuais
# .strftime("%H:%M:%S") formata a hora no formato desejado
hora_atual = datetime.now().strftime("%H:%M:%S")  

# Imprime a mensagem com a hora atual
# f-string (format string) permite incluir variáveis diretamente no texto com {}
print(f"Hello World! Agora são {hora_atual}.")  