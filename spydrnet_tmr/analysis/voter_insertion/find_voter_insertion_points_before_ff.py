"""
Find voter insertion points before every flip-flip
"""
import spydrnet as sdn

DATA_IN_PORT_NAME = "D"


def find_voter_insertion_points_before_ff(
    endpoints_to_replicate,
    primitive_names,
):
    """
    Find voter insertion points before every flip-flip

    Search for every flip-flip in the design within the endpoints to be
    replicated list that match the given flip-flip primitive names, and for
    each flip-flop find the pin connected to the data-in pin and
    add it to the insertion points set.

    :param endpoints_to_replicate: All hierarchical instances and ports to be replicated. This list determines the places that voters will need to be inserted.
    :param ff_primitive_names: Strings for flip-flop primitve names found in the design so that the algorithm can locate each of them.

    :return insertion_points: Set of pins at each point in the netlist
        where voters will be inserted.
    """
    endpoints_to_replicate = set(endpoints_to_replicate)
    primitive_names = set(primitive_names)

    insertion_points = set()

    # Identify all flip-flop instances
    for endpoint in [
        endpoint
        for endpoint in endpoints_to_replicate
        if isinstance(endpoint.item, sdn.ir.instance.Instance)
        and endpoint.item.reference.name in primitive_names
    ]:
        # Find the data-in pin for flip-flop
        for pin in endpoint.item.get_pins(selection=sdn.OUTSIDE):
            for port in [
                port
                for port in pin.get_ports()
                if port.name is DATA_IN_PORT_NAME
            ]:
                insertion_points.add(pin)

    print(
        "Identified {} insertion points for feedback voters before flip-flops.".format(
            len(insertion_points)
        )
    )

    return insertion_points
