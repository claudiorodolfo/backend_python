// Inclui a biblioteca iostream para entrada e saída padrão (cin, cout, cerr)
#include <iostream>
// Inclui a biblioteca string para manipulação de strings
#include <string>
// Inclui a biblioteca curl/curl.h para fazer requisições HTTP
#include <curl/curl.h>
// Inclui a biblioteca json.hpp para manipulação de JSON
// nlohmann::json — baixe de: https://github.com/nlohmann/json
#include "json.hpp"

// Define um alias para facilitar o uso da biblioteca JSON
using json = nlohmann::json;
// Usa o namespace std para não precisar escrever std:: antes de cada função
using namespace std;

// Função callback estática chamada pelo cURL para escrever dados recebidos
// contents: ponteiro para os dados recebidos
// size: tamanho de cada elemento
// nmemb: número de elementos
// userp: ponteiro para o buffer onde os dados serão armazenados
static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    // Converte userp para string* e adiciona os dados recebidos ao buffer
    ((string*)userp)->append((char*)contents, size * nmemb);
    // Retorna o número de bytes processados (necessário para o cURL)
    return size * nmemb;
}

// Função para validar CPF usando requisição HTTP GET
// cpf: string contendo o CPF a ser validado
// Retorna true se o CPF for válido, false caso contrário
bool validarCPF_GET(const string& cpf) {
    // Inicializa uma sessão cURL
    CURL *curl = curl_easy_init();
    // Se não conseguir inicializar, retorna false
    if (!curl) return false;

    // Monta a URL com o parâmetro CPF na query string
    string url = "http://localhost:8080/validar?cpf=" + cpf;
    // Buffer para armazenar a resposta do servidor
    string readBuffer;

    // Configura a URL da requisição
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    // Define a função callback para escrever os dados recebidos
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    // Define o buffer onde os dados serão escritos
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

    // Executa a requisição HTTP GET
    CURLcode res = curl_easy_perform(curl);
    // Limpa e libera os recursos do cURL
    curl_easy_cleanup(curl);

    // Verifica se a requisição foi bem-sucedida
    if (res != CURLE_OK) {
        // Imprime mensagem de erro no stream de erro padrão
        cerr << "Erro na requisição GET: " << curl_easy_strerror(res) << "\n";
        // Retorna false indicando falha
        return false;
    }

    // Tenta fazer o parse da resposta JSON
    try {
        // Faz o parse da string JSON recebida
        json j = json::parse(readBuffer);
        // Verifica se a resposta contém o campo "valido"
        if (j.contains("valido")) {
            // Retorna o valor booleano do campo "valido"
            return j["valido"].get<bool>();
        } else {
            // Se não contiver o campo esperado, imprime a resposta recebida
            cerr << "Resposta inesperada: " << readBuffer << "\n";
            // Retorna false
            return false;
        }
    } catch (...) {
        // Se houver erro ao fazer parse do JSON, imprime mensagem de erro
        cerr << "Falha ao parsear JSON GET\n";
        // Retorna false
        return false;
    }
}

// Função para validar CPF usando requisição HTTP POST
// cpf: string contendo o CPF a ser validado
// Retorna true se o CPF for válido, false caso contrário
bool validarCPF_POST(const string& cpf) {
    // Inicializa uma sessão cURL
    CURL *curl = curl_easy_init();
    // Se não conseguir inicializar, retorna false
    if (!curl) return false;

    // Define a URL do endpoint
    string url = "http://localhost:8000/cpf";
    // Cria um objeto JSON
    json body;
    // Adiciona o CPF ao objeto JSON
    body["cpf"] = cpf;
    // Converte o objeto JSON para string
    string jsonStr = body.dump();

    // Inicializa a lista de headers HTTP como nullptr
    struct curl_slist *headers = nullptr;
    // Adiciona o header Content-Type indicando que o corpo é JSON
    headers = curl_slist_append(headers, "Content-Type: application/json");

    // Buffer para armazenar a resposta do servidor
    string readBuffer;

    // Configura a URL da requisição
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    // Define os headers HTTP da requisição
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    // Define o corpo da requisição POST (dados JSON)
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonStr.c_str());
    // Define a função callback para escrever os dados recebidos
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    // Define o buffer onde os dados serão escritos
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

    // Executa a requisição HTTP POST
    CURLcode res = curl_easy_perform(curl);
    // Libera a memória alocada para os headers
    curl_slist_free_all(headers);
    // Limpa e libera os recursos do cURL
    curl_easy_cleanup(curl);

    // Verifica se a requisição foi bem-sucedida
    if (res != CURLE_OK) {
        // Imprime mensagem de erro no stream de erro padrão
        cerr << "Erro na requisição POST: " << curl_easy_strerror(res) << "\n";
        // Retorna false indicando falha
        return false;
    }

    // Tenta fazer o parse da resposta JSON
    try {
        // Faz o parse da string JSON recebida
        json j = json::parse(readBuffer);
        // Verifica se a resposta contém o campo "valido"
        if (j.contains("valido")) {
            // Retorna o valor booleano do campo "valido"
            return j["valido"].get<bool>();
        } else {
            // Se não contiver o campo esperado, imprime a resposta recebida
            cerr << "Resposta inesperada: " << readBuffer << "\n";
            // Retorna false
            return false;
        }
    } catch (...) {
        // Se houver erro ao fazer parse do JSON, imprime mensagem de erro
        cerr << "Falha ao parsear JSON POST\n";
        // Retorna false
        return false;
    }
}

// Função principal do programa
int main() {
    // Variável para armazenar o CPF digitado pelo usuário
    string cpf;
    // Solicita ao usuário que digite um CPF
    cout << "Digite um CPF (somente dígitos): ";
    // Lê o CPF digitado pelo usuário
    cin >> cpf;

    // Chama a função para validar CPF via GET e armazena o resultado
    bool ok_get = validarCPF_GET(cpf);
    // Imprime o resultado da validação via GET
    cout << "[GET] CPF " << cpf << (ok_get ? " válido\n" : " inválido\n");

    // Chama a função para validar CPF via POST e armazena o resultado
    bool ok_post = validarCPF_POST(cpf);
    // Imprime o resultado da validação via POST
    cout << "[POST] CPF " << cpf << (ok_post ? " válido\n" : " inválido\n");

    // Retorna 0 indicando que o programa terminou com sucesso
    return 0;
}
