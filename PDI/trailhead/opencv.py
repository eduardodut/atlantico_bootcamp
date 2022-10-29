# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('entrada.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1])
#largura da imagem print('Altura em pixels: ', end='')
print(imagem.shape[0])
#altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
# Importação das bibliotecas  
import cv2   
# Leitura da imagem com a função imread()  
imagem = cv2.imread('entrada.jpg')  


import cv2 
imagem = cv2.imread('ponte.jpg') 
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB 

print('O pixel (0, 0) tem as seguintes cores:') 
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)  

import cv2 
imagem = cv2.imread('ponte.jpg') 
for y in range(0, imagem.shape[0]):
   for x in range(0, imagem.shape[1]):
     imagem[y, x] = (255,0,0)
cv2.imshow("Imagem modificada", imagem) 
import cv2 
imagem = cv2.imread('ponte.jpg') 
for y in range(0, imagem.shape[0], 10): #percorre linhas
   for x in range(0, imagem.shape[1], 10): #percorre colunas
     imagem[y:y+5, x: x+5] = (0,255,255)
cv2.imshow("Imagem modificada", imagem) 
cv2.waitKey(0)  

import cv2
imagem = cv2.imread('ponte.jpg')
recorte = imagem[100:200, 100:200]
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("recorte.jpg", recorte) #salva no disco 