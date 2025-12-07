# Importa o módulo subprocess para executar comandos do sistema operacional
import subprocess
# Importa o módulo sys para acessar argumentos da linha de comando e sair do programa
import sys

# Define a função para encerrar processos que estão usando uma porta específica
def kill_process_on_port(port):
    # Tenta executar o código dentro do bloco try
    try:
        # Encontra o PID do processo usando a porta
        # Comando: lsof lista processos, -i :{port} filtra pela porta
        # grep LISTEN filtra apenas processos em modo LISTEN (escutando)
        # awk '{print $2}' extrai a segunda coluna (PID)
        command = f"lsof -i :{port} | grep LISTEN | awk '{{print $2}}'"
        # Executa o comando no shell, capturando stdout e stderr como texto
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Remove espaços em branco no início/fim e divide por quebra de linha
        # Isso cria uma lista de PIDs (pode ter múltiplos processos na mesma porta)
        pids = result.stdout.strip().split('\n')

        # Verifica se há PIDs encontrados e se o primeiro não está vazio
        if pids and pids[0]:
            # Imprime os PIDs encontrados na porta especificada
            print(f"Processos encontrados na porta {port}: {', '.join(pids)}")
            # Itera sobre cada PID encontrado
            for pid in pids:
                # Tenta encerrar cada processo
                try:
                    # Executa o comando kill -9 (força o encerramento) no PID
                    # check=True faz com que lance exceção se o comando falhar
                    subprocess.run(f"kill -9 {pid}", shell=True, check=True)
                    # Imprime mensagem de sucesso para o PID encerrado
                    print(f"Processo {pid} encerrado com sucesso.")
                except subprocess.CalledProcessError:
                    # Se não conseguir encerrar o processo, imprime mensagem de erro
                    print(f"Não foi possível encerrar o processo {pid}.")
            # Imprime mensagem confirmando que a porta foi liberada
            print(f"Porta {port} liberada.")
        else:
            # Se não encontrou nenhum processo, imprime mensagem informativa
            print(f"Nenhum processo encontrado escutando na porta {port}.")

    # Captura qualquer exceção genérica que possa ocorrer
    except Exception as e:
        # Imprime a mensagem de erro
        print(f"Ocorreu um erro: {e}")

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Verifica se o número de argumentos da linha de comando é menor que 2
    # (o primeiro argumento é sempre o nome do script)
    if len(sys.argv) < 2:
        # Imprime instruções de uso do script
        print("Uso: python matar_servidor.py <porta>")
        # Encerra o programa com código de erro 1
        sys.exit(1)
    
    # Tenta converter o segundo argumento (porta) para inteiro
    try:
        # Converte o segundo argumento (sys.argv[1]) para inteiro
        port = int(sys.argv[1])
        # Chama a função para encerrar processos na porta especificada
        kill_process_on_port(port)
    except ValueError:
        # Se a conversão falhar (porta não é um número), imprime erro
        print("Erro: A porta deve ser um número inteiro.")
        # Encerra o programa com código de erro 1
        sys.exit(1)
