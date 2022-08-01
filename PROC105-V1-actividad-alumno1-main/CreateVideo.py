import os
import cv2


path =r"C:\Users\malak\Downloads\PROC105-V1-actividad-alumno1-main\PROC105-V1-actividad-alumno1-main\Images"

#Variable para guardar las imagenes en lista
images = []

#Para recorrer toda la carpeta de imagenes
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)

        #agrega cada archivo a la matriz de images    
        images.append(file_name)
        
#Muestra el numero de imagenes que se guardaron en la lista
print(len(images))
#se guarda el numero de imagenes
count = len(images)
 
frame=cv2.imread(images[0])
#shape es una intruccion que ya da num. de filas, num. de columnas y canles de cada imagen
height,width,channels=frame.shape
size=(width,height)

#(nombre.mp4, codigo de 4 digitos que comprime los fotogramas, num. de fotogramas por segundo, tamaño)
video=cv2.VideoWriter("atardecer.mp4",cv2.VideoWriter_fourcc(*'DIVX'),25,size)

for i in range(0,count-1):
    frame=cv2.imread(images[i])
    video.write(frame)
#release es para cerrar el video
video.release()
print("listo")