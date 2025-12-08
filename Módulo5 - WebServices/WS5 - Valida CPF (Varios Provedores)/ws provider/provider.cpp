//curl -L -o httplib.h https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h
//g++ -std=c++11 -o provider provider.cpp -pthread
//./provider
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <map>
#include "httplib.h"

// Serviço fornecido pelo Web Service Provider
class CPFService {
public:
    bool validarCpf(const std::string& cpf) {
        // Remove todos os caracteres não numéricos do CPF, mantendo apenas dígitos
        std::string cpf_limpo = cpf;
        cpf_limpo.erase(std::remove(cpf_limpo.begin(), cpf_limpo.end(), '.'), cpf_limpo.end());
        cpf_limpo.erase(std::remove(cpf_limpo.begin(), cpf_limpo.end(), '-'), cpf_limpo.end());
        
        // Verifica se o CPF tem exatamente 11 dígitos após a limpeza
        if (cpf_limpo.length() != 11) {
            return false;
        }
        
        // Verifica se todos os dígitos são iguais (ex: 11111111111, 22222222222)
        bool todos_iguais = true;
        for (size_t i = 1; i < cpf_limpo.length(); i++) {
            if (cpf_limpo[i] != cpf_limpo[0]) {
                todos_iguais = false;
                break;
            }
        }
        if (todos_iguais) {
            return false;
        }

        // Calcula os dígitos verificadores
        int dig1 = calcDigito(cpf_limpo, 10);
        int dig2 = calcDigito(cpf_limpo, 11);

        // Compara os dois últimos dígitos do CPF com os dígitos calculados
        std::string digitos_calculados = std::to_string(dig1) + std::to_string(dig2);
        std::string digitos_cpf = cpf_limpo.substr(9, 2);
        
        return digitos_cpf == digitos_calculados;
    }

private:
    // Define função interna para calcular um dígito verificador do CPF
    int calcDigito(const std::string& cpf, int peso) {
        int s = 0;
        for (int i = 0; i < peso - 1; i++) {
            s += (cpf[i] - '0') * (peso - i);
        }
        int resto = (s * 10) % 11;
        if (resto == 10) {
            return 0;
        } else {
            return resto;
        }
    }
};

// Função para criar resposta JSON
std::string criarJsonResposta(const std::string& cpf, bool valido) {
    std::ostringstream json;
    json << "{\"cpf\":\"" << cpf << "\",\"valido\":" << (valido ? "true" : "false") << "}";
    return json.str();
}

std::string criarJsonErro(const std::string& mensagem) {
    std::ostringstream json;
    json << "{\"error\":\"" << mensagem << "\"}";
    return json.str();
}

int main() {
    httplib::Server svr;
    CPFService cpfService;

    // Handler para requisições GET /validar
    svr.Get("/validar", [&cpfService](const httplib::Request& req, httplib::Response& res) {
        std::cout << "Requisição GET recebida - Validar CPF" << std::endl;
        
        // Obtém o parâmetro cpf da query string
        auto it = req.params.find("cpf");
        if (it == req.params.end()) {
            res.status = 400;
            res.set_content(criarJsonErro("Parâmetro 'cpf' não fornecido"), "application/json");
            return;
        }
        
        std::string cpf = it->second;
        
        // Realiza a operação de validação
        bool resultado = cpfService.validarCpf(cpf);
        
        // Envia a resposta para o cliente
        res.status = 200;
        res.set_content(criarJsonResposta(cpf, resultado), "application/json");
    });

    // Handler para requisições POST
    svr.Post("/.*", [](const httplib::Request& req, httplib::Response& res) {
        // Este provider só aceita requisições GET
        res.status = 405;  // 405 Method Not Allowed
        res.set_header("Allow", "GET");  // Informa que apenas GET é permitido
        res.set_content(criarJsonErro("Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint."), "application/json");
    });

    // Handler catch-all para retornar 404 quando o endpoint não é /validar
    // Este handler só será chamado se nenhum handler anterior corresponder
    svr.Get(".*", [](const httplib::Request& req, httplib::Response& res) {
        // Verifica se o path não começa com /validar (para evitar conflito com o handler específico)
        if (req.path.find("/validar") != 0) {
            res.status = 404;
            res.set_content(criarJsonErro("Endpoint não encontrado"), "application/json");
        }
    });

    // Handler genérico para retornar 404 em caso de erro
    svr.set_error_handler([](const httplib::Request& req, httplib::Response& res) {
        if (res.status == 404) {
            res.set_content(criarJsonErro("Endpoint não encontrado"), "application/json");
        }
    });

    // Inicia o servidor HTTP na porta 8084
    std::cout << "Servidor iniciado em http://127.0.0.1:8084" << std::endl;
    svr.listen("127.0.0.1", 8084);

    return 0;
}
