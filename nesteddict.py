#nested dictionary
parent_child = {
    "child1": {
        "name": "jorg",
        "age":  22
    },

    "child": {
        "name": "bush",
        "age":  30
    }
}

parent_brother = {
    "brother1": {
        "name": "jonze",
        "age": 43
    },

    "brother2": {
        "name": "bus",
        "age": 65
    }

}
print(parent_brother)

print('create one dictionary from multiole dict')
parent_family = {
    'parents_child': parent_child,
    'parents_brotehr': parent_brother
}
print(parent_family)