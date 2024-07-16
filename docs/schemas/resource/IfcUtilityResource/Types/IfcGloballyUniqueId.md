# IfcGloballyUniqueId

An _IfcGloballyUniqueId_ holds an encoded string identifier that is used to uniquely identify an IFC object. An _IfcGloballyUniqueId_ is a Globally Unique Identifier (GUID) which is an auto-generated 128-bit number. Since this identifier is required for all IFC object instances, it is desirable to compress it to reduce overhead. The encoding of the base 64 character set is shown below:
<!-- end of short definition -->

<pre>
      1     2     3     4     5     6
 0123456789012345678901234567890123456789012345678901234567890123
"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_$";
</pre>


The resulting string is a fixed 22 character length string to be exchanged within the IFC exchange file structure.

The base64 encoding process may differ from common base64 implementations. The following steps are used:

 1. The first byte is encoded in the first two characters
 2. The remaining bytes are encoded in groups of 3, taking up 4 characters

As a result, the first character must be either a 0, 1, 2, or 3.

> EXAMPLE the generated base16 number f70dd363-bfe3-495d-84a0-2c02dcb7d4d2 will compress to 3t3TDZl_D9NOIWB0BSjzJI

> NOTE Refer to the BuildingSMART website ([technical.buildingsmart.org](http://technical.buildingsmart.org)) for more information and sample encoding algorithms.

> HISTORY New type in IFC1.5.1.
