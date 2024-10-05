def oxford_comma(items):
    if len(items) == 1:
        return items[0]  
    elif len(items) == 2:
        return " and ".join(items)  
    elif len(items) == 3:
        return f"{items[0]}, {items[1]}, and {items[2]}"  
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]
