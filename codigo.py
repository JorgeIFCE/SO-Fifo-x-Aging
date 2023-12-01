import random
from collections import deque
def fifo(page_references, num_frames):
 frames = deque(maxlen=num_frames) #numero de frames usados 
 page_faults = 0 #numero de faltas de paginas
# Função que verifica se a pagina já esta na memoria, se não estiver ele incrementa do numero de 
faltas de paginas e substitui pela mais antiga
 for page in page_references:
 if page not in frames:
 frames.append(page)
 page_faults += 1
 return page_faults
def aging(page_references, num_frames):
 frames = {page: 0 for page in range(num_frames)}
 page_faults = 0
 aging_factor = 0.5
# Função que verifica se a pagina já esta na memoria, se não estiver ele incrementa do numero de 
faltas de paginas e substitui pela mais antiga q n foi usada recentemente
 for i, page in enumerate(page_references):
 if page not in frames:
 page_faults += 1
 oldest_page = min(frames, key=frames.get)
 frames.pop(oldest_page)
 frames[page] = 0
 for frame in frames:
 frames[frame] >>= 1
 frames[page] |= (1 << (8 - 1))
 return page_faults
# Gera as paginas que serão usadas nos algoritmos
def generate_page_references(num_references, num_pages):
 return [random.randint(0, num_pages - 1) for _ in range(num_references)]
# Simula o algoritmo de paginação
def simulate_paging_algorithm(algorithm, page_references, num_frames):
 total_faults = 0
 for i in range(0, len(num_frames)):
 total_faults += algorithm(page_references, num_frames[i])
 return total_faults / len(num_frames)
# Definindo os parametros do algoritmo ao ser rodado
def main():
num_references = 1000
 num_pages = 100
 num_simulations = 10
 num_frames_list = [1, 2, 3, 4, 5]
 page_references = generate_page_references(num_references, num_pages)
# Resultados da FIFO
 print("Simulando o FIFO:")
 for num_frames in num_frames_list:
 avg_faults = simulate_paging_algorithm(fifo, page_references, [num_frames] * 
num_simulations)
 print(f"Media de faltas de paginas depois de 10 simulações (Frames={num_frames}): 
{avg_faults:.2f}")
# Resultados do Agin
 print("\nSimulando o Aging:")
 for num_frames in num_frames_list:
 avg_faults = simulate_paging_algorithm(aging, page_references, [num_frames] * 
num_simulations)
 print(f"Media de faltas de paginas depois de 10 simulações (Frames={num_frames}): 
{avg_faults:.2f}")
if __name__ == "__main__":
 main()
