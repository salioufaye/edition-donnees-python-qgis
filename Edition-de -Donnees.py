//Supprimer des element
projet = QgsProject.instance()
coucheReg = projet.mapLayersByName("regio_s")[0]
print(coucheReg)
--------------------------------------------------------
options= coucheReg.dataProvider().capabilities()
if options & QgsVectorDataProvider.DeleteFeatures:
    sup = coucheReg.dataProvider().deleteFeatures([2,5])
    coucheReg.triggerRepaint()
    
**********************************************************

*****************Ajouter des données:**************************
options= coucheReg.dataProvider().capabilities()
if options & QgsVectorDataProvider.AddFeatures:
    entite = QgsFeature(coucheReg.fields())
    entite.stAttributes(["2", "Saguenay-Lac-Saint-Jean"])
    # ajouter la geometriesChanged
    (res, ouFeats) = entite.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(coordX; coordY)))
    coucheReg.dataProvider().addFeatures([entite])
    print(res, ouFeats)
    coucheReg.triggerRepaint()

******************************************************************************************************


    

