# Import the required module
from skimage import exposure
from PDI.src.pdi_utils import show_image,  load_aerial_image
from scipy.stats import entropy
import matplotlib.pyplot as plt
import numpy as np

def compute_entropy(labels, base=None):
    value,counts = np.unique(labels[0], return_counts=True)
    return entropy(counts, base=base)

image_aerial = load_aerial_image()

# calcular e mostrar o histograma da imagem
hist_n_eq = plt.hist(image_aerial.ravel(), bins=256, range=(0,1.0))
plt.show()

# realizar a equalização do histograma
image_eq =  exposure.equalize_hist(image_aerial)

# calcular e mostrar o histograma da imagem equalizada
hist_eq = plt.hist(image_eq.ravel(), bins=256, range=(0,1.0))
plt.show()

# determinar a média do valor dos pixels que ocorrem na imagem não equalizada
img_mean_n_eq = np.mean(image_aerial)*255

# determinar a média do valor dos pixels que ocorrem na imagem equalizada
img_mean_eq = np.mean(image_eq)*255

# determinar a variância do valor dos pixels que ocorrem na imagem não equalizada
img_var_n_eq = np.var(image_aerial)*255

# determinar a variância do valor dos pixels que ocorrem na imagem equalizada
img_var_eq = np.var(image_eq)*255

# determinar os pixels que contêm baixa intensidade na escala de preto na imagem não equalizada
intensidade = 0.2
low_freq_region_n_eq = image_aerial <= intensidade

# determinar os pixels que contêm baixa intensidade na escala de preto na imagem equalizada
low_freq_region_eq = image_eq <= intensidade

# determinar a média do valor dos pixels de baixa intensidade na imagem não equalizada
mean_pixel_low_freq_n_eq = np.mean(image_aerial[low_freq_region_n_eq])

# determinar a média do valor dos pixels de baixa intensidade na imagem equalizada
mean_pixel_low_freq_eq = np.mean(image_eq[low_freq_region_eq])

# determinar a entropia do histograma da imagem não equalizada
hist_entropy_n_eq = compute_entropy(hist_n_eq, base=2)

# determinar a entropia do histograma da imagem equalizada
hist_entropy_eq = compute_entropy(hist_eq, base=2)

#Mostrar os valores calculdos
print("média de valores de pixel na imagem não eq: ",img_mean_n_eq )
print("média de valores de pixel  na imagem eq: ",img_mean_eq )

print("variância de valores de pixel na imagem não eq: ",img_var_n_eq )
print("variância de valores de pixel  na imagem eq: ",img_var_eq)

print("entropia de valores do histograma da imagem não eq: ",hist_entropy_n_eq )
print("entropia de valores do histograma da imagem eq: ", hist_entropy_eq)

print("número de pixels com intensidade menor que ", intensidade , " na imagem não eq: ",low_freq_region_n_eq.sum())
print("número de pixels com intensidade menor que ", intensidade , " na imagem eq: ", low_freq_region_eq.sum())

print("média de valores dos pixels de baixa intensidade na imagem não eq: ",mean_pixel_low_freq_n_eq)
print("média de valores dos pixels de baixa intensidade na imagem eq: ",mean_pixel_low_freq_eq)

# Show the original and resulting image
show_image(image_aerial, 'Original')

show_image(image_eq, 'Resulting image')