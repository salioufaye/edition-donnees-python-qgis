projet = QgsProject.instance()
print(projet)
path ="‪C:/Users/mameg/Downloads/GrandMontreal_Sentinel2.tif"
image = QgsRasterLayer(path, "GrandMontreal_Sentinel2", "gdal")
projet.addMapLayer(image)
image.renderer().setGreenBand(1)
image.renderer().setGreenBand(2)
image.renderer().setGreenBand(3)
image.triggerRepaint()



