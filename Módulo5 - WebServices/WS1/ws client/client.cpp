#include <iostream>
#include <string>
#include <curl/curl.h>
#include "json.hpp"  // nlohmann::json — baixe de: https://github.com/nlohmann/json

using json = nlohmann::json;
using namespace std;

static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

bool validarCPF_GET(const string& cpf) {
    CURL *curl = curl_easy_init();
    if (!curl) return false;

    string url = "http://localhost:8000/cpf?numero=" + cpf;
    string readBuffer;

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

    CURLcode res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK) {
        cerr << "Erro na requisição GET: " << curl_easy_strerror(res) << "\n";
        return false;
    }

    try {
        json j = json::parse(readBuffer);
        if (j.contains("valido")) {
            return j["valido"].get<bool>();
        } else {
            cerr << "Resposta inesperada: " << readBuffer << "\n";
            return false;
        }
    } catch (...) {
        cerr << "Falha ao parsear JSON GET\n";
        return false;
    }
}

bool validarCPF_POST(const string& cpf) {
    CURL *curl = curl_easy_init();
    if (!curl) return false;

    string url = "http://localhost:8000/cpf";
    json body;
    body["cpf"] = cpf;
    string jsonStr = body.dump();

    struct curl_slist *headers = nullptr;
    headers = curl_slist_append(headers, "Content-Type: application/json");

    string readBuffer;

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonStr.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

    CURLcode res = curl_easy_perform(curl);
    curl_slist_free_all(headers);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK) {
        cerr << "Erro na requisição POST: " << curl_easy_strerror(res) << "\n";
        return false;
    }

    try {
        json j = json::parse(readBuffer);
        if (j.contains("valido")) {
            return j["valido"].get<bool>();
        } else {
            cerr << "Resposta inesperada: " << readBuffer << "\n";
            return false;
        }
    } catch (...) {
        cerr << "Falha ao parsear JSON POST\n";
        return false;
    }
}

int main() {
    string cpf;
    cout << "Digite um CPF (somente dígitos): ";
    cin >> cpf;

    bool ok_get = validarCPF_GET(cpf);
    cout << "[GET] CPF " << cpf << (ok_get ? " válido\n" : " inválido\n");

    bool ok_post = validarCPF_POST(cpf);
    cout << "[POST] CPF " << cpf << (ok_post ? " válido\n" : " inválido\n");

    return 0;
}
