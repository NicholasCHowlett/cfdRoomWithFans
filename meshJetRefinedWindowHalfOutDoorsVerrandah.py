#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/nicho/Documents/devProjects/cfd/cfdMeshes')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_2 = geompy.MakeVertex(10, 0, 0)
Vertex_3 = geompy.MakeVertex(10, 2.5, 0)
Vertex_4 = geompy.MakeVertex(5, 2.5, 0)
Vertex_5 = geompy.MakeVertex(5, 2.1, 0)
Vertex_6 = geompy.MakeVertex(4.8, 2.1, 0)
Vertex_6_2 = geompy.MakeVertex(4.8, 2.5, 0)
Vertex_7 = geompy.MakeVertex(4.8, 2.9, 0)
Vertex_8 = geompy.MakeVertex(0, 2.5, 0)
Vertex_9 = geompy.MakeVertex(0, 2.1, 0)
Vertex_10 = geompy.MakeVertex(-0.2, 2.1, 0)
Vertex_11 = geompy.MakeVertex(-0.2, 2.6, 0)
Vertex_12 = geompy.MakeVertex(-4.2, 2.5, 0)
Vertex_13 = geompy.MakeVertex(-4.2, 0, 0)
Vertex_18 = geompy.MakeVertex(0, 1.8, 0)
Vertex_19 = geompy.MakeVertex(0, 1.7, 0)
Vertex_20 = geompy.MakeVertex(-0.5, 1.7, 0)
Vertex_21 = geompy.MakeVertex(-0.5, 1.8, 0)
Vertex_22 = geompy.MakeVertex(2, 1.8, 0)
Vertex_23 = geompy.MakeVertex(2, 1.7, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_13, Vertex_2)
Line_2 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
Line_3 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_4)
Line_4 = geompy.MakeLineTwoPnt(Vertex_4, Vertex_5)
Line_5 = geompy.MakeLineTwoPnt(Vertex_5, Vertex_6)
Line_6 = geompy.MakeLineTwoPnt(Vertex_6, Vertex_6_2)
Line_6_2 = geompy.MakeLineTwoPnt(Vertex_6_2, Vertex_7)
Line_7 = geompy.MakeLineTwoPnt(Vertex_7, Vertex_8)
Line_8 = geompy.MakeLineTwoPnt(Vertex_8, Vertex_9)
Line_9 = geompy.MakeLineTwoPnt(Vertex_9, Vertex_10)
Line_10 = geompy.MakeLineTwoPnt(Vertex_10, Vertex_11)
Line_11 = geompy.MakeLineTwoPnt(Vertex_11, Vertex_12)
Line_12 = geompy.MakeLineTwoPnt(Vertex_12, Vertex_13)
Line_17 = geompy.MakeLineTwoPnt(Vertex_18, Vertex_19)
Line_18 = geompy.MakeLineTwoPnt(Vertex_19, Vertex_20)
Line_19 = geompy.MakeLineTwoPnt(Vertex_20, Vertex_21)
Line_17_vertex_2 = geompy.GetSubShape(Line_17, [2])
Line_20 = geompy.MakeLineTwoPnt(Vertex_21, Line_17_vertex_2)
Line_21 = geompy.MakeLineTwoPnt(Vertex_18, Vertex_22)
Line_22 = geompy.MakeLineTwoPnt(Vertex_22, Vertex_23)
Line_23 = geompy.MakeLineTwoPnt(Vertex_23, Vertex_19)
FaceFan = geompy.MakeFaceWires([Line_17, Line_18, Line_19, Line_20], 1)
FaceFanRegion = geompy.MakeFaceWires([Line_21, Line_22, Line_23, Line_17], 1)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
Translation_1 = geompy.MakeTranslation(OZ_1, -0.25, 1.75, 0)
Rotation_1 = geompy.MakeRotation(FaceFan, Translation_1, -20*math.pi/180.0)
Rotation_2 = geompy.MakeRotation(FaceFanRegion, Translation_1, -20*math.pi/180.0)
FaceBuilding = geompy.MakeFaceWires([Line_1, Line_2, Line_3, Line_4, Line_5, Line_6, Line_6_2, Line_7, Line_8, Line_9, Line_10, Line_11, Line_12], 1)
FaceDomain = geompy.MakeCutList(FaceBuilding, [Rotation_1], True)
window = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(window, [28])
walls = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(walls, [10, 16, 20, 26, 18, 22, 14, 24, 12, 8, 3])
fanOutlet = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fanOutlet, [37])
fanInlet = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fanInlet, [33])
fanSides = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(fanSides, [30, 35])
outside = geompy.CreateGroup(FaceDomain, geompy.ShapeType["EDGE"])
geompy.UnionIDs(outside, [6])
[window, walls, fanOutlet, fanInlet, fanSides, outside] = geompy.GetExistingSubObjects(FaceDomain, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_6_2, 'Vertex_6_2' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Vertex_9, 'Vertex_9' )
geompy.addToStudy( Vertex_10, 'Vertex_10' )
geompy.addToStudy( Vertex_11, 'Vertex_11' )
geompy.addToStudy( Vertex_12, 'Vertex_12' )
geompy.addToStudy( Vertex_13, 'Vertex_13' )
geompy.addToStudy( Vertex_18, 'Vertex_18' )
geompy.addToStudy( Vertex_19, 'Vertex_19' )
geompy.addToStudy( Vertex_20, 'Vertex_20' )
geompy.addToStudy( Vertex_21, 'Vertex_21' )
geompy.addToStudy( Vertex_22, 'Vertex_22' )
geompy.addToStudy( Vertex_23, 'Vertex_23' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Line_6, 'Line_6' )
geompy.addToStudy( Line_6_2, 'Line_6_2' )
geompy.addToStudy( Line_7, 'Line_7' )
geompy.addToStudy( Line_8, 'Line_8' )
geompy.addToStudy( Line_9, 'Line_9' )
geompy.addToStudy( Line_10, 'Line_10' )
geompy.addToStudy( Line_11, 'Line_11' )
geompy.addToStudy( Line_12, 'Line_12' )
geompy.addToStudy( Line_17, 'Line_17' )
geompy.addToStudy( Line_18, 'Line_18' )
geompy.addToStudy( Line_19, 'Line_19' )
geompy.addToStudyInFather( Line_17, Line_17_vertex_2, 'Line_17:vertex_2' )
geompy.addToStudy( Line_20, 'Line_20' )
geompy.addToStudy( Line_21, 'Line_21' )
geompy.addToStudy( Line_22, 'Line_22' )
geompy.addToStudy( Line_23, 'Line_23' )
geompy.addToStudy( FaceFan, 'FaceFan' )
geompy.addToStudy( FaceFanRegion, 'FaceFanRegion' )
geompy.addToStudy( OZ_1, 'OZ' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Rotation_1, 'Rotation_1' )
geompy.addToStudy( Rotation_2, 'Rotation_2' )
geompy.addToStudy( FaceBuilding, 'FaceBuilding' )
geompy.addToStudy( FaceDomain, 'FaceDomain' )
geompy.addToStudyInFather( FaceDomain, window, 'window' )
geompy.addToStudyInFather( FaceDomain, walls, 'walls' )
geompy.addToStudyInFather( FaceDomain, fanOutlet, 'fanOutlet' )
geompy.addToStudyInFather( FaceDomain, fanInlet, 'fanInlet' )
geompy.addToStudyInFather( FaceDomain, fanSides, 'fanSides' )
geompy.addToStudyInFather( FaceDomain, outside, 'outside' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

MeshDomain = smesh.Mesh(FaceDomain)
NETGEN_1D_2D = MeshDomain.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN2D_0_1_0_01 = NETGEN_1D_2D.Parameters()
NETGEN2D_0_1_0_01.SetMaxSize( 0.1 )
NETGEN2D_0_1_0_01.SetMinSize( 0.01 )
NETGEN2D_0_1_0_01.SetSecondOrder( 0 )
NETGEN2D_0_1_0_01.SetOptimize( 1 )
NETGEN2D_0_1_0_01.SetFineness( 2 )
NETGEN2D_0_1_0_01.SetChordalError( -1 )
NETGEN2D_0_1_0_01.SetChordalErrorEnabled( 0 )
NETGEN2D_0_1_0_01.SetUseSurfaceCurvature( 1 )
NETGEN2D_0_1_0_01.SetFuseEdges( 1 )
NETGEN2D_0_1_0_01.SetUseDelauney( 0 )
NETGEN2D_0_1_0_01.SetQuadAllowed( 0 )
NETGEN2D_0_1_0_01.SetLocalSizeOnShape(Rotation_1, 0.01)
NETGEN2D_0_1_0_01.SetLocalSizeOnShape(Rotation_2, 0.01)
NETGEN2D_0_1_0_01.SetWorstElemMeasure( 79 )
NETGEN2D_0_1_0_01.SetCheckChartBoundary( 96 )
isDone = MeshDomain.Compute()
[ window_extruded, walls_extruded, fanOutlet_extruded, fanInlet_extruded, fanSides_extruded, outside_extruded, smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6 ] = MeshDomain.ExtrusionSweepObjects( [ MeshDomain ], [ MeshDomain ], [ MeshDomain ], [ 0, 0, 0.1 ], 1, 1, [  ], 0, [  ], [  ], 0 )
MeshDomain.RemoveGroup( smeshObj_6 )
MeshDomain.RemoveGroup( smeshObj_5 )
MeshDomain.RemoveGroup( smeshObj_4 )
MeshDomain.RemoveGroup( smeshObj_3 )
MeshDomain.RemoveGroup( smeshObj_2 )
MeshDomain.RemoveGroup( smeshObj_1 )

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN2D_0_1_0_01, 'NETGEN2D_0.1_0.01')
smesh.SetName(window_extruded, 'window_extruded')
smesh.SetName(walls_extruded, 'walls_extruded')
smesh.SetName(fanOutlet_extruded, 'fanOutlet_extruded')
smesh.SetName(fanInlet_extruded, 'fanInlet_extruded')
smesh.SetName(fanSides_extruded, 'fanSides_extruded')
smesh.SetName(outside_extruded, 'outside_extruded')
smesh.SetName(MeshDomain.GetMesh(), 'MeshDomain')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
