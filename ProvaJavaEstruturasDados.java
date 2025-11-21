/**
 * Solução da Prova - Estruturas de Dados
 * Implementação dos métodos solicitados para manipulação de carros
 * utilizando Fila Dinâmica com Dupla Terminação (DEQue) e Pilha Dinâmica (Stack)
 */

/**
 * Classe Car representando um carro com suas características
 */
class Car {
    private String licensePlate;  // Identificador único, não pode ser nulo
    private String mark;
    private String model;
    private String color;
    private String ownerName;
    
    /**
     * Construtor da classe Car
     * @param licensePlate Placa do carro (não pode ser nula)
     * @param mark Marca do carro
     * @param model Modelo do carro
     * @param color Cor do carro
     * @param ownerName Nome do proprietário
     */
    public Car(String licensePlate, String mark, String model, String color, String ownerName) {
        if (licensePlate == null) {
            throw new IllegalArgumentException("License plate cannot be null");
        }
        this.licensePlate = licensePlate;
        this.mark = mark;
        this.model = model;
        this.color = color;
        this.ownerName = ownerName;
    }
    
    // Getters e Setters
    public String getLicensePlate() {
        return licensePlate;
    }
    
    public void setLicensePlate(String licensePlate) {
        if (licensePlate == null) {
            throw new IllegalArgumentException("License plate cannot be null");
        }
        this.licensePlate = licensePlate;
    }
    
    public String getMark() {
        return mark;
    }
    
    public void setMark(String mark) {
        this.mark = mark;
    }
    
    public String getModel() {
        return model;
    }
    
    public void setModel(String model) {
        this.model = model;
    }
    
    public String getColor() {
        return color;
    }
    
    public void setColor(String color) {
        this.color = color;
    }
    
    public String getOwnerName() {
        return ownerName;
    }
    
    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }
    
    @Override
    public String toString() {
        return "Car{" +
                "licensePlate='" + licensePlate + '\'' +
                ", mark='" + mark + '\'' +
                ", model='" + model + '\'' +
                ", color='" + color + '\'' +
                ", ownerName='" + ownerName + '\'' +
                '}';
    }
}

public class ProvaJavaEstruturasDados {
    DEQueable<Car> queueCars = new LinkedDEQue<>(20);
    Stackable<Car> stackCars = new LinkedStack<>(20);
    /**
     * Remove e retorna um carro da fila com dupla terminação cuja placa corresponde ao valor fornecido.
     * @param licensePlate Placa do carro a ser removido
     * @return O carro removido se encontrado, null caso contrário
     */
    public Car deleteCar(String licensePlate) {
        DEQueable<Car> tempQueue = new LinkedDEQue<>(20);
        Car foundCar = null;
        while (!queueCars.isEmpty()) {
            Car currentCar = queueCars.dequeue();
            if (currentCar.getLicensePlate().equalsIgnoreCase(licensePlate)) {
                foundCar = currentCar;
                break;
            } else {
                tempQueue.enqueue(currentCar);
            }
        }
        while (!queueCars.isEmpty()) {
            tempQueue.enqueue(queueCars.dequeue());
        }
        queueCars = tempQueue;
        return foundCar;
    }

/**
 * Retorna um array contendo todos os carros da fila com dupla terminação 
 * cujo modelo corresponde ao informado.
 * @param model Modelo dos carros a serem buscados
 * @return Array contendo todos os carros com o modelo especificado, 
 *         ou array vazio se nenhum for encontrado
 */
public Car[] getCarsByModel(String model) {   
    DEQueable<Car> tempQueue = new LinkedDEQue<>(20);
    DEQueable<Car> resultQueue = new LinkedDEQue<>(20);
    while (!queueCars.isEmpty()) {
        Car currentCar = queueCars.dequeue();
        if (model.equalsIgnoreCase(currentCar.getModel())) {
            resultQueue.enqueue(currentCar);
        }
        tempQueue.enqueue(currentCar);
    }
    queueCars = tempQueue;
    return toArray(resultQueue);
}

    /**
     * Retorna (sem remover) um carro da pilha cuja placa corresponde ao valor informado.
     * @param licensePlate Placa do carro a ser buscado
     * @return O carro encontrado se existir, null caso contrário
     */
    public Car getCarByLicensePlate(String licensePlate) {      
        Stackable<Car> tempStack = new LinkedStack<>(20);
        Car foundCar = null;   
        while (!stackCars.isEmpty()) {
            Car currentCar = stackCars.pop();
            if (currentCar.getLicensePlate().equalsIgnoreCase(licensePlate)) {
                foundCar = currentCar;
                tempStack.push(currentCar);
                break;
            }
        }
        while (!tempStack.isEmpty()) {
            stackCars.push(tempStack.pop());
        }   
        return foundCar;
    }

    /**
     * Remove todos os carros da pilha cujo dono coincide com o valor informado.
     * @param ownerName Nome do proprietário dos carros a serem removidos
     */
    public void removeCarsByOwner(String ownerName) {
        Stackable<Car> tempStack = new LinkedStack<>(20);
        while (!stackCars.isEmpty()) {
            Car currentCar = stackCars.pop();    
            if (!ownerName.equalsIgnoreCase(currentCar.getOwnerName())) {
                tempStack.push(currentCar);
            }
        }
        while (!tempStack.isEmpty()) {
            stackCars.push(tempStack.pop());
        }
    }

    /**
     * Converte uma fila com dupla terminação (DEQue) em um array de Car.
     * @param queue Fila com dupla terminação contendo os carros
     * @return Array contendo todos os carros da fila, ou array vazio se a fila estiver vazia
     */
    private Car[] toArray(DEQueable<Car> queue) {
        if (queue == null || queue.isEmpty()) {
            return new Car[0];
        }
        
        // Criar uma lista temporária para armazenar os elementos
        java.util.ArrayList<Car> list = new java.util.ArrayList<>();
        
        // Criar uma fila auxiliar para preservar a fila original
        DEQueable<Car> tempQueue = new LinkedDEQue<>(queue.size());
        
        // Percorrer toda a fila e adicionar os elementos na lista
        while (!queue.isEmpty()) {
            Car currentCar = queue.dequeue();
            list.add(currentCar);
            tempQueue.enqueue(currentCar);
        }
        
        // Restaurar a fila original
        while (!tempQueue.isEmpty()) {
            queue.enqueue(tempQueue.dequeue());
        }
        
        // Converter ArrayList para array
        return list.toArray(new Car[0]);
    }
}
