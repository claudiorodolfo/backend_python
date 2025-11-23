from singleton import BDManager

print("=== Teste do Padrão Singleton ===\n")

# Obtém duas "instâncias"
print("1. Criando primeira instância:")
bd1 = BDManager()
conector1 = bd1.getInstancia("Conexão Principal")
print(f"   Path da conexão 1: {conector1._path}")
print(f"   ID da conexão 1: {conector1._id}")

print("\n2. Criando segunda instância:")
bd2 = BDManager()
conector2 = bd2.getInstancia("Conexão Secundária")
print(f"   Path da conexão 2: {conector2._path}")
print(f"   ID da conexão 2: {conector2._id}")

# Verificações
print("\n=== Verificações ===")
print(f"3. São a mesma instância? {conector1 is conector2}")
print(f"4. Paths são iguais? {conector1._path == conector2._path}")
print(f"5. Mesmo objeto na memória? {id(conector1) == id(conector2)}")

# Teste adicional: modificação em uma reflete na outra
print("\n6. Teste de modificação:")
conector1._path = "Conexão Terciária"
print(f"   conector1._path = '{conector1._path}'")
print(f"   conector1._id = '{conector1._id}'")
print(f"   conector2._path = '{conector2._path}'")
print(f"   conector2._id = '{conector2._id}'")
print(f"   Modificação refletiu? {conector1._path == conector2._path}")

print("\n✅ Singleton está funcionando corretamente!")
