class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu_nome = gpu_nome
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    def mostrar_configuracao(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostrar_gpu()
        self.cpu.mostrar_cpu()

    class GPU:
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memmoria_gb = memoria_gb

        def mostrar_gpu(self):
            print(f'GPU: {self.nome} - {self.memmoria_gb}')

    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def mostrar_cpu(self):
            print(f'{self.nome} - {self.cores} - {self.clock_ghz}')


pc1 = Computador('Dell XPS', 'NVIDIA RTX 4090', 24, 'Core I5', 6, 3.4)
pc1.mostrar_configuracao()
