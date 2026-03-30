from app.schemas.pessoas import PessoaCreate, PessoaOut, PessoaUpdate

class PessoasRepository:
    def __init__(self) -> None:
        self._dados: list[PessoaOut] = []
        self._next_id = 1

    def list(self, nome: str | None, email: str | None, ativa: bool | None) -> list[PessoaOut]:
        dados = self._dados
        if nome:
            dados = [p for p in dados if nome.lower() in p.nome.lower()]
        if email:
            dados = [p for p in dados if email.lower() in p.email.lower()]
        if ativa is not None:
            dados = [p for p in dados if p.ativa is ativa]
        return dados

    def get(self, pessoa_id: int) -> PessoaOut | None:
        return next((p for p in self._dados if p.id == pessoa_id), None)

    def create(self, payload: PessoaCreate) -> PessoaOut:
        pessoa = PessoaOut(id=self._next_id, **payload.model_dump())
        self._dados.append(pessoa)
        self._next_id += 1
        return pessoa

    def update(self, pessoa_id: int, payload: PessoaUpdate) -> PessoaOut | None:
        atual = self.get(pessoa_id)
        if not atual:
            return None
        data = atual.model_dump()
        data.update({k: v for k, v in payload.model_dump().items() if v is not None})
        nova = PessoaOut(**data)
        self._dados[self._dados.index(atual)] = nova
        return nova

    def delete(self, pessoa_id: int) -> bool:
        atual = self.get(pessoa_id)
        if not atual:
            return False
        self._dados.remove(atual)
        return True
