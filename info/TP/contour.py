def contour (im, seuil):
    """im : image en niveau de gris
    renvoie une image en niveau de gris"""
    nb_lig ,nb_col = im. shape
    im2 =np. zeros (( nb_lig ,nb_col))
    for i in range (1, nb_lig -1):
        for j in range (1, nb_col -1):
            p1= im [i-1,j]
            p2= im [i,j-1]
            p3= im [i+1,j]
            p4= im [i,j+1]
            norme =np.sqrt ((p1-p3 )**2+( p2-p4 )**2)
            if norme > seuil :
                im2 [i,j]=1
    return im2

##Question 9 : test
im_contour=contour(imC,0.2)
plt.figure("Ciel : contour")
plt.imshow(im_contour,cmap='gray')