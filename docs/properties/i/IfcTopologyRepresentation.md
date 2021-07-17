IfcTopologyRepresentation
=========================

_IfcTopologyRepresentation_ represents the concept of a particular topological representation of a product or a product component within a representation context. This representation context does not need to be (but may be) a geometric representation context. Several representation types for shape representation are included as predefined types:

<table>
  <tbody>
    <tr>
      <td><b>Vertex</b></td>
      <td>topological vertex
representation (with or without assigned geometry)</td>
    </tr>
    <tr>
      <td><b>Edge</b></td>
      <td>topological edge
representation (with or without assigned geometry)</td>
    </tr>
    <tr>
      <td><b>Path</b></td>
      <td>topological path
representation (with or without assigned geometry)</td>
    </tr>
    <tr>
      <td><b>Face</b></td>
      <td>topological face
representation (with or without assigned geometry)</td>
    </tr>
    <tr>
      <td><b>Shell</b></td>
      <td>topological shell
representation (with or without assigned geometry)</td>
    </tr>
    <tr>
      <td><b>Undefined</b></td>
      <td>no constraints imposed</td>
    </tr>
  </tbody>
</table>

The representation type is given as a string value at the inherited attribute '_RepresentationType_'.

> HISTORY&nbsp; New entity in IFC2x2.
