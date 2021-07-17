IfcIndexedColourMap
===================

The _IfcIndexedColourMap_ provides the assignment of colour information to individual faces. It is used for colouring faces of tessellated face sets. The _IfcIndexedColourMap_ defines an index into an indexed list of colour information. The _Colours_ are a two-dimensional list of colours provided by three RGB values. The _ColourIndex_ attribute corresponds to the _CoordIndex_ of the _IfcTessellatedFaceSet_ defining the corresponding index list of faces. The Opacity attribute provides the alpha channel for all faces of the tessellated face set.

Figure 1 shows the use of _IfcTriangulatedFaceSet_ with colours per face.

!["IfcIndexedColourMap_01"](../../../../../../figures/ifcindexedcolourmap-fig1.png "Figure 1 &mdash; Indexed colour map")

&nbsp;

<table>
  <tr>
    <td><img src="../../../../../../figures/ifcindexedcolourmap_example-01.png" alt="IfcIndexedColourMap_example-01"></td>
    <td>
      <p>&nbsp;</p>
      Figure 2 illustrates an <i>IfcTriangulatedFaceSet</i> represented by
      <ul>
        <li class="small"><em>IfcTriangulatedFaceSet.CoordIndex</em>: ((1,6,5),(1,2,6), (6,2,7), (7,2,3), (7,8,6), (6,8,5), (5,8,1), (1,8,4), (4,2,1), (2,4,3), (4,8,7), (7,3,4))</li>
        <li class="small"><em>IfcCartesianPointList.CoordList</em>: ((0.,0.,0.), (1.,0.,0.), (1.,1.,0.), (0.,1.,0.), (0.,0.,2.), (1.,0.,2.), (1.,1.,2.), (0.,1.,2.))</li>
        <li class="small"><em>IfcIndexedColourMap.ColourIndex</em>: (1, 1, 2, 2, 3, 3, 1, 1, 1, 1, 1, 1, )</li>
        <li class="small"><em>IfcColourRgbList.ColourList</em>: ((1.,0.,0.), (0.,1.,0.), (1.,1.,0.))</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td><p class="figure">Figure 2 &mdash; Indexed colour map geometry </p></td>
    <td>&nbsp;</td>
  </tr>
</table>

> HISTORY&nbsp; New entity in IFC4.
