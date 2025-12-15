projet = QgsProject.instance()
coucheReg = projet.mapLayersByName("regio_s")[0]
print(coucheReg)
--------------------------------------------------------
options= coucheReg.dataProvider().capabilities()
if options & QgsVectorDataProvider.DeleteFeatures:
    sup = coucheReg.dataProvider().deleteFeatures([2,5])
    coucheReg.triggerRepaint()
    
**********************************************************
    