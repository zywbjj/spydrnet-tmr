def uniquify_nmr_property(replicas, property_keys, suffix="NMR"):
    """
    Make a specific property have a unique value between nmr replicas. Doing this prevents errors in programs like Vivado when a modified netlist is read in.

    **Example:**
    
    .. code-block::
    
        replicas = sdn_TMR.apply_nmr(items_to_replicate, 3, name_suffix='TMR', rename_original=True)
        sdn_TMR.uniquify_nmr_property(replicas, {'HBLKNM', 'HLUTNM', 'SOFT_HLUTNM'}, "TMR")

    :param replicas: the map from an original element to its replicas generated by :ref:`apply_nmr`
    :param property_keys: A set of property keys whose values should be made unique.
    :param suffix: a suffix to append to the value of the property with a unique index further appended.
    :return:
    """
    if isinstance(property_keys, str):
        property_keys = {property_keys}
    else:
        property_keys = set(property_keys)
    property_keys_lower = {x.lower() for x in property_keys}
    for original, copies in replicas.items():
        _update_edif_properties(original, property_keys, property_keys_lower, suffix + '_0')
        for copy_index, copy in enumerate(copies, 1):
            _update_edif_properties(copy, property_keys, property_keys_lower, suffix + '_' + str(copy_index))


def _update_edif_properties(element, property_keys, property_keys_lower, suffix):
    if 'EDIF.properties' in element:
        edif_properties = element['EDIF.properties']
        for property in edif_properties:
            if ('identifier' in property and property['identifier'].lower() in property_keys_lower) or \
                    ('original_identifier' in property and property['original_identifier'] in property_keys):
                if 'value' in property:
                    value = property['value']
                    if isinstance(value, str):
                        property['value'] = value + '_' + suffix
    elif "VERILOG.InlineConstraints" in element:
        properties = element["VERILOG.InlineConstraints"]
        # print(properties.__class__)
        new_properties = dict()
        for prop_0, prop_1 in properties.items():
            if any(prop_key in prop_0.lower() for prop_key in property_keys_lower):
                # print("HERE " + prop_0 + " : " + prop_1)
                value = prop_1
                if isinstance(value, str):
                    prop_1 = value[:len(value)-1] + "_" + suffix + value[len(value)-1]
            new_properties[prop_0] = prop_1
        element["VERILOG.InlineConstraints"] = new_properties

    else:
        None
