//curl -L -o json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
//g++ -std=c++11 -o client client.cpp -lcurl
//./client

#include <iostream>
#include <string>
#include <curl/curl.h>
// Inclui a biblioteca json.hpp para manipulação de JSON
#include "json.hpp"

// Define um alias para facilitar o uso da biblioteca JSON
using json = nlohmann::json;

using namespace std;

// Classe para cliente de validação de CPF
class CPFCliente {
private:
    string base_url;
    
    // Função callback estática chamada pelo cURL para escrever dados recebidos
    static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
        ((string*)userp)->append((char*)contents, size * nmemb);
        return size * nmemb;
    }

public:
    CPFCliente() : base_url("http://localhost:8080") {}
    
    // Método para validar CPF usando requisição HTTP GET
    void validar(const string& cpf) {
        // Inicializa uma sessão cURL
        CURL *curl = curl_easy_init();

        // Monta a URL com o parâmetro CPF na query string
        string endpoint = base_url + "/validar";
        string dados = "?cpf=" + cpf;
        string url = endpoint + dados;
        // Buffer para armazenar a resposta do servidor
        string readBuffer;

        // Configura a URL da requisição
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        // Executa a requisição HTTP GET
        CURLcode res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);

        // Faz o parse da string JSON recebida
        json j = json::parse(readBuffer);
        
        bool ok_get = j["valido"].get<bool>();
        cout << "CPF " << cpf << (ok_get ? " válido\n" : " inválido\n");
    }
};

int main() {
        // Cria uma instância do cliente e valida o CPF
    CPFCliente cliente;
    cliente.validar("11144477735");
    cliente.validar("11111111111");

    return 0;
}
