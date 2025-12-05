import subprocess
import sys

def kill_process_on_port(port):
    try:
        # Encontra o PID do processo usando a porta
        command = f"lsof -i :{port} | grep LISTEN | awk '{{print $2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        pids = result.stdout.strip().split('\n')

        if pids and pids[0]:
            print(f"Processos encontrados na porta {port}: {', '.join(pids)}")
            for pid in pids:
                try:
                    subprocess.run(f"kill -9 {pid}", shell=True, check=True)
                    print(f"Processo {pid} encerrado com sucesso.")
                except subprocess.CalledProcessError:
                    print(f"Não foi possível encerrar o processo {pid}.")
            print(f"Porta {port} liberada.")
        else:
            print(f"Nenhum processo encontrado escutando na porta {port}.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python matar_servidor.py <porta>")
        sys.exit(1)
    
    try:
        port = int(sys.argv[1])
        kill_process_on_port(port)
    except ValueError:
        print("Erro: A porta deve ser um número inteiro.")
        sys.exit(1)
