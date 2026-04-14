def communist_sort(arr):
    """
    Divides the total equally among all elements.
    Must be in integers. Fractional wealth is seized by the state.
    """
    if not arr:
        return arr
    
    total = sum(arr)
    equal_share = total // len(arr) # Integer division
    
    return [equal_share] * len(arr)


def capitalist_sort(arr):
    """
    Privatizes profits and socializes losses.
    Consolidates all positive wealth to the top. Makes all positive elements 0, 
    except the last positive element which gets the total.
    Negative elements (debt) remain exactly where they are.
    """
    if not arr:
        return arr
        
    # Calculate the total extractable wealth (only positive numbers)
    total_wealth = sum(x for x in arr if x > 0)
    
    # If there is no positive wealth to extract, nothing changes
    if total_wealth == 0:
        return list(arr)
        
    # Find the CEO (the index of the last positive element)
    last_pos_index = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > 0:
            last_pos_index = i
            break
            
    # Process the array
    result = []
    for i, x in enumerate(arr):
        if x > 0:
            if i == last_pos_index:
                # The 1% absorbs all the positive wealth
                result.append(total_wealth)
            else:
                # The rest of the positive elements are drained to 0
                result.append(0)
        else:
            # Debt and zero-values remain untouched
            result.append(x)
            
    return result


def island_sort(arr):
    """
    Banishes anyone over 18 from the island entirely (deleted from memory).
    The remaining youth establish a perfectly ordered society.
    """
    if not arr:
        return arr
        
    # Only the young survive, and they immediately organize
    return sorted([x for x in arr if x < 18])


def six_seven_sort(arr):
    """
    Ignores the original values entirely and replaces the array 
    with an alternating series of 6s and 7s.
    """
    if not arr:
        return arr
        
    return [6 if i % 2 == 0 else 7 for i in range(len(arr))]
