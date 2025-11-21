/**
 * RESPOSTAS DA PROVA - Estruturas de Dados
 * Apenas os métodos solicitados nas questões
 */

// ============================================================================
// QUESTÃO 1
// ============================================================================

/**
 * Remove e retorna um carro da fila com dupla terminação cuja placa 
 * corresponde ao valor fornecido.
 * 
 * @param queueCars Fila com dupla terminação contendo os carros
 * @param licensePlate Placa do carro a ser removido
 * @return O carro removido se encontrado, null caso contrário
 */
public Car deleteCar(DEQueable<Car> queueCars, String licensePlate) {
    if (queueCars == null || licensePlate == null || queueCars.isEmpty()) {
        return null;
    }
    
    // Criar uma fila auxiliar para armazenar temporariamente os carros
    DEQueable<Car> tempQueue = new LinkedDEQue<>(queueCars.size());
    Car foundCar = null;
    
    // Percorrer toda a fila procurando o carro com a placa especificada
    while (!queueCars.isEmpty()) {
        Car currentCar = queueCars.removeFirst(); // Remove do início
        
        if (currentCar.getLicensePlate().equals(licensePlate)) {
            // Encontrou o carro, não adiciona de volta
            foundCar = currentCar;
        } else {
            // Não é o carro procurado, adiciona na fila temporária
            tempQueue.addLast(currentCar);
        }
    }
    
    // Restaurar todos os carros que não foram removidos
    while (!tempQueue.isEmpty()) {
        queueCars.addLast(tempQueue.removeFirst());
    }
    
    return foundCar;
}

// ============================================================================
// QUESTÃO 2
// ============================================================================

/**
 * Retorna um array contendo todos os carros da fila com dupla terminação 
 * cujo modelo corresponde ao informado.
 * 
 * @param queueCars Fila com dupla terminação contendo os carros
 * @param model Modelo dos carros a serem buscados
 * @return Array contendo todos os carros com o modelo especificado, 
 *         ou array vazio se nenhum for encontrado
 */
public Car[] getCarsByModel(DEQueable<Car> queueCars, String model) {
    if (queueCars == null || model == null || queueCars.isEmpty()) {
        return new Car[0];
    }
    
    // Lista temporária para armazenar os carros encontrados
    java.util.ArrayList<Car> foundCars = new java.util.ArrayList<>();
    
    // Criar uma fila auxiliar para restaurar a fila original
    DEQueable<Car> tempQueue = new LinkedDEQue<>(queueCars.size());
    
    // Percorrer toda a fila procurando carros com o modelo especificado
    while (!queueCars.isEmpty()) {
        Car currentCar = queueCars.removeFirst();
        
        if (model.equals(currentCar.getModel())) {
            // Encontrou um carro com o modelo especificado
            foundCars.add(currentCar);
        }
        
        // Adiciona na fila temporária para restaurar depois
        tempQueue.addLast(currentCar);
    }
    
    // Restaurar todos os carros na fila original
    while (!tempQueue.isEmpty()) {
        queueCars.addLast(tempQueue.removeFirst());
    }
    
    // Converter ArrayList para array
    return foundCars.toArray(new Car[0]);
}

// ============================================================================
// QUESTÃO 3
// ============================================================================

/**
 * Retorna (sem remover) um carro da pilha cuja placa corresponde ao valor informado.
 * 
 * @param stackCars Pilha contendo os carros
 * @param licensePlate Placa do carro a ser buscado
 * @return O carro encontrado se existir, null caso contrário
 */
public Car getCarByLicensePlate(Stackable<Car> stackCars, String licensePlate) {
    if (stackCars == null || licensePlate == null || stackCars.isEmpty()) {
        return null;
    }
    
    // Criar uma pilha auxiliar para restaurar a pilha original
    Stackable<Car> tempStack = new LinkedStack<>(stackCars.size());
    Car foundCar = null;
    
    // Percorrer toda a pilha procurando o carro com a placa especificada
    while (!stackCars.isEmpty()) {
        Car currentCar = stackCars.pop(); // Remove do topo
        
        if (currentCar.getLicensePlate().equals(licensePlate)) {
            // Encontrou o carro
            foundCar = currentCar;
        }
        
        // Adiciona na pilha temporária para restaurar depois
        tempStack.push(currentCar);
    }
    
    // Restaurar todos os carros na pilha original (ordem inversa)
    while (!tempStack.isEmpty()) {
        stackCars.push(tempStack.pop());
    }
    
    return foundCar;
}

// ============================================================================
// QUESTÃO 4
// ============================================================================

/**
 * Remove todos os carros da pilha cujo dono coincide com o valor informado.
 * 
 * @param stackCars Pilha contendo os carros
 * @param ownerName Nome do proprietário dos carros a serem removidos
 */
public void removeCarsByOwner(Stackable<Car> stackCars, String ownerName) {
    if (stackCars == null || ownerName == null || stackCars.isEmpty()) {
        return;
    }
    
    // Criar uma pilha auxiliar para armazenar os carros que não serão removidos
    Stackable<Car> tempStack = new LinkedStack<>(stackCars.size());
    
    // Percorrer toda a pilha removendo carros do proprietário especificado
    while (!stackCars.isEmpty()) {
        Car currentCar = stackCars.pop(); // Remove do topo
        
        if (!ownerName.equals(currentCar.getOwnerName())) {
            // Não é do proprietário especificado, mantém na pilha temporária
            tempStack.push(currentCar);
        }
        // Se for do proprietário especificado, simplesmente não adiciona de volta
    }
    
    // Restaurar os carros que não foram removidos (ordem inversa)
    while (!tempStack.isEmpty()) {
        stackCars.push(tempStack.pop());
    }
}



