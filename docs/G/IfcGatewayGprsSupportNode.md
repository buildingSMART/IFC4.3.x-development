IfcGatewayGprsSupportNode
=========================
The gateway GPRS support node is a component of the GPRS core network that
extends the GSM to allow packet switching functionalities. This component is
responsible for the internetworking between the GPRS network and external
packet switched networks (e.g. the internet).  
The GGSN converts the GPRS packets coming from the SGSN into the appropriate
packet data protocol (PDP) format (e.g., IP or X.25) and sends them out on the
corresponding Packet Data Network (PDN). In the other direction, PDP addresses
of incoming data packets are converted to the GSM address of the destination
user.  
The GGSN is responsible for IP address assignment and is the default router
for the connected user equipment (UE). The GGSN also performs authentication
and billing functions. The location register function in the GGSN stores
subscription information and routeing information (needed to tunnel packet
data traffic destined for a GPRS MS to the SGSN where the MS is registered)
for each subscriber for which the GGSN has at least one PDP context active.


